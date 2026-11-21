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
