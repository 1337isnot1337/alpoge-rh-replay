import Mathlib

namespace ReplayAnalysis

open Topology TopologicalSpace Set

/-- A locally compact second-countable Hausdorff space is Polish. -/
theorem polish_of_lcsc (Y : Type*) [TopologicalSpace Y] [LocallyCompactSpace Y] [T2Space Y]
    [SecondCountableTopology Y] : PolishSpace Y := by
  let _ := TopologicalSpace.metrizableSpaceMetric Y
  have hemb : IsEmbedding ((↑) : Y → UniformSpace.Completion Y) :=
    (UniformSpace.Completion.isUniformEmbedding_coe Y).isEmbedding
  have hdense : DenseRange ((↑) : Y → UniformSpace.Completion Y) :=
    UniformSpace.Completion.denseRange_coe
  have hopen : IsOpen (range ((↑) : Y → UniformSpace.Completion Y)) := by
    rw [isOpen_iff_forall_mem_open]
    rintro _ ⟨y, rfl⟩
    obtain ⟨K, hK, hKy⟩ := exists_compact_mem_nhds y
    obtain ⟨V, hVK, hVo, hyV⟩ := mem_nhds_iff.1 hKy
    obtain ⟨U, hUo, hUV⟩ := hemb.isInducing.isOpen_iff.1 hVo
    refine ⟨U, ?_, hUo, ?_⟩
    · have hcl : IsClosed (((↑) : Y → UniformSpace.Completion Y) '' K) :=
        (hK.image hemb.continuous).isClosed
      calc U ⊆ closure (U ∩ range ((↑) : Y → UniformSpace.Completion Y)) :=
            hdense.open_subset_closure_inter hUo
        _ ⊆ closure (((↑) : Y → UniformSpace.Completion Y) '' K) := by
            apply closure_mono
            rintro _ ⟨hz, ⟨z, rfl⟩⟩
            refine ⟨z, hVK ?_, rfl⟩
            rw [← hUV]
            exact hz
        _ = ((↑) : Y → UniformSpace.Completion Y) '' K := hcl.closure_eq
        _ ⊆ range ((↑) : Y → UniformSpace.Completion Y) := image_subset_range _ _
    · show y ∈ ((↑) : Y → UniformSpace.Completion Y) ⁻¹' U
      rw [hUV]
      exact hyV
  have : PolishSpace (range ((↑) : Y → UniformSpace.Completion Y)) := hopen.polishSpace
  exact hemb.toHomeomorph.isClosedEmbedding.polishSpace

/-- An element of an ultrametric normed field integral over the integers has norm at most one. -/
theorem norm_le_one_of_isIntegral {K : Type*} [NormedField K] [IsUltrametricDist K] {x : K} (hx : IsIntegral ℤ x) : ‖x‖ ≤ 1 := by
  have := (Valuation.integer.integers (NormedField.valuation (K := K))).mem_of_integral hx.tower_top
  rw [Valuation.mem_integer_iff, NormedField.valuation_apply] at this
  exact_mod_cast this

/-- A polynomial times a decaying Gaussian is bounded on the nonnegative reals. -/
theorem poly_mul_gaussian_bounded :
    ∀ (c : ℝ), (0 : ℝ) < c → ∀ (N : ℕ), ∃ (C : ℝ), ∀ (r : ℝ), (0 : ℝ) ≤ r →
      ((1 : ℝ) + r) ^ N * Real.exp (-(c * r ^ (2 : ℕ))) ≤ C := by
  intro c hc N
  refine ⟨Real.exp ((N : ℝ) ^ 2 / (4 * c)), fun r hr => ?_⟩
  have h1 : ((1 : ℝ) + r) ^ N ≤ Real.exp ((N : ℝ) * r) := by
    calc ((1 : ℝ) + r) ^ N ≤ (Real.exp r) ^ N :=
          pow_le_pow_left₀ (by linarith) (by linarith [Real.add_one_le_exp r]) N
      _ = Real.exp ((N : ℝ) * r) := by rw [← Real.exp_nat_mul]
  calc ((1 : ℝ) + r) ^ N * Real.exp (-(c * r ^ (2 : ℕ)))
      ≤ Real.exp ((N : ℝ) * r) * Real.exp (-(c * r ^ (2 : ℕ))) :=
        mul_le_mul_of_nonneg_right h1 (Real.exp_pos _).le
    _ = Real.exp ((N : ℝ) * r + -(c * r ^ (2 : ℕ))) := (Real.exp_add _ _).symm
    _ ≤ Real.exp ((N : ℝ) ^ 2 / (4 * c)) := by
        apply Real.exp_le_exp.mpr
        rw [le_div_iff₀ (by positivity)]
        nlinarith [sq_nonneg (2 * c * r - N)]

end ReplayAnalysis
