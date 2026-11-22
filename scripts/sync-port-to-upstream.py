#!/usr/bin/env python3
"""Sync landed Lean 4.36 port patches from alpoge-rh-replay onto a branch of
leanprover-community/riemann-hypothesis (or a fork such as rohanarun/riemann-hypothesis).

Usage:
  python3 scripts/sync-port-to-upstream.py \
      --upstream-repo /Users/rohanarun/riemann-hypothesis \
      --base origin/main \
      --branch port/lean-4.36 \
      [--push fork] \
      [--dry-run]

What it does:
1. Reads target Lean & Mathlib pins from port/target.json.
2. Reads all landed port/patches/M*.json and M*.patch files.
3. Creates/resets <branch> from <base> in <upstream-repo>.
4. Updates lean-toolchain and lakefile.toml to the target Lean 4.36 / Mathlib pins.
5. Applies every landed .patch whose target file still exists in <upstream-repo>/src/
   (automatically skipping modules pruned on upstream main).
6. Collects contributor Co-authored-by trailers from git history of port/patches/.
7. Commits all changes cleanly (and optionally pushes to --push <remote>).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPLAY_ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=check)


def patch_target_path(patch_text: str) -> str | None:
    for line in patch_text.splitlines():
        if line.startswith('+++ '):
            path = line[4:].split('\t')[0].strip()
            if path.startswith('b/'):
                path = path[2:]
            return path
    return None


def collect_coauthors(replay_root: Path) -> list[str]:
    proc = run(
        ['git', '-C', str(replay_root), 'log', '--format=%an <%ae>', '--', 'port/patches'],
        check=False,
    )
    if proc.returncode != 0:
        return []
    seen: set[str] = set()
    coauthors: list[str] = []
    for line in proc.stdout.splitlines():
        author = line.strip()
        if not author or author in seen:
            continue
        if 'noreply.github.com' in author and author.startswith('github-actions'):
            continue
        seen.add(author)
        coauthors.append(author)
    return sorted(coauthors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--upstream-repo', type=Path, required=True,
                        help='Local clone of leanprover-community/riemann-hypothesis')
    parser.add_argument('--base', default='origin/main',
                        help='Base ref in upstream repo (default: origin/main)')
    parser.add_argument('--branch', default='port/lean-4.36',
                        help='Target branch name to create/reset (default: port/lean-4.36)')
    parser.add_argument('--push', default='',
                        help='Remote name to force-push the synced branch to (e.g. fork)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Check patch applicability without creating a commit or pushing')
    args = parser.parse_args()

    upstream = args.upstream_repo.resolve()
    if not (upstream / '.git').exists():
        raise SystemExit(f'Not a git repo: {upstream}')

    target = json.loads((REPLAY_ROOT / 'port' / 'target.json').read_text())
    lean_ver = target['lean']
    mathlib_rev = target['mathlib']

    patches_dir = REPLAY_ROOT / 'port' / 'patches'
    json_files = sorted(patches_dir.glob('M*.json'))
    patch_files = sorted(patches_dir.glob('M*.patch'))
    print(f'Found {len(json_files):,} port records ({len(patch_files):,} .patch files) in {patches_dir}')

    # Ensure clean working tree in upstream repo
    st = run(['git', '-C', str(upstream), 'status', '--porcelain'])
    if st.stdout.strip():
        raise SystemExit(f'Upstream repo has uncommitted changes:\n{st.stdout[:400]}')

    # Checkout fresh branch from base
    print(f'Checking out {args.branch} from {args.base} in {upstream}...')
    run(['git', '-C', str(upstream), 'checkout', '-B', args.branch, args.base])

    # Update lean-toolchain
    tc_path = upstream / 'lean-toolchain'
    tc_path.write_text(lean_ver + '\n')

    # Update Mathlib rev in lakefile.toml
    lf_path = upstream / 'lakefile.toml'
    lf_text = lf_path.read_text()
    new_lf, n_sub = re.subn(
        r'(name\s*=\s*"mathlib"[^\[]*?rev\s*=\s*")([0-9a-f]{40})(")',
        rf'\g<1>{mathlib_rev}\g<3>',
        lf_text,
        count=1,
        flags=re.S,
    )
    if n_sub != 1:
        raise SystemExit('Failed to update mathlib rev in lakefile.toml')
    lf_path.write_text(new_lf)

    applied: list[str] = []
    skipped_pruned: list[str] = []
    failed: list[tuple[str, str]] = []

    for pf in patch_files:
        mid = pf.stem
        rel = patch_target_path(pf.read_text())
        if not rel or not (upstream / rel).is_file():
            skipped_pruned.append(mid)
            continue
        res = run(['git', '-C', str(upstream), 'apply', '--whitespace=nowarn', str(pf)], check=False)
        if res.returncode == 0:
            applied.append(mid)
        else:
            # Fallback to GNU patch -p1 for non-git unified diffs if needed
            res2 = run(['patch', '-p1', '--forward', '--no-backup-if-mismatch', '-d', str(upstream), '-i', str(pf)], check=False)
            if res2.returncode == 0:
                applied.append(mid)
            else:
                failed.append((mid, (res.stderr or res2.stdout or res2.stderr).strip()[:200]))

    print(f'\nPatch sync summary:')
    print(f'  Applied cleanly : {len(applied):,}')
    print(f'  Skipped (pruned): {len(skipped_pruned):,}')
    print(f'  Failed          : {len(failed):,}')
    for mid, err in failed[:20]:
        print(f'    FAIL {mid}: {err}')

    if failed:
        print(f'\nWARNING: {len(failed)} patch(es) failed to apply cleanly.')

    if args.dry_run:
        run(['git', '-C', str(upstream), 'reset', '--hard', args.base])
        print('\nDry run complete (working tree reset).')
        return 1 if failed else 0

    coauthors = collect_coauthors(REPLAY_ROOT)
    trailers = '\n'.join(f'Co-authored-by: {a}' for a in coauthors)
    msg = (
        f'Port {len(json_files):,} modules ({len(applied):,} patched) to {lean_ver}\n\n'
        f'Synced from rohanarun/alpoge-rh-replay port/patches/ onto {args.base}.\n'
        f'- Lean toolchain: {lean_ver}\n'
        f'- Mathlib rev: {mathlib_rev}\n'
        f'- Applied patches: {len(applied):,} (skipped {len(skipped_pruned):,} upstream-pruned)\n\n'
        f'{trailers}\n'
    )

    run(['git', '-C', str(upstream), 'add', '-A'])
    run(['git', '-C', str(upstream), 'commit', '-m', msg])
    sha = run(['git', '-C', str(upstream), 'rev-parse', '--short', 'HEAD']).stdout.strip()
    print(f'\nCommitted {sha} on branch {args.branch}!')

    if args.push:
        print(f'Pushing {args.branch} to {args.push}...')
        run(['git', '-C', str(upstream), 'push', '-f', args.push, f'{args.branch}:{args.branch}'])
        print(f'Pushed {args.branch} -> {args.push}!')

    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
