import json
import tempfile
import unittest
from pathlib import Path

from validate_ports import validate


class PortRecordTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name)
        self.target = {'lean': 'lean-version', 'mathlib': 'mathlib-commit'}
        self.row = {'id': 'M000001', 'module': 'Sample', 'source_sha256': 'a' * 64}
        self.record = {**self.target, 'module': 'Sample', 'source_sha256': 'a' * 64,
                       'notes': 'unchanged'}
        self.path = self.folder / 'M000001.json'
        self.patch = self.path.with_suffix('.patch')

    def errors(self):
        self.path.write_text(json.dumps(self.record))
        return list(validate(self.folder, {'M000001': self.row}, self.target))

    def test_unchanged_and_patched_modules(self):
        self.assertEqual(self.errors(), [])
        self.record['notes'] = 'Use renamed lemma.'
        self.assertTrue(self.errors())
        self.patch.touch()
        self.assertTrue(self.errors())
        self.patch.write_text('sample diff')
        self.assertEqual(self.errors(), [])
        self.record['notes'] = 'unchanged'
        self.assertTrue(self.errors())

    def test_mismatched_identity_and_pins(self):
        for key in ('module', 'source_sha256', 'lean', 'mathlib'):
            with self.subTest(key=key):
                original = self.record[key]
                self.record[key] = 'wrong'
                self.assertIn(key, ' '.join(self.errors()))
                self.record[key] = original

    def test_orphan_patch_and_unknown_record(self):
        (self.folder / 'M000002.patch').touch()
        (self.folder / 'M000003.json').write_text('{}')
        report = ' '.join(self.errors())
        self.assertIn('M000002', report)
        self.assertIn('M000003', report)

    def test_invalid_records_report_the_filename(self):
        for content in ('{', 'null', '[]'):
            with self.subTest(content=content):
                self.path.write_text(content)
                errors = list(validate(self.folder, {'M000001': self.row}, self.target))
                self.assertIn(self.path.name, ' '.join(errors))
        del self.record['notes']
        self.assertIn('notes', ' '.join(self.errors()))
