import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import grants


def issue(number, target, login, labels=()):
    return dict(number=number, title=f'Claim {target}', user=dict(login=login),
                labels=[dict(name=name) for name in labels], comments=len(labels) and 1,
                url=f'https://api.github.com/repos/o/r/issues/{number}')


class PausedClaimantTest(unittest.TestCase):
    def run_reconcile(self, issues, history, paused):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'paused.txt'
            path.write_text(paused)
            writes = []
            rows = [dict(id=f'M00000{i}', packet='P0001', state='open') for i in range(1, 4)]
            with patch.object(grants, 'load', return_value=rows), \
                    patch.object(grants, 'PAUSED', path):
                grants.reconcile(lambda route: issues if route.startswith('/issues?') else history,
                                 lambda *args: writes.append(args))
            return writes

    def test_new_claim_from_paused_login_is_refused_and_existing_grant_kept(self):
        kept = issue(5, 'M000001', 'Paused', ['claim', 'claim-granted'])
        grant = dict(id=1, issue_url='https://api.github.com/repos/o/r/issues/5', created_at='2026-11-21T00:00:00Z',
                     user=dict(login='github-actions[bot]'), body='Granted `M000001`. Begin.')
        new = issue(6, 'M000002', 'paused')
        other = issue(7, 'M000003', 'someone')
        writes = self.run_reconcile([kept, new, other], [grant], '# note\npaused  # reason\n')
        routes = {(route, method): body for route, method, *body in writes}
        self.assertNotIn(('/issues/5/labels/claim-granted', 'DELETE'), routes)
        self.assertEqual(routes[('/issues/6/labels', 'POST')], [{'labels': ['claim', 'claim-conflict']}])
        self.assertIn('paused', routes[('/issues/6/comments', 'POST')][0]['body'])
        self.assertEqual(routes[('/issues/7/labels', 'POST')], [{'labels': ['claim', 'claim-granted']}])

    def test_missing_file_pauses_nobody(self):
        self.assertEqual(grants.load_paused(Path('/nonexistent/paused.txt')), set())


if __name__ == '__main__':
    unittest.main()
