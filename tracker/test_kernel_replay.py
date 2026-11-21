import json
from pathlib import Path
import subprocess
import tempfile
import threading
import unittest
from unittest.mock import patch

import replay_evidence as evidence
import tasks
import worker_build


class KernelReplayTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.project = self.root / 'project'
        self.out = self.root / 'receipt'
        self.out.mkdir()
        (self.out / 'receipt.json').write_text('{}\n')
        self.rows = [dict(id=f'M{i:06}', module=f'Fixture.Module{i}') for i in range(3)]
        self.receipt = dict(objects={})
        self.objects = []
        for row in self.rows:
            path = self.project / '.lake/build/lib/lean' / (row['module'].replace('.', '/') + '.olean')
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(row['module'])
            self.objects.append(path)
            self.receipt['objects'][row['id']] = tasks.digest(path)

    def run_record(self, rows=None):
        rows = self.rows if rows is None else rows
        return dict(command=evidence.replay_command(rows), exit_code=0,
                    transcript=''.join('replaying ' + row['module'] + '\n' for row in rows))

    def parallel_record(self):
        return dict(receipt_sha256=tasks.digest(self.out / 'receipt.json'),
                    replays=[self.run_record(self.rows[:2]), self.run_record(self.rows[2:])])

    def test_legacy_and_parallel_records(self):
        legacy = dict(self.run_record(), receipt_sha256=tasks.digest(self.out / 'receipt.json'))
        evidence.check_replay(legacy, self.out, self.rows)
        evidence.check_replay(self.parallel_record(), self.out, self.rows)

    def test_parallel_record_is_bound_to_receipt(self):
        record = self.parallel_record()
        (self.out / 'receipt.json').write_text('{"changed": true}')
        with self.assertRaisesRegex(ValueError, 'different receipt'):
            evidence.check_replay(record, self.out, self.rows)

    def test_batch_cannot_borrow_a_replay_line_from_another_batch(self):
        record = self.parallel_record()
        line = 'replaying Fixture.Module0\n'
        record['replays'][0]['transcript'] = record['replays'][0]['transcript'].replace(line, '')
        record['replays'][1]['transcript'] += line
        with self.assertRaisesRegex(ValueError, 'Missing kernel replay line'):
            evidence.check_replay(record, self.out, self.rows)

    def test_missing_duplicate_extra_and_reordered_targets_are_rejected(self):
        for rows in [self.rows[:2], self.rows + self.rows[:1],
                     self.rows + [dict(id='M999999', module='Fixture.Other')], self.rows[::-1]]:
            with self.subTest(rows=rows):
                record = dict(receipt_sha256=tasks.digest(self.out / 'receipt.json'),
                              replays=[self.run_record(rows)])
                with self.assertRaisesRegex(ValueError, 'coverage mismatch'):
                    evidence.check_replay(record, self.out, self.rows)

    def test_failed_or_boolean_exit_status_is_rejected(self):
        for code in [1, -9, False]:
            record = self.parallel_record()
            record['replays'][1]['exit_code'] = code
            with self.subTest(code=code), self.assertRaisesRegex(ValueError, 'exit code'):
                evidence.check_replay(record, self.out, self.rows)

    def test_unexpected_flags_or_empty_batches_are_rejected(self):
        for command in [['lake', 'env', 'leanchecker', '--fresh', 'Fixture.Module0'],
                        evidence.replay_command([])]:
            record = self.parallel_record()
            record['replays'][0]['command'] = command
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, 'command'):
                evidence.check_replay(record, self.out, self.rows)

    def test_malformed_or_ambiguous_batch_records_are_rejected(self):
        for batches in [[], {}, [None]]:
            record = self.parallel_record()
            record['replays'] = batches
            with self.subTest(batches=batches), self.assertRaises(ValueError):
                evidence.check_replay(record, self.out, self.rows)
        record = self.parallel_record()
        record.update(self.run_record())
        with self.assertRaisesRegex(ValueError, 'Ambiguous'):
            evidence.check_replay(record, self.out, self.rows)

    @staticmethod
    def success(command, **kwargs):
        return subprocess.CompletedProcess(command, 0, ''.join('replaying ' + n + '\n' for n in command[4:]))

    def test_default_writer_preserves_legacy_record(self):
        with patch.object(subprocess, 'run', side_effect=self.success) as run:
            worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt, [], {})
        self.assertEqual(run.call_count, 1)
        record = json.loads((self.out / evidence.REPLAY_FILE).read_text())
        self.assertNotIn('replays', record)
        evidence.check_replay(record, self.out, self.rows)

    def test_parallel_writer_really_overlaps_processes(self):
        barrier = threading.Barrier(2)
        seen = []

        def run(command, **kwargs):
            seen.append(command)
            self.assertEqual(kwargs['env']['LEAN_NUM_THREADS'], '1')
            barrier.wait(timeout=5)
            return self.success(command, **kwargs)

        with patch.object(subprocess, 'run', side_effect=run):
            worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt,
                                              [], {'REPLAY_KERNEL_JOBS': '2'})
        self.assertEqual(len(seen), 2)
        record = json.loads((self.out / evidence.REPLAY_FILE).read_text())
        self.assertNotIn('command', record)
        evidence.check_replay(record, self.out, self.rows)

    def test_invalid_job_count_never_launches_a_checker(self):
        for jobs in ['0', '-1', '1.5', '', 'many']:
            with self.subTest(jobs=jobs), patch.object(subprocess, 'run') as run:
                with self.assertRaisesRegex(ValueError, 'positive integer'):
                    worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt,
                                                      [], {'REPLAY_KERNEL_JOBS': jobs})
                run.assert_not_called()

    def test_failed_batch_cannot_write_success_evidence(self):
        def run(command, **kwargs):
            if 'Fixture.Module2' in command:
                return subprocess.CompletedProcess(command, 1, 'kernel rejected declaration')
            return self.success(command, **kwargs)
        with patch.object(subprocess, 'run', side_effect=run):
            with self.assertRaisesRegex(ValueError, 'kernel rejected'):
                worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt,
                                                  [], {'REPLAY_KERNEL_JOBS': '2'})
        self.assertFalse((self.out / evidence.REPLAY_FILE).exists())

    def test_object_tampering_cannot_write_success_evidence(self):
        def run(command, **kwargs):
            self.objects[0].write_text('changed object')
            return self.success(command, **kwargs)
        with patch.object(subprocess, 'run', side_effect=run):
            with self.assertRaisesRegex(ValueError, 'Cached object changed'):
                worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt,
                                                  [], {'REPLAY_KERNEL_JOBS': '2'})
        self.assertFalse((self.out / evidence.REPLAY_FILE).exists())

    def exact_record(self):
        return dict(method=evidence.EXACT_METHOD,
                    receipt_sha256=tasks.digest(self.out / 'receipt.json'),
                    driver_source=evidence.exact_driver_source(self.rows, 2),
                    driver_sha256=evidence.hashlib.sha256(evidence.exact_driver_source(self.rows, 2).encode()).hexdigest(), workers=2,
                    command=['lake', 'env', 'lean', '/receipt/' + evidence.EXACT_DRIVER_FILE], exit_code=0,
                    transcript=''.join('replaying ' + r['module'] + '\n' for r in self.rows[::-1])
                    + 'exact replay completed 3 modules\n')

    def test_exact_completion_order_can_differ_from_requested_order(self):
        evidence.check_replay(self.exact_record(), self.out, self.rows)

    def test_exact_rejects_unreviewed_driver_and_unknown_method(self):
        for field, value in [('driver_source', 'def main := pure 0'),
                             ('driver_sha256', '0' * 64), ('method', 'other-checker')]:
            record = self.exact_record()
            record[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                evidence.check_replay(record, self.out, self.rows)

    def test_exact_rejects_incomplete_duplicate_extra_and_failed_checks(self):
        for change in ['missing', 'duplicate', 'extra', 'no-completion', 'failed', 'boolean']:
            record = self.exact_record()
            if change == 'missing':
                record['transcript'] = record['transcript'].replace('replaying Fixture.Module1\n', '')
            elif change == 'duplicate':
                record['transcript'] += 'replaying Fixture.Module1\n'
            elif change == 'extra':
                record['transcript'] += 'replaying Fixture.Other\n'
            elif change == 'no-completion':
                record['transcript'] = record['transcript'].replace('exact replay completed 3 modules\n', '')
            else:
                record['exit_code'] = False if change == 'boolean' else 1
            with self.subTest(change=change), self.assertRaises(ValueError):
                evidence.check_replay(record, self.out, self.rows)

    def test_exact_rejects_changed_commands_worker_counts_and_mixed_formats(self):
        for change in ['module', 'driver', 'flags', 'workers', 'boolean', 'mixed']:
            record = self.exact_record()
            if change == 'module': record['driver_source'] = record['driver_source'].replace('Fixture.Module1', 'Fixture.Other')
            elif change == 'driver': record['command'][3] = '/receipt/other.lean'
            elif change == 'flags': record['command'].insert(3, '--fresh')
            elif change == 'workers': record['workers'] = 0
            elif change == 'boolean': record['workers'] = True
            else: record['replays'] = [self.run_record()]
            with self.subTest(change=change), self.assertRaises(ValueError):
                evidence.check_replay(record, self.out, self.rows)

    def exact_success(self, command, **kwargs):
        self.assertEqual(kwargs['env']['LEAN_NUM_THREADS'], '2')
        self.assertEqual(kwargs['env']['LEAN_STACK_SIZE_KB'], '65536')
        self.assertEqual(Path(command[3]).read_text(), evidence.exact_driver_source(self.rows, 2))
        return subprocess.CompletedProcess(command, 0,
            ''.join('replaying ' + row['module'] + '\n' for row in self.rows[::-1])
            + f'exact replay completed {len(self.rows)} modules\n')

    def test_exact_writer_runs_one_process_and_embeds_reproducible_driver(self):
        with patch.object(subprocess, 'run', side_effect=self.exact_success) as run:
            worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt, [],
                {'REPLAY_KERNEL_METHOD': evidence.EXACT_METHOD, 'REPLAY_KERNEL_THREADS': '2'})
        self.assertEqual(run.call_count, 1)
        record = json.loads((self.out / evidence.REPLAY_FILE).read_text())
        evidence.check_replay(record, self.out, self.rows)
        self.assertEqual(record['method'], evidence.EXACT_METHOD)

    def test_exact_driver_mutation_cannot_write_success_receipt(self):
        def run(command, **kwargs):
            result = self.exact_success(command, **kwargs)
            Path(command[3]).write_text('def main := pure 0')
            return result
        with patch.object(subprocess, 'run', side_effect=run):
            with self.assertRaisesRegex(ValueError, 'driver changed'):
                worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt, [],
                    {'REPLAY_KERNEL_METHOD': evidence.EXACT_METHOD, 'REPLAY_KERNEL_THREADS': '2'})
        self.assertFalse((self.out / evidence.REPLAY_FILE).exists())

    def test_exact_bad_configuration_never_launches(self):
        configurations = [dict(REPLAY_KERNEL_THREADS=x) for x in ['0', '-1', '', 'many']]
        configurations.append(dict(REPLAY_KERNEL_JOBS='2'))
        for config in configurations:
            with self.subTest(config=config), patch.object(subprocess, 'run') as run:
                with self.assertRaises(ValueError):
                    worker_build.record_cached_replay(self.project, self.out, self.rows, self.receipt, [],
                        dict(REPLAY_KERNEL_METHOD=evidence.EXACT_METHOD, **config))
                run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
