import io
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

import claims_graphql


class GatewayRetryTest(unittest.TestCase):
    def test_gateway_timeouts_are_retried_on_reads(self):
        client = claims_graphql.ClaimsGraphQL('o/r', 't')
        calls = []

        def query(text, **variables):
            calls.append(text)
            if len(calls) < 3:
                raise HTTPError('u', 504, 'Gateway Timeout', {}, io.BytesIO(b''))
            return {'ok': 1}

        with patch.object(client, 'query', query), patch.object(claims_graphql, 'GATEWAY_DELAY', 0):
            self.assertEqual(client.read_query('x'), {'ok': 1})
        self.assertEqual(len(calls), 3)

    def test_other_errors_are_not_retried(self):
        client = claims_graphql.ClaimsGraphQL('o/r', 't')

        def query(text, **variables):
            raise HTTPError('u', 401, 'Unauthorized', {}, io.BytesIO(b''))

        with patch.object(client, 'query', query):
            with self.assertRaises(HTTPError):
                client.read_query('x')


class GatewayApplyTest(unittest.TestCase):
    def test_gateway_error_on_apply_replans_from_a_fresh_snapshot(self):
        snapshots, applies = [], []

        class Transport:
            def __init__(self, repo, token):
                pass

            def snapshot(self):
                snapshots.append(1)

            def pages(self, route):
                return iter([])

            def queue(self, *args):
                pass

            def apply(self):
                applies.append(1)
                if len(applies) == 1:
                    raise HTTPError('u', 502, 'Bad Gateway', {}, io.BytesIO(b''))

        with patch.object(claims_graphql, 'ClaimsGraphQL', Transport), \
                patch.object(claims_graphql, 'GATEWAY_DELAY', 0), \
                patch.dict('os.environ', {'GITHUB_REPOSITORY': 'o/r', 'GITHUB_TOKEN': 't'}):
            claims_graphql.reconcile(lambda get_pages, mutate: None)
        self.assertEqual((len(snapshots), len(applies)), (2, 2))


if __name__ == '__main__':
    unittest.main()
