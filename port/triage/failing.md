# Modules that fail unchanged on the port target

215 unported live modules currently fail to compile unchanged on `leanprover/lean4:v4.36.0` + Mathlib `fc4f59e577` (out of 4,784 triaged across Depths 0–1; already-ported and upstream-pruned modules excluded). Full compiler output is in `results.json` (`excerpt`). Pick work with `python3 tracker/port.py next --include-partial`.

| ID | Depth | Packet | Module | Errors | First error |
|---|---:|---|---|---:|---|
| M000495 | 0 | P0001 | `CompanionTheory.HarishChandraModules.BesselParameterIntegrals.ContDiffOnExpPartialHomeomorphSymm` | 2 | line 216: failed to compile definition, consider marking it as 'noncomputable' because it depends on 'Exists.choose', which is 'no |
| M002046 | 0 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.AdelicCMFields.UnitaryHeckeCharacterIdele` | 6 | line 170: Application type mismatch: The argument |
| M002162 | 0 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.DivisorBase.MultiplicationKernelIdentity` | 2 | line 34: Unknown constant `Polynomial.eval₂_finset_prod` |
| M002315 | 0 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.GlobalSignature.StabiliserCardinality` | 1 | line 38: Application type mismatch: The argument |
| M002358 | 0 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.HeightDefect.SchurLatticeConjugates` | 1 | line 79: Unknown constant `dvd_iff_multiplicity_pos.mpr` |
| M002361 | 0 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.HeightDefect.SphereBlockLogMean` | 9 | line 37: unsolved goals |
| M002399 | 0 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.JetGauges.NodalSeriesPeriods` | 2 | line 147: Application type mismatch: The argument |
| M002422 | 0 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.JetGauges.TraceFormDualSystem` | 1 | line 155: failed to compile definition, consider marking it as 'noncomputable' because it depends on 'pairing', which is 'noncompu |
| M004739 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.NonGaloisDescent.FiniteCocycles` | 3 | line 115: Unknown constant `MvPolynomial.coeff` |
| M004836 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.NonGaloisDescent.NormPowLeNormFactorial` | 23 | line 25: Unknown constant `IsUltrametricDist.exists_norm_finset_sum_le_of_nonempty` |
| M004886 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.QuasicoherentCohomology.AlgebraMapBaseMemMaximalIdealIff` | 1 | line 84: Application type mismatch: The argument |
| M005012 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.ShimuraVarieties.ExistsIsAdaptedOfIsLocalRing` | 6 | line 90: Unknown constant `Finsupp.finset_sum_apply` |
| M005055 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.ThetaMetrics.HasSumLocallyUniformlyWeierstrassZetaExcept` | 4 | line 418: Tactic `rfl` failed: The left-hand side |
| M005057 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.ThetaMetrics.IsAddFundamentalDomainLatticeDomain` | 1 | line 116: Unknown identifier `integral_finset_sum` |
| M005063 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.ThetaMetrics.MemIffConjugateNotMem` | 1 | line 26: Function expected at |
| M005066 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.ThetaMetrics.NormDetStrongContragredientDomRestrictAnnihilato` | 4 | line 63: `ring_nf` made no progress on the goal |
| M005069 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.ThetaMetrics.SumFinsuppAntidiagProdPowDivMultiFactorial` | 13 | line 82: Unknown identifier `coeff_add` |
| M005070 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.ThetaMetrics.TensorContentEqPolyContentScalarCoeffs` | 61 | line 183: Unknown identifier `coeff` |
| M005131 | 0 | P0003 | `Development.AbelianVarietyTheory.Definitions.TwistedInnerProducts.LeviEmbMemNormalizerLower` | 1 | line 85: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M005329 | 0 | P0003 | `Development.AbelianVarietyTheory.Proofs.AbelianSchemeLawProofs.SpecHomCompCoaction` | 6 | line 88: Invalid alternative name `zero`: There are no unhandled alternatives |
| M005460 | 0 | P0003 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ExistsForallAbvSubLt` | 2 | line 21: Unknown constant `WithAbs.norm_eq_abv` |
| M005486 | 0 | P0003 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ExistsIsUnitFormSelfOfNotMem` | 2 | line 26: Application type mismatch: The argument |
| M005526 | 0 | P0003 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ExistsPrimeInvolutionOfRingInvolution` | 2 | line 44: `simp` made no progress |
| M026435 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIntegralInvOneAddPrimeMulPadic` | 1 | line 16: Application type mismatch: The argument |
| M026517 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsInvariantPosDefHermitian` | 1 | line 92: Unknown identifier `continuous_finset_sum` |
| M026561 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIsAlgebraicRatFuncFractionRingDedekind` | 2 | line 19: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M026632 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIsLocalHomAdicCompletionExtend` | 3 | line 40: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg.49' using tactics |
| M027309 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLocalHomAdicCompletionExtend` | 7 | line 19: could not synthesize default value for parameter 'h₂' using tactics |
| M028264 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPolyAnnihilatesCommutingLinearCombination` | 4 | line 15: Unknown constant `Algebra.adjoinCommRingOfComm` |
| M028335 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPowEqOneIsUnitOneSubPow` | 2 | line 26: Unknown constant `Polynomial.eval_finset_sum` |
| M028442 | 0 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPrimitiveAnnihilator` | 1 | line 103: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M067505 | 0 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CoeffDetGenericSumMemOfCharpolyCoeffMem` | 2 | line 158: Unknown constant `MvPolynomial.coeff` |
| M067529 | 0 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CoeffZeroSmulMemMap` | 1 | line 24: Unknown constant `Polynomial.coeff` |
| M068206 | 0 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.DetOneAddSmulBlkMem` | 4 | line 63: Unknown constant `MvPolynomial.coeff` |
| M137664 | 0 | P0065 | `Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilActions.IsFirstChernFamily` | 1 | line 22: Application type mismatch: The argument |
| M137997 | 0 | P0065 | `Development.WeilBound.CoreStatements.CentralCharts.TraceMulReNonneg` | 2 | line 136: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M138011 | 0 | P0065 | `Development.WeilBound.CoreStatements.CommonZeroEvaluation.EventuallyRoot` | 2 | line 141: Unknown identifier `finset_sum_coeff` |
| M138259 | 0 | P0065 | `Development.WeilBound.CoreStatements.GaussianSeminormBounds.RealSeminormFiltration.RLLieD` | 4 | line 159: Function expected at |
| M138319 | 0 | P0065 | `Development.WeilBound.CoreStatements.HodgeTatePoints.DvrOfHeightOne` | 4 | line 21: could not synthesize default value for parameter 'h₂' using tactics |
| M138323 | 0 | P0065 | `Development.WeilBound.CoreStatements.HodgeTatePoints.EqOfProdEq` | 2 | line 18: Application type mismatch: The argument |
| M138393 | 0 | P0065 | `Development.WeilBound.CoreStatements.HodgeTatePoints.HtatHensA` | 3 | line 386: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg.49' using tactics |
| M138437 | 0 | P0065 | `Development.WeilBound.CoreStatements.HodgeTatePoints.KftwoHostA` | 2 | line 111: Function expected at |
| M138481 | 0 | P0065 | `Development.WeilBound.CoreStatements.HodgeTatePoints.PdvrExt` | 5 | line 30: Application type mismatch: The argument |
| M138505 | 0 | P0065 | `Development.WeilBound.CoreStatements.HodgeTatePoints.RaCarry` | 1 | line 82: Function expected at |
| M138541 | 0 | P0065 | `Development.WeilBound.CoreStatements.HodgeTatePoints.SiuaNum` | 18 | line 7: Application type mismatch: The argument |
| M138643 | 0 | P0065 | `Development.WeilBound.CoreStatements.HomogeneousNonvanishing.TwGFree` | 1 | line 16: Application type mismatch: The argument |
| M138682 | 0 | P0065 | `Development.WeilBound.CoreStatements.IdealCycleValues.FlatColon` | 3 | line 91: Invalid alternative name `zero`: There are no unhandled alternatives |
| M138855 | 0 | P0065 | `Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.BocksteinBaseChange.AdmissibleMinors.ExistsWeightBasisFiltration` | 1 | line 65: Invalid projection: Projection operates on types of the form `C ...` where C is a constant. The expression |
| M139060 | 0 | P0065 | `Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.ConeSectionRestriction.ExistsTmulOneEqOfIsIntegral` | 1 | line 27: Invalid alternative name `zero`: There are no unhandled alternatives |
| M154372 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ArchimedeanOrbitMeasures.PiCoord` | 5 | line 82: Application type mismatch: The argument |
| M154373 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ArchimedeanOrbitMeasures.PiDens` | 1 | line 99: Application type mismatch: The argument |
| M154461 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.BetaUniqueness.EqZeroOfNormLtOne` | 2 | line 102: Function expected at |
| M154822 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.DyadicStableLattices.RatIntOfIntegral` | 2 | line 64: Function expected at |
| M154854 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ExplicitFormula.LGrowthGamma` | 2 | line 162: (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |
| M154857 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ExplicitFormula.LStructA` | 1 | line 31: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M154866 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ExplicitFormula.NormLogDerivReflLe` | 2 | line 74: Unknown constant `DifferentiableAt.finset_prod` |
| M155057 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.GelfandPairConvolution.Unimod` | 4 | line 31: Ambiguous term |
| M155114 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.GelfandTsetlinTopCoefficient.CardEraseIccMin` | 1 | line 29: Function expected at |
| M155138 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.GramInjectivity.GramVanish` | 4 | line 25: Unknown identifier `coeff` |
| M155258 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.HighestWeightFixedVectors.MonomialMemGe` | 22 | line 12: Unknown identifier `coeff` |
| M155323 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.InertDensity.ExistsTraceNeZero` | 1 | line 52: Application type mismatch: The argument |
| M155435 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.IwasawaMeasureExistence.MulEquivHaarCharEqOfChart` | 1 | line 35: unsolved goals |
| M155577 | 0 | P0075 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LatticeIndices.ExistsGl` | 2 | line 52: Unknown constant `Finsupp.coe_finset_sum` |
| M162746 | 0 | P0081 | `GroundTheory.AutomorphicForms.HarishChandraCentre.Symmetric` | 1 | line 150: Unknown identifier `coeff` |
| M162805 | 0 | P0081 | `GroundTheory.AutomorphicForms.LocallyProfinite` | 1 | line 65: No goals to be solved |
| M162841 | 0 | P0081 | `GroundTheory.AutomorphicForms.PartialDifferential.AnalyticHypoSeries` | 2 | line 156: Application type mismatch: The argument |
| M162869 | 0 | P0081 | `GroundTheory.AutomorphicForms.RealGroupsLie` | 2 | line 216: failed to compile definition, consider marking it as 'noncomputable' because it depends on 'Exists.choose', which is 'no |
| M162890 | 0 | P0081 | `GroundTheory.AutomorphicForms.RestrictedHaarProduct` | 1 | line 178: Invalid projection: Projection operates on types of the form `C ...` where C is a constant. The expression |
| M162903 | 0 | P0081 | `GroundTheory.AutomorphicForms.SphericalLaurent` | 2 | line 136: Unknown constant `AlgEquiv.toAlgHom_eq_coe` |
| M163002 | 0 | P0081 | `GroundTheory.FunctionField.PlaceDefs` | 5 | line 297: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M163016 | 0 | P0081 | `GroundTheory.GlobalFields.Adele.IntegersLattice` | 1 | line 60: Tactic `rfl` failed: The left-hand side |
| M163029 | 0 | P0081 | `GroundTheory.GlobalFields.AnalyticClassNumber.QuadraticHurwitzZero` | 1 | line 235: Type mismatch |
| M163043 | 0 | P0081 | `GroundTheory.GlobalFields.Artin.LogCharpoly` | 7 | line 97: Application type mismatch: The argument |
| M163300 | 0 | P0081 | `GroundTheory.GlobalFields.SemilocalAlgebras.ContinuousCompletionMap` | 2 | line 66: failed to synthesize instance of type class |
| M163303 | 0 | P0081 | `GroundTheory.GlobalFields.SemilocalAlgebras.Infinite` | 3 | line 99: unsolved goals |
| M163332 | 0 | P0081 | `GroundTheory.GlobalFields.TateThesis.DegreeOnePrimes` | 3 | line 19: failed to synthesize instance of type class |
| M163509 | 0 | P0081 | `GroundTheory.HeightsAndTheta.Heights.Antisymmetric.Statements` | 2 | line 84: Unknown identifier `coeff` |
| M163724 | 0 | P0081 | `GroundTheory.HeightsAndTheta.Heights.ArithmeticBezout.Statements` | 2 | line 276: Unknown identifier `coeff` |
| M163819 | 0 | P0081 | `GroundTheory.HeightsAndTheta.Heights.ArithmeticBezout.ZeroLocusDimHAlg` | 1 | line 22: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M163820 | 0 | P0081 | `GroundTheory.HeightsAndTheta.Heights.ArithmeticBezout.ZeroLocusDimHGeo` | 1 | line 107: Application type mismatch: The argument |
| M174743 | 0 | P0093 | `ReciprocityTheory.ReductiveGroups.DiscreteSeries.TailIntegrals.IntegrableUnitIndicator` | 3 | (not in excerpt) |
| M174786 | 0 | P0093 | `ReciprocityTheory.ReductiveGroups.DiscreteSeries.TensorRepresentations.CoefAInnerEqZero` | 1 | line 110: Invalid projection: Projection operates on types of the form `C ...` where C is a constant. The expression |
| M174859 | 0 | P0093 | `ReciprocityTheory.ReductiveGroups.DiscreteSeries.TensorRepresentations.UnitarizeA` | 1 | line 78: unsolved goals |
| M174904 | 0 | P0093 | `ReciprocityTheory.ReductiveGroups.PlaceCounting.RaySplA` | 1 | line 39: Application type mismatch: The argument |
| M175056 | 0 | P0093 | `ReciprocityTheory.SemistableReduction.AlgebraicIndependentOfDerivations` | 7 | line 27: Unknown identifier `coeff` |
| M175065 | 0 | P0093 | `ReciprocityTheory.SemistableReduction.BWPolyA` | 2 | line 28: Unknown constant `Polynomial.eval_finset_sum` |
| M175072 | 0 | P0093 | `ReciprocityTheory.SemistableReduction.DetGramEqProdGramSchmidt` | 2 | line 72: Function expected at |
| M175082 | 0 | P0093 | `ReciprocityTheory.SemistableReduction.GaussIndepOfLeTrdeg` | 2 | line 86: Unknown constant `Cardinal.nat_lt_aleph0` |
| M175112 | 0 | P0093 | `ReciprocityTheory.SemistableReduction.SemiContractA` | 3 | line 31: Application type mismatch: The argument |
| M175165 | 0 | P0093 | `ReciprocityTheory.SemistableReduction.TorusMeanA` | 1 | line 88: Invalid projection: Projection operates on types of the form `C ...` where C is a constant. The expression |
| M175170 | 0 | P0093 | `ReciprocityTheory.SemistableReduction.UnipotentA` | 1 | line 93: Unknown constant `Polynomial.coeff` |
| M005622 | 1 | P0097 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.GramLeadingMinorLowerBoundIntegral` | 1 | line 34: Function expected at |
| M005636 | 1 | P0097 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.HeightOneSpectrumPlacesOverFiniteSet` | 1 | line 47: Type mismatch |
| M005650 | 1 | P0097 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.HilbertFinitenessLeftInvariantMatrixPoly` | 1 | line 78: Unknown identifier `coeff` |
| M005759 | 1 | P0097 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.MulLogEqNegLogMul` | 1 | line 14: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M006003 | 1 | P0098 | `Development.AbelianVarietyTheory.Proofs.CharacterTheory.ExistsInducedIntPrimeTo` | 2 | line 96: Invalid field `exists_card_eq`: The environment does not contain `And.exists_card_eq`, so it is not possible to project  |
| M006007 | 1 | P0098 | `Development.AbelianVarietyTheory.Proofs.CharacterTheory.ExistsIntRelationOfIsIntegralRelation` | 2 | line 14: Function expected at |
| M021076 | 1 | P0102 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DetEqOneUnitaryPrincipalCongruenceLevelThree` | 1 | line 25: `simp` made no progress |
| M022742 | 1 | P0102 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.EtaleChartLocalizationFiniteTypeFormallyUnramifi` | 2 | line 75: failed to synthesize |
| M027625 | 1 | P0104 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsMultilinearFormOfPicTorsion` | 2 | line 47: Application type mismatch: The argument |
| M028423 | 1 | P0104 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPrimeNotMemForallGtEqMaximalIdeal` | 1 | line 35: Unknown constant `IsLocalization.comap_map_of_isPrime_disjoint` |
| M029517 | 1 | P0105 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSubMemMaximalIdealPointedEtaleNeighbourhoo` | 2 | line 26: failed to synthesize |
| M051585 | 1 | P0115 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SummableExpNegTraceTotallyPositiveFractionalIdea` | 1 | line 40: Function expected at |
| M053945 | 1 | P0115 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TraceRingOfIntegersActionLatticeEq` | 2 | line 7: Unknown constant `DistribMulAction.toAddMonoidHom` |
| M057125 | 1 | P0116 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ContinuousAtZeroOfSqueezePowBounds` | 2 | line 15: unsolved goals |
| M057505 | 1 | P0116 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsDyadicShellIndex` | 2 | line 60: Function expected at |
| M068758 | 1 | P0121 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsConstOfLvlInvariant` | 2 | line 164: Unknown constant `Polynomial.coeff` |
| M070093 | 1 | P0122 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.FactorialTruncatedLogAdditivityDefectCoeffDvd` | 4 | line 20: Unknown identifier `coeff` |
| M072490 | 1 | P0123 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LvlPolyDistinguished` | 2 | line 58: Unknown constant `Polynomial.coeff` |
| M073989 | 1 | P0124 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.SetLIntegralAverageAbelianQuotient` | 1 | line 29: Application type mismatch: The argument |
| M075422 | 1 | P0124 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.WittVectorGaussNormUltrametric` | 1 | line 135: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M075718 | 1 | P0124 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.AssociatedPrimeLocalizationDvr` | 3 | line 80: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg.58' using tactics |
| M101273 | 1 | P0130 | `Development.AutomorphicArithmetic.AdelicQuotients.IrreducibleHermitianFormUnique` | 1 | line 80: Unknown identifier `integral_finset_sum` |
| M101335 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AdditiveValuationNorms.Imports` | 1 | line 18: Unknown constant `Polynomial.coeff` |
| M101430 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.DeEqDet` | 2 | line 19: Unknown identifier `coeff` |
| M101475 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.DualLattice` | 4 | line 10: Application type mismatch: The argument |
| M101490 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.HidaCompleteRings.Component` | 1 | line 15: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M101588 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.LagCoi` | 1 | line 59: Unknown identifier `eval_finset_sum` |
| M101595 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.LimElt` | 1 | line 21: Unknown identifier `continuous_mul_left` |
| M101596 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.LimKer` | 2 | line 35: Unknown identifier `continuous_mul_left` |
| M101597 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.LimOut` | 3 | line 63: Unknown identifier `continuous_mul_left` |
| M101598 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.LocFactor` | 2 | line 30: Application type mismatch: The argument |
| M101616 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.MonomialRepresentations.TwistOfRed` | 2 | line 190: Function expected at |
| M101631 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.ResNormal` | 2 | line 50: Application type mismatch: The argument |
| M101640 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.SubgroupQuot` | 1 | line 19: Unknown constant `Group.closure_finite_fg` |
| M101644 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.TnAlgMapSmulMem` | 2 | line 52: Application type mismatch: The argument |
| M102552 | 1 | P0131 | `Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebra.CoFinite` | 2 | line 121: Application type mismatch: The argument |
| M103498 | 1 | P0133 | `Development.AutomorphicArithmetic.AutomorphicVarieties.GaloisLibrary.FerreroWashingtonIndex.SinSupp` | 2 | line 21: Unknown constant `Finsupp.finset_sum_apply` |
| M103605 | 1 | P0133 | `Development.AutomorphicArithmetic.AutomorphicVarieties.GaloisLibrary.LocalRingsCompletion.DvrIntClosure` | 4 | line 62: could not synthesize default value for parameter 'h₂' using tactics |
| M119671 | 1 | P0137 | `Development.AutomorphicSpectrum.Definitions.CommutativeAlgebra.LieLatticeData` | 2 | line 32: Unknown constant `DistribMulAction.toAddMonoidHom` |
| M119901 | 1 | P0137 | `Development.AutomorphicSpectrum.Proofs.AdelicProofs.SchurTranslationsCharacters` | 1 | line 182: Unknown identifier `continuous_add_right` |
| M120428 | 1 | P0137 | `Development.AutomorphicSpectrum.Proofs.AlgebraProofs.LocallyFreeOfFiniteProjective` | 1 | line 96: Invalid alternative name `zero`: There are no unhandled alternatives |
| M120855 | 1 | P0137 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.AicValOfIsColim` | 1 | line 36: Application type mismatch: The argument |
| M120957 | 1 | P0137 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.ArchimedeanOrbitalIntegralContinuous` | 4 | line 11: Unknown identifier `continuous_finset_sum` |
| M126399 | 1 | P0140 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.ParabolicHaarDecomposition` | 1 | line 83: Application type mismatch: The argument |
| M126459 | 1 | P0140 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.PartialFractionDiagonalIdentity` | 5 | line 55: Unknown identifier `finset_sum_coeff` |
| M126772 | 1 | P0140 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.QuadraticBoxVolumeBound` | 3 | line 15: Unknown constant `ENNReal.coe_finset_prod` |
| M127223 | 1 | P0141 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.SchurOpOfSchurL` | 7 | line 17: Type mismatch: After simplification, term |
| M127658 | 1 | P0141 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.SmulSmulMemRange` | 3 | line 21: Invalid alternative name `zero`: There are no unhandled alternatives |
| M127676 | 1 | P0141 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.SolveUnitriangular` | 1 | (not in excerpt) |
| M128804 | 1 | P0141 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.WedgeBoundFinitePlaces` | 6 | line 39: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M131896 | 1 | P0142 | `Development.AutomorphicSpectrum.Proofs.GeometryProofs.RiemannFormHermitianLattice` | 2 | line 54: unsolved goals |
| M132280 | 1 | P0142 | `Development.AutomorphicSpectrum.Proofs.GeometryProofs.TorusPointOverFractionField` | 1 | line 90: Unknown constant `Ideal.bot_prime` |
| M132300 | 1 | P0142 | `Development.AutomorphicSpectrum.Proofs.GeometryProofs.TraceIntegralSubringExtension` | 2 | line 95: Unknown constant `Finsupp.finset_sum_apply` |
| M144140 | 1 | P0146 | `Formalism.CharacterColumnKernels.IdempotentNormalForms.ProdEraseZero` | 7 | line 9: Function expected at |
| M144185 | 1 | P0146 | `Formalism.CorankShare.CorankShareProofs.LayerCakeFormula` | 1 | line 73: Unknown constant `intervalIntegral.integral_finset_sum` |
| M144197 | 1 | P0146 | `Formalism.CyclotomicNorms.NonsquarefreeBounds.NonsquarefreeMonicBoundHolds` | 4 | line 16: Unknown identifier `finset_sum_coeff` |
| M144273 | 1 | P0146 | `Formalism.DoubleCosetMeasures.LowerUnipotentOrbits.DoubleCosetEqPreimage` | 2 | line 237: Function expected at |
| M144283 | 1 | P0146 | `Formalism.DoubleCosetMeasures.LowerUnipotentOrbits.TwoSided` | 6 | line 56: Unknown identifier `continuous_mul_right` |
| M144357 | 1 | P0146 | `Formalism.FilteredPoleLength.LocalDescentLevels.GAdjugateNormBound` | 2 | line 17: Function expected at |
| M150358 | 1 | P0149 | `Formalism.LocalToGlobal.ProjectiveLattices.GenSectB` | 7 | line 35: Unknown identifier `coeff` |
| M150744 | 1 | P0149 | `Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits.GaugeLatticeShifts.LieAveraging.AvgCore` | 1 | line 62: unsolved goals |
| M150792 | 1 | P0149 | `Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits.GaugeLatticeShifts.PiMapMulRight` | 3 | line 54: Application type mismatch: The argument |
| M155460 | 1 | P0153 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.JetIntegrality.CoeffPowEqZeroOfDegreeLt` | 14 | line 17: Application type mismatch: The argument |
| M155467 | 1 | P0153 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.JetIntegrality.InvOmega` | 9 | line 119: Application type mismatch: The argument |
| M155470 | 1 | P0153 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.JetIntegrality.TwoUnit` | 11 | line 12: Application type mismatch: The argument |
| M155482 | 1 | P0153 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LFunctionEvaluation.LsumEqOfSubset` | 5 | line 15: Unknown identifier `coeff` |
| M155484 | 1 | P0153 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LFunctionMinors.FintypeColChoice` | 2 | line 35: Unknown identifier `coeff` |
| M155843 | 1 | P0153 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LocalDualGenerator.IsClosedO` | 2 | line 140: Unknown identifier `continuous_finset_sum` |
| M156048 | 1 | P0154 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LowerShearHaar.MeasurePreservingOfCard` | 2 | line 14: Application type mismatch: The argument |
| M156359 | 1 | P0154 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ProductFormulaHaar.InjectiveOfLinearIndependent` | 2 | line 26: Unknown constant `IsValuativeTopology.isClosed_closedBall` |
| M156378 | 1 | P0154 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ProjectionLattices.IsIntegralTraceOfPow` | 1 | line 40: Function expected at |
| M156432 | 1 | P0154 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.RamificationBound.CtNonneg` | 1 | line 36: Unknown identifier `coeff` |
| M156508 | 1 | P0154 | `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.RootSubgroupBasics.TriShear` | 2 | line 14: Application type mismatch: The argument |
| M158144 | 1 | P0157 | `Formalism.SatakeDualWeyl.AdelicIwasawaHecke.Upqcpt` | 1 | (not in excerpt) |
| M158646 | 1 | P0157 | `Formalism.SharpRestriction.Divisibility.GeneratorPowers.AevalDiagMonomial` | 29 | line 18: Unknown identifier `coeff` |
| M159420 | 1 | P0157 | `Formalism.SharpRestriction.GrowthBounds.ColumnSpanDensity.QuadraticBasis.QuadRoots` | 5 | line 10: Application type mismatch: The argument |
| M159875 | 1 | P0157 | `Formalism.SharpRestriction.GrowthBounds.MultisetValuation.JpSubstExpand` | 3 | line 169: Unknown constant `MvPolynomial.coeff` |
| M160340 | 1 | P0157 | `Formalism.SharpRestriction.GrowthBounds.TwistedSubstitution.TwistedMonomialFiltration.TMemLaurentFiltration` | 7 | line 92: Unknown identifier `coeff` |
| M160459 | 1 | P0157 | `Formalism.SharpRestriction.LevelLetterCocycles.CyclotomicPowerSeries.CycloSimple` | 2 | line 39: Application type mismatch: The argument |
| M160462 | 1 | P0157 | `Formalism.SharpRestriction.LevelLetterCocycles.CyclotomicPowerSeries.ExpRescaleCoeff` | 3 | line 10: Application type mismatch: The argument |
| M160984 | 1 | P0157 | `Formalism.SharpRestriction.LevelLetterCocycles.RepresentationCongruences.CoeffEqZeroOfSumEqZero` | 1 | line 80: Unknown constant `Polynomial.coeff` |
| M161153 | 1 | P0157 | `Formalism.SharpRestriction.LevelLetterCocycles.WildPro` | 1 | line 148: Function expected at |
| M161230 | 1 | P0158 | `Formalism.SharpRestriction.ValuationFrobeniusEpsilon.LeastPrimeTwists.QuotientShiftIrreducible.NoetherianQuotientCalc.RuleDev` | 1 | line 316: Invalid projection: Projection operates on types of the form `C ...` where C is a constant. The expression |
| M161355 | 1 | P0158 | `Formalism.SubspaceCounting.SubspaceCountingProofs.DetDivides` | 1 | (not in excerpt) |
| M161393 | 1 | P0158 | `Formalism.TameInertiaTowers.CentralOrderTwo.Groups` | 1 | line 142: Function expected at |
| M161399 | 1 | P0158 | `Formalism.TameInertiaTowers.CentralOrderTwo.TwoAdic` | 4 | line 8: Type mismatch |
| M161432 | 1 | P0158 | `Formalism.ThetaLogCoordinates.DualWeylCoordinates.DefsMod` | 2 | line 129: Unknown constant `MvPolynomial.coeff` |
| M161571 | 1 | P0158 | `Formalism.ThetaLogCoordinates.JacobiPathWeights.StatementE` | 1 | line 82: Unknown identifier `coeff` |
| M162107 | 1 | P0159 | `Formalism.WachModuleLifts.WachModuleProofs.LemmaCSharpG` | 1 | line 131: No goals to be solved |
| M162110 | 1 | P0159 | `Formalism.WachModuleLifts.WachModuleProofs.LemmaHLift` | 1 | line 13: Application type mismatch: The argument |
| M162140 | 1 | P0159 | `Formalism.WindowSums.AnnihilatorPolynomials.ValProd` | 3 | line 51: unsolved goals |
| M162142 | 1 | P0159 | `Formalism.WindowSums.AnnihilatorPolynomials.ZpowVal` | 3 | line 91: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M164952 | 1 | P0163 | `GroundTheory.HeightsAndTheta.Heights.CountingLowerBound.PMeanCountBound` | 1 | line 98: Application type mismatch: The argument |
| M165181 | 1 | P0163 | `GroundTheory.HeightsAndTheta.Heights.DiscreteValuationNumbers.PMaximalIdealHeightFG` | 2 | line 19: `simp` made no progress |
| M165205 | 1 | P0163 | `GroundTheory.HeightsAndTheta.Heights.DiscreteValuationNumbers.PPrincipalReductionOfBoundedGens` | 1 | line 425: Application type mismatch: The argument |
| M165414 | 1 | P0163 | `GroundTheory.HeightsAndTheta.Heights.EffectiveHilbertSamuel.PLocUnifAnalytic` | 1 | line 96: failed to compile definition, consider marking it as 'noncomputable' because it depends on 'instCommCStarAlgebraComplex' |
| M165778 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.FiniteCovolume.PDoubleCosetCovolume` | 2 | line 104: Application type mismatch: The argument |
| M165846 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.FiniteCovolume.PUnipotentModulusHaar` | 1 | line 35: unsolved goals |
| M165849 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.FiniteCovolume.PUnitsInvHaar` | 1 | line 49: Application type mismatch: The argument |
| M166056 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HeightKernels.AltFrob` | 1 | line 106: failed to synthesize |
| M166090 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HeightKernels.PCauchyBinet` | 2 | line 18: Type mismatch |
| M166187 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HeightKernels.PHadamardPSD` | 3 | line 16: Function expected at |
| M166233 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HeightKernels.PPlueckerNormSq` | 2 | line 22: unsolved goals |
| M166324 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HeightKernels.RestCutBasic` | 8 | line 81: Unknown identifier `coeff` |
| M166500 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HilbertSamuel.IrreducibleConnected.PMonicRootGrowth` | 4 | line 10: Unknown identifier `coeff` |
| M166606 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HilbertSamuel.PConstantsDescend` | 1 | line 143: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M166639 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HilbertSamuel.PFiniteSeparatingModel` | 1 | line 76: Unknown constant `Polynomial.coeff` |
| M166849 | 1 | P0164 | `GroundTheory.HeightsAndTheta.Heights.HilbertSamuel.PSerreGraded` | 3 | line 222: Unknown constant `MvPolynomial.coeff` |
| M167348 | 1 | P0165 | `GroundTheory.HeightsAndTheta.Heights.HodgeLowerBound.PFlagIntMuOneCoeff` | 5 | line 17: Unknown identifier `coeff` |
| M167351 | 1 | P0165 | `GroundTheory.HeightsAndTheta.Heights.HodgeLowerBound.PFlagIntMuProdSlice` | 9 | line 37: Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| M167577 | 1 | P0165 | `GroundTheory.HeightsAndTheta.Heights.IntegralModels.FiniteIntegralClosureCharZero` | 5 | line 41: Application type mismatch: The argument |
| M167808 | 1 | P0165 | `GroundTheory.HeightsAndTheta.Heights.Intersections.PAdjoinIndepRelfinrank` | 3 | line 39: Unknown constant `MvPolynomial.coeff` |
| M167901 | 1 | P0165 | `GroundTheory.HeightsAndTheta.Heights.Intersections.PRelAlgClosureFinite` | 3 | line 30: Unknown identifier `coeff` |
| M167902 | 1 | P0165 | `GroundTheory.HeightsAndTheta.Heights.Intersections.PRelBaseChange` | 2 | line 38: Invalid alternative name `zero`: There are no unhandled alternatives |
| M168029 | 1 | P0165 | `GroundTheory.HeightsAndTheta.Heights.Intersections.StatementsFibreLocal` | 1 | line 13: Unknown identifier `coeff` |
| M172531 | 1 | P0169 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ArithmeticIntersection.Inhabit` | 10 | line 8: Application type mismatch: The argument |
| M172533 | 1 | P0169 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ArithmeticIntersection.KappaA` | 1 | line 49: unsolved goals |
| M172558 | 1 | P0169 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ArithmeticIntersection.MultihomogeneousIdeals.SwapLoc` | 2 | line 244: Unknown constant `IsLocalization.comap_map_of_isPrime_disjoint` |
| M172561 | 1 | P0169 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ArithmeticIntersection.SymExp` | 4 | line 6: Application type mismatch: The argument |
| M173750 | 1 | P0170 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.TaylorDiscriminants.DiscriminantEstimates.DiscriminantLemmas.UniformDiscreteness.FgOfUnifDiscrete` | 2 | line 122: Insufficient number of fields for `⟨...⟩` constructor: Constructor `Eq.refl` does not have explicit fields, but 2 were p |
| M173754 | 1 | P0170 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.TaylorDiscriminants.DiscriminantEstimates.DiscriminantLemmas.WickFormula.GenVan` | 2 | line 23: Unknown identifier `coeff_zero` |
| M173779 | 1 | P0170 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.TaylorDiscriminants.Taylor` | 4 | (not in excerpt) |
| M173836 | 1 | P0170 | `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.TaylorDiscriminants.WickVanishing.MonoVal` | 8 | line 25: Application type mismatch: The argument |
| M174012 | 1 | P0170 | `ReciprocityTheory.ReductiveGroups.DiscreteSeries.DiscreteSeriesExistence.CayleyChartDomainIsOpen` | 2 | line 24: Unknown identifier `eLpNorm_eq_lintegral_rpow_enorm` |
