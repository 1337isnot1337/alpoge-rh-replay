# Coordinator progress

Updated 2026-11-20 16:50 UTC.

The full source build, axiom audit and fresh-kernel verification of RH are pending. Volunteers can claim work using the [contributor guide](CONTRIBUTING.md).

## Distributed replay

The coordinator provisioned one primary and 31 helpers. The first wave reserved up to 11,114 project modules beyond its initial build snapshot. A completed helper bundle becomes evidence of successful reuse when the primary accepts it with rebuilding disabled.

29 helpers published bundles and 2 were last seen compiling. The primary selected 29 ready bundles covering 11,114 distinct modules for transfer, checksum checks, and a Lake reuse check.

| Helper | Batch target | Project modules including prerequisites | Last observed state |
|---|---|---:|---|
| 1 | `GroundTheory.ProfiniteCohomology.PoitouTate.RealEvenLevel` | 772 | compiling |
| 2 | `Development.AutomorphicSpectrum.Proofs.MetricProofs.ZeroSetChartIdealEqChartSetStatement` | 689 | ready |
| 3 | `Formalism.HermitianCurvature.HermitianCurvatureProofs.CutGCoreGTRTrans` | 689 | ready |
| 4 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.InertiaFixedFieldMaximalIdealDvdUniformizerStatement` | 797 | ready |
| 5 | `Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.AdmissibleDoubledHermitianThetaFamily` | 593 | ready |
| 6 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsKummerClassOnFinerEtaleNbhdCurveStatement` | 424 | ready |
| 7 | `Formalism.WachLatticeTwists.RealDisplaySplitting.GaloisTheoremThirdForms` | 376 | ready |
| 8 | `Development.AutomorphicArithmetic.Foundations.Convolution.ConvolutionKernels.KernelTransforms.CompatEx` | 422 | ready |
| 9 | `Formalism.LocalToGlobal.TorsionIntegrality.QuadraticSemicharacters.CayleyGaussianIntegrals.SelfDualCovolumeProof` | 404 | ready |
| 10 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinaryEisensteinEigenfunctionalExists` | 327 | ready |
| 11 | `Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.LevelChainValuations.GaloisCupProducts.HomPullRHofGood` | 404 | ready |
| 12 | `Development.EtaleCohomology.EtaleSheaves.AwSpec` | 340 | ready |
| 13 | `Development.AutomorphicSpectrum.Proofs.MetricProofs.MixedIntegralTendstoOffDivisorStatement` | 398 | ready |
| 14 | `Development.AutomorphicArithmetic.AutomorphicVarieties.FrobeniusSmoothVectors.ChainedOfComap` | 332 | ready |
| 15 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.FiniteDimensionalChartLatticeStatement` | 560 | ready |
| 16 | `Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.DualFamilyCounting.AlphaDiscriminantHolds` | 328 | ready |
| 17 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsDeRhamFrameLimitLatticeBreuilKisinTowerStatement` | 746 | ready |
| 18 | `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GlobalUnitaryForms.IntegralStabilizers.SideGLoc` | 399 | ready |
| 19 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.IoConstOfMem` | 658 | ready |
| 20 | `Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.TranscendenceTraces.IsolateSpecHolds` | 330 | ready |
| 21 | `ReciprocityTheory.ReductiveGroups.DiscreteSeries.InfinitesimalDecay.ProjectionSquareIntegrable` | 799 | ready |
| 22 | `Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.SpecAbsolutelyIntegrallyClosedCohomology` | 411 | ready |
| 23 | `GroundTheory.PAdicHodge.WAFracB` | 353 | compiling |
| 24 | `Formalism.SharpRestriction.GrowthBounds.ProofRowTieVals` | 306 | ready |
| 25 | `CompanionTheory.AutomorphicTheory.SiegelWeilFiniteness.AdelicCovolumeFinite` | 362 | ready |
| 26 | `Development.AutomorphicSpectrum.Proofs.AlgebraProofs.FlagFurtherTermIndependentStatement` | 462 | ready |
| 27 | `Development.AutomorphicSpectrum.Proofs.GeometryProofs.ComponentSpecializationLatticeBasisStatement` | 301 | ready |
| 28 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.AmplitudeExpansionOverFinitePlaces` | 423 | ready |
| 29 | `Formalism.SharpRestriction.GrowthBounds.FockGramWindow.RestWinOfLvl` | 705 | ready |
| 30 | `Formalism.SharpRestriction.LevelLetterCocycles.LocalTheoremOfInputs` | 622 | ready |
| 31 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NefLineBundleNumericalTheoremsProofStatement` | 528 | ready |

The earlier two-worker trial transferred 150 previously unbuilt modules. The receiver compiled one original downstream module and replayed its declarations with the Lean kernel. [Pilot receipt](evidence/pilot-receipt.json)
