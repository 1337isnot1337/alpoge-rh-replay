#!/usr/bin/env bash
# Smoke tests for verify.sh: direct invocation and per-architecture
# toolchain pin selection. Covers the two regressions a reviewer found
# on the hardening change: verify.sh lost its executable bit (so the
# documented ./verify.sh command failed immediately), and the toolchain
# pins were the Linux x86_64 digests only (so a native Linux AArch64
# setup, as the Docker instructions produce on Apple Silicon, failed
# the first integrity check).
set -uo pipefail
repo="$(cd "$(dirname "$0")/.." && pwd -P)"
pass=0; fail=0
report() { # name ok
  if [[ "$2" == 0 ]]; then echo "PASS  $1"; pass=$((pass+1));
  else echo "FAIL  $1"; fail=$((fail+1)); fi
}

# --- Direct invocation ---------------------------------------------------
[[ -x "$repo/verify.sh" ]]; report "verify.sh is executable" $?
out="$("$repo/verify.sh" 2>&1)"; rc=$?
[[ "$rc" != 0 && "$out" == *"Supply an empty directory path"* ]]
report "direct ./verify.sh invocation reaches the usage check" $?

# --- Pin selection ---------------------------------------------------------
# Extract the shipped pin/function block exactly as verify.sh carries it.
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
awk '/^# Integrity pins\./{f=1} /^mkdir "\$work\/parts"/{f=0} f' \
  "$repo/verify.sh" > "$tmp/funcs.sh"
grep -q "select_toolchain_pins()" "$tmp/funcs.sh"
report "pin block defines select_toolchain_pins" $?

pins_for() { # arch -> "lean leanchecker lake libleanshared" digests
  ( source "$tmp/funcs.sh"
    select_toolchain_pins "$1" >/dev/null 2>&1 || exit 1
    printf '%s %s %s %s' "$lean_bin_sha256" "$leanchecker_bin_sha256" \
      "$lake_bin_sha256" "$libleanshared_sha256" )
}
x86="$(pins_for x86_64)"; rc_x86=$?
arm="$(pins_for aarch64)"; rc_arm=$?
arm_alias="$(pins_for arm64)"; rc_alias=$?
[[ "$rc_x86" == 0 && "$x86" == e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550* ]]
report "x86_64 selects the pinned Linux x86_64 digests" $?
[[ "$rc_arm" == 0 && -n "$arm" && "$arm" != "$x86" ]]
report "aarch64 selects its own, different digests" $?
[[ "$rc_alias" == 0 && "$arm_alias" == "$arm" ]]
report "arm64 selects the aarch64 digests" $?
ok=0
for digest in $arm; do
  [[ "$digest" =~ ^[0-9a-f]{64}$ ]] || ok=1
done
report "aarch64 digests are all SHA-256 shaped" $ok
pins_for riscv64 >/dev/null 2>&1
[[ "$?" != 0 ]]
report "an unsupported architecture is rejected" $?

echo "== verify.sh smoke tests: $pass passed, $fail failed"
[[ "$fail" == 0 ]]
