import Mathlib.Algebra.MvPolynomial.Basic

variable {σ R : Type} [CommSemiring R]

-- Exact body of MvPolynomial.coeff at the replay's pinned Mathlib commit.
def oldCoeff (e : σ →₀ ℕ) (p : MvPolynomial σ R) : R :=
  @DFunLike.coe ((σ →₀ ℕ) →₀ R) _ _ _ (AddMonoidAlgebra.coeff p) e

example (e : σ →₀ ℕ) (p : MvPolynomial σ R) : oldCoeff e p = p.coeff e := rfl

example (e : σ →₀ ℕ) (p : MvPolynomial σ R) : R := p.coeff e

-- The coefficient update also applies under the product shape in SymMat/SymDMat.
example (n : ℕ) (e : Fin n →₀ ℕ) (β : Fin n → ℕ) (c : Fin n → Fin n → R) :
    oldCoeff e (∏ m : Fin n, (∑ a : Fin n, MvPolynomial.C (c a m) * MvPolynomial.X a) ^ β m) =
      (∏ m : Fin n, (∑ a : Fin n, MvPolynomial.C (c a m) * MvPolynomial.X a) ^ β m).coeff e := rfl
