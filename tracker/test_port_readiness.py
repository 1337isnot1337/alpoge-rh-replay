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
