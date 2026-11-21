import Mathlib

/-! Trusted challenge for `leanprover/comparator`: the four statement definitions copied verbatim from the
published `Statements.lean` (SHA-256 79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf) and the five
public theorems of `Main` with `sorry`. Comparator checks that the solution uses exactly these constants. -/

def RiemannZetaZerosOnLine : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * ((n : ℂ) + 1)) → s ≠ 1 → s.re = 1 / 2

def DirichletLNonvanishingRightOfHalf : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),
    1 / 2 < s.re → (χ ≠ 1 ∨ s ≠ 1) → DirichletCharacter.LFunction χ s ≠ 0

def DirichletLZerosOnLine : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),
    0 < s.re → s.re < 1 → DirichletCharacter.LFunction χ s = 0 → s.re = 1 / 2

def PrimitiveDirichletLZerosOnLine : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N), χ.IsPrimitive →
    ∀ s : ℂ, 0 < s.re → s.re < 1 → DirichletCharacter.LFunction χ s = 0 → s.re = 1 / 2

theorem riemannHypothesis : RiemannHypothesis := sorry

theorem riemannZeta_eq_zero_re : RiemannZetaZerosOnLine := sorry

theorem LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf := sorry

theorem LFunction_eq_zero_re : DirichletLZerosOnLine := sorry

theorem LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine := sorry
