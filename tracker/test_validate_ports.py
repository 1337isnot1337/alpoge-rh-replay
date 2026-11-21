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
        self.row = {'id': 'M000001', 'module': 'Sample', 'source_sha256': 'a' * 64, 'imports': []}
        self.record = {**self.target, 'module': 'Sample', 'source_sha256': 'a' * 64,
                       'notes': 'unchanged'}
        self.path = self.folder / 'M000001.json'
        self.patch = self.path.with_suffix('.patch')
        self.valid_patch = (
            '--- a/src/Sample.lean\n'
            '+++ b/src/Sample.lean\n'
            '@@ -1 +1 @@\n'
            '-theorem foo : True := by trivial\n'
            '+theorem foo : True := by exact trivial\n'
        )

    def errors(self):
        self.path.write_text(json.dumps(self.record))
        return list(validate(self.folder, {'M000001': self.row}, self.target))

    def test_unchanged_and_patched_modules(self):
        self.assertEqual(self.errors(), [])
        self.record['notes'] = 'Use renamed lemma.'
        self.assertTrue(self.errors())
        self.patch.touch()
        self.assertTrue(self.errors())
        self.patch.write_text(self.valid_patch)
        self.assertEqual(self.errors(), [])
        self.record['notes'] = 'unchanged'
        self.assertTrue(self.errors())

    def test_patch_must_target_only_own_source_file(self):
        self.record['notes'] = 'Use renamed lemma.'
        self.patch.write_text(
            '--- a/src/Other.lean\n'
            '+++ b/src/Other.lean\n'
            '@@ -1 +1 @@\n'
            '-a\n'
            '+b\n'
        )
        self.assertIn('a/src/Sample.lean', ' '.join(self.errors()))

    def test_patch_rejects_forbidden_constructs_but_allows_comments(self):
        self.record['notes'] = 'Use renamed lemma.'
        for token in ('sorry', 'admit', 'axiom', 'native_decide', 'unsafe', 'implemented_by'):
            with self.subTest(token=token):
                self.patch.write_text(
                    '--- a/src/Sample.lean\n'
                    '+++ b/src/Sample.lean\n'
                    '@@ -1 +1 @@\n'
                    '-theorem foo : True := by trivial\n'
                    f'+theorem foo : True := by {token}\n'
                )
                self.assertIn(token, ' '.join(self.errors()))

        self.patch.write_text(
            '--- a/src/Sample.lean\n'
            '+++ b/src/Sample.lean\n'
            '@@ -1 +1 @@\n'
            '-theorem foo : True := by trivial\n'
            '+-- no sorry or axiom here\n'
            '+theorem foo : True := /- not unsafe -/ trivial\n'
        )
        self.assertEqual(self.errors(), [])

    def test_git_metadata_must_describe_an_existing_file(self):
        self.record['notes'] = 'Use renamed lemma.'
        header = 'diff --git a/src/Sample.lean b/src/Sample.lean\n'
        for metadata in ('index 0000000..0000000 100644',
                         'index 0000000..123abcd 100644',
                         'index 123abcd..0000000',
                         'new file mode 100644', 'deleted file mode 100644'):
            with self.subTest(metadata=metadata):
                self.patch.write_text(header + metadata + '\n' + self.valid_patch)
                self.assertIn('creation/deletion metadata', ' '.join(self.errors()))
        self.patch.write_text(header + 'index 123abcd..456def0 100644\n' + self.valid_patch)
        self.assertEqual(self.errors(), [])

    def test_unported_project_imports_are_rejected(self):
        dep_row = {'id': 'M000000', 'module': 'Base', 'source_sha256': 'b' * 64, 'imports': []}
        self.row['imports'] = ['M000000']
        self.path.write_text(json.dumps(self.record))
        by_id = {'M000000': dep_row, 'M000001': self.row}
        self.assertIn('M000000', ' '.join(validate(self.folder, by_id, self.target)))
        (self.folder / 'M000000.json').write_text(json.dumps({
            **self.target, 'module': 'Base', 'source_sha256': 'b' * 64, 'notes': 'unchanged',
        }))
        self.assertEqual(list(validate(self.folder, by_id, self.target)), [])

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
