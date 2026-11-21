# M101080 dependency semantics review

M101080 is an already ported external dependency of P0101, in packet P0042. Its only direct uses of `eLpNorm` are the two sides of `eLpNorm_rhoFun`, both at exponent 2. Its existing record and patch are retained unchanged.

At the replay Mathlib pin `0df444a360eaa60ab8c11dca51a86af692955474`, the finite nonzero-exponent branch of `eLpNorm` is `eLpNorm' f p.toReal μ`. At target pin `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`, the same branch applies when `AEStronglyMeasurable f μ`; otherwise the target returns infinity. The integral definition of `eLpNorm'` is identical in the two inspected files. Exponent 2 is finite and nonzero.

The right-hand function is `f : L2 l`, so `Lp.aestronglyMeasurable f` supplies its measurability. The left-hand function is `rhoFun w f`, the product of `phase w` and a translate of `f`. `continuous_phase w` gives measurability of the phase, and `measurePreserving_add_right volume (pPart w)` gives measurability of the translate. Their product is almost everywhere strongly measurable. The existing landed patch already constructs precisely these witnesses when calling `eLpNorm_congr_norm_ae`.

Thus the target `eLpNorm_eq_eLpNorm'` rewrites both sides to the same integral quantities used at the replay pin. No extra hypothesis is required, and the theorem retains its pinned meaning. The target `MemLp` characterization is also equivalent here: finiteness of the target norm implies almost everywhere strong measurability, while on measurable functions the norms agree. The existing proof of `memLp_rhoFun` uses that characterization. No new source change is needed.

Sources inspected: `Mathlib/MeasureTheory/Function/LpSeminorm/Defs.lean` at both exact pins, the SHA-verified pinned M101080 source, and the existing M101080 port patch. The adjacent JSON receipt records their hashes.
