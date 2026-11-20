"""Build the bot's commit message from the claim issues changed in the index."""

import json
import os
import re
import subprocess

from submissions import gh_output


def changed_issues(repo):
    def changed_rows(path):
        diff = subprocess.check_output(
            ['git', 'diff', '--cached', '--no-color', '--no-ext-diff', '-U0', '--', path], text=True)
        return (line[1:] for line in diff.splitlines() if line.startswith(('+', '-')))

    numbers = set()
    issue_link = re.compile(r'\]\(https://github\.com/' + re.escape(repo) + r'/issues/(\d+)(?:#issuecomment-\d+)?\)')
    for row in changed_rows('README.md'):
        if row.startswith('| [@') and (match := issue_link.search(row)):
            numbers.add(int(match[1]))
    for row in changed_rows('tracker/activity.tsv'):
        fields = row.split('\t')
        if len(fields) == 4 and fields[2].isdigit():
            numbers.add(int(fields[2]))
    return numbers


def commit_message(repo):
    authors = {}
    for number in sorted(changed_issues(repo)):
        try:
            issue = json.loads(gh_output(['gh', 'api', f'repos/{repo}/issues/{number}']))
        except subprocess.CalledProcessError as exc:
            if '(HTTP 404)' in exc.stderr or '(HTTP 410)' in exc.stderr:
                continue  # A deleted issue can still have rows to remove.
            raise
        user = issue.get('user')
        if user and user['type'] == 'User' and user['login'] != 'ghost':
            authors[user['id']] = user['login']

    trailers = [f'Co-authored-by: {login} <{user_id}+{login}@users.noreply.github.com>'
                for user_id, login in sorted(authors.items())]
    return '\n'.join(['Update replay contributor credits', '', *trailers]).rstrip()


if __name__ == '__main__':
    print(commit_message(os.environ['GITHUB_REPOSITORY']))
