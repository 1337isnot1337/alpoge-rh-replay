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
        self.assertEqual(routes[('/issues/6', 'PATCH')], [{'state': 'closed', 'state_reason': 'not_planned'}])
        self.assertNotIn(('/issues/7', 'PATCH'), routes)
        self.assertNotIn(('/issues/5', 'PATCH'), routes)
        self.assertEqual(routes[('/issues/7/labels', 'POST')], [{'labels': ['claim', 'claim-granted']}])

    def test_graphql_queues_close_for_refused_claim(self):
        import claims_graphql
        client = claims_graphql.ClaimsGraphQL('o/r', 't')
        client.issues = {6: {'id': 'I6'}}
        client.queue('/issues/6', 'PATCH', {'state': 'closed', 'state_reason': 'not_planned'})
        self.assertEqual(client.writes, ['closeIssue(input:{issueId:"I6",stateReason:NOT_PLANNED}){clientMutationId}'])

    def test_completed_target_claim_is_closed_with_pull_hint(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'paused.txt'
            path.write_text('')
            writes = []
            rows = [dict(id='M000001', packet='P0001', state='volunteer-build-reviewed'),
                    dict(id='M000002', packet='P0002', state='assigned')]
            with patch.object(grants, 'load', return_value=rows), patch.object(grants, 'PAUSED', path):
                grants.reconcile(lambda route: [issue(8, 'M000001', 'v'), issue(9, 'M000002', 'w')] if route.startswith('/issues?') else [],
                                 lambda *args: writes.append(args))
        routes = {(route, method): body for route, method, *body in writes}
        self.assertIn('already completed', routes[('/issues/8/comments', 'POST')][0]['body'])
        self.assertEqual(routes[('/issues/8', 'PATCH')], [{'state': 'closed', 'state_reason': 'not_planned'}])
        self.assertNotIn(('/issues/9', 'PATCH'), routes)
        self.assertIn('overlaps', routes[('/issues/9/comments', 'POST')][0]['body'])

    def test_missing_file_pauses_nobody(self):
        self.assertEqual(grants.load_paused(Path('/nonexistent/paused.txt')), set())


if __name__ == '__main__':
    unittest.main()
