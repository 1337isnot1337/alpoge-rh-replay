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
| `poc/` | Three small projects without Mathlib that show what comparator accepts and rejects |

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

comparator and lean4export are rebuilt with Lean 4.33.1, the project's toolchain; both compile unchanged.

### Requirements from comparator's README
- **Fresh volume.** Nothing from the project may have been built outside the sandbox. `run-comparator.sh` refuses a volume with `lean/.lake/build`. The project's lakefile is TOML, so `--prepare-only` runs no project code.
- **Trusted challenge.** `Challenge.lean` and its imports (Mathlib at the pinned commit) must be trusted.
- **Unprivileged user.** Don't run it as root.
- **AF_UNIX guard.** The script uses comparator's `systemd-run --property=RestrictAddressFamilies=~AF_UNIX` line. `COMPARATOR_NO_SYSTEMD=1` skips it, for test machines without a systemd user session; that is weaker.

## Tested so far

**Mathlib-free projects (`poc/`, `poc/results.txt`)**, run with the exact command above on Linux 7.0:

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
