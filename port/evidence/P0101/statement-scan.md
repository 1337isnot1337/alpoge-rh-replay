# P0101 statement compatibility scan

The live packet consists of 51 modules. The other 13 original packet members
are listed in `port/pruned.txt` at the bound tracker commit and are excluded
from the build and from new port records. The 51 live modules have a complete
100-source project-import closure, including 49 landed prerequisites. None of
those 100 sources is pruned.

All pinned source SHA-256 values were verified against
`tracker/modules.jsonl.gz`. The 49 prerequisites use their landed port records;
seven of them have mechanical patches. Both the pinned closure and the closure
after those landed patches were scanned with the repository's `reused_names`
checker. Neither scan finds `IsLattice`, `IsAddTorsionFree`, or
`IsMulTorsionFree`.

## Reviewed statement spelling changes

`M018206` and `M018208` each replace two removed coefficient accessor calls in
their wrapper theorem statement. At the replay-pinned [Mathlib commit](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Algebra/MvPolynomial/Basic.lean),
`MvPolynomial.coeff e p` is defined by applying `AddMonoidAlgebra.coeff p` to `e`.
Target notation `p.coeff e` is the same application. The exact old accessor body
was checked against that source and its equality to target field notation was
proved by `rfl` in the earlier coefficient compatibility probe. Thus both edited
statement types are definitionally equivalent to their pinned forms.

Every coefficient index, polynomial operand, coefficient ring, quantifier and
hypothesis is preserved. The original proof bodies, imports and options are
byte-unchanged. The corrected wrapper types also match their already landed
prerequisite theorem types: `GlobalTheory.coeff_allOnes_sumAlgEquiv_mkDerivation`
and `GlobalTheory.TriangularityLowCoeff.exists_mul_coeff_eq_zero`, respectively.
Both complete statement types elaborate in narrow diagnostic-only Lean 4.36.0
checks. Those checks do not replace the full original-header module build.

## Reviewed proof-only changes

`M018507` renames three `AddSubmonoidClass.coe_finset_sum` proof references to
`AddSubmonoidClass.coe_finsetSum`. Target Mathlib generates this same coercion
identity from `SubmonoidClass.coe_finsetProd` in
`Mathlib/Algebra/Group/Submonoid/BigOperators.lean`. No declaration changes.

`M018797` supplies the scalar ring before the prime ideal to
`Ideal.ramificationIdx_pos`, matching the target signature. It also removes the
obsolete `ramificationIdx'_eq_ramificationIdx` rewrite after
`HeightOneSpectrum.valuation_liesOver`, whose target statement already has the
`ramificationIdx` exponent. The existing `change` step and `he`/`pow_one` finish
are retained. No declaration changes.

`M019711` renames two `continuousOn_finset_sum` proof references to
`continuousOn_finsetSum`, the target additive counterpart of
`continuousOn_finsetProd` in `Mathlib/Topology/Algebra/Monoid.lean`. The same
finite sets and elementwise continuity proof are retained. No declaration
changes.

## Complete build and elaboration audit

The full original-header CI build at commit
`2fe325b7dca90e391286053ea748c57323b96576` compiled all 51 live targets
successfully. The exact upstream `port/islattice_audit.lean` then inspected all
51 elaborated target modules, including unchanged modules, and reported
`islattice-audit: 51 module(s), 0 hit(s)` with exit status 0. Source and object
hashes were unchanged during the audit.

## Newly flagged eLpNorm dependency

The updated checker from upstream
`f7b6ec1e1791ba2fd7d21a3c42dc1caa8d75174b` finds no `eLpNorm` occurrence in
any of the 51 live target sources. The only occurrence in their complete
100-source closure is the two sides of `eLpNorm_rhoFun` in already-landed
external dependency M101080. Its record and patch are retained byte-for-byte.
Both sides use exponent 2 on functions that are almost everywhere strongly
measurable under the existing hypotheses. The replay and target definitions
therefore reduce to the same `eLpNorm'` integral formula; no extra hypothesis or
source change is needed. The exact pinned-definition and existing-patch review
is preserved in `M101080-eLpNorm-review.md` and its adjacent hash receipt.

The known-name scan and required IsLattice audit do not compare every imported
Mathlib declaration; the maintainer's final statement comparison remains
separate.
