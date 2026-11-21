# P0128 statement compatibility review

All 108 pinned source files were hash-checked before editing. Among the 64 packet
targets, M090336 is the only module that uses a known reused Mathlib name. Its
`Submodule.IsLattice` uses must retain the original full-span condition. The
other reused-name occurrence in the closure is in the already ported prerequisite
M006436; that landed patch supplies the corresponding torsion-free proof facts.
No target source contains `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`, or
`implemented_by` tokens.

## M090336: full rational lattices

The module is
`Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.RelIndexDualSubmoduleInfOfSelfDual`.
Every lattice mentioned here is a submodule `L : Submodule ℤ V` of an additive
commutative group with a rational module structure.

At the replay Mathlib pin, `Submodule.IsLattice ℚ L` has exactly two fields:
`L.FG` and `Submodule.span ℚ (L : Set V) = ⊤`. At the target pin,
`Submodule.IsLattice ℚ L` has a different meaning: finite generation and
preservation of linear independence under extension of scalars. Full rational
span is expressed by `Submodule.IsFullLattice ℚ L`.

For the existing integer/rational scalar pair, the old predicate and the target
full-lattice predicate are equivalent. Starting from the old two fields,
`Submodule.IsLattice.of_fg ℚ` supplies the target independence field because ℚ
is the fraction field of ℤ; the same full-span equality supplies the remaining
field. Conversely, a target full lattice has the original finite-generation and
full-span fields. This argument uses only the existing assumptions. It does not
add a finite-dimensionality, independence, or freeness hypothesis.

The patch therefore replaces each type-level `.IsLattice ℚ` with
`.IsFullLattice ℚ`, including the intermediate set predicate in `card_selfDual_le`.
The affected declaration statements are:

- `isLattice_of_fg_dualSubmodule`
- `exists_basis_span_eq_of_isLattice`
- `finrank_eq_of_isLattice`
- `isLattice_dualSubmodule`
- `relIndex_ne_zero_of_isLattice`
- `relIndex_dualSubmodule`
- `relIndex_dualSubmodule_inf_of_selfDual`

Their names, quantifiers, ambient types, remaining assumptions and conclusions
are preserved. The predicate spelling expresses the same full-lattice
conditions as the pinned source. The statement of `card_selfDual_le` does not
mention the lattice predicate and is unchanged.

The two constructor proofs use `Submodule.IsLattice.of_fg ℚ` to fill the new
independence field from the same finite-generation facts. Proof-local
`Module.Finite ℤ L` and `Module.Free ℤ L` facts restore the facts formerly supplied
by the old lattice instances; the target declarations are ordinary theorems
`Submodule.IsLattice.finite` and `.free`. These derived facts introduce no new
assumption. No definition or theorem name is changed.

Exact Mathlib sources:

- [Replay lattice definition](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Algebra/Module/Lattice.lean).
- [Target lattice definition and fraction-field construction](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Algebra/Module/Lattice/Basic.lean).
- [Target full-lattice definition](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Algebra/Module/Lattice/Full.lean).

The counting proof now supplies the source set of `Set.encard_le_encard`
explicitly before Lean elaborates the projection `hM.2`. The set is exactly the
existing union index predicate: full lattice, contained in `L`, and relative
index `m`. The same projection discards the full-lattice condition, so the subset
proof and resulting inequality are unchanged. This proof-only annotation fixes
an unresolved expected type reported by the complete original-header build.

## M089534: underlying sheaf projection

The module is
`Development.AbelianVarietyTheory.Proofs.SatakeParameters.SubsingletonObjOfIsEmpty`.
Its theorem `subsingleton_obj_of_isEmpty` concludes
`Subsingleton (G.val.obj (op U))`. At the replay Mathlib pin, the deprecated
abbreviation `Sheaf.val (F : Sheaf J A)` is defined to be exactly `F.obj`.
The target removes that abbreviation and retains the same full-subcategory
object projection.

Replacing `G.val.obj (op U)` with `G.obj.obj (op U)` therefore substitutes the
old abbreviation's body. The two conclusions are definitionally equal. Every
binder, hypothesis and proof byte is preserved, and the sheaf or presheaf itself
does not change.

Exact Mathlib sources:

- [Replay Sheaf.val abbreviation](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/CategoryTheory/Sites/Sheaf.lean).
- [Target sheaf definition and object projection](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/CategoryTheory/Sites/Sheaf.lean).

## M090732: formal partial-derivative parameter

The module is
`Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.IsUnitDetOfProductMapNeZero`.
The conclusion of `GlobalTheory.DiscrJacobian.associated_discr_norm_jacobian`
contains `pderiv R j (f i)`. At the target Mathlib pin the coefficient ring
parameter of `MvPowerSeries.pderiv` became implicit, while the variable index
remains explicit. The repair writes `pderiv (R := R) j (f i)`, preserving the
ring, index, power series and resulting derivation.

The exact old and target source blocks defining `pderiv` and its underlying
function `pderivFun` are byte-identical. The old declaration is preceded by
`variable (R) in`; the target uses the surrounding implicit `R`. Thus the changed
conclusion applies the same formal partial derivative in the same determinant.
The other three parameter-spelling changes are in the proof. All theorem names,
binders, hypotheses and remaining conclusion text are unchanged.

The same module has three proof-only ideal-theorem migrations. The old algebra
specializations are now named
`Ideal.isMaximal_under_of_isIntegral_of_isMaximal` and
`Ideal.isMaximal_of_isIntegral_of_isMaximal_under`. Their `Ideal.under` is the
same inverse image along the existing algebra map as the source's `Ideal.comap`.
The explicit base-ring arguments select the existing algebra structures;
maximality, primality and integrality hypotheses are already present.

Exact Mathlib sources:

- [Replay partial derivative](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/RingTheory/MvPowerSeries/Derivative.lean).
- [Target partial derivative](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/RingTheory/MvPowerSeries/Derivative.lean).
- [Target integral ideal theorems](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/RingTheory/Ideal/GoingUp.lean).

## Proof-only finite-product APIs

M091528 replaces two `Finset.one_le_prod` calls with `Finset.one_le_prod₀`.
M091792 replaces one `Finset.prod_le_prod` call with `Finset.prod_le_prod₀`.
The target versions apply to real numbers with nonnegative multiplication; they
retain the same pointwise lower bounds or nonnegativity and comparison premises
used by the source. The product expressions and their bounds are unchanged.
No definition or theorem statement changes in either module.

The exact target declarations are in
[Mathlib/Algebra/Order/BigOperators/GroupWithZero/Finset.lean](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Algebra/Order/BigOperators/GroupWithZero/Finset.lean).

## Proof-only matrix elaboration repairs

M090143 adds `Function.swap` to one existing simplification set so the remaining
transposed-matrix applications reduce to the same entries with swapped indices.
M091441 qualifies `Matrix.mul_apply`, `Matrix.map_apply` and `Matrix.one_apply`
in one existing simplification step. This selects the intended matrix-entry
lemmas instead of homonymous function lemmas. Both original identities,
congruence steps, definitions, theorem statements and assumptions are unchanged.
Neither repair changes an import, source header, Lean option or heartbeat limit.

## Required elaborated IsLattice audit

The complete original-header rerun at commit
`76932d45b947f835b4327ac9a9f8d1c134e60fb2` built all 64 target modules
successfully, including all seven repairs and the 57 unchanged modules. It then
ran the exact upstream `port/islattice_audit.lean` over all 64 built targets.
The audit reported `islattice-audit: 64 module(s), 0 hit(s)` and exited with
status 0. Source and object hashes were unchanged during the audit.

The audit checks elaborated statement types and definition bodies for
`Submodule.IsLattice`; theorem proof bodies may use its new API legitimately.
The original artifact preserves the exact script, runner, complete audit log,
module list, command, exit status and source/object hashes. The audit script
SHA-256 is `aa5d944f11e687880959ea125061ef562594ba8352076da4b83e2f496cb9e39b`.

The latest upstream scanner at
`67be0d3a90f3d5df3291a2452a12ed387d2080e0` also checks `eLpNorm` semantics.
It finds no occurrence of that name in the 108-source closure. The only flagged
pinned modules remain M090336 and the preserved landed prerequisite M006436,
whose respective lattice and torsion-free uses are reviewed above. No target
or prerequisite port record or patch changed between the CI base and this
submission base.

The maintainer's final Mathlib-only statement comparison and axiom audit remain
separate checks. A successful port and this required audit do not establish a
verdict on the claimed RH proof.
