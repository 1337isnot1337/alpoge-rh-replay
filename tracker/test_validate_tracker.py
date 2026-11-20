"""Regression tests for validate_tracker.py.

The case that matters: a reviewed receipt whose task list was replaced
with copies of one unrelated (but valid) module id, with its object
digests emptied, used to pass validation.  The validator must reject it,
while still accepting the repository as it stands.
"""
import gzip
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / 'tracker' / 'validate_tracker.py'
RECEIPT = Path('evidence/volunteers/P0012.json')


def run_validator(root):
    return subprocess.run([sys.executable, str(VALIDATOR), str(root)],
                          capture_output=True, text=True)


class ValidateTrackerTests(unittest.TestCase):
    def test_repository_as_it_stands_passes(self):
        result = run_validator(ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_corrupted_reviewed_receipt_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / 'repo'
            shutil.copytree(ROOT, copy,
                            ignore=shutil.ignore_patterns('.git', '__pycache__'))
            with gzip.open(copy / 'tracker/modules.jsonl.gz', 'rt') as f:
                rows = [json.loads(line) for line in f if line.strip()]
            unrelated = next(r['id'] for r in rows if r['packet'] != 'P0012')
            receipt_path = copy / RECEIPT
            receipt = json.loads(receipt_path.read_text())
            receipt['tasks'] = [unrelated] * 64
            receipt['objects'] = {}
            receipt_path.write_text(json.dumps(receipt))
            result = run_validator(copy)
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            for check_name in ('evidence.reviewed_tasks_unique',
                               'evidence.reviewed_tasks_match_claim',
                               'evidence.reviewed_objects_match_tasks'):
                self.assertIn(f'FAIL {check_name}', result.stdout)


if __name__ == '__main__':
    unittest.main()
