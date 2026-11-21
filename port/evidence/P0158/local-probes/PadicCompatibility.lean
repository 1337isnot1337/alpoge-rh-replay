import Mathlib.NumberTheory.Padics.PadicVal.Basic

example (z : ℤ) (hz : z ≠ 0) : (padicValInt 2 z : ℕ∞) = emultiplicity (2 : ℤ) z := by
  haveI : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
  rw [padicValInt,
    multiplicity_eq_emultiplicity (Int.natAbs_ne_zero.mpr hz), Int.emultiplicity_natAbs]
  rfl

example (e : ℕ) (he : e ≠ 0) : (padicValNat 2 e : ℕ∞) = emultiplicity (2 : ℤ) (e : ℤ) := by
  haveI : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
  rw [Nat.padicValNat_def, multiplicity_eq_emultiplicity he, ← Int.natCast_emultiplicity]
  rfl

example (e : ℕ) : padicValNat 2 e ≤ Nat.log 2 e := by
  rw [Nat.padicValNat_def]
  exact multiplicity_le_nat_log e

example (j : ℕ) : padicValNat 2 (2 ^ j) = j := by
  haveI : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
  rw [Nat.padicValNat_def, Nat.multiplicity_prime_pow]
