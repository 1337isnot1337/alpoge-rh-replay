#!/usr/bin/env bash
set -euo pipefail
record="$(cd "$(dirname "$0")" && pwd -P)"
work="${1:?Supply an empty directory path on a large Linux build volume}"
mkdir -p "$work"
work="$(cd "$work" && pwd -P)"
if [[ -n "$(ls -A "$work")" ]]; then
  echo "Choose an empty directory for this independent replay." >&2
  exit 1
fi
exec > >(tee "$work/replay.log") 2>&1
export ELAN_HOME="$work/elan"
export XDG_CACHE_HOME="$work/cache"
mkdir "$work/parts"
cd "$work/parts"
while read -r hash part; do
  curl --fail --location --retry 4 --output "$part" "https://alpo.ge/lean.tar.gz.$part"
done < "$record/parts.sha256"
sha256sum -c "$record/parts.sha256"
cat part* | tar -xz --no-same-owner -C "$work"
cd "$work/lean"
test "$(cat lean-toolchain)" = "leanprover/lean4:v4.33.1"
lean --version
lake exe cache get
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = "0df444a360eaa60ab8c11dca51a86af692955474"
if [[ "${2:-}" == "--prepare-only" ]]; then echo "Prepared project in $work/lean"; exit 0; fi
lake build +Main:olean
echo REPLAY_SOURCE_BUILD_PASSED
lake env lean "$record/Audit.lean"
echo REPLAY_AXIOM_AUDIT_PASSED
lake env leanchecker --fresh Main
echo REPLAY_FRESH_KERNEL_PASSED
