# Comparator check of `Main`

This is an additional, independent check of `Main`'s five public theorems with [leanprover/comparator](https://github.com/leanprover/comparator), the Lean FRO's judge for adversarial proofs. It does not change `verify.sh` or any existing marker.

## Why

`Audit.lean` and `audit/CompareMain.lean` are elaborated in a process that imports `Main`, and `leanchecker --fresh` has no axiom allowlist. The minimal repro in #8271 shows what follows: elaborators registered inside a project's import closure can make the axiom audit pass with exit 0 for a theorem that depends on `axiom cheat : False`, and the fresh-kernel stage accepts it too.

Comparator doesn't elaborate anything from the solution in the judging process:
1. It builds `Challenge` and `Main` with Lake inside a [landrun](https://github.com/Zouuup/landrun) sandbox, where only the project's `.lake` is writable.
2. It exports both with `lean4export`, also sandboxed.
3. It checks that every constant in the statements of the five theorems is identical in the trusted `Challenge` and in `Main`.
4. It checks that the proofs use only `propext`, `Quot.sound` and `Classical.choice`.
5. It replays `Main`'s environment in the Lean kernel.

Elaborator overrides, notation, instances and `initialize` blocks in the project can't change any of these steps.

## Files

| File | What it is |
|---|---|
| `Challenge.lean` | `import Mathlib`, the four definitions copied verbatim from the published `Statements.lean` (SHA-256 `79ef7ca7…b47bf`), and the five theorems with `sorry` |
| `config.json` | Comparator config: challenge `Challenge`, solution `Main`, the five names, the three permitted axioms |
| `run-comparator.sh` | Builds pinned comparator, lean4export and landrun, then runs comparator on a copy of a freshly prepared volume |
| `build-tools.sh` | The pins, the tool build and the sandboxed run, shared by the two scripts |
| `poc/` | Three small projects without Mathlib that show what comparator accepts and rejects |
| `run-poc.sh` | Runs comparator on the three `poc/` projects and fails unless each gives its expected result |
| `../../.github/workflows/comparator-poc.yml` | CI job that runs `run-poc.sh` on every change to this directory |

## Run it

```bash
./verify.sh /path/to/fresh-volume --prepare-only
audit/comparator/run-comparator.sh /path/to/fresh-volume /path/to/tools-dir
```

It prints `REPLAY_COMPARATOR_PASSED` only if comparator exits 0. It needs Linux with Landlock (kernel ≥ 5.13), `systemd-run --user`, git, a C toolchain and Go (or `COMPARATOR_LANDRUN=/path/to/landrun`). The check builds all of `Main` inside the sandbox, so it costs about one full source build.

Pins:

| Tool | Version |
|---|---|
| comparator | `3927ad38` (tag v4.33.0) |
| lean4export | `15f6055e` (from that tag's manifest) |
| landrun | `ec104f6e` (main, as comparator's README requires) |

comparator and lean4export are rebuilt with Lean 4.33.1, the project's toolchain; both compile unchanged. The next section explains why.

### Why Lean 4.33.1 for a v4.33.0 tag

comparator has no release for 4.33.1: its tags go from v4.33.0 to v4.34.0. `build-tools.sh` checks out tag v4.33.0 and replaces its `lean-toolchain` with `leanprover/lean4:v4.33.1` before building. We did this on purpose, for three reasons:

1. **lean4export has to be 4.33.1.** It reads the project's `.olean` files, and Lean only loads `.olean` files written by the same Lean version. A lean4export built with 4.33.0 cannot read this project.
2. **No Lean-level API changed.** [v4.33.0...v4.33.1](https://github.com/leanprover/lean4/compare/v4.33.0...v4.33.1) has 14 commits. They touch only `src/kernel/`, `src/runtime/`, `src/include/lean/lean.h`, the CMake files and tests. No `.lean` file under `src/` changed, so comparator and lean4export get the same `Lean` library interface they were written against. Both compile with no source changes.
3. **The replay kernel is the patched one.** Comparator replays the solution in the C++ kernel linked into its binary. The 4.33.1 kernel commits are soundness fixes:
   - `is_prop` requires a sort (lean4#14807, #14843);
   - generated recursors are type-checked (#14808);
   - occurrences of the inductive types being declared are checked for uniformity (#14582);
   - `is_def_eq` caching is order-independent (#14806);
   - the size of `Nat` numbers the kernel computes is bounded (#14849).

   A 4.33.0 build would replay with the kernel that lacks these fixes. The 4.33.1 build checks at least as strictly, and it is the same kernel the project is compiled with.

The `poc/` projects pin 4.33.1 too, and CI runs them with this exact build.

### Requirements from comparator's README
- **Fresh volume.** Nothing from the project may have been built outside the sandbox. `run-comparator.sh` refuses a volume with `lean/.lake/build`. The project's lakefile is TOML, so `--prepare-only` runs no project code.
- **Trusted challenge.** `Challenge.lean` and its imports (Mathlib at the pinned commit) must be trusted.
- **Unprivileged user.** Don't run it as root.
- **AF_UNIX guard.** The script uses comparator's `systemd-run --property=RestrictAddressFamilies=~AF_UNIX` line. On machines without a systemd user session (CI runners), `COMPARATOR_SYSTEMD=system` applies the same property through the system manager with `sudo systemd-run --uid=<you>`, so the job still runs as the unprivileged user. `COMPARATOR_NO_SYSTEMD=1` skips the guard and is weaker.

## Tested so far

**Mathlib-free projects (`poc/`, `poc/results.txt`)**, run with the exact command above on Linux 7.0. CI reruns them on every change to `audit/comparator/` (`comparator-poc.yml`, `run-poc.sh`). The job fails if any project gives a different exit code or message:

| Project | Expected | Result |
|---|---|---|
| `cheat`: `axiom cheat : False` plus `command_elab` overrides for `#print axioms` and `run_cmd`. `Audit.lean`-style checking passes this with exit 0. | reject | `Illegal axiom detected: 'cheat'`, exit 1 |
| `weakened`: the solution redefines the statement as `True` | reject | `Const does not match between challenge and target 'Claim'`, exit 1 |
| `honest`: a real proof | accept | `Your solution is okay!`, exit 0 |

**The real archive project, against the pinned Mathlib**, on a Kaggle CPU machine with `COMPARATOR_NO_SYSTEMD=1`, so without the AF_UNIX guard. `Main` is replaced by a stub that states the five theorems with `sorry`:

| Case | Expected | Result |
|---|---|---|
| Genuine `Statements.lean` | statements match, then `sorryAx` is rejected | `Illegal axiom detected: 'sorryAx'` |
| `RiemannZetaZerosOnLine` with one extra hypothesis | reject at the statement check | `Const does not match between challenge and target 'RiemannZetaZerosOnLine'` |

Comparator checks statements before axioms (`verifyMatch` runs `compareAt`, then `checkAxioms`). So the first case shows that `Challenge.lean` matches the published statements constant for constant.

**Not tested:** the full `Main`. That needs the complete source build inside the sandbox, which is a job for the primary.
