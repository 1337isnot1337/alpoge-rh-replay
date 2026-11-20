import os
from pathlib import Path
import tempfile
import unittest

import tasks


class ReceiptTests(unittest.TestCase):
    def test_project_oleans_names_modules_and_ignores_other_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            build = Path(tmp)
            self.assertEqual(tasks.project_oleans(build), {})
            lib = build / 'lib/lean/Formalism/BehrendSets'
            lib.mkdir(parents=True)
            (lib / 'Statement.olean').write_bytes(b'')
            (lib / 'Statement.ilean').write_bytes(b'')
            (build / 'lib/lean/Main.olean').write_bytes(b'')
            self.assertEqual(set(tasks.project_oleans(build)), {'Formalism.BehrendSets.Statement', 'Main'})

    def test_rebuilt_imports_lists_new_or_rewritten_modules_except_targets(self):
        before = {'A': 1, 'B': 1, 'Target': 1}
        after = {'A': 1, 'B': 2, 'C': 5, 'Target': 3}
        self.assertEqual(tasks.rebuilt_imports(before, after, {'Target'}), ['B', 'C'])
        self.assertEqual(tasks.rebuilt_imports(before, before, {'Target'}), [])

    def test_rebuilt_imports_detects_a_rewritten_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            build = Path(tmp)
            olean = build / 'lib/lean/Dep.olean'
            olean.parent.mkdir(parents=True)
            olean.write_bytes(b'old')
            before = tasks.project_oleans(build)
            os.utime(olean, ns=(0, before['Dep'] + 1_000_000_000))
            target = build / 'lib/lean/Target.olean'
            target.write_bytes(b'new')
            self.assertEqual(tasks.rebuilt_imports(before, tasks.project_oleans(build), {'Target'}), ['Dep'])

    def test_host_resources_reports_cpu_count(self):
        info = tasks.host_resources()
        self.assertEqual(info['cpu_count'], os.cpu_count())
        if Path('/proc/meminfo').exists():
            self.assertGreater(info['mem_total_kib'], 0)
            self.assertIn('peak_child_rss_kib', info)


if __name__ == '__main__':
    unittest.main()
