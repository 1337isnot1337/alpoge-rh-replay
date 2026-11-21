# P0158 source review

The 64 target files and their 36 project prerequisites were fetched from the pinned source mirror at commit `8ec38f92ac54b5c91bc07f4f6f88ea61691b7975`. Each file's SHA-256 was checked against `tracker/modules.jsonl.gz` before compilation.

No file in this 100-file source closure uses `IsLattice`, `IsAddTorsionFree`, or `IsMulTorsionFree`, the reused names listed in `tracker/port_build.py` at replay commit `2187a604f76741e64a5e17ab0d3ea9dc1477ab37`.

The 64 pristine target files contain no `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, or `implemented_by` tokens. Candidate unified diffs are separately checked by the repository's `validate_patch_content` function.

The first local build was interrupted during resource diagnosis without obtaining a compiler verdict. It is not success evidence. Only complete CI evidence that passes the finalizer's source, toolchain, dependency, and log checks may produce port records.

## Proof edits

`M161230` changes only the proof of `good_bot`: applying `Eq.symm` in a separate tactic allows the expected generating set to be inferred before Lean elaborates `hx.1`. A narrow Lean 4.36.0 test with `Mathlib.LinearAlgebra.Span.Defs` reproduced the original projection error and compiled the corrected proof. No declaration statement or definition is changed.

`M161355` uses `p.coeff 0` instead of the removed `coeff 0 p` in the proof of `isUnit_of_degreeOf_eq_zero`. The coefficient equivalence below applies. No declaration statement or definition is changed.

`M161393` changes the theorem name from `Finset.prod_le_prod` to `Finset.prod_le_prod₀`, retaining the same two arguments proving nonnegativity and the pointwise bound. A narrow target-toolchain test reproduced the old call's failure and compiled the replacement. No declaration statement or definition is changed.

`M161399` changes only proofs: the four valuation sites explicitly rewrite computational `padicValNat` values to the extensionally equal `multiplicity` values through `Nat.padicValNat_def`, use the corresponding multiplicity lemmas, or unfold the current `padicValInt` definition. All four proof patterns compiled in a narrow target-toolchain test. The definition and theorem statements in the packet remain unchanged.

## Definition-body equivalence for the coefficient API

The source at the replay-pinned [Mathlib commit](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Algebra/MvPolynomial/Basic.lean) defines `MvPolynomial.coeff e p` as application of `AddMonoidAlgebra.coeff p` to `e`. In target Mathlib, `p.coeff e` is the same field application. A narrow Lean 4.36.0 probe copies the exact old accessor body under the local name `oldCoeff` and proves `oldCoeff e p = p.coeff e` by `rfl`. It also proves this equality for the product expression shape used by `SymMat` and `SymDMat`.

`M161432` changes the bodies of `SymMat` and `SymDMat` only to use that target coefficient API. The polynomial products, exponents, coefficient indices, parameters, and declared result types are unchanged. The definition bodies are definitionally equivalent through the accessor identity.

`M161571` changes the body of the proposition `CoordChangeCoeff` only from `coeff e H` to `H.coeff e`. Every quantifier, polynomial expression, exponent, and other proposition is unchanged. This definition is definitionally equivalent through the same accessor identity.

The accompanying full-packet CI artifact supplies the module compilation results. The narrow API probes are explanatory evidence and do not replace full-module compilation.
