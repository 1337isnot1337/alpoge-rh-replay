"""Check that open GitHub grants cover exactly the requested replay targets."""

import argparse
from collections.abc import Mapping
import json
import re
import subprocess

if __package__:
    from .tasks import load, repo, select
else:
    from tasks import load, repo, select


def gh_api(route, paginate=False):
    command = ['gh', 'api', route]
    if paginate:
        command += ['--paginate', '--slurp']
    return json.loads(subprocess.check_output(command, text=True))


def check_grants(issue_numbers, targets, owner):
    rows = load()
    covered = set()
    for number in issue_numbers:
        if type(number) is not int or number < 1:
            raise ValueError('Claim issue numbers must be positive integers.')
        route = f'repos/{repo}/issues/{number}'
        issue = gh_api(route)
        claim = re.fullmatch(r'Claim (P\d{4}|M\d{6})', issue['title'])
        if ('pull_request' in issue or issue['state'] != 'open' or not claim
                or issue['user']['login'].casefold() != owner.casefold()
                or not any(label['name'] == 'claim-granted' for label in issue['labels'])):
            raise ValueError(f'Issue #{number} is not an open grant for @{owner}.')

        comments = gh_api(f'{route}/comments?per_page=100', paginate=True)
        prefix = f'Granted `{claim[1]}`.'
        if not any(comment['user']['login'] == 'github-actions[bot]'
                   and comment['body'].startswith(prefix)
                   for page in comments for comment in page):
            raise ValueError(f'Issue #{number} is missing the bot grant for {claim[1]}.')

        modules = {row['module'] for row in select(rows, claim[1])}
        if covered & modules:
            raise ValueError(f'Issue #{number} duplicates another grant in this worker.')
        covered.update(modules)

    if not covered or covered != set(targets) or len(covered) != len(targets):
        raise ValueError('The grants must exactly cover the requested build targets.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=argparse.FileType())
    parser.add_argument('issues', nargs='+', type=int)
    args = parser.parse_args()
    batch = json.load(args.batch)
    if not isinstance(batch, Mapping):
        parser.error('Expected a batch JSON object.')
    owner = gh_api('user')['login']
    try:
        check_grants(args.issues, batch['targets'], owner)
    except ValueError as error:
        parser.exit(1, f'{error}\n')
    print(f'GitHub confirmed {len(args.issues)} grant(s) for @{owner}.')


if __name__ == '__main__':
    main()
