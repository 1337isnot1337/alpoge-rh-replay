from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import scan
import check


class ProofScanTests(unittest.TestCase):
    def test_groups_by_statement_and_script_and_rejects_changed_input(self):
        source = (b'theorem a : True := by\n  trivial\n\n'
                  b'private theorem b : True := by\n  trivial\n'
                  b'theorem c : 0 = 0 := by\n  trivial\n')
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / 'src').mkdir()
            (project / 'tracker').mkdir()
            file = project / 'src/T.lean'
            file.write_bytes(source)
            row = dict(id='M000001', module='T', source_sha256=hashlib.sha256(source).hexdigest())
            with gzip.open(project / 'tracker/modules.jsonl.gz', 'wt') as stream:
                stream.write(json.dumps(row) + '\n')
            key = hashlib.sha256(b': True := by\n  trivial').digest()
            with patch.object(scan, 'ROOT', project):
                result = scan.scan(project, 1, {key})
                self.assertEqual(result['candidates'], 3)
                self.assertEqual(result['occurrences_after_first'], 1)
                self.assertEqual([(m['name'], m['line']) for m in result['matches']], [('a', 1), ('b', 4)])
                header_key = hashlib.sha256(b': True').digest()
                headers = scan.scan(project, 1, {header_key}, mode='header')
                self.assertEqual(headers['mode'], 'header')
                self.assertEqual([m['name'] for m in headers['matches']], ['a', 'b'])
                self.assertNotIn('mode', result)
                file.write_bytes(source + b'\n')
                with self.assertRaisesRegex(ValueError, 'Source hash mismatch'):
                    scan.scan(project, 1, {key})

    def test_ignores_possible_multiline_comment_content(self):
        self.assertEqual(list(scan.declarations(b'/-\ntheorem a : True := by\n  trivial\n-/')), [])

    def test_header_and_alpha_modes(self):
        scripts = [
            'theorem a (α : Type) (x : α) : x = x := by rfl',
            'lemma b (α : Type) (x : α) : x = x := by simp',
            'theorem c (β : Type) (y : β) : y = y := by rfl',
            'theorem d (β : Type) (y : β) : y ≠ y := by contradiction',
        ]
        data = ('\n'.join(scripts) + '\n').encode()
        for mode, count in [('exact', 4), ('header', 3), ('alpha', 2)]:
            self.assertEqual(len({k for k, _, _ in scan.declarations(data, mode)}), count)

    def test_alpha_respects_scope_and_projections(self):
        self.assertEqual(scan.alpha_header('(x : T) (w : x) : w.x = x'),
                         '($0 : T) ($1 : $0) : $1.x = $0')
        self.assertNotEqual(scan.alpha_header('(x : x) : x'), scan.alpha_header('(y : y) : y'))
        self.assertNotEqual(scan.alpha_header('(x : T) : ∀ x, P x'), scan.alpha_header('(z : T) : ∀ x, P z'))
        self.assertEqual(scan.alpha_header('(x : T) : ∃ y, R x y'),
                         scan.alpha_header('(z : T) : ∃ y, R z y'))
        self.assertNotEqual(scan.alpha_header('(x : T) : P.x'), scan.alpha_header('(y : T) : P.y'))
        self.assertNotEqual(scan.alpha_header('(x : T) : f (x := x) = x'),
                            scan.alpha_header('(y : T) : f (y := y) = y'))

    def test_header_ignores_default_proof_inside_binder(self):
        block = b'(h : True := by trivial) : True := by trivial'
        self.assertEqual(scan.statement_header(block), '(h : True := by trivial) : True')
        self.assertIsNone(scan.statement_header(b': let x := by exact 0; x = x := by rfl'))

    def test_results_record_matches_source_digests(self):
        here = Path(__file__).resolve().parent
        results = json.loads((here / 'results.json').read_text(encoding='utf-8'))
        for filename, expected_sha in results['source_sha256'].items():
            raw = (here / filename).read_bytes().replace(b'\r\n', b'\n')
            self.assertEqual(hashlib.sha256(raw).hexdigest(), expected_sha, filename)
        latest = results['runs'][0]
        exact = {name for names in check.LIBRARIES.values() for name in names}
        new = {name for names in check.STRUCTURAL_LIBRARIES.values() for name in names}
        self.assertEqual(set(latest['checked']), exact | new)
        self.assertEqual(sum(latest['checked'][n] for n in exact), 194)
        expected = Counter()
        for full, tasks in check.STRUCTURAL_CASES.values():
            expected[full.split('.')[-1]] += len(tasks.split())
        self.assertEqual({name: latest['checked'][name] for name in new}, dict(expected))
        self.assertTrue(set(check.STRUCTURAL_LIBRARIES) <= set(latest['kernel_replayed']))
        self.assertTrue({'OriginalStructural', 'SharedStructural'} <= set(latest['kernel_replayed']))


if __name__ == '__main__':
    unittest.main()
