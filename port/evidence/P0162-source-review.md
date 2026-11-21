# P0162 source and statement review

The packet has 64 target modules and 47 project prerequisites. All 111 pristine source hashes match `tracker/modules.jsonl.gz`. The repository's known reused-name scan finds no occurrence of `IsLattice`, `IsAddTorsionFree`, or `IsMulTorsionFree` in that closure. The accompanying source-closure review records each checked hash. This is a review of the listed compatibility risks, not a general comparison of every Mathlib declaration.

The five patches preserve every theorem statement. Four change proofs only. The fifth adds `noncomputable` to one definition without changing its name, type, or body. No source import header, elaboration budget, or replay pin changes.

## M164152: explicit arguments in the surjectivity proof

`HolomorphicIsolatedFibreOpen.proof` applies the existing `ProperHolomorphicSurjective.Statement` hypothesis. Its later mapping and properness arguments already require the range `ball (g u) ε`; the patch supplies that range explicitly.

For the nonempty-domain witness, the old proof applies `mem_ball_self` directly to the goal `u ∈ g ⁻¹' ball (g u) ε`. The target elaborator repeatedly unfolds the metric while trying to infer the ball center. The patch first uses `change g u ∈ ball (g u) ε`, then applies the same `mem_ball_self hε`. Membership in a preimage reduces to membership of the image, so these goals are definitionally equal. The witness remains `u`, and its other membership proof remains unchanged.

The actual legacy-source profiler identified this nonempty witness as the timeout site. Scratch diagnostics used a separate module header to reduce local import memory; that header is absent from the patch. Final acceptance requires the complete packet build with the original source headers and the original heartbeat limit.

## M164165: coordinate projection

The target [`contDiff_apply`](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Analysis/Calculus/ContDiff/Operations.lean) takes a family of codomain types. Replacing its old second argument `ℝ` with `(fun _ => ℝ)` specifies the same coordinate projection from `Fin n → ℝ` to `ℝ`.

## M164192: TFAE indices

The target [`List.TFAE.out`](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Data/List/TFAE.lean) uses indices starting at one. The replacement `.out 1 5` selects the same first and fifth propositions as the old `.out 0 4`: being a principal ideal ring and principality of the maximal ideal. The reverse implication used by the proof is unchanged.

## M164319: product bound and composition source

[`Finset.prod_le_prod₀`](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Algebra/Order/BigOperators/GroupWithZero/Finset.lean) retains the original proof's two hypotheses: nonnegativity and the pointwise bound. The patch changes the theorem name and retains both arguments.

The [`DifferentiableOn.comp`](https://github.com/leanprover-community/mathlib4/blob/fc4f59e577feb1a4956671bc04ac18aaaf8cd842/Mathlib/Analysis/Calculus/FDeriv/Comp.lean) call now supplies `(s := U ×ˢ {s : ℂ | s ≠ 0})`. This is the product set already required by the goal and the original membership proof. Supplying it earlier lets Lean identify the conjunction before elaborating its projections. The composed functions, domain, and proof arguments remain unchanged.

## M164467: noncomputable sequence definition

`seqWithLimit` contains real division. Adding `noncomputable` prevents Lean from requesting an executable implementation of that operation for this definition. The complete defining expression remains:

```lean
insert 0 (Set.range fun n : ℕ => fun _ : Fin 1 =>
  ((1 / ((n : ℝ) + 1) : ℝ) : ℂ))
```

The defining equality is still proved by `rfl`. No axiom, assumption, or replacement value is introduced.

## Evidence boundary

The local probes explain the mechanical changes. The complete CI artifact, checked against the frozen candidate manifest, supplies the final compilation evidence. The eventual full-port axiom audit and Mathlib-only statement comparison remain separate maintainer checks. This packet does not establish a verdict on the claimed RH proof and earns no replay credit.
