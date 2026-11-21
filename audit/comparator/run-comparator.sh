#!/usr/bin/env bash
# Usage: audit/comparator/run-comparator.sh <prepared-volume> <tools-dir>
# <prepared-volume>: a fresh volume from `./verify.sh <dir> --prepare-only`, with nothing built in lean/.lake/build.
# <tools-dir>: an empty or reused directory for the pinned comparator, lean4export and landrun builds.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd -P)"
vol="$(cd "${1:?Supply the volume prepared by verify.sh --prepare-only}" && pwd -P)"
mkdir -p "${2:?Supply a directory for the comparator tools}"
tools="$(cd "$2" && pwd -P)"

toolchain="leanprover/lean4:v4.33.1"
comparator_rev="3927ad383f208ae977c340a91c48ac9b497d2097"   # leanprover/comparator tag v4.33.0
lean4export_rev="15f6055e299ad5b89345e533cc2192f4cc00f659"  # pinned by that tag's lake-manifest.json
landrun_rev="ec104f6edc1e14d7fec6d31146f1ec6f9c192c5a"      # Zouuup/landrun main, as comparator's README requires

fail() { echo "REPLAY_COMPARATOR_FAILED: $1" >&2; exit 1; }

export ELAN_HOME="$vol/elan"
export XDG_CACHE_HOME="$vol/cache"
[[ -d "$vol/lean" && -d "$ELAN_HOME" ]] || fail "$vol is not a volume prepared by verify.sh --prepare-only"
[[ "$(cat "$vol/lean/lean-toolchain")" == "$toolchain" ]] || fail "unexpected lean-toolchain"
[[ ! -e "$vol/lean/.lake/build" ]] ||
  fail "$vol/lean/.lake/build exists: project code was built outside the sandbox, use a fresh prepared volume"
command -v elan >/dev/null || fail "elan is not on PATH"
if [[ "${COMPARATOR_NO_SYSTEMD:-0}" != 1 ]]; then
  command -v systemd-run >/dev/null || fail "systemd-run is required (comparator README run command); COMPARATOR_NO_SYSTEMD=1 skips it"
fi

clone_at() {
  local url="$1" rev="$2" dir="$3"
  [[ -d "$dir/.git" ]] || git clone -q "$url" "$dir"
  git -C "$dir" fetch -q origin
  git -C "$dir" checkout -q --force --detach "$rev"
  [[ "$(git -C "$dir" rev-parse HEAD)" == "$rev" ]] || fail "$url is not at $rev"
  [[ -z "$(git -C "$dir" status --porcelain --untracked-files=no)" ]] || fail "$dir has modified tracked files"
}

clone_at https://github.com/leanprover/comparator "$comparator_rev" "$tools/comparator"
(
  cd "$tools/comparator"
  echo "$toolchain" > lean-toolchain
  elan run "$toolchain" lake build lean4export comparator
)
[[ "$(git -C "$tools/comparator/.lake/packages/lean4export" rev-parse HEAD)" == "$lean4export_rev" ]] ||
  fail "lean4export is not at $lean4export_rev"
comparator_bin="$tools/comparator/.lake/build/bin/comparator"
lean4export_bin="$tools/comparator/.lake/packages/lean4export/.lake/build/bin/lean4export"

if [[ -n "${COMPARATOR_LANDRUN:-}" ]]; then
  landrun_bin="$COMPARATOR_LANDRUN"
else
  command -v go >/dev/null || fail "go is required to build landrun from source (or set COMPARATOR_LANDRUN)"
  clone_at https://github.com/Zouuup/landrun "$landrun_rev" "$tools/landrun"
  (cd "$tools/landrun" && go build -o "$tools/landrun-bin" ./cmd/landrun)
  landrun_bin="$tools/landrun-bin"
fi
"$landrun_bin" --version >/dev/null 2>&1 || fail "landrun does not run"

proj="$vol/lean-comparator"
[[ ! -e "$proj" ]] || fail "$proj already exists, use a fresh prepared volume"
cp -a "$vol/lean" "$proj"
cp "$here/Challenge.lean" "$proj/src/Challenge.lean"
cp "$here/config.json" "$proj/comparator-config.json"
printf '\n[[lean_lib]]\nname = "Challenge"\nroots = ["Challenge"]\n' >> "$proj/lakefile.toml"

elan_bin="$(dirname "$(command -v elan)")"
run_cmd="elan run $toolchain lake env '$comparator_bin' comparator-config.json"
if [[ "${COMPARATOR_NO_SYSTEMD:-0}" == 1 ]]; then
  echo "WARNING: running without the systemd-run AF_UNIX guard from comparator's README" >&2
  (cd "$proj" && COMPARATOR_LANDRUN="$landrun_bin" COMPARATOR_LEAN4EXPORT="$lean4export_bin" bash -c "$run_cmd") ||
    fail "comparator rejected Main or did not finish"
else
  systemd-run --property=RestrictAddressFamilies=~AF_UNIX --user --pipe --wait --quiet \
    -E PATH="$elan_bin:/usr/local/bin:/usr/bin:/bin" -E ELAN_HOME="$ELAN_HOME" -E XDG_CACHE_HOME="$XDG_CACHE_HOME" -E HOME="$HOME" \
    -E COMPARATOR_LANDRUN="$landrun_bin" -E COMPARATOR_LEAN4EXPORT="$lean4export_bin" \
    --working-directory "$proj" -- bash -c "$run_cmd" ||
    fail "comparator rejected Main or did not finish"
fi
echo REPLAY_COMPARATOR_PASSED
