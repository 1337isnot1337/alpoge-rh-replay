#!/usr/bin/env bash
# Usage: audit/comparator/run-poc.sh <tools-dir>
# Runs the pinned comparator on the three Mathlib-free projects in poc/ and checks that it rejects
# `cheat` and `weakened` and accepts `honest`. Prints REPLAY_COMPARATOR_POC_PASSED only if all three do.
# Uses the elan and ELAN_HOME of the calling environment; the projects pin Lean v4.33.1.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd -P)"
mkdir -p "${1:?Supply a directory for the comparator tools}"
tools="$(cd "$1" && pwd -P)"

fail() { echo "REPLAY_COMPARATOR_POC_FAILED: $1" >&2; exit 1; }
source "$here/build-tools.sh"

export ELAN_HOME="${ELAN_HOME:-$HOME/.elan}"
check_systemd
build_tools "$tools"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
chmod 755 "$work"

# name, expected exit (0 = accept, 1 = reject), line comparator must print
cases=(
  "cheat 1 Illegal axiom detected: 'cheat'"
  "weakened 1 Const does not match between challenge and target 'Claim'"
  "honest 0 Your solution is okay!"
)
bad=0
for c in "${cases[@]}"; do
  read -r name want marker <<<"$c"
  [[ "$(cat "$here/poc/$name/lean-toolchain")" == "$toolchain" ]] || fail "poc/$name does not pin $toolchain"
  cp -a "$here/poc/$name" "$work/$name"
  rm -rf "$work/$name/.lake"
  echo "== $name (expect $([[ $want == 0 ]] && echo accept || echo reject))"
  set +e
  run_sandboxed "$work/$name" config.json 2>&1 | tee "$work/$name.log"
  rc=${PIPESTATUS[0]}
  set -e
  echo "exit=$rc"
  if [[ ( $want == 0 && $rc != 0 ) || ( $want != 0 && $rc == 0 ) ]]; then
    echo "MISMATCH: poc/$name exited $rc" >&2
    bad=1
  elif ! grep -qF -- "$marker" "$work/$name.log"; then
    echo "MISMATCH: poc/$name did not print: $marker" >&2
    bad=1
  fi
done
[[ $bad == 0 ]] || fail "comparator did not behave as poc/results.txt says"
echo REPLAY_COMPARATOR_POC_PASSED
