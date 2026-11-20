#!/usr/bin/env bash
set -euo pipefail
record="$(cd "$(dirname "$0")" && pwd -P)"
work="${1:?Supply an empty directory path on a large Linux build volume}"
if ! command -v elan >/dev/null; then
  echo "Install elan and make it available on PATH before starting the replay." >&2
  exit 1
fi
mkdir -p "$work"
work="$(cd "$work" && pwd -P)"
if [[ -n "$(ls -A "$work")" ]]; then
  echo "Choose an empty directory for this independent replay." >&2
  exit 1
fi
exec > >(tee "$work/replay.log") 2>&1
export ELAN_HOME="$work/elan"
export XDG_CACHE_HOME="$work/cache"

# Integrity pins. Preparing and building execute archive code (tactics,
# macros and `run_cmd` blocks run as the user), and everything that later
# judges the result -- the lean, leanchecker and lake binaries and the
# shared libraries they load, Audit.lean and parts.sha256 -- sits in trees
# that code could in principle rewrite. So the checker binaries and shared
# libraries are pinned to the official release digests, the audit inputs
# are hashed before any archive code runs, and both are re-verified
# immediately before the audit and fresh-kernel stages. The library pins
# matter as much as the binary ones: bin/lean, bin/leanchecker and bin/lake
# are small launchers, and the kernel itself lives in
# lib/lean/libleanshared.so, which they load from the same tree.
#
# The digests are those of bin/lean, bin/leanchecker, bin/lake and the
# lib/lean shared libraries in the official lean-4.33.1-linux.tar.zst
# release (Linux x86_64), whose own SHA-256 is
# 890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235
# (https://github.com/leanprover/lean4/releases/tag/v4.33.1). elan does not
# checksum the toolchain it downloads, so the installed binaries and shared
# libraries are checked against these pins instead.
lean_bin_sha256="e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550"
leanchecker_bin_sha256="84bc3e7cd6efa5bfecd1e7c37571fed9428fb2b3e16da0ddf62f2163573486d0"
lake_bin_sha256="60330ab6f07dce20f3fa9ebb08e8b984ea9549eac172afeb15d9d2227060e2b3"
libleanshared_sha256="23d636cac1cadcba37beac30eff9b9b20d66cee726cf5defb4ae39f1284a3e5a"
liblake_shared_sha256="b1d164bf248f35b9e9664e696f4cd05a79a7066065510fb9b459139c78beb354"
libleanshared_1_sha256="2f96493ac9046f64ec7bcb78102a4c1e7cd9a7042487f246af45eda8a96667f5"
libleanshared_2_sha256="2f96493ac9046f64ec7bcb78102a4c1e7cd9a7042487f246af45eda8a96667f5"
libinit_shared_sha256="2f96493ac9046f64ec7bcb78102a4c1e7cd9a7042487f246af45eda8a96667f5"

integrity_failed() {
  echo "REPLAY_INTEGRITY_CHECK_FAILED: $1" >&2
  exit 1
}

digest() { sha256sum "$1" | cut -d' ' -f1; }

# Recompute every recorded digest: the pinned toolchain binaries and shared
# libraries plus Audit.lean and parts.sha256 as they were when the archive
# was verified.
verify_integrity() {
  local toolchain_bin="$ELAN_HOME/toolchains/leanprover--lean4---v4.33.1/bin"
  local toolchain_lib="$ELAN_HOME/toolchains/leanprover--lean4---v4.33.1/lib/lean"
  [[ "$(digest "$toolchain_bin/lean")" == "$lean_bin_sha256" ]] ||
    integrity_failed "bin/lean does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$toolchain_bin/leanchecker")" == "$leanchecker_bin_sha256" ]] ||
    integrity_failed "bin/leanchecker does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$toolchain_bin/lake")" == "$lake_bin_sha256" ]] ||
    integrity_failed "bin/lake does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$toolchain_lib/libleanshared.so")" == "$libleanshared_sha256" ]] ||
    integrity_failed "lib/lean/libleanshared.so does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$toolchain_lib/libLake_shared.so")" == "$liblake_shared_sha256" ]] ||
    integrity_failed "lib/lean/libLake_shared.so does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$toolchain_lib/libleanshared_1.so")" == "$libleanshared_1_sha256" ]] ||
    integrity_failed "lib/lean/libleanshared_1.so does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$toolchain_lib/libleanshared_2.so")" == "$libleanshared_2_sha256" ]] ||
    integrity_failed "lib/lean/libleanshared_2.so does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$toolchain_lib/libInit_shared.so")" == "$libinit_shared_sha256" ]] ||
    integrity_failed "lib/lean/libInit_shared.so does not match the pinned Lean 4.33.1 release digest"
  [[ "$(digest "$record/Audit.lean")" == "$audit_digest" ]] ||
    integrity_failed "Audit.lean changed after the archive was verified"
  [[ "$(digest "$record/parts.sha256")" == "$parts_digest" ]] ||
    integrity_failed "parts.sha256 changed after the archive was verified"
  echo REPLAY_INTEGRITY_CHECK_PASSED
}

# Every dependency Lake resolved must sit at the revision lake-manifest.json
# records, with no tracked file modified. The clean check covers tracked
# files only (--untracked-files=no): Lake and the Mathlib cache write build
# outputs inside these trees, and those are untracked or ignored. The
# project tree itself is pinned by parts.sha256 over the archive it was
# extracted from; if it ever ships as a git checkout, its tracked files
# must be clean too.
verify_pristine_dependencies() {
  local packages_dir name rev dir base checked=0 seen=" "
  packages_dir="$(sed -n 's/.*"packagesDir": "\([^"]*\)".*/\1/p' lake-manifest.json | head -n 1)"
  packages_dir="${packages_dir:-.lake/packages}"
  [[ -d "$packages_dir" ]] ||
    integrity_failed "dependency directory $packages_dir is missing"
  if [[ -d .git && -n "$(git status --porcelain --untracked-files=no)" ]]; then
    integrity_failed "the project tree has modified tracked files"
  fi
  # The manifest is machine-generated: within the packages array each entry
  # lists "rev" before "name". The root project's own trailing "name" lies
  # outside the array and is not a dependency.
  while read -r name rev; do
    dir="$packages_dir/$name"
    [[ -d "$dir/.git" ]] ||
      integrity_failed "dependency $name is missing or is not a git checkout"
    [[ "$(git -C "$dir" rev-parse HEAD)" == "$rev" ]] ||
      integrity_failed "dependency $name is not at the revision lake-manifest.json records ($rev)"
    [[ -z "$(git -C "$dir" status --porcelain --untracked-files=no)" ]] ||
      integrity_failed "dependency $name has modified tracked files"
    checked=$((checked + 1))
    seen+="$name "
  done < <(awk '
    /"packages": \[/ { in_packages = 1 }
    in_packages && /"rev":/ { rev = $0; sub(/.*: "/, "", rev); sub(/".*/, "", rev) }
    in_packages && /"name":/ { name = $0; sub(/.*: "/, "", name); sub(/".*/, "", name); print name, rev }
    in_packages && /^[[:space:]]*\],/ { in_packages = 0 }
  ' lake-manifest.json)
  [[ "$checked" -gt 0 ]] ||
    integrity_failed "no dependencies parsed from lake-manifest.json"
  for dir in "$packages_dir"/*/; do
    base="$(basename "$dir")"
    [[ "$seen" == *" $base "* ]] ||
      integrity_failed "unexpected directory $base in $packages_dir"
  done
  echo REPLAY_DEPENDENCIES_PRISTINE_PASSED
}

mkdir "$work/parts"
cd "$work/parts"
while read -r hash part; do
  curl --fail --location --retry 4 --output "$part" "https://alpo.ge/lean.tar.gz.$part"
done < "$record/parts.sha256"
sha256sum -c "$record/parts.sha256"
audit_digest="$(digest "$record/Audit.lean")"
parts_digest="$(digest "$record/parts.sha256")"
cat part* | tar -xz --no-same-owner -C "$work"
cd "$work/lean"
toolchain="$(cat lean-toolchain)"
test "$toolchain" = "leanprover/lean4:v4.33.1"
elan toolchain install "$toolchain"
elan run "$toolchain" lean --version
verify_integrity
lake_cmd=(elan run "$toolchain" lake)
"${lake_cmd[@]}" exe cache get
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = "0df444a360eaa60ab8c11dca51a86af692955474"
verify_pristine_dependencies
if [[ "${2:-}" == "--prepare-only" ]]; then echo "Prepared project in $work/lean"; exit 0; fi
"${lake_cmd[@]}" build +Main:olean
echo REPLAY_SOURCE_BUILD_PASSED
verify_integrity
verify_pristine_dependencies
"${lake_cmd[@]}" env lean "$record/Audit.lean"
echo REPLAY_AXIOM_AUDIT_PASSED
verify_integrity
"${lake_cmd[@]}" env leanchecker --fresh Main
echo REPLAY_FRESH_KERNEL_PASSED
