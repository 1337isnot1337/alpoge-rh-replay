import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset

example (f : Fin 5 → ℕ) (hfin : ∀ i, f i ≤ 2) :
    (∏ i, f i) ≤ ∏ _i : Fin 5, 2 :=
  Finset.prod_le_prod₀ (fun _ _ => Nat.zero_le _) (fun i _ => hfin i)
