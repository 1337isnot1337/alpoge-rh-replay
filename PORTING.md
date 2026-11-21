# Porting track: newer Lean and Mathlib

This is an optional track, separate from the replay. The replay checks the archive **exactly as published**, on Lean 4.33.1 and the pinned Mathlib commit, and nothing here changes it. Port work never earns replay credit. It never touches `verify.sh`, `Audit.lean`, `parts.sha256`, the claims bot or the completed ledger.

The port asks a different question: does the same proof still go through on a current toolchain? A port also lets newer checkers read the result. Lean 4.34.0 fixed three kernel soundness issues, and some v4.36.0 checkers cannot read 4.33-era files.

## Target

`port/target.json` records the target:

- **Lean:** `leanprover/lean4:v4.36.0`, the latest stable release (2026-11-16).
- **Mathlib:** not pinned yet. The first port PR pins it: the newest Mathlib `master` commit whose `lean-toolchain` is `v4.36.0`, with its full commit hash. A maintainer reviews that choice before any other port work merges.

Retargeting to a later release is a separate PR that updates `port/target.json` and says which landed patches need rework.

## Unit of work

Work in **packets**, the same 64-module groups the replay uses (`python3 tracker/tasks.py show P0123`), in import-depth order. A module can only be ported once everything it imports is ported, so start at depth 0 and move up. `python3 tracker/tasks.py next --cold` lists shallow packets.

Each ported module is stored as a **patch against its pinned source**, not as a copy of the archive:

```
port/patches/<ModuleId>.patch       # unified diff against the pinned source file
port/patches/<ModuleId>.json        # {"module", "source_sha256", "lean", "mathlib", "notes"}
```

`source_sha256` must equal the module's hash in `tracker/modules.jsonl.gz`, so a patch always applies to the published file. If a module needs no changes, add only the `.json` with `"notes": "unchanged"`.

## Claim and submit

1. **Reserve.** Open an issue titled `Port P0123` (or `Port M000123` for one module) and add the label `port`. The replay claims bot ignores these titles, and maintainers resolve overlaps: the earlier open issue wins. Close the issue if you stop.
2. **Port.** Use a fresh checkout of the pinned archive with the target toolchain and Mathlib. Fix each module until `lake build +<Module>:olean` succeeds.
3. **Submit a PR to `main`** that adds the packet's `port/patches/` files and links the issue. Include the build transcript for every module in the packet, ending in success, plus the exact toolchain and Mathlib commit.

## Rules a port PR must follow

- **No `sorry`, `admit`, new `axiom`, `@[implemented_by]`, `native_decide` or `unsafe`** that the original module didn't have.
- **Don't change statements.** Proofs may change freely. A changed definition, theorem statement or instance needs a `notes` entry explaining why it is equivalent. Any change to `Main`, `Statements` or the five public theorems is reviewed separately and will usually be refused.
- **Keep it mechanical.** Prefer the smallest change: renamed lemmas, changed tactic behavior, new implicit arguments. Don't refactor or golf proofs as part of a port.
- **One packet per PR.** That keeps review and rework manageable.

## When the port is complete

When every module has a patch or an `unchanged` record, a maintainer assembles the ported tree from the pinned archive plus the patches. They then build `Main`, run the axiom audit and the Mathlib-only statement comparison, and run the independent checkers on the target toolchain. That result is reported **separately** from the replay's own verdict.
