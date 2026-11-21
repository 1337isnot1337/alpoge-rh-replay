# P0122 source review

P0122 has 64 live packet members and no pruned members at the preparation base
`9a157d64bc3c855beb81945a4b46e3b2d64be66a`. Fifty target records are already
landed, all marked `unchanged`; this submission is intended to add the remaining
14 records. Every live member is included in the fresh packet build.

The complete import closure contains 121 pinned source files. Each was checked
against its SHA-256 in `tracker/modules.jsonl.gz` before being copied to the
fresh project. The source mirror is pinned at
`8ec38f92ac54b5c91bc07f4f6f88ea61691b7975`. The six existing prerequisite patches
for M005725, M069416, M070042, M070165, M070632, and M172240 are applied without
changing their bytes or records. No replay pin or replay ledger is changed.

The 121-file closure has no occurrence of `IsLattice`, `IsAddTorsionFree`,
`IsMulTorsionFree`, or `eLpNorm`. The complete hash-verified closure was checked
again with the upstream reused-name scanner from `f7b6ec1e`, including its new
warning about the changed nonmeasurable-function behavior of `eLpNorm`.
All 121 pristine source files contain no `sorry`, `admit`, `axiom`,
`native_decide`, `unsafe`, or `implemented_by` token. Candidate diffs are also
subject to the repository's `validate_patch_content` check before finalization.

## Coefficient accessor equivalence

M070093 changes exactly three uses of the removed `MvPolynomial.coeff m p`
spelling to `p.coeff m`. The affected declarations are the statement of
`coeff_monomial_two`, the body of the predicate `Good`, and the statement of
`logDefect_coeff_dvd`. No proof body changes.

At the replay-pinned [Mathlib commit](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Algebra/MvPolynomial/Basic.lean),
the removed accessor is defined by applying `AddMonoidAlgebra.coeff p` to the
index `m` through `DFunLike.coe`. The target's field accessor is exactly that
application on the same `MvPolynomial` abbreviation. Copying the pinned
accessor body under a diagnostic name gives an equality to `p.coeff m` proved
by `rfl` on the target toolchain.

In all three changed uses, the polynomial, coefficient index, result type,
quantifiers, and surrounding equality or divisibility expression are retained.
`Good` therefore remains the same predicate, and the two theorem statements
remain the same propositions by definitional equality.

The full candidate body, together with the exact imported project prerequisite
declarations, passed a narrow-import Lean 4.36.0 diagnostic in 3.530 seconds.
That diagnostic uses a `module` header to limit local import memory use; the
actual candidate preserves the pinned source's legacy header and original
imports. An earlier legacy diagnostic was stopped by its 60-second time bound
before producing a compiler verdict. These diagnostics explain the repair;
the complete original-header CI run described below establishes packet completion.

## Identity scalar map in M069414

The target `MultilinearMap` structure takes an explicit scalar ring homomorphism.
The single changed result-type line selects `RingHom.id A` in `altMultilinear`.
The identity homomorphism reduces the new scalar compatibility field to the
pinned equation `f (update m i (c • x)) = c • f (update m i x)`. Its function and
additive fields have the same types as in the replay-pinned structure. The
underlying `alt` function, additivity proof, scalar proof, and all theorem
statements and hypotheses are unchanged. This is the same A-multilinear object
expressed in the generalized target type.

An independent review compared the exact old Mathlib structure with the target
structure and confirmed the unchanged definition body and theorem text. A
bounded narrow-import diagnostic accepted the definition and accompanying
proofs. A broader diagnostic under an artificial `module` header encountered a
private-instance reduction limitation at the final theorem; that header is not
part of the patch. The final original-header full-module build passed in
12.195 seconds with the exact reviewed source hash, without that diagnostic
limitation and without any further source change.

## Maximal ideal lemma in M069951

The only change is a proof call to
`Ideal.isMaximal_under_of_isIntegral_of_isMaximal (R := K.O) M`.
The former `comap` name now takes a general ring homomorphism. The target's
algebra-specialized `under` theorem has the intended arguments, and
`Ideal.under` is the comap along the existing `algebraMap`. The existing finite
module fact supplies the same integrality hypothesis; the local maximality
fact is unchanged. Every definition, theorem statement, and assumption is
unchanged. A bounded diagnostic with the same comap goal and hypotheses passed.

## Baseline and final evidence

The original complete baseline artifact checked all 64 live targets and the
121-file source closure on the exact target. It recorded 62 successful modules
and exactly two failures, M069414 and M069951. M070093's coefficient repair
passed its full original-header module in that baseline. The failed baseline
is preserved separately and is not completion evidence. The final candidate
set contains exactly the three patches described above. The final fresh run
compiled all 64 live targets successfully and then ran the exact upstream
elaboration audit on all 64 module names. It reported zero hits and exited 0
in 6.186 seconds. The artifact supplies every successful module transcript,
source and patch hashes, and the source/object bindings checked by the audit.
The 107 landed records and six prerequisite patches in the closure are
preserved exactly.

Final CI: [run 44961800540](https://github.com/1337isnot1337/alpoge-rh-replay/actions/runs/44961800540),
commit `c8c78895dd8d33bd86bae34d3fffefc79842da92`. The original artifact archive
has SHA-256 `f00786a957674e8ced55620374caf5dcba5aaaf7582df499f879e1127e4bb81a`;
all 88 internal file digests were checked before finalization.

## Review of existing prerequisite patches

All six already-landed prerequisite patches were also read. Their changes are
proof-local: the Metric extended-ball API rename, three finite-sum lemma
renames, removal of a redundant terminal `rfl`, and the renamed finite-product
inequality retaining its nonnegativity and pointwise bounds. None changes a
definition body or theorem statement. Their existing record and patch bytes
are preserved exactly.
