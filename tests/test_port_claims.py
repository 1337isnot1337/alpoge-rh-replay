"""Integration tests for port claim selection on a miniature offline ledger."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
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
        self.lookup = Mock()
        self.port.subprocess = types.SimpleNamespace(run=self.gh, check_output=self.lookup)
        self.main_records(None, None)

    def main_records(self, *records, lean=None):
        pins = json.loads((self.port.ROOT / 'port' / 'target.json').read_text())
        if lean is not None:
            pins['lean'] = lean
        result = {f'm{i}': entry for i, entry in enumerate(records)}
        result['pins'] = {'text': json.dumps(pins)}
        self.lookup.return_value = json.dumps({'data': {'repository': result}})

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

    def test_completed_packet_or_module_is_rejected_even_with_empty_local_ledger(self):
        self.main_records({'oid': 'a'}, {'oid': 'b'})
        for target in ('P0001', 'M000002'):
            with self.subTest(target=target), self.assertRaisesRegex(SystemExit, 'already fully ported'):
                self.run_cli('claim', target)
            query = next(arg for arg in self.lookup.call_args.args[0] if arg.startswith('query='))
            self.assertIn('main:port/patches/M000002.json', query)
            self.assertEqual('main:port/patches/M000001.json' in query, target == 'P0001')
        self.gh.assert_not_called()

    def test_partly_ported_packet_can_still_be_claimed(self):
        self.main_records({'oid': 'a'}, None)
        self.run_cli('claim', 'P0001')
        self.gh.assert_called_once()

    def test_retarget_or_failed_lookup_cannot_open_issue(self):
        self.main_records(None, lean='different toolchain')
        with self.assertRaisesRegex(SystemExit, 'target changed'):
            self.run_cli('claim', 'M000002')
        self.lookup.side_effect = subprocess.CalledProcessError(1, 'gh')
        with self.assertRaises(subprocess.CalledProcessError):
            self.run_cli('claim', 'M000002')
        self.gh.assert_not_called()

    def test_show_accepts_a_single_module_id(self):
        self.assertEqual(self.run_cli('show', 'M000002').split(),
                         ['M000002', '0', 'untriaged', 'Example.M000002'])


if __name__ == '__main__':
    unittest.main()
