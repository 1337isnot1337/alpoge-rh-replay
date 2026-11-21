import Mathlib.LinearAlgebra.Span.Defs

variable {R M : Type} [Semiring R] [AddCommMonoid M] [Module R M]

def IsHomSubFor (P : M → Prop) (N : Submodule R M) : Prop :=
  N = Submodule.span R {x | x ∈ N ∧ P x}

example (P : M → Prop) : IsHomSubFor P (⊥ : Submodule R M) := by
  apply Eq.symm
  exact Submodule.span_eq_bot.2 (fun x hx => (Submodule.mem_bot _).1 hx.1)
