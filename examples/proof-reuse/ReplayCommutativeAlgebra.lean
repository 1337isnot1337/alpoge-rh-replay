import Mathlib

namespace ReplayCommutativeAlgebra

open IsLocalRing

universe u

/-- An element of a number field admits a positive integral denominator. -/
theorem exists_nat_mul_isIntegral {E : Type*} [Field E] [NumberField E] (x : E) :
    ∃ D : ℕ, 0 < D ∧ IsIntegral ℤ ((D : E) * x) := by
  obtain ⟨n, hn, -, hi⟩ := NumberField.exists_nat_le_mulHeight₁ x
  exact ⟨n, Nat.pos_of_ne_zero hn, hi⟩

/-- Replacing a basis vector by a vector with nonzero coordinate there still spans the space. -/
theorem span_insert_image_erase_eq_top {K V : Type*} [Field K] [AddCommGroup V]
    [Module K V] {N : ℕ} (b : Module.Basis (Fin N) K V) (v : V) {j : Fin N}
    (hj : b.repr v j ≠ 0) :
    Submodule.span K (insert v (⇑b '' ↑(Finset.univ.erase j))) = ⊤ := by
  classical
  set W := Submodule.span K (insert v (⇑b '' ↑(Finset.univ.erase j))) with hW
  have hb : ∀ i, i ≠ j → b i ∈ W := fun i hi =>
    Submodule.subset_span (Set.mem_insert_of_mem _ ⟨i, by simp [hi], rfl⟩)
  have hvW : v ∈ W := Submodule.subset_span (Set.mem_insert _ _)
  have hbj : b j ∈ W := by
    have h1 : ∑ i, b.repr v i • b i = v := b.sum_repr v
    rw [← Finset.add_sum_erase _ _ (Finset.mem_univ j)] at h1
    have h2 : b.repr v j • b j ∈ W := by
      rw [eq_sub_of_add_eq h1]
      exact W.sub_mem hvW (W.sum_mem fun i hi => W.smul_mem _ (hb i (Finset.ne_of_mem_erase hi)))
    have h3 := W.smul_mem (b.repr v j)⁻¹ h2
    rwa [smul_smul, inv_mul_cancel₀ hj, one_smul] at h3
  rw [eq_top_iff, ← b.span_eq, Submodule.span_le]
  rintro _ ⟨i, rfl⟩
  by_cases hi : i = j
  · subst hi; exact hbj
  · exact hb i hi

/-- Quotienting a local ring by an element of its maximal ideal gives a local ring. -/
theorem isLocalRing_quotient_span_singleton {R : Type*} [CommRing R] [IsLocalRing R]
    {x : R} (hx : x ∈ maximalIdeal R) : IsLocalRing (R ⧸ Ideal.span ({x} : Set R)) := by
  have hne : Ideal.span ({x} : Set R) ≠ ⊤ := fun h => by
    have hle : Ideal.span ({x} : Set R) ≤ maximalIdeal R :=
      Ideal.span_le.mpr (Set.singleton_subset_iff.mpr hx)
    rw [h] at hle
    exact (inferInstance : (maximalIdeal R).IsMaximal).ne_top (top_le_iff.mp hle)
  have : Nontrivial (R ⧸ Ideal.span ({x} : Set R)) := Ideal.Quotient.nontrivial_iff.mpr hne
  exact IsLocalRing.of_surjective' (Ideal.Quotient.mk _) Ideal.Quotient.mk_surjective

/-- The maximal ideal of a Noetherian local ring vanishes if it is contained in its square. -/
theorem maximalIdeal_eq_bot_of_le_sq (R : Type*) [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] (h : maximalIdeal R ≤ maximalIdeal R ^ 2) : maximalIdeal R = ⊥ := by
  apply Submodule.eq_bot_of_le_smul_of_le_jacobson_bot (maximalIdeal R) (maximalIdeal R)
    (IsNoetherian.noetherian _)
  · rw [pow_two] at h
    exact h
  · exact (IsLocalRing.jacobson_eq_maximalIdeal ⊥ bot_ne_top).ge

/-- Prime avoidance selects an element of the maximal ideal outside its square and every minimal prime. -/
theorem exists_mem_maximalIdeal_notMem_sq_notMem_minimalPrimes (R : Type*) [CommRing R]
    [IsLocalRing R] [IsNoetherianRing R] (hsq : ¬ maximalIdeal R ≤ maximalIdeal R ^ 2)
    (hmin : ¬ ∃ p ∈ minimalPrimes R, maximalIdeal R ≤ p) :
    ∃ x, x ∈ maximalIdeal R ∧ x ∉ maximalIdeal R ^ 2 ∧ ∀ p ∈ minimalPrimes R, x ∉ p := by
  classical
  have hfin : (minimalPrimes R).Finite := minimalPrimes.finite_of_isNoetherianRing R
  by_contra hcon
  push Not at hcon
  have hsub : ((maximalIdeal R : Set R)) ⊆ ⋃ i ∈ (↑(insert (maximalIdeal R ^ 2) hfin.toFinset) :
      Set (Ideal R)), (i : Set R) := by
    intro z hz
    simp only [Set.mem_iUnion]
    by_cases h2 : z ∈ maximalIdeal R ^ 2
    · exact ⟨maximalIdeal R ^ 2, by simp, h2⟩
    · obtain ⟨p, hp, hzp⟩ := hcon z hz h2
      exact ⟨p, by simp [hp], hzp⟩
  obtain ⟨i, hi, hle⟩ := (Ideal.subset_union_prime (f := fun i : Ideal R => i)
    (maximalIdeal R ^ 2) (maximalIdeal R ^ 2) (by
      intro i hi hne _
      rw [Finset.mem_insert, Set.Finite.mem_toFinset] at hi
      exact Ideal.IsMinimalPrime.isPrime (hi.resolve_left hne))).mp hsub
  rw [Finset.mem_insert, Set.Finite.mem_toFinset] at hi
  rcases hi with rfl | hi
  · exact hsq hle
  · exact hmin ⟨i, hi, hle⟩

/-- A nonzero vector has a nonzero coordinate in every basis. -/
theorem exists_repr_ne_zero {K V ι : Type*} [Field K] [AddCommGroup V] [Module K V]
    (b : Module.Basis ι K V) {v : V} (hv : v ≠ 0) : ∃ j, b.repr v j ≠ 0 := by
  by_contra h
  simp only [not_exists, ne_eq, not_not] at h
  exact hv (b.repr.map_eq_zero_iff.mp (Finsupp.ext fun j => by simpa using h j))

/-- Removing a nonzero cotangent direction reduces the embedding dimension by at least one. -/
theorem spanFinrank_maximalIdeal_quotient_succ_le (R : Type u) [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] {x : R} (hx : x ∈ maximalIdeal R) (hx2 : x ∉ maximalIdeal R ^ 2)
    [IsLocalRing (R ⧸ Ideal.span ({x} : Set R))] :
    Submodule.spanFinrank (maximalIdeal (R ⧸ Ideal.span ({x} : Set R))) + 1 ≤
      Module.finrank (ResidueField R) (CotangentSpace R) := by
  classical
  let b := Module.finBasis (ResidueField R) (CotangentSpace R)
  have hv : (maximalIdeal R).toCotangent ⟨x, hx⟩ ≠ 0 := by
    rw [Ne, Ideal.toCotangent_eq_zero]; exact hx2
  obtain ⟨j, hj⟩ := exists_repr_ne_zero b hv
  have htop := span_insert_image_erase_eq_top b _ hj
  choose y hy using fun i => (maximalIdeal R).toCotangent_surjective (b i)
  have hcot : Submodule.span (ResidueField R) ((maximalIdeal R).toCotangent ''
      (insert (⟨x, hx⟩ : maximalIdeal R) (y '' ↑(Finset.univ.erase j)))) = ⊤ := by
    refine Eq.trans ?_ htop
    congr 1
    simp only [Set.image_insert_eq, Set.image_image, hy]
  have hspan0 := IsLocalRing.CotangentSpace.span_image_eq_top_iff.mp hcot
  have hspan : Submodule.span R (Subtype.val ''
      (insert (⟨x, hx⟩ : maximalIdeal R) (y '' ↑(Finset.univ.erase j)))) = maximalIdeal R := by
    calc _ = Submodule.map (maximalIdeal R).subtype (Submodule.span R
          (insert (⟨x, hx⟩ : maximalIdeal R) (y '' ↑(Finset.univ.erase j)))) :=
          (Submodule.map_span _ _).symm
      _ = Submodule.map (maximalIdeal R).subtype ⊤ := by rw [hspan0]
      _ = maximalIdeal R := Submodule.map_subtype_top _
  obtain ⟨F, hF⟩ : ∃ F : Finset R, F = (Finset.univ.erase j).image (fun i => (y i : R)) := ⟨_, rfl⟩
  have hm : Ideal.span (insert x (F : Set R)) = maximalIdeal R := by
    refine Eq.trans ?_ hspan
    rw [hF, Finset.coe_image, Set.image_insert_eq, Set.image_image]
  have hcomap : Ideal.comap (Ideal.Quotient.mk (Ideal.span ({x} : Set R)))
      (maximalIdeal (R ⧸ Ideal.span ({x} : Set R))) = maximalIdeal R :=
    IsLocalRing.eq_maximalIdeal (Ideal.comap_isMaximal_of_surjective _ Ideal.Quotient.mk_surjective)
  have hx0 : Ideal.Quotient.mk (Ideal.span ({x} : Set R)) x = 0 :=
    Ideal.Quotient.eq_zero_iff_mem.mpr (Ideal.mem_span_singleton_self x)
  have hQ : maximalIdeal (R ⧸ Ideal.span ({x} : Set R)) =
      Ideal.span ((F.image (Ideal.Quotient.mk (Ideal.span ({x} : Set R))) : Finset _) :
        Set (R ⧸ Ideal.span ({x} : Set R))) := by
    rw [← Ideal.map_comap_of_surjective _ Ideal.Quotient.mk_surjective
      (maximalIdeal (R ⧸ Ideal.span ({x} : Set R))), hcomap, ← hm, Ideal.map_span,
      Set.image_insert_eq, hx0, Ideal.span_insert, Ideal.span_singleton_eq_bot.mpr rfl, bot_sup_eq,
      Finset.coe_image]
  have hcard : (F.image (Ideal.Quotient.mk (Ideal.span ({x} : Set R)))).card ≤
      Module.finrank (ResidueField R) (CotangentSpace R) - 1 := by
    calc (F.image (Ideal.Quotient.mk (Ideal.span ({x} : Set R)))).card ≤ F.card := Finset.card_image_le
      _ ≤ (Finset.univ.erase j).card := by rw [hF]; exact Finset.card_image_le
      _ = _ := by rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, Fintype.card_fin]
  have hpos : 0 < Module.finrank (ResidueField R) (CotangentSpace R) := Fin.pos j
  rw [hQ]
  have := spanBound (F.image (Ideal.Quotient.mk (Ideal.span ({x} : Set R))))
  omega
where
  spanBound {A : Type u} [CommRing A] (s : Finset A) :
      Submodule.spanFinrank (Ideal.span (s : Set A)) ≤ s.card :=
    (Submodule.spanFinrank_span_le_ncard_of_finite s.finite_toSet).trans_eq (Set.ncard_coe_finset s)

end ReplayCommutativeAlgebra
