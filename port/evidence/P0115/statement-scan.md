# P0115 statement compatibility

The build scope contains all 45 live packet members and their 43 external
prerequisites. All 88 pinned source hashes were checked against the module
ledger. The 19 packet members listed in `port/pruned.txt` are excluded and are
not represented as compiled modules. The source scan found no uses of the
known reused names `IsLattice`, `IsAddTorsionFree`, or `IsMulTorsionFree` in this
closure.

## M051585: finite product comparison

The patch replaces `Finset.prod_le_prod` with `Finset.prod_le_prod₀` in the proof
of `summable_pi_prod`. The existing proof supplies both the nonnegativity of
each left factor and the comparison of corresponding factors. The target
lemma takes exactly those two arguments. No theorem statement or definition
changes, and every other proof step is unchanged.

The target declaration is in
[Mathlib's finite products with zero](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Algebra/Order/BigOperators/GroupWithZero/Finset.lean).

## M053945: removed scalar action alias

The patch replaces two occurrences of `DistribMulAction.toAddMonoidHom` with
`DistribSMul.toAddMonoidHom`. One occurrence is in the statement of
`trace_lattice_eq`; the other is in the proof-local equality `hφ`.

At the replay Mathlib pin, the removed declaration was already a deprecated
alias with this complete definition body:

```lean
DistribSMul.toAddMonoidHom A x
```

The replacement therefore denotes the same additive homomorphism, whose
underlying map is scalar multiplication by `x`. Its conversion by
`toIntLinearMap` and the trace of that linear map are unchanged. The target
declaration uses the same scalar multiplication and additive structure. No
type, hypothesis, quantifier, index, or conclusion is added or removed. This
is a definitional replacement, not an additional mathematical assumption.

The pinned alias is in the
[replay action definitions](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Algebra/GroupWithZero/Action/Defs.lean).
The replacement is in the
[target action definitions](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Algebra/GroupWithZero/Action/Defs.lean).
The downloaded replay file has SHA-256
`a93ae4530f70b40200c9c9f1aced293b3ceaacd73058887f0d4d7878489a5b24`.

## Remaining source scope

The other live targets retain their pinned source text. Existing prerequisite
patches are applied from landed records and are preserved byte for byte. The
two candidate diffs introduce no proof holes, axioms, unsafe declarations,
`native_decide`, or `implemented_by`. This source comparison and the bounded
reused-name scan do not replace the maintainer's final axiom audit or
Mathlib-only statement comparison.
