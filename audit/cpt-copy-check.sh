#!/usr/bin/env bash
# Audit the declarations added at build time by `cpt_copy_thms` in `CutMainCpt.lean:945` (M146056)
# without loading project frontend extensions, and replay `CutMainCpt.olean` through `leanchecker`.
#
# Run through `lake env` from the replay's `lean/` directory after building `CutMainCpt` (or `Main`):
#
#   lake build +Formalism.HermitianCurvature.HermitianCurvatureProofs.CutMainCpt:olean
#   lake env bash /path/to/audit/cpt-copy-check.sh [OUTPUT_JSON]
#
# If OUTPUT_JSON is supplied, `AuditCutMainCpt.lean` also writes the full JSON manifest there.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd -P)"
: "${LEAN_PATH:?run this script through lake env}"
json_out="${1:-}"

digest() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | cut -d' ' -f1
  else
    shasum -a 256 "$1" | cut -d' ' -f1
  fi
}

check_source() {
  local id="$1" expected="$2" rel="$3"
  [[ -f "$rel" ]] || { echo "missing source file $rel ($id); run from the replay's lean/ directory" >&2; exit 1; }
  local actual
  actual="$(digest "$rel")"
  if [[ "$actual" != "$expected" ]]; then
    echo "source SHA-256 mismatch for $id ($rel): expected $expected, got $actual" >&2
    exit 1
  fi
}

# Verify the four `Cut*Cpt*` sources against their pinned archive digests in tracker/modules.jsonl.gz.
check_source M145590 2142903f6f9f969f51e2129acd7b8b00db9d3e99dacacd5c512f33654b1c0b31 \
  src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutCptCopy.lean
check_source M145591 6579b8acd326a8ae17b69d16c2268126d28f384be6a1d86c741eccf02b378e82 \
  src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutCptDefs.lean
check_source M145592 e0606c482c5dc3e336331095207a0ddde048cd4af9d84e791384f6754081d984 \
  src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutCptManual.lean
check_source M146056 97fbcae09ea8fb69e40390016b724e65ecb0bbf324e8f6ccdd075e9f0074a93b \
  src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutMainCpt.lean
echo "CPT_COPY_SOURCE_HASHES_VERIFIED"

lean --version

if [[ -n "$json_out" ]]; then
  mkdir -p "$(dirname "$json_out")"
  lean --tstack=400000 --run "$here/AuditCutMainCpt.lean" --json "$json_out"
else
  lean --tstack=400000 --run "$here/AuditCutMainCpt.lean"
fi

LEAN_NUM_THREADS="${LEAN_NUM_THREADS:-1}" leanchecker --verbose \
  Formalism.HermitianCurvature.HermitianCurvatureProofs.CutMainCpt
echo "CPT_COPY_KERNEL_REPLAY_PASSED"
