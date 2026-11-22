"""Keep replay reads alive through temporary API failures without hiding other errors."""
import io
import json
import subprocess
import unittest
from unittest.mock import call, patch

import submissions
import worker_github


def response(code, stdout='', stderr=''):
    return subprocess.CompletedProcess([], code, stdout, stderr)


class GitHubReadRetryTests(unittest.TestCase):
    def test_claim_watch_retries_observed_graphql_server_error(self):
        failure = response(1, stderr='gh: Something went wrong while executing your query on '
                           '2026-11-22T05:24:51Z. Please include this ID when reporting the issue.')
        issue = dict(number=123, title='Claim P1234', state='OPEN', author={'login': 'worker'},
                     labels={'nodes': [{'name': 'claim-granted'}]}, comments={'totalCount': 1})
        success = response(0, json.dumps({'data': {'repository': {'i123': issue}}}))
        github = worker_github.GitHub.__new__(worker_github.GitHub)
        with patch.object(submissions.subprocess, 'run', side_effect=[failure, success]) as run, \
                patch.object(submissions.time, 'sleep') as sleep, patch('sys.stderr', io.StringIO()):
            watched = list(github.watch([123]))
        self.assertEqual(watched, [dict(number=123, title='Claim P1234', state='open',
                                       user={'login': 'worker'}, labels=[{'name': 'claim-granted'}], comments=1)])
        self.assertEqual(run.call_args_list[0], run.call_args_list[1])
        self.assertEqual(run.call_args.args[0][:3], ['gh', 'api', 'graphql'])
        sleep.assert_called_once_with(1)

    def test_transient_http_errors_retry_same_paginated_read(self):
        for status in (500, 502, 503, 504):
            with self.subTest(status=status), \
                    patch.object(submissions.subprocess, 'run', side_effect=[
                        response(1, stderr=f'gh: temporary server failure (HTTP {status})'),
                        response(0, '[[{"number": 123}], [{"number": 124}]]')]) as run, \
                    patch.object(submissions.time, 'sleep') as sleep, patch('sys.stderr', io.StringIO()):
                self.assertEqual(list(submissions.pages('owner/repo', 'issues?per_page=100')),
                                 [{'number': 123}, {'number': 124}])
                self.assertEqual(run.call_args_list[0], run.call_args_list[1])
                sleep.assert_called_once_with(1)

    def test_exhausted_server_failures_preserve_last_output_and_error(self):
        command = ['gh', 'api', 'repos/owner/repo/issues/123']
        failures = [response(1, f'partial {i}', f'gh: failure {i} (HTTP 503)')
                    for i in range(submissions.ATTEMPTS)]
        with patch.object(submissions.subprocess, 'run', side_effect=failures) as run, \
                patch.object(submissions.time, 'sleep') as sleep, patch('sys.stderr', io.StringIO()):
            with self.assertRaises(subprocess.CalledProcessError) as raised:
                submissions.gh_output(command)
        self.assertEqual(run.call_count, submissions.ATTEMPTS)
        self.assertEqual(sleep.call_args_list, [call(1), call(2), call(4)])
        self.assertEqual(raised.exception.cmd, command)
        self.assertEqual(raised.exception.output, failures[-1].stdout)
        self.assertEqual(raised.exception.stderr, failures[-1].stderr)

    def test_permissions_missing_resources_and_invalid_queries_fail_immediately(self):
        for error in ['gh: Bad credentials (HTTP 401)', 'gh: Resource not accessible (HTTP 403)',
                      'gh: Not Found (HTTP 404)', 'gh: Validation Failed (HTTP 422)',
                      'gh: Not Implemented (HTTP 501)', 'gh: Field does not exist on type Issue',
                      'gh: certificate verification failed']:
            with self.subTest(error=error), \
                    patch.object(submissions.subprocess, 'run', return_value=response(1, stderr=error)) as run, \
                    patch.object(submissions.time, 'sleep') as sleep, patch('sys.stderr', io.StringIO()):
                with self.assertRaises(subprocess.CalledProcessError):
                    submissions.gh_output(['gh', 'api', 'graphql'])
                self.assertEqual(run.call_count, 1)
                sleep.assert_not_called()

    def test_mutation_failure_is_not_retried(self):
        failure = subprocess.CalledProcessError(1, ['gh', 'api'], stderr='gh: failure (HTTP 503)')
        with patch.object(worker_github.subprocess, 'check_output', side_effect=failure) as post, \
                patch.object(submissions.time, 'sleep') as sleep:
            with self.assertRaises(subprocess.CalledProcessError):
                worker_github.post('repos/owner/repo/issues', title='Claim P1234')
        post.assert_called_once()
        sleep.assert_not_called()


if __name__ == '__main__':
    unittest.main()
