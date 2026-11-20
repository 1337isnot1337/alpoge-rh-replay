"""Show active replay claims and submissions in the public README."""

import json
import os
from pathlib import Path
import re
import subprocess

from claim_comments import COMMENT_FEED, comments_by_issue

ROOT = Path(__file__).resolve().parents[1]


def pages(repo, route):
    output = subprocess.check_output(
        ['gh', 'api', '--paginate', '--slurp', f'repos/{repo}/{route}'],
        text=True,
    )
    for page in json.loads(output):
        yield from page


def volunteer_updates(repo):
    reviewed = set()
    for path in (ROOT / 'evidence/volunteers').glob('*.json'):
        receipt = json.loads(path.read_text())
        reviewed.add((receipt['contributor'].lower(), receipt['packet']))

    candidates = []
    for issue in pages(repo, 'issues?labels=claim&state=all&per_page=100'):
        if 'pull_request' in issue:
            continue
        claim = re.fullmatch(r'Claim (P\d{4}|M\d{6})', issue['title'])
        login = issue['user']['login']
        if (not claim or not re.fullmatch(r'[A-Za-z0-9-]+', login)
                or issue['user']['type'] != 'User'
                or (login.lower(), claim[1]) in reviewed):
            continue

        candidates.append((issue, login, claim[1]))

    histories = comments_by_issue((issue for issue, _, _ in candidates), pages(repo, COMMENT_FEED))
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


def replace_section(text, marker, lines, empty):
    start = f'<!-- {marker}-start -->'
    end = f'<!-- {marker}-end -->'
    rendered = '\n'.join(lines) if len(lines) > 2 else empty
    return text[:text.index(start) + len(start)] + '\n\n' + rendered + '\n\n' + text[text.index(end):]


def main():
    repo = os.environ['GITHUB_REPOSITORY']
    claimed = ['| Contributor | Task | Status |', '|---|---|---|']
    pending = ['| Contributor | Task | Review |', '|---|---|---|']
    for number, login, task, comment in sorted(volunteer_updates(repo)):
        link = f'https://github.com/{repo}/issues/{number}'
        person = f'[@{login}](https://github.com/{login})'
        if comment is None:
            claimed.append(f'| {person} | [{task}]({link}) | Claimed |')
        else:
            pending.append(f'| {person} | [{task}]({link}#issuecomment-{comment}) | Pending review |')

    readme = ROOT / 'README.md'
    current = readme.read_text()
    updated = replace_section(current, 'active-volunteers', claimed, 'No active claims awaiting evidence.')
    updated = replace_section(updated, 'pending-volunteers', pending, 'No submissions awaiting review.')
    if updated != current:
        readme.write_text(updated)


if __name__ == '__main__':
    main()
