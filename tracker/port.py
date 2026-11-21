"""Pick and reserve porting work (see PORTING.md).

  python3 tracker/port.py next [--limit 10]   # shallowest open packets with no open Port issue
  python3 tracker/port.py show P0123          # modules, depth, and port status of one packet
  python3 tracker/port.py claim P0123         # open a 'Port P0123' issue with the port label

A packet is done when every module has port/patches/<ID>.json. Ports go in import-depth
order, so `next` only offers packets whose project imports are already ported.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

import tasks

ROOT = Path(__file__).resolve().parent.parent
PATCHES = ROOT / 'port' / 'patches'
TRIAGE = ROOT / 'port' / 'triage' / 'results.json'


def ported():
    return {p.stem for p in PATCHES.glob('M*.json')}


def triage():
    if not TRIAGE.exists():
        return {}
    return {r['id']: r['status'] for r in json.loads(TRIAGE.read_text())['results']}


def port_issues():
    taken = set()
    for issue in tasks.open_issues():
        if 'pull_request' in issue:
            continue
        match = re.fullmatch(r'Port (P\d{4}|M\d{6})', issue['title'])
        if match:
            taken.add(match[1])
    return taken


def packets(rows):
    groups = {}
    for row in rows:
        groups.setdefault(row['packet'], []).append(row)
    return groups


def ready(packet_rows, done):
    """Every project import outside the packet must already be ported."""
    inside = {r['id'] for r in packet_rows}
    for row in packet_rows:
        for dep in row['imports']:
            if dep not in inside and dep not in done:
                return False
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    nxt = sub.add_parser('next'); nxt.add_argument('--limit', type=int, default=10)
    show = sub.add_parser('show'); show.add_argument('packet')
    claim = sub.add_parser('claim'); claim.add_argument('packet')
    args = parser.parse_args()

    rows = list(tasks.module_rows())
    by_id = {r['id']: r for r in rows}
    done, status = ported(), triage()
    groups = packets(rows)

    if args.command == 'show':
        for r in sorted(groups.get(args.packet, []), key=lambda r: r['id']):
            state = 'ported' if r['id'] in done else status.get(r['id'], 'untriaged')
            print(r['id'], r['depth'], state, r['module'])
        return
    if args.command == 'claim':
        if not re.fullmatch(r'P\d{4}|M\d{6}', args.packet) or (args.packet not in groups and args.packet not in by_id):
            raise SystemExit('Unknown packet or module ID')
        if args.packet in port_issues():
            raise SystemExit('Already reserved by an open Port issue')
        subprocess.run(['gh', 'issue', 'create', '--repo', tasks.repo, '--title', f'Port {args.packet}',
                        '--label', 'port', '--body', 'Porting this packet to the target in port/target.json. See PORTING.md.'],
                       check=True)
        return
    taken = port_issues()
    choices = []
    for packet, members in groups.items():
        if packet in taken or all(r['id'] in done for r in members) or not ready(members, done):
            continue
        depth = max(r['depth'] for r in members)
        failing = sum(status.get(r['id']) == 'fail' for r in members)
        choices.append((depth, -failing, packet, len(members), failing))
    for depth, _, packet, size, failing in sorted(choices)[:args.limit]:
        print(f'{packet}\tdepth {depth}\t{size} modules\t{failing} known failing on the target')


if __name__ == '__main__':
    main()
