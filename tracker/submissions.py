"""Credit replay submissions from claim authors in the public README."""

import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- pending-volunteers-start -->'
END = '<!-- pending-volunteers-end -->'


def pages(repo, route):
    output = subprocess.check_output(
        ['gh', 'api', '--paginate', '--slurp', f'repos/{repo}/{route}'],
        text=True,
    )
    for page in json.loads(output):
        yield from page


def pending_submissions(repo):
    reviewed = set()
    for path in (ROOT / 'evidence/volunteers').glob('*.json'):
        receipt = json.loads(path.read_text())
        reviewed.add((receipt['contributor'].lower(), receipt['packet']))

    for issue in pages(repo, 'issues?labels=claim&state=all&per_page=100'):
        if 'pull_request' in issue:
            continue
        claim = re.fullmatch(r'Claim ([PM][0-9]+)', issue['title'])
        login = issue['user']['login']
        if (not claim or not re.fullmatch(r'[A-Za-z0-9-]+', login)
                or issue['user']['type'] != 'User'
                or (login.lower(), claim[1]) in reviewed):
            continue

        number = int(issue['number'])
        comments = pages(repo, f'issues/{number}/comments?per_page=100')
        submission_ids = [
            int(comment['id'])
            for comment in comments
            if comment['user']['login'] == login
            and comment['body'].splitlines()
            and comment['body'].splitlines()[0].strip().casefold() == 'replay submission'
        ]
        if submission_ids:
            yield number, login, claim[1], max(submission_ids)


def main():
    repo = os.environ['GITHUB_REPOSITORY']
    rows = sorted(pending_submissions(repo))
    lines = ['| Contributor | Task | Review |', '|---|---|---|']
    for number, login, task, comment in rows:
        link = f'https://github.com/{repo}/issues/{number}#issuecomment-{comment}'
        lines.append(f'| [@{login}](https://github.com/{login}) | [{task}]({link}) | Pending review |')

    readme = ROOT / 'README.md'
    current = readme.read_text()
    rendered = '\n'.join(lines) if rows else 'No submissions awaiting review.'
    updated = current[:current.index(START) + len(START)]
    updated += '\n\n' + rendered + '\n\n' + current[current.index(END):]
    if updated != current:
        readme.write_text(updated)


if __name__ == '__main__':
    main()
