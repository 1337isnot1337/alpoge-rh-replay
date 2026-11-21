"""Integration tests for port claim selection on a miniature offline ledger."""

import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import Mock, patch


class PortClaimTests(unittest.TestCase):
    def setUp(self):
        self.issues = []
        self.modules = [
            dict(id=ident, packet=packet, module=f'Example.{ident}', depth=0, imports=[])
            for ident, packet in (
                ('M000001', 'P0001'), ('M000002', 'P0001'), ('M000003', 'P0002'),
            )
        ]
        tasks = types.SimpleNamespace(
            repo='owner/test', open_issues=lambda: iter(self.issues),
            module_rows=lambda: iter(self.modules),
        )
        path = Path(__file__).resolve().parents[1] / 'tracker' / 'port.py'
        spec = importlib.util.spec_from_file_location('port_under_test', path)
        self.port = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {'tasks': tasks}):
            spec.loader.exec_module(self.port)
        self.port.ported = set
        self.port.triage = dict
        self.gh = Mock()
        self.port.subprocess = types.SimpleNamespace(run=self.gh)

    def run_cli(self, *args):
        output = io.StringIO()
        with patch.object(sys, 'argv', ['port.py', *args]), contextlib.redirect_stdout(output):
            self.port.main()
        return output.getvalue()

    def reserve(self, target):
        self.issues.append({'title': f'Port {target}'})

    def test_next_skips_packet_with_reserved_member(self):
        self.reserve('M000001')
        self.assertEqual([line.split('\t')[0] for line in self.run_cli('next').splitlines()], ['P0002'])

    def test_claim_rejects_packet_with_reserved_member(self):
        self.reserve('M000002')
        with self.assertRaisesRegex(SystemExit, 'Port M000002'):
            self.run_cli('claim', 'P0001')
        self.gh.assert_not_called()

    def test_claim_rejects_member_of_reserved_packet(self):
        self.reserve('P0001')
        with self.assertRaisesRegex(SystemExit, 'Port P0001'):
            self.run_cli('claim', 'M000001')
        self.gh.assert_not_called()

    def test_claim_allows_independent_module(self):
        self.reserve('M000001')
        self.run_cli('claim', 'M000002')
        command = self.gh.call_args.args[0]
        self.assertEqual(command[:3], ['gh', 'issue', 'create'])
        self.assertEqual(command[command.index('--title') + 1], 'Port M000002')
        self.assertEqual(self.gh.call_args.kwargs, {'check': True})

    def test_show_accepts_a_single_module_id(self):
        self.assertEqual(self.run_cli('show', 'M000002').split(),
                         ['M000002', '0', 'untriaged', 'Example.M000002'])


if __name__ == '__main__':
    unittest.main()
