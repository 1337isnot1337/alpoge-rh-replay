"""Unit tests for tracker/publish.py (the automated publish sweep).

Hermetic: the HTTP opener and replay_evidence.verify are stubbed, so
nothing here touches the network or the GitHub CLI.
"""

import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import publish


class ArtifactUrlsTest(unittest.TestCase):
    def test_blob_rewrite_and_dedupe(self):
        body = ('Receipt: https://github.com/a/b/blob/main/receipt.json\n'
                'Again: https://github.com/a/b/blob/main/receipt.json\n'
                'Log: `https://www.github.com/a/b/blob/main/build.log`')
        found = publish.artifact_urls(body)
        self.assertEqual(found['receipt.json'],
                         ['https://raw.githubusercontent.com/a/b/main/receipt.json'])
        self.assertEqual(found['build.log'],
                         ['https://raw.githubusercontent.com/a/b/main/build.log'])

    def test_allowed(self):
        self.assertTrue(publish.allowed('https://release-assets.githubusercontent.com/x/receipt.json'))
        self.assertTrue(publish.allowed('https://gist.githubusercontent.com/x/receipt.json'))
        self.assertFalse(publish.allowed('http://github.com/a/receipt.json'))
        self.assertFalse(publish.allowed('file://github.com/etc/passwd'))
        self.assertFalse(publish.allowed('https://github.com.evil.example/receipt.json'))
        handler = publish._AllowlistRedirects()
        with self.assertRaises(ValueError):
            handler.redirect_request(None, None, 302, 'm', {}, 'file://github.com/etc/passwd')


class CleanTest(unittest.TestCase):
    def test_control_characters_and_length(self):
        cleaned = publish.clean('bad\n::error::\x07' + 'x' * 5000)
        self.assertNotIn('\n', cleaned)
        self.assertLessEqual(len(cleaned), 300)


class ReceiptShapeTest(unittest.TestCase):
    def test_legit_receipt(self):
        receipt = {'host': {'cpu_count': None, 'mem_total_kib': 1024},
                   'started_utc': '2026-11-20T00:00:00+00:00',
                   'elapsed_seconds': 12.5,
                   'toolchain': 'Lean (version 4.33.1, x86_64-unknown-linux-gnu, '
                                'commit ' + 'a' * 40 + ', Release)'}
        self.assertIsNone(publish.receipt_shape_error(receipt))

    def test_hostile_shapes(self):
        self.assertIn('host', publish.receipt_shape_error({'host': [[['x']]]}))
        self.assertIn('host', publish.receipt_shape_error({'host': {'evil': 1}}))
        self.assertIn('host', publish.receipt_shape_error({'host': {'cpu_count': '8'}}))
        self.assertIn('elapsed', publish.receipt_shape_error({'elapsed_seconds': float('nan')}))
        self.assertIn('elapsed', publish.receipt_shape_error({'elapsed_seconds': 10 ** 400}))
        self.assertIn('elapsed', publish.receipt_shape_error({'elapsed_seconds': -1}))
        self.assertIn('toolchain', publish.receipt_shape_error({'toolchain': 'x' * 600}))
        self.assertIn('started_utc', publish.receipt_shape_error({'started_utc': 'x' * 100}))


class LoadCompletedTest(unittest.TestCase):
    def roundtrip(self, text):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'completed.tsv'
            path.write_bytes(text if isinstance(text, bytes) else text.encode())
            return publish.load_completed(path)

    def test_roundtrip(self):
        credited = self.roundtrip('id\tpacket\tmodule\tevidence\nM000001\tP0001\tA\tx\n')
        self.assertEqual(list(credited), ['M000001'])

    def test_rejects_bad_files(self):
        with self.assertRaises(ValueError):
            self.roundtrip('id\tpacket\tmodule\tevidence\nM000001\tP\tA\tx\nM000001\tP\tA\tx\n')
        with self.assertRaises(ValueError):
            self.roundtrip('id\tpacket\tmodule\tevidence\nM000002\tP\tB\tx\nM000001\tP\tA\tx\n')
        with self.assertRaises(ValueError):
            self.roundtrip(b'id\tpacket\tmodule\tevidence\r\nM000001\tP\tA\tx\r\n')
        with self.assertRaises(ValueError):
            self.roundtrip('id\tpacket\tmodule\tevidence\nM000001\tP\tA\n')


class GrantTest(unittest.TestCase):
    def issue(self, state='open', labels=('claim-granted',)):
        return {'state': state, 'labels': [{'name': name} for name in labels]}

    def comments(self, granted=True):
        out = []
        if granted:
            out.append({'user': {'login': 'github-actions[bot]'}, 'body': 'Granted `P9999`. Begin.'})
        return out

    def test_grant_states(self):
        self.assertTrue(publish.grant_in_force(self.issue(), self.comments(), 'P9999'))
        self.assertFalse(publish.grant_in_force(self.issue(state='closed'), self.comments(), 'P9999'))
        self.assertFalse(publish.grant_in_force(
            self.issue(labels=('claim-granted', 'claim-conflict')), self.comments(), 'P9999'))
        self.assertFalse(publish.grant_in_force(self.issue(), self.comments(granted=False), 'P9999'))
        self.assertFalse(publish.grant_in_force(self.issue(), self.comments(), 'P8888'))


def make_tar(path, members):
    with tarfile.open(path, 'w:gz') as tf:
        for name, data in members:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))


class CheckBundleTest(unittest.TestCase):
    def test_valid_bundle(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'b.tar.gz'
            make_tar(path, [('lib/lean/A.olean', b'olean')])
            publish.check_bundle(path)  # must not raise

    def test_sparse_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'b.tar.gz'
            smap = b'0\n0\n'
            with tarfile.open(path, 'w:gz') as tf:
                info = tarfile.TarInfo('lib/lean/A.olean')
                info.pax_headers = {'GNU.sparse.major': '1', 'GNU.sparse.minor': '0',
                                    'GNU.sparse.name': 'lib/lean/A.olean',
                                    'GNU.sparse.realsize': '109951162777600'}
                info.size = len(smap)
                tf.addfile(info, io.BytesIO(smap))
            with self.assertRaises(ValueError):
                publish.check_bundle(path)

    def test_negative_size_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'b.tar.gz'
            with tarfile.open(path, 'w:gz') as tf:
                info = tarfile.TarInfo('lib/lean/A.olean')
                info.pax_headers = {'GNU.sparse.realsize': '-99999999999999'}
                info.size = 0
                tf.addfile(info, io.BytesIO(b''))
            with self.assertRaises(ValueError):
                publish.check_bundle(path)


class _FailResponse:
    def read1(self, n=-1):
        return b'x' * 1000

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class _FailOpener:
    def open(self, request, timeout=None):
        return _FailResponse()


class DownloadBudgetTest(unittest.TestCase):
    def test_failed_downloads_consume_budget(self):
        opener, publish._OPENER = publish._OPENER, _FailOpener()
        try:
            budget = {'used': 0, 'cap': 2500}
            with tempfile.TemporaryDirectory() as td:
                with self.assertRaises(publish._BudgetExceeded):
                    publish.fetch_one(
                        ['https://raw.githubusercontent.com/a/b/main/targets.tar.gz'],
                        Path(td), 'targets.tar.gz', budget)
            self.assertGreater(budget['used'], 2500)
        finally:
            publish._OPENER = opener


ROWS = [
    {'id': 'M000001', 'packet': 'P9999', 'module': 'A.One', 'state': 'open', 'depth': 0, 'imports': []},
    {'id': 'M000002', 'packet': 'P9999', 'module': 'A.Two', 'state': 'open', 'depth': 0, 'imports': []},
]
BODY = ('Replay submission\n\nReceipt: https://raw.githubusercontent.com/a/b/main/receipt.json\n'
        'Log: https://raw.githubusercontent.com/a/b/main/build.log\n'
        'Bundle: https://raw.githubusercontent.com/a/b/main/targets.tar.gz')


def make_context(login='alice'):
    rows = [dict(r) for r in ROWS]
    return {
        'issues': {7: {'number': 7, 'state': 'open', 'labels': [{'name': 'claim-granted'}]}},
        'histories': {7: [
            {'id': 50, 'user': {'login': 'github-actions[bot]'},
             'body': 'Granted `P9999`. Begin.', 'html_url': 'u0'},
            {'id': 60, 'user': {'login': login}, 'body': BODY, 'html_url': 'u1'},
        ]},
        'rows': rows, 'rows_by_module': {r['module']: r for r in rows},
        'credited': {}, 'run_url': None,
        'verify_budget': {'used': 0.0, 'cap': 5400.0},
        'verify_by_login': {},
    }


class _PayloadResponse:
    def __init__(self, data):
        self._io = io.BytesIO(data)

    def read1(self, n=-1):
        return self._io.read(n)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class PublishCandidateTest(unittest.TestCase):
    def setUp(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        # Point ROOT at the temp dir so the evidence-exists gate does
        # not read the real repository's evidence directory.
        root, publish.ROOT = publish.ROOT, Path(td.name)
        self.addCleanup(setattr, publish, 'ROOT', root)
        bundle = Path(td.name) / 'b.tar.gz'
        make_tar(bundle, [('lib/lean/A/One.olean', b'olean')])
        self.payloads = {'build.log': b'Build completed successfully (2 jobs).\n',
                         'targets.tar.gz': bundle.read_bytes()}
        opener = publish._OPENER
        publish._OPENER = type('O', (), {
            'open': lambda s, req, timeout=None: _PayloadResponse(
                self.payloads[req.full_url.rsplit('/', 1)[-1]])})()
        self.addCleanup(setattr, publish, '_OPENER', opener)
        verify = publish.replay_evidence.verify
        publish.replay_evidence.verify = lambda d, t, r: {
            'kernel_replayed_targets': [], 'built_targets': ['A.One', 'A.Two']}
        self.addCleanup(setattr, publish.replay_evidence, 'verify', verify)

    def run_candidate(self, receipt, login='alice'):
        self.payloads['receipt.json'] = (
            receipt if isinstance(receipt, bytes) else json.dumps(receipt).encode())
        return publish.publish_candidate((7, login, 'P9999', 60), make_context(login))

    def test_happy_path_record(self):
        receipt = {'tasks': ['M000001', 'M000002'], 'exit_code': 0,
                   'bundle_sha256': 'ab' * 32, 'toolchain': 'Lean (version 4.33.1, ...)',
                   'host': {'cpu_count': 8}, 'unreviewed_junk': 'x' * 100}
        text, targets, reason = self.run_candidate(receipt)
        self.assertIsNotNone(text, reason)
        record = json.loads(text)
        self.assertNotIn('unreviewed_junk', record)
        self.assertEqual(record['packet'], 'P9999')
        self.assertEqual(record['automation']['built_targets'], ['A.One', 'A.Two'])

    def test_skips(self):
        base = {'tasks': ['M000001', 'M000002'], 'exit_code': 0, 'bundle_sha256': 'ab' * 32}
        text, _, reason = self.run_candidate(dict(base, host=[[0]]))
        self.assertIsNone(text)
        self.assertIn('host', reason)
        text, _, reason = self.run_candidate({'tasks': [], 'exit_code': 0})
        self.assertIsNone(text)
        self.assertIn('no bundle', reason)
        text, _, reason = self.run_candidate(base, login='ghost')
        self.assertIsNone(text)
        self.assertIn('ghost', reason)
        text, _, reason = self.run_candidate(
            b'{"tasks": [], "exit_code": 0, "bundle_sha256": "' + b'ab' * 32 + b'", "elapsed_seconds": NaN}')
        self.assertIsNone(text)
        self.assertIn('does not parse', reason)


class RecheckTest(unittest.TestCase):
    def issue(self, **overrides):
        issue = {'number': 7, 'state': 'open', 'title': 'Claim P9999',
                 'labels': [{'name': 'claim'}, {'name': 'claim-granted'}],
                 'user': {'login': 'alice'}}
        issue.update(overrides)
        return issue

    def comments(self, body='Replay submission\n\nlinks', granted=True, login='alice'):
        out = [{'id': 60, 'user': {'login': login}, 'body': body, 'html_url': 'u1'}]
        if granted:
            out.insert(0, {'id': 50, 'user': {'login': 'github-actions[bot]'},
                           'body': 'Granted `P9999`. Begin.', 'html_url': 'u0'})
        return out

    def test_still_in_force(self):
        self.assertTrue(publish.recheck_record(
            self.issue(), self.comments(), 'P9999', 60, 'alice'))
        # The verified body still matches byte-for-byte.
        self.assertTrue(publish.recheck_record(
            self.issue(), self.comments(), 'P9999', 60, 'alice',
            'Replay submission\n\nlinks'))
        # Same opening line, but the body (artifact links) was edited
        # after verification: the record must not ride the stale check.
        self.assertFalse(publish.recheck_record(
            self.issue(), self.comments(), 'P9999', 60, 'alice',
            'Replay submission\n\nEDITED links'))

    def test_drops(self):
        # Issue vanished from the fresh snapshot (label removed).
        self.assertFalse(publish.recheck_record(None, [], 'P9999', 60, 'alice'))
        # Retitled during the run.
        self.assertFalse(publish.recheck_record(
            self.issue(title='Claim P8888'), self.comments(), 'P9999', 60, 'alice'))
        # Grant comment deleted during the run.
        self.assertFalse(publish.recheck_record(
            self.issue(), self.comments(granted=False), 'P9999', 60, 'alice'))
        # Submission comment deleted during the run.
        self.assertFalse(publish.recheck_record(
            self.issue(), self.comments()[:1], 'P9999', 60, 'alice'))
        # Submission comment edited into a withdrawal.
        self.assertFalse(publish.recheck_record(
            self.issue(), self.comments(body='Withdrawing this submission.'),
            'P9999', 60, 'alice'))
        # Account deleted (author collapsed to ghost).
        self.assertFalse(publish.recheck_record(
            self.issue(), self.comments(), 'P9999', 60, 'ghost'))
        # Issue author changed (transferred/reassigned claim).
        self.assertFalse(publish.recheck_record(
            self.issue(user={'login': 'mallory'}), self.comments(), 'P9999', 60, 'alice'))


class VerifyWorkerTest(unittest.TestCase):
    def test_cpu_hog_is_skipped_not_fatal(self):
        verify = publish.replay_evidence.verify
        cpu, wall = publish.VERIFY_CPU_SECONDS, publish.VERIFY_WALL_SECONDS

        def hog(directory, targets, rows):
            while True:
                pass

        publish.replay_evidence.verify = hog
        publish.VERIFY_CPU_SECONDS = 2
        publish.VERIFY_WALL_SECONDS = 30
        try:
            with tempfile.TemporaryDirectory() as td:
                directory = Path(td)
                make_tar(directory / 'targets.tar.gz', [('lib/lean/A.olean', b'olean')])
                result, reason = publish.verify_candidate(directory, [], {})
                self.assertIsNone(result)
                self.assertIsNotNone(reason)
        finally:
            publish.replay_evidence.verify = verify
            publish.VERIFY_CPU_SECONDS = cpu
            publish.VERIFY_WALL_SECONDS = wall


if __name__ == '__main__':
    unittest.main()
