import unittest
from unittest.mock import patch

import claims_graphql
import grants


def comment(number, body, login='github-actions', kind='Bot'):
    author = {'login': login, '__typename': kind} if login else None
    return {'databaseId': number, 'body': body, 'author': author}


def comments(nodes=(), before=None):
    return {'nodes': list(nodes), 'pageInfo': {
        'startCursor': before, 'hasPreviousPage': before is not None,
    }}


def issue(number, title, labels=(), history=None):
    return {'id': f'I{number}', 'number': number, 'title': title,
            'labels': {'nodes': [{'name': name} for name in labels]},
            'comments': comments() if history is None else history}


def page(nodes, after=None):
    return {'repository': {
        'claim': {'id': 'L1'}, 'granted': {'id': 'L2'}, 'conflict': {'id': 'L3'},
        'issues': {'nodes': nodes, 'pageInfo': {
            'endCursor': after, 'hasNextPage': after is not None,
        }},
    }}


class ClaimsGraphQLTests(unittest.TestCase):
    def test_hundred_issue_pages_preserve_grants_from_full_comment_history(self):
        # The grant is at the end of a full issue page, followed by an
        # overlapping new request on the next page. Its trusted bot history
        # spans two older comment pages; recent comments cannot forge a grant.
        packet = issue(100, 'Claim P0001', ('claim', 'claim-granted'), comments([
            comment(300, 'Granted `P9999`.', 'owner', 'User'),
            comment(301, 'Granted `P9999`.', 'dependabot', 'Bot'),
            comment(302, 'Granted `P9999`.', None),
        ], before='comment-200'))
        first = [issue(n, 'Unrelated issue') for n in range(1, 100)] + [packet]
        second = [issue(101, 'Claim M000001')]
        transport = claims_graphql.ClaimsGraphQL('r/p', 'unused-test-token')
        requests = []

        def query(text, **variables):
            requests.append((text, variables))
            if 'issues(states:OPEN' in text:
                self.assertIn('issues(states:OPEN, first:100, after:$after)', text)
                self.assertIn('comments(last:30)', text)
                if variables['after'] is None:
                    return page(first, after='issue-100')
                self.assertEqual(variables['after'], 'issue-100')
                return page(second)
            self.assertIn('comments(last:100, before:$before)', text)
            self.assertEqual(variables['id'], 'I100')
            if variables['before'] == 'comment-200':
                history = comments([
                    comment(200, 'Granted `P0001`.', 'github-actions[bot]'),
                    comment(250, 'No grant.', 'owner', 'User'),
                ], before='comment-100')
            else:
                self.assertEqual(variables['before'], 'comment-100')
                history = comments([comment(100, 'Granted `P9999`.')])
            return {'node': {'comments': history}}

        with patch.object(transport, 'query', side_effect=query):
            transport.snapshot()

        self.assertEqual(set(transport.issues), {100, 101})
        self.assertEqual(transport.issues[100]['comments'], 6)
        self.assertEqual([c['id'] for c in transport.comments], [200, 100])
        self.assertTrue(all(c['user']['login'] == 'github-actions[bot]'
                            for c in transport.comments))
        self.assertEqual([v['after'] for q, v in requests if 'issues(states:OPEN' in q],
                         [None, 'issue-100'])
        self.assertEqual([v['before'] for q, v in requests if 'comments(last:100' in q],
                         ['comment-200', 'comment-100'])

        writes = []
        # Already-recorded build evidence must not revoke an existing grant.
        rows = [{'id': 'M000001', 'packet': 'P0001', 'state': 'build-observed'}]
        with patch.object(grants, 'load', return_value=rows):
            grants.reconcile(get_pages=transport.pages,
                             mutate=lambda *args: writes.append(args))
        self.assertEqual([w[0] for w in writes],
                         ['/issues/101/labels', '/issues/101/comments'])
        self.assertEqual(writes[0][2], {'labels': ['claim', 'claim-conflict']})

    def test_short_final_page_keeps_renamed_labeled_claims(self):
        renamed = issue(101, 'Edited claim title', ('claim', 'claim-granted'))
        transport = claims_graphql.ClaimsGraphQL('r/p', 'unused-test-token')
        with patch.object(transport, 'query', side_effect=[
                page([issue(n, 'Unrelated issue') for n in range(1, 101)], after='issue-100'),
                page([renamed]),
        ]) as query:
            transport.snapshot()
        self.assertEqual(query.call_count, 2)
        self.assertEqual(query.call_args.kwargs['after'], 'issue-100')
        self.assertEqual(list(transport.issues), [101])
        self.assertEqual(transport.comments, [])


if __name__ == '__main__':
    unittest.main()
