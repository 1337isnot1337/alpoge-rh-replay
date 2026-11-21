#!/usr/bin/env bash
# Usage: audit/comparator/run-comparator.sh <prepared-volume> <tools-dir>
# <prepared-volume>: a fresh volume from `./verify.sh <dir> --prepare-only`, with nothing built in lean/.lake/build.
# <tools-dir>: an empty or reused directory for the pinned comparator, lean4export and landrun builds.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd -P)"
vol="$(cd "${1:?Supply the volume prepared by verify.sh --prepare-only}" && pwd -P)"
mkdir -p "${2:?Supply a directory for the comparator tools}"
tools="$(cd "$2" && pwd -P)"

fail() { echo "REPLAY_COMPARATOR_FAILED: $1" >&2; exit 1; }
source "$here/build-tools.sh"

export ELAN_HOME="$vol/elan"
export XDG_CACHE_HOME="$vol/cache"
[[ -d "$vol/lean" && -d "$ELAN_HOME" ]] || fail "$vol is not a volume prepared by verify.sh --prepare-only"
[[ "$(cat "$vol/lean/lean-toolchain")" == "$toolchain" ]] || fail "unexpected lean-toolchain"
[[ ! -e "$vol/lean/.lake/build" ]] ||
  fail "$vol/lean/.lake/build exists: project code was built outside the sandbox, use a fresh prepared volume"
command -v elan >/dev/null || fail "elan is not on PATH"
check_systemd

build_tools "$tools"

proj="$vol/lean-comparator"
[[ ! -e "$proj" ]] || fail "$proj already exists, use a fresh prepared volume"
cp -a "$vol/lean" "$proj"
cp "$here/Challenge.lean" "$proj/src/Challenge.lean"
cp "$here/config.json" "$proj/comparator-config.json"
printf '\n[[lean_lib]]\nname = "Challenge"\nroots = ["Challenge"]\n' >> "$proj/lakefile.toml"

run_sandboxed "$proj" comparator-config.json || fail "comparator rejected Main or did not finish"
echo REPLAY_COMPARATOR_PASSED
