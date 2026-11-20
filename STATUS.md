# Coordinator progress

Updated 2026-11-20 16:03 UTC.

The full source build, axiom audit and fresh-kernel verification of RH are pending. Volunteers can claim work using the [contributor guide](CONTRIBUTING.md).

## Distributed replay

The coordinator provisioned one primary and 31 helpers. The first wave reserved up to 11,114 project modules beyond its initial build snapshot. A completed helper bundle becomes evidence of successful reuse when the primary accepts it with rebuilding disabled.

| Helper | Batch target | Project modules including prerequisites | Last observed state |
|---|---|---:|---|
| 1 | `GroundTheory.ProfiniteCohomology.PoitouTate.RealEvenLevel` | 772 | query error |
| 2 | `Development.AutomorphicSpectrum.Proofs.MetricProofs.ZeroSetChartIdealEqChartSetStatement` | 689 | query error |
| 3 | `Formalism.HermitianCurvature.HermitianCurvatureProofs.CutGCoreGTRTrans` | 689 | query error |
| 4 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.InertiaFixedFieldMaximalIdealDvdUniformizerStatement` | 797 | query error |
| 5 | `Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.AdmissibleDoubledHermitianThetaFamily` | 593 | query error |
| 6 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsKummerClassOnFinerEtaleNbhdCurveStatement` | 424 | query error |
| 7 | `Formalism.WachLatticeTwists.RealDisplaySplitting.GaloisTheoremThirdForms` | 376 | query error |
| 8 | `Development.AutomorphicArithmetic.Foundations.Convolution.ConvolutionKernels.KernelTransforms.CompatEx` | 422 | query error |
| 9 | `Formalism.LocalToGlobal.TorsionIntegrality.QuadraticSemicharacters.CayleyGaussianIntegrals.SelfDualCovolumeProof` | 404 | query error |
| 10 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinaryEisensteinEigenfunctionalExists` | 327 | query error |
| 11 | `Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.LevelChainValuations.GaloisCupProducts.HomPullRHofGood` | 404 | query error |
| 12 | `Development.EtaleCohomology.EtaleSheaves.AwSpec` | 340 | query error |
| 13 | `Development.AutomorphicSpectrum.Proofs.MetricProofs.MixedIntegralTendstoOffDivisorStatement` | 398 | query error |
| 14 | `Development.AutomorphicArithmetic.AutomorphicVarieties.FrobeniusSmoothVectors.ChainedOfComap` | 332 | query error |
| 15 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.FiniteDimensionalChartLatticeStatement` | 560 | query error |
| 16 | `Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.DualFamilyCounting.AlphaDiscriminantHolds` | 328 | query error |
| 17 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsDeRhamFrameLimitLatticeBreuilKisinTowerStatement` | 746 | query error |
| 18 | `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GlobalUnitaryForms.IntegralStabilizers.SideGLoc` | 399 | query error |
| 19 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.IoConstOfMem` | 658 | query error |
| 20 | `Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.TranscendenceTraces.IsolateSpecHolds` | 330 | query error |
| 21 | `ReciprocityTheory.ReductiveGroups.DiscreteSeries.InfinitesimalDecay.ProjectionSquareIntegrable` | 799 | query error |
| 22 | `Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.SpecAbsolutelyIntegrallyClosedCohomology` | 411 | query error |
| 23 | `GroundTheory.PAdicHodge.WAFracB` | 353 | query error |
| 24 | `Formalism.SharpRestriction.GrowthBounds.ProofRowTieVals` | 306 | query error |
| 25 | `CompanionTheory.AutomorphicTheory.SiegelWeilFiniteness.AdelicCovolumeFinite` | 362 | query error |
| 26 | `Development.AutomorphicSpectrum.Proofs.AlgebraProofs.FlagFurtherTermIndependentStatement` | 462 | query error |
| 27 | `Development.AutomorphicSpectrum.Proofs.GeometryProofs.ComponentSpecializationLatticeBasisStatement` | 301 | query error |
| 28 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.AmplitudeExpansionOverFinitePlaces` | 423 | query error |
| 29 | `Formalism.SharpRestriction.GrowthBounds.FockGramWindow.RestWinOfLvl` | 705 | query error |
| 30 | `Formalism.SharpRestriction.LevelLetterCocycles.LocalTheoremOfInputs` | 622 | query error |
| 31 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NefLineBundleNumericalTheoremsProofStatement` | 528 | query error |

The earlier two-worker trial transferred 150 previously unbuilt modules. The receiver compiled one original downstream module and replayed its declarations with the Lean kernel. [Pilot receipt](evidence/pilot-receipt.json)
