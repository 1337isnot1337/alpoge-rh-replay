import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import tasks


def row(task, packet, imports=(), state='open'):
    return dict(id=task, packet=packet, module=task, imports=imports,
                depth=int(bool(imports)), state=state)


class ColdModuleTests(unittest.TestCase):
    def test_claims_and_ledger_states(self):
        rows = [row('M1', 'P1'), row('M2', 'P1'), row('M3', 'P2'),
                row('M4', 'P3', state='build-observed'), row('M5', 'P3', state='assigned')]
        self.assertEqual([r['id'] for r, _, _ in tasks.cold_modules(rows, {'M1', 'P2'})], ['M2'])
        self.assertEqual(tasks.cold_modules(rows, {'P1', 'P2'}), [])

    def test_rank_by_sole_import_then_direct_consumers_then_id(self):
        rows = [row('A', 'P1'), row('B', 'P1'), row('C', 'P1'), row('D', 'P1'),
                row('E', 'P2', ['A', 'A']), row('F', 'P2', ['B', 'C']),
                row('G', 'P2', ['B', 'C']), row('H', 'P3', ['D']),
                row('I', 'P4', ['D']), row('J', 'P5', ['D'], state='assigned')]
        ranked = tasks.cold_modules(rows, {'P3', 'I'})
        self.assertEqual([(r['id'], sole, direct) for r, sole, direct in ranked],
                         [('A', 1, 1), ('B', 0, 2), ('C', 0, 2), ('D', 0, 0)])

    def test_cold_cli_and_default_packet_suggestions(self):
        rows = [row('M1', 'P1'), row('M2', 'P1', state='assigned'), row('M3', 'P2', ['M1'])]
        def next_output(*args):
            output = io.StringIO()
            with patch.object(tasks, 'load', return_value=rows), patch.object(tasks, 'claims', return_value=set()), \
                 patch('sys.argv', ['tasks.py', 'next', *args]), redirect_stdout(output):
                self.assertEqual(tasks.main(), 0)
            return output.getvalue()
        self.assertEqual(next_output(), 'P2 depth 1 begins with M3\n')
        self.assertEqual(next_output('--cold', '--limit', '1'),
                         'M1 P1 M1 sole-project-import consumers 1 direct consumers 1\n')
        self.assertEqual(next_output('--cold', '--limit', '0'), '')


if __name__ == '__main__':
    unittest.main()
