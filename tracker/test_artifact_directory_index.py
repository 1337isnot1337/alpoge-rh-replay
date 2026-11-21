from pathlib import Path
import tempfile, unittest
from unittest.mock import patch
from artifact_directory_index import ArtifactDirectoryIndex


class DirectoryIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def make(self, *names):
        for name in names:
            (self.root / name).write_text(name)

    def test_matches_glob_with_shared_prefixes_and_suffixes(self):
        self.make('Foo.olean', 'Foo.olean.private', 'Foo.olean.server', 'Foo.ir',
                  'Foo.ir.sig', 'Foo.trace', 'Foo.setup.json', 'Foo.c',
                  'FooBar.olean', 'Foo', 'Other.olean', 'Ω.olean')
        index = ArtifactDirectoryIndex()
        for stem in ['Foo', 'FooBar', 'Other', 'Missing', 'Ω']:
            self.assertEqual(index.matches(self.root / stem), list(self.root.glob(stem + '.*')))
        index.verify()

    def test_unusual_stems_keep_glob_semantics(self):
        self.make('A.B.olean', 'A1.olean', 'A2.olean', '.Hidden.olean')
        index = ArtifactDirectoryIndex()
        for stem in ['A.B', 'A*', 'A?', 'A[12]', '.Hidden']:
            self.assertEqual(index.matches(self.root / stem), list(self.root.glob(stem + '.*')))
        index.verify()

    def test_added_semantic_artifact_is_rejected(self):
        self.make('Foo.olean'); index = ArtifactDirectoryIndex(); index.matches(self.root / 'Foo')
        self.make('Foo.olean.private')
        with self.assertRaises(ValueError): index.verify()

    def test_added_unexpected_artifact_is_rejected(self):
        self.make('Foo.olean'); index = ArtifactDirectoryIndex(); index.matches(self.root / 'Foo')
        self.make('Foo.unexpected')
        with self.assertRaises(ValueError): index.verify()

    def test_removed_artifact_is_rejected(self):
        self.make('Foo.olean'); index = ArtifactDirectoryIndex(); index.matches(self.root / 'Foo')
        (self.root / 'Foo.olean').unlink()
        with self.assertRaises(ValueError): index.verify()

    def test_new_artifact_for_unrelated_module_is_allowed(self):
        self.make('Foo.olean'); index = ArtifactDirectoryIndex(); index.matches(self.root / 'Foo')
        self.make('Other.olean'); index.verify()

    def test_late_selected_module_is_not_silently_omitted(self):
        self.make('Foo.olean'); index = ArtifactDirectoryIndex(); index.matches(self.root / 'Foo')
        self.make('Other.olean'); self.assertEqual(index.matches(self.root / 'Other'), [])
        with self.assertRaises(ValueError): index.verify()

    def test_missing_directory_matches_glob(self):
        path = self.root / 'missing' / 'Foo'; index = ArtifactDirectoryIndex()
        self.assertEqual(index.matches(path), list(path.parent.glob('Foo.*'))); index.verify()

    def test_created_directory_with_selected_artifact_is_rejected(self):
        path = self.root / 'missing' / 'Foo'; index = ArtifactDirectoryIndex(); index.matches(path)
        path.parent.mkdir(); path.with_suffix('.olean').write_text('x')
        with self.assertRaises(ValueError): index.verify()

    def test_directory_members_are_preserved_for_existing_validation(self):
        (self.root / 'Foo.unexpected').mkdir(); index = ArtifactDirectoryIndex()
        self.assertEqual(index.matches(self.root / 'Foo'), list(self.root.glob('Foo.*'))); index.verify()

    def test_ignored_generated_setup_changes_are_allowed(self):
        self.make('Foo.olean', 'Foo.setup.json')
        index = ArtifactDirectoryIndex(ignored_suffixes=('.setup.json',))
        self.assertEqual(index.matches(self.root / 'Foo'), list(self.root.glob('Foo.*')))
        (self.root / 'Foo.setup.json').unlink(); index.verify()
        self.make('Foo.extra.setup.json'); index.verify()
        self.make('Foo.olean.private')
        with self.assertRaises(ValueError): index.verify()


    def test_directory_reads_do_not_grow_with_module_count(self):
        self.make(*(f'Mod{i}.olean' for i in range(32)))
        original = Path.iterdir
        reads = []
        def counted(directory):
            reads.append(directory)
            return original(directory)
        with patch.object(Path, 'iterdir', counted):
            index = ArtifactDirectoryIndex()
            for i in range(32):
                self.assertEqual(index.matches(self.root / f'Mod{i}'), [self.root / f'Mod{i}.olean'])
            index.verify()
        self.assertLessEqual(len(reads), 2)


if __name__ == '__main__':
    unittest.main()
