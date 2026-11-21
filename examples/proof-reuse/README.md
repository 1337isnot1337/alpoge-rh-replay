# Reusing proofs across the replay archive

Four Mathlib-only libraries supply checked replacements for **267 extracted declarations** on the pinned archive. The structural scan adds **73 sites across 10 lemma families** to the previous 194. Each comparison elaborates the source proof and a call to the shared lemma against the source statement. [Native measurements](results.json)

The original eight lemmas in [ReplayTopology.lean](ReplayTopology.lean) and [ReplayAlgebra.lean](ReplayAlgebra.lean) cover these exact statement-and-script matches:

- **84 occurrences** (across 5 fingerprints: 33, 21, 11, 10, and 9 sites) of `Spec.map` / `spMap` contravariant composition on ring homomorphisms;
- **27 occurrences** of the residue-field cardinality / absolute-norm identity `normV w = normV (w.under (𝓞 K)) ^ w.asIdeal.inertiaDeg (𝓞 K)` in number field extensions;
- **19 occurrences** of continuity for homomorphisms into units;
- **15 occurrences** showing no number field is simultaneously totally real and totally complex;
- **14 occurrences** showing quotients of compact totally disconnected groups by closed normal subgroups are totally disconnected;
- **14 occurrences** of continuity of characteristic polynomial coefficients for matrices over topological commutative rings;
- **12 occurrences** characterizing `ℤ_[l]`-integrality in `PadicAlgCl l` via `‖x‖ ≤ 1`;
- **9 occurrences** showing algebra homomorphisms from local `O`-algebras into nontrivial integral `O`-algebras are local.

## Use the lemmas

Copy the relevant module into a project with the pinned Mathlib and declare it as a Lake target. The first eight lemmas are listed below. [ReplayAnalysis.lean](ReplayAnalysis.lean) and [ReplayCommutativeAlgebra.lean](ReplayCommutativeAlgebra.lean) contain the additional families in the structural measurement table.

| Goal | Declaration | Sites |
| --- | --- | ---: |
| Compose `Spec.map (CommRingCat.ofHom ·)` (or its symmetric form) | `ReplayAlgebra.specMap_ofHom_comp` | 84 |
| Express `Nat.card (𝓞 K' ⧸ w.asIdeal)` as a power of the base residue-field cardinality | `ReplayAlgebra.cardQuot_under_eq_pow_inertiaDeg` | 27 |
| Prove continuity of a homomorphism into units from continuity after coercion | `ReplayTopology.continuous_unitsHom` | 19 |
| Derive `False` from `[IsTotallyReal F]` and `[IsTotallyComplex F]` | `ReplayAlgebra.not_isTotallyReal_and_isTotallyComplex` | 15 |
| Give `G ⧸ N` a totally disconnected topology for compact totally disconnected `G` and closed normal `N` | `ReplayTopology.totallyDisconnected_quotient` | 14 |
| Prove continuity of `fun M : Matrix ι ι K => M.charpoly.coeff i` | `ReplayTopology.continuous_charpoly_coeff` | 14 |
| Relate `IsIntegral ℤ_[l] x` and `‖x‖ ≤ 1` for `x : PadicAlgCl l` | `ReplayAlgebra.padicAlgCl_isIntegral_iff_norm_le_one` | 12 |
| Show `f : R →ₐ[O] A` is `IsLocalHom` when `R` is local and `A` is nontrivial integral over `O` | `ReplayAlgebra.isLocalHom_of_isIntegral` | 9 |

```lean
import ReplayTopology
import ReplayAlgebra

open AlgebraicGeometry CategoryTheory IsDedekindDomain NumberField
open scoped Padic

example {A B C : Type*} [CommRing A] [CommRing B] [CommRing C]
    (f : A →+* B) (g : B →+* C) :
    Spec.map (CommRingCat.ofHom g) ≫ Spec.map (CommRingCat.ofHom f) =
      Spec.map (CommRingCat.ofHom (g.comp f)) :=
  ReplayAlgebra.specMap_ofHom_comp f g

example {K K' : Type*} [Field K] [NumberField K] [Field K'] [NumberField K'] [Algebra K K']
    (w : HeightOneSpectrum (𝓞 K')) :
    Nat.card (𝓞 K' ⧸ w.asIdeal) =
      Nat.card (𝓞 K ⧸ (w.under (𝓞 K)).asIdeal) ^ w.asIdeal.inertiaDeg (𝓞 K) :=
  ReplayAlgebra.cardQuot_under_eq_pow_inertiaDeg K w

example {K : Type*} [CommRing K] [TopologicalSpace K] [IsTopologicalRing K] (n i : ℕ) :
    Continuous fun M : Matrix (Fin n) (Fin n) K => M.charpoly.coeff i :=
  ReplayTopology.continuous_charpoly_coeff i

example {O R A : Type*} [CommRing O] [CommRing R] [IsLocalRing R] [Algebra O R]
    [CommRing A] [Nontrivial A] [Algebra O A] [Algebra.IsIntegral O A] (f : R →ₐ[O] A) :
    IsLocalHom f :=
  ReplayAlgebra.isLocalHom_of_isIntegral f
```

## Measured elaboration cost

### Exact statement-and-script matches

| Lean declaration workload | Sites | Original heartbeats | Shared consumer heartbeats | Library lemma heartbeats |
| --- | ---: | ---: | ---: | ---: |
| `specMap_ofHom_comp` (5 fingerprints) | 84 | 15,105 | 9,842 | 188 |
| `cardQuot_under_eq_pow_inertiaDeg` | 27 | 39,097 | 2,297 | 1,135 |
| `continuous_unitsHom` | 19 | 4,037 | 2,248 | 188 |
| `not_isTotallyReal_and_isTotallyComplex` | 15 | 854 | 255 | 56 |
| `totallyDisconnected_quotient` | 14 | 9,886 | 714 | 684 |
| `continuous_charpoly_coeff` | 14 | 3,940 | 897 | 276 |
| `padicAlgCl_isIntegral_iff_norm_le_one` | 12 | 14,042 | 637 | 1,176 |
| `isLocalHom_of_isIntegral` | 9 | 30,812 | 1,359 | 3,448 |
| **Total** | **194** | **117,773** | **18,249** | **7,151** |

Combined elaboration drops from **117,773** heartbeats to **25,400** heartbeats (`18,249 + 7,151`), a **78.4% reduction** across the 194 declarations under identical per-batch imports with Lean 4.33.1 (`819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) and Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`. (Note: importing both `ReplayTopology` and `ReplayAlgebra` slightly enlarges the Mathlib environment compared with importing `ReplayTopology` alone, shifting the 33-declaration `ReplayTopology`-only baseline from 11,858 to 13,923 original heartbeats while keeping both original and shared batches under identical imports.) The official replay checks hashes of the published sources; use the shared lemmas in a separate research checkout or when writing new proofs. [Compiler results and source digests](results.json)

### Structurally matched statements

The 73 additional sites come from 54 distinct source modules at import depths 0–102. They have 57 distinct statement-and-script fingerprints, 26 literal normalized headers, and 15 outer-binder-normalized headers. We shortlisted recognizable Mathlib statements with repeated, substantial proof bodies and measured the resulting families. The table ranks the checked families by net heartbeat savings.

| Shared lemma | Sites | Original | Calls | One library proof | Net saved |
| --- | ---: | ---: | ---: | ---: | ---: |
| `norm_le_one_of_isIntegral` | 30 | 59,197 | 3,244 | 1,249 | 54,704 |
| `exists_nat_mul_isIntegral` | 12 | 28,203 | 1,740 | 153 | 26,310 |
| `spanFinrank_maximalIdeal_quotient_succ_le` | 3 | 18,328 | 1,169 | 4,334 | 12,825 |
| `polish_of_lcsc` | 5 | 9,312 | 138 | 1,776 | 7,398 |
| `span_insert_image_erase_eq_top` | 4 | 10,667 | 1,216 | 2,538 | 6,913 |
| `poly_mul_gaussian_bounded` | 3 | 7,303 | 262 | 2,340 | 4,701 |
| `exists_mem_maximalIdeal_notMem_sq_notMem_minimalPrimes` | 4 | 6,264 | 1,181 | 1,723 | 3,360 |
| `exists_repr_ne_zero` | 4 | 4,800 | 1,189 | 1,362 | 2,249 |
| `isLocalRing_quotient_span_singleton` | 4 | 2,253 | 345 | 374 | 1,534 |
| `maximalIdeal_eq_bot_of_le_sq` | 4 | 2,623 | 723 | 623 | 1,277 |
| **New subtotal** | 73 | 148,950 | 11,207 | 16,472 | 121,271 |

For the new sites, 148,950 original heartbeats become 11,207 for the calls plus 16,472 for one copy of each library proof, an 81.4% reduction. Across all 267 sites the corresponding measurement is 266,723 to 53,079 (80.1% reduction). Each comparison uses identical imports in its original and shared batches. Source reading, scanner time, imports, preparing common prerequisites, and kernel replay are outside the measured commands.

## Find another repeated proof

From the tracker repository, point the scanner at a volume prepared by `verify.sh`.

```bash
volume=/path/to/prepared/replay-volume
python3 examples/proof-reuse/scan.py "$volume/lean" --limit 20
```

Inspect any group by passing its full SHA-256 to `--match`. The result includes every matching task ID, local declaration name and line.

The fingerprint covers the text following a declaration name, including its binders, proposition and tactic script, with outer whitespace trimmed. The recognizer looks for plain column-zero theorem or lemma declarations with indented continuations and a literal `:= by`. It skips files containing block-comment, string or backtick delimiters and blocks with line comments. Different local namespaces, variables and instances can give identical text different meanings. Check a proposed abstraction with Lean in the intended context before using it.

The optional modes group statements across different tactic scripts. For example, run `python3 examples/proof-reuse/scan.py "$volume/lean" --mode alpha --limit 10`. Pass the same mode with `--match SHA256` to list all corresponding sites.

| Mode | Candidate blocks | Repeated groups | Occurrences beyond first |
| --- | ---: | ---: | ---: |
| `exact` | 665,170 | 12,478 | 15,932 |
| `header` | 664,404 | 61,917 | 71,808 |
| `alpha` | 664,404 | 64,940 | 78,983 |

All three scans verify source hashes from the tracker and use its full 175,187-module index. Header mode collapses whitespace before the outer proof delimiter. Alpha mode also renames named outer binders by position, retaining binder kinds, dependencies, projection names and named argument labels. The lexical recognizer skips ambiguous proof delimiters and leaves unsupported binding syntax unchanged. Namespace resolution and local instances still require Lean to check each candidate.

To contribute a lemma, record the fingerprint and matching task IDs, then compare the hypotheses and imports at those sites. Add the shared declaration and a check that applies it to the original statements. Include the compiler and Mathlib pins, axiom check, and measured cost of both the original proofs and the shared lemma plus its uses. Link the new declaration and its evidence from this guide so other agents can find it.

## Reproduce the Lean check

Start in the tracker checkout. The example uses the same prepared volume as the contributor build.

```bash
example="$(pwd)/examples/proof-reuse"
export ELAN_HOME="$volume/elan" XDG_CACHE_HOME="$volume/cache"
cd "$volume/lean"
elan run leanprover/lean4:v4.33.1 lake env python3 "$example/check.py" "$PWD"
```

The checker verifies the compiler commit, Mathlib revision and SHA-256 of every matched archive module. The original wrapped batch imports two depth-0 modules that define `normV` and `spMap`. The structural batch includes exact sibling declarations where the archived proof refers to earlier results in the same file, and one depth-0 module for a norm bound. Both sides get the same auxiliary environment. All four shared libraries and all six original/shared batches are compiled, audited against `propext`, `Classical.choice` and `Quot.sound`, and replayed by name using `leanchecker -v`. These receipts cover the extracted declarations; the contributor build handles whole-module replay.
