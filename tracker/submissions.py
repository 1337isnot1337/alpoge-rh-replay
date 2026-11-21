"""Show active replay claims and submissions in the public README."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

from claim_comments import comments_by_issue, repository_comments
from volunteer_tables import update_reviewed, update_table

ROOT = Path(__file__).resolve().parents[1]
ATTEMPTS = 4


def rate_limit_delay(stderr, attempt):
    """Seconds to wait before retrying a rate-limited gh call, or None for other failures."""
    if 'rate limit' not in stderr.lower():
        return None
    try:
        resources = json.loads(subprocess.check_output(['gh', 'api', 'rate_limit'], text=True))['resources']
        resets = [int(resources[name]['reset']) for name in ('core', 'graphql')
                  if resources[name]['remaining'] == 0]
    except (subprocess.CalledProcessError, KeyError, TypeError, ValueError):
        resets = []
    if resets:
        return max(1, max(resets) - int(time.time()) + 1)
    return 60 * 2 ** attempt


def gh_output(command):
    """Run a read-only gh command and return its stdout, waiting out GitHub rate limits."""
    for attempt in range(ATTEMPTS):
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        delay = rate_limit_delay(result.stderr, attempt)
        if delay is None or attempt == ATTEMPTS - 1:
            sys.stderr.write(result.stderr)
            raise subprocess.CalledProcessError(result.returncode, command, result.stdout, result.stderr)
        print(f'GitHub rate limit on `{" ".join(command[:3])}`. Retrying after {delay}s.', file=sys.stderr, flush=True)
        time.sleep(delay)


def pages(repo, route):
    for page in json.loads(gh_output(['gh', 'api', '--paginate', '--slurp', f'repos/{repo}/{route}'])):
        yield from page


def claim_snapshot(repo):
    issues = [issue for issue in pages(repo, 'issues?labels=claim&state=all&per_page=100')
              if 'pull_request' not in issue]
    histories = comments_by_issue(issues, repository_comments(lambda route: pages(repo, route)))
    return issues, histories


def volunteer_updates(repo, issue_authors, snapshot=None):
    issues, histories = claim_snapshot(repo) if snapshot is None else snapshot
    reviewed = set()
    for path in (ROOT / 'evidence/volunteers').glob('*.json'):
        receipt = json.loads(path.read_text())
        reviewed.add((receipt['contributor'].lower(), receipt['packet']))

    candidates = []
    for issue in issues:
        user = issue.get('user') or {}
        login = user.get('login') or ''
        if user.get('type') != 'User' or not login:
            continue
        if login != 'ghost' and isinstance(user.get('id'), int):
            issue_authors[str(issue['number'])] = (user['id'], login)

        claim = re.fullmatch(r'Claim (P\d{4}|M\d{6})', issue['title'])
        if not claim or not re.fullmatch(r'[A-Za-z0-9-]+', login) or (login.lower(), claim[1]) in reviewed:
            continue

        candidates.append((issue, login, claim[1]))

    for issue, login, target in candidates:
        number = issue['number']
        comments = histories[number]
        submission_ids = [
            int(comment['id'])
            for comment in comments
            if comment['user']['login'] == login
            and comment['body'].splitlines()
            and comment['body'].splitlines()[0].strip().casefold() == 'replay submission'
        ]
        if submission_ids:
            yield number, login, target, max(submission_ids)
        elif issue['state'] == 'open' and any(label['name'] == 'claim-granted' for label in issue['labels']):
            prefix = f'Granted `{target}`.'
            if any(comment['user']['login'] == 'github-actions[bot]' and comment['body'].startswith(prefix)
                   for comment in comments):
                yield number, login, target, None


def main(update_activity=False):
    repo = os.environ['GITHUB_REPOSITORY']
    snapshot = claim_snapshot(repo)
    issue_authors = {}
    claimed = ['| Contributor | Task | Status |', '|---|---|---|']
    pending = ['| Contributor | Task | Review |', '|---|---|---|']
    for number, login, task, comment in sorted(volunteer_updates(repo, issue_authors, snapshot)):
        link = f'https://github.com/{repo}/issues/{number}'
        person = f'[@{login}](https://github.com/{login})'
        if comment is None:
            claimed.append(f'| {person} | [{task}]({link}) | Claimed |')
        else:
            pending.append(f'| {person} | [{task}]({link}#issuecomment-{comment}) | Pending review |')

    readme = ROOT / 'README.md'
    current = readme.read_text()
    updated = update_table(ROOT, current, 'active-volunteers', claimed)
    updated = update_table(ROOT, updated, 'pending-volunteers', pending)
    updated = update_reviewed(ROOT, updated)
    if updated != current:
        readme.write_text(updated)
    if update_activity:
        from activity import update
        update(repo, snapshot)
    return issue_authors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--issue-authors', type=Path, help='Write claim issue authors to this JSON file')
    parser.add_argument('--update-activity', action='store_true',
                        help='Refresh the chart and roster using the same claim snapshot')
    args = parser.parse_args()
    issue_authors = main(args.update_activity)
    if args.issue_authors:
        args.issue_authors.write_text(json.dumps(issue_authors))
