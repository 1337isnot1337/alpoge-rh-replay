# Sourced by run-comparator.sh and run-poc.sh: the pinned tools and the sandboxed comparator run.
# Needs `fail` defined by the caller, elan on PATH and ELAN_HOME set.

toolchain="leanprover/lean4:v4.33.1"
comparator_rev="3927ad383f208ae977c340a91c48ac9b497d2097"   # leanprover/comparator tag v4.33.0
lean4export_rev="15f6055e299ad5b89345e533cc2192f4cc00f659"  # pinned by that tag's lake-manifest.json
landrun_rev="ec104f6edc1e14d7fec6d31146f1ec6f9c192c5a"      # Zouuup/landrun main, as comparator's README requires

clone_at() {
  local url="$1" rev="$2" dir="$3"
  [[ -d "$dir/.git" ]] || git clone -q "$url" "$dir"
  git -C "$dir" fetch -q origin
  git -C "$dir" checkout -q --force --detach "$rev"
  [[ "$(git -C "$dir" rev-parse HEAD)" == "$rev" ]] || fail "$url is not at $rev"
  [[ -z "$(git -C "$dir" status --porcelain --untracked-files=no)" ]] || fail "$dir has modified tracked files"
}

# build_tools <tools-dir>: sets comparator_bin, lean4export_bin, landrun_bin.
# comparator v4.33.0 is built with Lean v4.33.1; README.md ("Why Lean 4.33.1") explains why that is sound.
build_tools() {
  local tools="$1"
  command -v elan >/dev/null || fail "elan is not on PATH"
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
}

# check_systemd: the AF_UNIX guard needs systemd-run unless COMPARATOR_NO_SYSTEMD=1.
check_systemd() {
  [[ "${COMPARATOR_NO_SYSTEMD:-0}" == 1 ]] && return
  command -v systemd-run >/dev/null || fail "systemd-run is required (comparator README run command); COMPARATOR_NO_SYSTEMD=1 skips it"
}

# run_sandboxed <project-dir> <config.json name>: runs comparator in the project, returns its exit code.
# Default is comparator's README line (`systemd-run --user`). COMPARATOR_SYSTEMD=system applies the same
# AF_UNIX restriction through the system manager (sudo, still as the calling user) for machines without a
# systemd user session, such as CI runners. COMPARATOR_NO_SYSTEMD=1 drops the guard.
run_sandboxed() {
  local proj="$1" config="$2" elan_bin run_cmd
  elan_bin="$(dirname "$(command -v elan)")"
  run_cmd="elan run $toolchain lake env '$comparator_bin' '$config'"
  if [[ "${COMPARATOR_NO_SYSTEMD:-0}" == 1 ]]; then
    echo "WARNING: running without the systemd-run AF_UNIX guard from comparator's README" >&2
    (cd "$proj" && COMPARATOR_LANDRUN="$landrun_bin" COMPARATOR_LEAN4EXPORT="$lean4export_bin" bash -c "$run_cmd")
    return
  fi
  local scope=(--user)
  [[ "${COMPARATOR_SYSTEMD:-user}" == system ]] && scope=(--uid="$(id -u)" --gid="$(id -g)")
  local runner=(systemd-run)
  [[ "${COMPARATOR_SYSTEMD:-user}" == system ]] && runner=(sudo systemd-run)
  "${runner[@]}" --property=RestrictAddressFamilies=~AF_UNIX "${scope[@]}" --pipe --wait --quiet \
    -E PATH="$elan_bin:/usr/local/bin:/usr/bin:/bin" -E ELAN_HOME="$ELAN_HOME" -E XDG_CACHE_HOME="${XDG_CACHE_HOME:-$HOME/.cache}" -E HOME="$HOME" \
    -E COMPARATOR_LANDRUN="$landrun_bin" -E COMPARATOR_LEAN4EXPORT="$lean4export_bin" \
    --working-directory "$proj" -- bash -c "$run_cmd"
}
