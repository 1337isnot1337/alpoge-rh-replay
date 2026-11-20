# Independent replay of Alpöge’s RH release

Levent Alpöge announced a Lean proof of the Riemann Hypothesis on November 20, 2026. This repository records an independent attempt to check his published archive. Credit for the claimed proof belongs to Alpöge and his collaborators. [Original announcement](https://alpo.ge/remark.pdf)

## Current status

**Full replay in progress.** No full RH verification receipt has been produced by this project. The [two-worker pilot](evidence/pilot-receipt.json) transferred 150 previously unbuilt modules; the primary reused them and kernel-checked one downstream module.

Current cloud progress is recorded in the [worker status report](STATUS.md). See the [live progress dashboard](https://rohanarun.github.io/alpoge-rh-replay/) for the module ledger breakdown.

## Contributors

Choose any of **175,187 module tasks** or one of **2,858 work packets**. Each module has a source digest, direct dependencies, import depth, and a coordinator snapshot state. Use the [contributor guide](CONTRIBUTING.md) to find an available packet, claim it, build it, and return evidence. Browse the [packet index](tracker/packets.tsv), [snapshot totals](tracker/summary.json), or [open volunteer claims](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue%20is%3Aopen%20in%3Atitle%20Claim).

Start with the [agent instructions](auto-research.md) to claim work and submit replay evidence. Start your evidence comment with `Replay submission` to be credited automatically. Maintainers review the evidence before marking a task complete.

Working on a new Lean proof? The verified lemma library includes continuity of units-valued homomorphisms and total disconnectedness of quotient groups. [Import and use the lemmas](examples/proof-reuse/README.md#use-the-lemmas)

<!-- volunteer-roster-start -->

**Replay volunteers (78)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,067 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M140447](https://github.com/rohanarun/alpoge-rh-replay/issues/6398) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M043021](https://github.com/rohanarun/alpoge-rh-replay/issues/6402) | Claimed |
| [@jwr404](https://github.com/jwr404) | [M126265](https://github.com/rohanarun/alpoge-rh-replay/issues/6403) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M173199](https://github.com/rohanarun/alpoge-rh-replay/issues/6404) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M102216](https://github.com/rohanarun/alpoge-rh-replay/issues/6405) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M114944](https://github.com/rohanarun/alpoge-rh-replay/issues/6406) | Claimed |
| [@jwr404](https://github.com/jwr404) | [M131988](https://github.com/rohanarun/alpoge-rh-replay/issues/6407) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M102955](https://github.com/rohanarun/alpoge-rh-replay/issues/6408) | Claimed |
| [@WilmervH](https://github.com/WilmervH) | [P1875](https://github.com/rohanarun/alpoge-rh-replay/issues/6409) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115525](https://github.com/rohanarun/alpoge-rh-replay/issues/6410) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115694](https://github.com/rohanarun/alpoge-rh-replay/issues/6413) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M161110](https://github.com/rohanarun/alpoge-rh-replay/issues/6415) | Claimed |
| [@jwr404](https://github.com/jwr404) | [M138513](https://github.com/rohanarun/alpoge-rh-replay/issues/6418) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M028363](https://github.com/rohanarun/alpoge-rh-replay/issues/6419) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M108287](https://github.com/rohanarun/alpoge-rh-replay/issues/6421) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M158928](https://github.com/rohanarun/alpoge-rh-replay/issues/6422) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M104089](https://github.com/rohanarun/alpoge-rh-replay/issues/6427) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115730](https://github.com/rohanarun/alpoge-rh-replay/issues/6430) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115229](https://github.com/rohanarun/alpoge-rh-replay/issues/6432) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M110102](https://github.com/rohanarun/alpoge-rh-replay/issues/6434) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[962 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@ANdATIon](https://github.com/ANdATIon) | [M069558](https://github.com/rohanarun/alpoge-rh-replay/issues/6384#issuecomment-7053152881) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M058567](https://github.com/rohanarun/alpoge-rh-replay/issues/6385#issuecomment-7053138125) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M088042](https://github.com/rohanarun/alpoge-rh-replay/issues/6395#issuecomment-7053156871) | Pending review |
| [@drew2apps](https://github.com/drew2apps) | [M165923](https://github.com/rohanarun/alpoge-rh-replay/issues/6399#issuecomment-7053143627) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M103314](https://github.com/rohanarun/alpoge-rh-replay/issues/6400#issuecomment-7053142570) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115800](https://github.com/rohanarun/alpoge-rh-replay/issues/6411#issuecomment-7053158701) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M090995](https://github.com/rohanarun/alpoge-rh-replay/issues/6412#issuecomment-7053145010) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115593](https://github.com/rohanarun/alpoge-rh-replay/issues/6414#issuecomment-7053160040) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M002019](https://github.com/rohanarun/alpoge-rh-replay/issues/6416#issuecomment-7053145104) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M164722](https://github.com/rohanarun/alpoge-rh-replay/issues/6417#issuecomment-7053153562) | Pending review |
| [@Trefoiler](https://github.com/Trefoiler) | [M057592](https://github.com/rohanarun/alpoge-rh-replay/issues/6420#issuecomment-7053146472) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M015116](https://github.com/rohanarun/alpoge-rh-replay/issues/6423#issuecomment-7053145833) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M037382](https://github.com/rohanarun/alpoge-rh-replay/issues/6424#issuecomment-7053146957) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M038820](https://github.com/rohanarun/alpoge-rh-replay/issues/6425#issuecomment-7053148117) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M038883](https://github.com/rohanarun/alpoge-rh-replay/issues/6426#issuecomment-7053149274) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M001442](https://github.com/rohanarun/alpoge-rh-replay/issues/6428#issuecomment-7053151375) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M103321](https://github.com/rohanarun/alpoge-rh-replay/issues/6429#issuecomment-7053148856) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M168696](https://github.com/rohanarun/alpoge-rh-replay/issues/6431#issuecomment-7053148681) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M101641](https://github.com/rohanarun/alpoge-rh-replay/issues/6435#issuecomment-7053148365) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M101525](https://github.com/rohanarun/alpoge-rh-replay/issues/6436#issuecomment-7053149659) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[3,697 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M026409](https://github.com/rohanarun/alpoge-rh-replay/issues/5115#issuecomment-7052676031) | 1 | [Build evidence verified](evidence/volunteers/M026409.json) |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M043800](https://github.com/rohanarun/alpoge-rh-replay/issues/5122#issuecomment-7052817258) | 1 | [Build evidence verified](evidence/volunteers/M043800.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115812](https://github.com/rohanarun/alpoge-rh-replay/issues/5112#issuecomment-7052675398) | 1 | [Build evidence verified](evidence/volunteers/M115812.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115451](https://github.com/rohanarun/alpoge-rh-replay/issues/5108#issuecomment-7052674759) | 1 | [Build evidence verified](evidence/volunteers/M115451.json) |
| [@dhudakk](https://github.com/dhudakk) | [M013837](https://github.com/rohanarun/alpoge-rh-replay/issues/5099#issuecomment-7052902639) | 1 | [Build evidence verified](evidence/volunteers/M013837.json) |
| [@emsi](https://github.com/emsi) | [P1924](https://github.com/rohanarun/alpoge-rh-replay/issues/5148#issuecomment-7052859712) | 64 | [Build evidence verified](evidence/volunteers/P1924.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M111006](https://github.com/rohanarun/alpoge-rh-replay/issues/5097#issuecomment-7052813452) | 1 | [Build evidence verified](evidence/volunteers/M111006.json) |
| [@chriswilson413](https://github.com/chriswilson413) | [M012949](https://github.com/rohanarun/alpoge-rh-replay/issues/5096#issuecomment-7052722711) | 1 | [Build evidence verified](evidence/volunteers/M012949.json) |
| [@TomMoeras](https://github.com/TomMoeras) | [P1827](https://github.com/rohanarun/alpoge-rh-replay/issues/5114#issuecomment-7052774574) | 64 | [Build evidence verified](evidence/volunteers/P1827.json) |
| [@hipotures](https://github.com/hipotures) | [P1623](https://github.com/rohanarun/alpoge-rh-replay/issues/5085#issuecomment-7052795943) | 64 | [Build evidence verified](evidence/volunteers/P1623.json) |
| [@TomMoeras](https://github.com/TomMoeras) | [P1804](https://github.com/rohanarun/alpoge-rh-replay/issues/5128#issuecomment-7052885508) | 64 | [Build evidence verified](evidence/volunteers/P1804.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M042393](https://github.com/rohanarun/alpoge-rh-replay/issues/4854#issuecomment-7052925974) | 1 | [Build evidence verified](evidence/volunteers/M042393.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M110248](https://github.com/rohanarun/alpoge-rh-replay/issues/4839#issuecomment-7052925463) | 1 | [Build evidence verified](evidence/volunteers/M110248.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M101260](https://github.com/rohanarun/alpoge-rh-replay/issues/4834#issuecomment-7052924382) | 1 | [Build evidence verified](evidence/volunteers/M101260.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M038709](https://github.com/rohanarun/alpoge-rh-replay/issues/4832#issuecomment-7052923371) | 1 | [Build evidence verified](evidence/volunteers/M038709.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M115228](https://github.com/rohanarun/alpoge-rh-replay/issues/4833#issuecomment-7052923857) | 1 | [Build evidence verified](evidence/volunteers/M115228.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M115309](https://github.com/rohanarun/alpoge-rh-replay/issues/4820#issuecomment-7052922848) | 1 | [Build evidence verified](evidence/volunteers/M115309.json) |
| [@emsi](https://github.com/emsi) | [P1727](https://github.com/rohanarun/alpoge-rh-replay/issues/3939#issuecomment-7052802638) | 64 | [Build evidence verified](evidence/volunteers/P1727.json) |
| [@JamCh01](https://github.com/JamCh01) | [P1578](https://github.com/rohanarun/alpoge-rh-replay/issues/3850#issuecomment-7052751075) | 64 | [Build evidence verified](evidence/volunteers/P1578.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1536](https://github.com/rohanarun/alpoge-rh-replay/issues/2050#issuecomment-7052857399) | 64 | [Build evidence verified](evidence/volunteers/P1536.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 15,633 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 14,470 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **47,323 / 175,187** |

[See each completed part and its evidence](completed/README.md) · [Machine-readable ledger](tracker/completed.tsv)

<!-- completed-end -->

## Give this prompt to an agent

> Help independently replay the claimed RH proof using https://github.com/rohanarun/alpoge-rh-replay. Read auto-research.md and fast-forward to the latest main commit. Use `python3 tracker/tasks.py next` to find a fully open shallow packet of up to 64 modules. Prefer a packet if its import depth and your resources make it feasible. On a cold or constrained worker, start with one target from `next --cold`. For a partial packet, choose an open module and claim it individually.
>
> Wait for the claim-granted label and matching bot comment before building. Use the pinned inputs, build the targets and their required imports, and submit the receipt, log, and artifact hashes on the claim issue. Keep submitted claims open for review. If you have capacity after submitting, refresh the queue and use the same prepared checkout for a new grant. Release claims you abandon. Report exactly what passed and leave the full-RH verdict to the final audit.

[Full instructions for agents](auto-research.md) · [Claims and conflicts](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+in%3Atitle+Claim)

## Reproduce the check

On Linux, install the elan launcher and ensure its `lean` and `lake` commands are on your PATH. The script also requires Bash, Git, curl, GNU tar, sha256sum, a C toolchain, network access, and a large writable build volume. Run from this repository with a fresh output directory.

```bash
./verify.sh /path/to/empty/replay-directory
```

The script compares every archive part with its SHA-256 digest, checks the toolchain and mathlib revision, builds the final module from source, and writes the transcript to `replay.log` in the output directory. The pinned Lean compiler is 4.33.1 and the mathlib commit is `0df444a360eaa60ab8c11dca51a86af692955474`.

### Integrity checkpoints

The script re-verifies what it depends on at each stage, so archive code that runs during preparation and the build cannot silently replace the tools or records that judge its output. In execution order:

1. **Archive verification.** Every downloaded archive part is checked against `parts.sha256` with `sha256sum -c`. The SHA-256 digests of `Audit.lean` and `parts.sha256` are recorded before any archive code runs.
2. **Manifest pin.** Immediately after extraction — before elan installs the toolchain or Lake runs — the SHA-256 digest of the extracted `lake-manifest.json` is recorded.
3. **Toolchain integrity.** After `elan toolchain install`, immediately before a `--prepare-only` run returns, after the source build (immediately before the audit), and immediately before the fresh-kernel check: `bin/lean`, `bin/leanchecker` and `bin/lake`, and the shared libraries they load (`libleanshared.so`, `libLake_shared.so`, `libleanshared_1.so`, `libleanshared_2.so`, `libInit_shared.so`), still match the digests pinned in `verify.sh` from the official Lean 4.33.1 Linux release for the machine's architecture (x86_64 or AArch64), and `Audit.lean` and `parts.sha256` still match the digests recorded at step 1. Prints `REPLAY_INTEGRITY_CHECK_PASSED`.
4. **Dependency check.** After the Mathlib cache download (the mathlib checkout is separately pinned to the recorded commit above), immediately before a `--prepare-only` run returns, and again after the source build: `lake-manifest.json` still matches the digest recorded at step 2; every package the manifest records is a git checkout at the revision the manifest records, with no tracked file modified — a `git status` that itself fails is treated as a failure, not as a clean tree; the project tree's tracked files, if it is a git checkout, are likewise unmodified; and the packages directory contains no package the manifest does not record. Prints `REPLAY_DEPENDENCIES_PRISTINE_PASSED`.

## Read the evidence

1. `REPLAY_SOURCE_BUILD_PASSED` means Lake built the module containing the final theorem.
2. `REPLAY_AXIOM_AUDIT_PASSED` means the five public theorems in `Main` type-checked against their statements, which `Audit.lean` writes out with Mathlib definitions only. The audit rejects any reported axiom beyond propositional extensionality, classical choice, and quotient soundness.
3. `REPLAY_FRESH_KERNEL_PASSED` means Lean’s checker replayed the declarations imported by `Main` in a fresh environment. It uses the same Lean kernel implementation.

The script prints two further markers. `REPLAY_DEPENDENCIES_PRISTINE_PASSED` means every package recorded in `lake-manifest.json` is checked out at its recorded revision with no tracked file modified. `REPLAY_INTEGRITY_CHECK_PASSED` is printed after the toolchain is installed and again immediately before the audit and fresh-kernel stages: the `lean`, `leanchecker` and `lake` binaries and the shared libraries they load (including `libleanshared.so`, which contains the kernel) still match the digests pinned in `verify.sh` from the official Lean 4.33.1 Linux release for the machine's architecture (x86_64 or AArch64), and `Audit.lean` and `parts.sha256` are unchanged since the archive was verified, so code executed during the build cannot silently replace the tools or statements that judge its output.

An optional statement check runs after these three when `REPLAY_STATEMENT_CHECK=1` is set. It compares the five theorems in `Main` with propositions elaborated in a module that imports only Mathlib, and prints `REPLAY_STATEMENT_CHECK_PASSED`. It can also be run against a completed checkout; see [audit/README.md](audit/README.md).

A completed report should include the exit status, all three outputs, the printed theorem and axioms, and a checksum for the archived transcript. A machine or storage failure leaves the mathematical claim unresolved.

## Optional determinant check

The [M115707 example](examples/M115707/README.md) compares a shorter local Gram determinant argument with the published module. This check runs separately from the volunteer replay.

## Volunteer activity

![Cumulative chart of volunteers, granted claims, and replay submissions](tracker/activity.svg)

[How the chart is counted](ACTIVITY.md) · [Event data](tracker/activity.tsv)

## License

The original replay tooling and documentation in this repository are available under the [MIT License](LICENSE). Upstream Lean source, Mathlib, and third-party artifacts retain their respective licenses.
