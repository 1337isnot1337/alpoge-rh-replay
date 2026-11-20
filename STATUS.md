# Coordinator progress

Updated 2026-11-20 16:09 UTC.

The full source build, axiom audit and fresh-kernel verification of RH are pending. Volunteers can claim work using the [contributor guide](CONTRIBUTING.md).

## Distributed replay

The coordinator provisioned one primary and 31 helpers. The first wave reserved up to 11,114 project modules beyond its initial build snapshot. A completed helper bundle becomes evidence of successful reuse when the primary accepts it with rebuilding disabled.

| Helper | Batch target | Project modules including prerequisites | Last observed state |
|---|---|---:|---|
| 1 | `GroundTheory.ProfiniteCohomology.PoitouTate.RealEvenLevel` | 772 | compiling |
| 2 | `Development.AutomorphicSpectrum.Proofs.MetricProofs.ZeroSetChartIdealEqChartSetStatement` | 689 | compiling |
| 3 | `Formalism.HermitianCurvature.HermitianCurvatureProofs.CutGCoreGTRTrans` | 689 | compiling |
| 4 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.InertiaFixedFieldMaximalIdealDvdUniformizerStatement` | 797 | compiling |
| 5 | `Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.AdmissibleDoubledHermitianThetaFamily` | 593 | compiling |
| 6 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsKummerClassOnFinerEtaleNbhdCurveStatement` | 424 | compiling |
| 7 | `Formalism.WachLatticeTwists.RealDisplaySplitting.GaloisTheoremThirdForms` | 376 | compiling |
| 8 | `Development.AutomorphicArithmetic.Foundations.Convolution.ConvolutionKernels.KernelTransforms.CompatEx` | 422 | compiling |
| 9 | `Formalism.LocalToGlobal.TorsionIntegrality.QuadraticSemicharacters.CayleyGaussianIntegrals.SelfDualCovolumeProof` | 404 | compiling |
| 10 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinaryEisensteinEigenfunctionalExists` | 327 | compiling |
| 11 | `Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.LevelChainValuations.GaloisCupProducts.HomPullRHofGood` | 404 | compiling |
| 12 | `Development.EtaleCohomology.EtaleSheaves.AwSpec` | 340 | compiling |
| 13 | `Development.AutomorphicSpectrum.Proofs.MetricProofs.MixedIntegralTendstoOffDivisorStatement` | 398 | compiling |
| 14 | `Development.AutomorphicArithmetic.AutomorphicVarieties.FrobeniusSmoothVectors.ChainedOfComap` | 332 | compiling |
| 15 | `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.FiniteDimensionalChartLatticeStatement` | 560 | compiling |
| 16 | `Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.DualFamilyCounting.AlphaDiscriminantHolds` | 328 | compiling |
| 17 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsDeRhamFrameLimitLatticeBreuilKisinTowerStatement` | 746 | compiling |
| 18 | `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GlobalUnitaryForms.IntegralStabilizers.SideGLoc` | 399 | compiling |
| 19 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.IoConstOfMem` | 658 | compiling |
| 20 | `Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.TranscendenceTraces.IsolateSpecHolds` | 330 | compiling |
| 21 | `ReciprocityTheory.ReductiveGroups.DiscreteSeries.InfinitesimalDecay.ProjectionSquareIntegrable` | 799 | compiling |
| 22 | `Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.SpecAbsolutelyIntegrallyClosedCohomology` | 411 | compiling |
| 23 | `GroundTheory.PAdicHodge.WAFracB` | 353 | compiling |
| 24 | `Formalism.SharpRestriction.GrowthBounds.ProofRowTieVals` | 306 | compiling |
| 25 | `CompanionTheory.AutomorphicTheory.SiegelWeilFiniteness.AdelicCovolumeFinite` | 362 | compiling |
| 26 | `Development.AutomorphicSpectrum.Proofs.AlgebraProofs.FlagFurtherTermIndependentStatement` | 462 | compiling |
| 27 | `Development.AutomorphicSpectrum.Proofs.GeometryProofs.ComponentSpecializationLatticeBasisStatement` | 301 | compiling |
| 28 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.AmplitudeExpansionOverFinitePlaces` | 423 | compiling |
| 29 | `Formalism.SharpRestriction.GrowthBounds.FockGramWindow.RestWinOfLvl` | 705 | compiling |
| 30 | `Formalism.SharpRestriction.LevelLetterCocycles.LocalTheoremOfInputs` | 622 | compiling |
| 31 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NefLineBundleNumericalTheoremsProofStatement` | 528 | compiling |

The earlier two-worker trial transferred 150 previously unbuilt modules. The receiver compiled one original downstream module and replayed its declarations with the Lean kernel. [Pilot receipt](evidence/pilot-receipt.json)
