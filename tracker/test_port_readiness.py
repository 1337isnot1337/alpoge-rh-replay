import io
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import port


class PortReadinessTest(unittest.TestCase):
    def test_next_waits_for_external_imports(self):
        rows = [
            dict(id='M000001', module='Base', packet='P0001', depth=0, imports=[]),
            dict(id='M000002', module='Consumer', packet='P0002', depth=1, imports=['M000001']),
        ]
        for done, expected in [(set(), ['P0001']), ({'M000001'}, ['P0002'])]:
            with self.subTest(done=done), patch.object(sys, 'argv', ['port.py', 'next']), \
                    patch.object(port.tasks, 'module_rows', return_value=rows), \
                    patch.object(port, 'ported', return_value=done), \
                    patch.object(port, 'triage', return_value={}), \
                    patch.object(port, 'port_issues', return_value=set()), \
                    redirect_stdout(io.StringIO()) as output:
                port.main()
                packets = [line.split()[0] for line in output.getvalue().splitlines()]
                self.assertEqual(packets, expected)

    def test_ready_allows_intra_packet_imports(self):
        packet_rows = [
            dict(id='M000001', module='Base', packet='P0002', depth=0, imports=[]),
            dict(id='M000002', module='Consumer', packet='P0002', depth=1, imports=['M000001']),
        ]
        self.assertTrue(port.ready(packet_rows, set()))

        with_external = packet_rows + [
            dict(id='M000003', module='ExternalConsumer', packet='P0002', depth=2, imports=['M000002', 'M000099']),
        ]
        self.assertFalse(port.ready(with_external, set()))
        self.assertTrue(port.ready(with_external, {'M000099'}))

    def test_ready_blocks_unknown_import_ids(self):
        packet_rows = [
            dict(id='M000010', module='Mystery', packet='P0003', depth=1, imports=['M999999']),
        ]
        self.assertFalse(port.ready(packet_rows, set()))
        self.assertFalse(port.ready(packet_rows, {'M000001'}))

    def test_ready_members_follow_internal_dependencies_but_not_blocked_ones(self):
        rows = [
            dict(id='M000003', imports=['M000002']),
            dict(id='M000002', imports=['M000001']),
            dict(id='M000001', imports=[]),
            dict(id='M000004', imports=['M999999']),
            dict(id='M000005', imports=['M000004']),
        ]
        self.assertEqual([r['id'] for r in port.ready_members(rows, {'M000001'})],
                         ['M000003', 'M000002'])

    def test_ready_members_stop_on_cycles_and_unknown_imports(self):
        rows = [dict(id='M000001', imports=['M000002']),
                dict(id='M000002', imports=['M000001']),
                dict(id='M000003', imports=['M999999'])]
        self.assertEqual(port.ready_members(rows, set()), [])

    def test_partial_suggestions_count_only_unported_members_and_preserve_reservations(self):
        rows = [
            dict(id='M000001', module='Done', packet='P0001', depth=1, imports=['M900001']),
            dict(id='M000002', module='Ready', packet='P0001', depth=1, imports=['M900001']),
            dict(id='M000003', module='Blocked', packet='P0001', depth=1, imports=['M900002']),
            dict(id='M000004', module='Whole', packet='P0002', depth=2, imports=['M900001']),
            dict(id='M000005', module='NoReady', packet='P0003', depth=1, imports=['M900002']),
        ]
        cases = [([], ['P0002']), (['--include-partial'], ['P0002', 'P0001'])]
        for flags, expected in cases:
            with self.subTest(flags=flags), patch.object(sys, 'argv', ['port.py', 'next', *flags]), \
                    patch.object(port.tasks, 'module_rows', return_value=rows), \
                    patch.object(port, 'ported', return_value={'M000001', 'M900001'}), \
                    patch.object(port, 'triage', return_value={}), \
                    patch.object(port, 'port_issues', return_value=set()), \
                    redirect_stdout(io.StringIO()) as output:
                port.main()
                self.assertEqual([line.split()[0] for line in output.getvalue().splitlines()], expected)
                if flags:
                    self.assertIn('1/2 unported modules ready (3 total)', output.getvalue())
                    self.assertIn('1 waiting for imports', output.getvalue())
        for reservation in ['P0001', 'M000002', 'M000003']:
            with self.subTest(reservation=reservation), \
                    patch.object(sys, 'argv', ['port.py', 'next', '--include-partial']), \
                    patch.object(port.tasks, 'module_rows', return_value=rows), \
                    patch.object(port, 'ported', return_value={'M000001', 'M900001'}), \
                    patch.object(port, 'triage', return_value={}), \
                    patch.object(port, 'port_issues', return_value={reservation}), \
                    redirect_stdout(io.StringIO()) as output:
                port.main()
                self.assertNotIn('P0001', output.getvalue())

    def test_show_ready_only_omits_completed_and_blocked_members(self):
        rows = [
            dict(id='M000001', module='Done', packet='P0001', depth=1, imports=[]),
            dict(id='M000002', module='Ready', packet='P0001', depth=1, imports=['M900001']),
            dict(id='M000003', module='Blocked', packet='P0001', depth=1, imports=['M900002']),
        ]
        with patch.object(sys, 'argv', ['port.py', 'show', 'P0001', '--ready-only']), \
                patch.object(port.tasks, 'module_rows', return_value=rows), \
                patch.object(port, 'ported', return_value={'M000001', 'M900001'}), \
                patch.object(port, 'triage', return_value={}), \
                redirect_stdout(io.StringIO()) as output:
            port.main()
            self.assertEqual(output.getvalue().splitlines(), ['M000002 1 untriaged Ready'])
