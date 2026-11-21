import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import activity
import submissions


class CreditSnapshotTests(unittest.TestCase):
    def test_snapshot_reuses_comments_and_renders_new_evidence(self):
        repo = 'owner/project'
        claim = {'number': 5, 'title': 'Claim M000001', 'state': 'open', 'labels': [],
                 'user': {'type': 'User', 'id': 17, 'login': 'alice'}}
        empty_claim = dict(claim, number=6, title='Claim M000002')
        link = f'https://github.com/{repo}/issues/5#issuecomment-9'
        comment = {'id': 9, 'user': claim['user'], 'body': 'Replay submission',
                   'created_at': '2026-11-21T12:00:00Z', 'html_url': link}
        with TemporaryDirectory() as tmp, patch.dict('os.environ', GITHUB_REPOSITORY=repo):
            root = Path(tmp)
            evidence = root / 'evidence' / 'volunteers'
            evidence.mkdir(parents=True)
            markers = ['active-volunteers', 'pending-volunteers', 'volunteers', 'volunteer-roster']
            readme = root / 'README.md'
            readme.write_text('\n'.join(f'<!-- {m}-start --><!-- {m}-end -->' for m in markers))
            saved = root / 'claims.json'
            with patch.object(submissions, 'claim_snapshot', return_value=([claim, empty_claim], {5: [comment]})) as fetch, \
                    patch.object(submissions, 'ROOT', root), patch.object(activity, 'TRACKER', root / 'tracker'):
                submissions.write_claim_snapshot(repo, saved)
                for reviewed in (False, True):
                    if reviewed:
                        receipt = {'contributor': 'alice', 'packet': 'M000001', 'claim': link, 'tasks': ['M000001']}
                        (evidence / 'M000001.json').write_text(json.dumps(receipt))
                    authors = submissions.main(True, snapshot=submissions.read_claim_snapshot(repo, saved))
                    self.assertEqual(authors, {'5': (17, 'alice'), '6': (17, 'alice')})
                    self.assertEqual('Pending review |' in readme.read_text(), not reviewed)
                    self.assertEqual('Build evidence verified' in readme.read_text(), reviewed)
                    self.assertIn('submission\t5\talice', (root / 'tracker' / 'activity.tsv').read_text())
                fetch.assert_called_once_with(repo)
            with self.assertRaisesRegex(ValueError, 'different repository'):
                submissions.read_claim_snapshot('another/repo', saved)
