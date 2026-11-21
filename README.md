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

**Replay volunteers (91)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@21Z121Z1](https://github.com/21Z121Z1), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@aulafy](https://github.com/aulafy), [@BenCaunt](https://github.com/BenCaunt), [@BouquetAntoine](https://github.com/BouquetAntoine), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@ChristosMaglaras](https://github.com/ChristosMaglaras), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@HaqtanEfe](https://github.com/HaqtanEfe), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@ljagiello](https://github.com/ljagiello), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@mdpmcc](https://github.com/mdpmcc), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RhizoNymph](https://github.com/RhizoNymph), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@Sethumathavanpk](https://github.com/Sethumathavanpk), [@shardmods](https://github.com/shardmods), [@Sigomi](https://github.com/Sigomi), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@TOTOGT](https://github.com/TOTOGT), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@UnityChaos](https://github.com/UnityChaos), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,080 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M004254](https://github.com/rohanarun/alpoge-rh-replay/issues/11798) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M123041](https://github.com/rohanarun/alpoge-rh-replay/issues/11799) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M140448](https://github.com/rohanarun/alpoge-rh-replay/issues/11801) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M087338](https://github.com/rohanarun/alpoge-rh-replay/issues/11810) | Claimed |
| [@hipotures](https://github.com/hipotures) | [P1945](https://github.com/rohanarun/alpoge-rh-replay/issues/11863) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M063061](https://github.com/rohanarun/alpoge-rh-replay/issues/11876) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M044602](https://github.com/rohanarun/alpoge-rh-replay/issues/11877) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M080312](https://github.com/rohanarun/alpoge-rh-replay/issues/11879) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M069411](https://github.com/rohanarun/alpoge-rh-replay/issues/11883) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M048786](https://github.com/rohanarun/alpoge-rh-replay/issues/11885) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M005753](https://github.com/rohanarun/alpoge-rh-replay/issues/11886) | Claimed |
| [@dgahelper](https://github.com/dgahelper) | [P1956](https://github.com/rohanarun/alpoge-rh-replay/issues/11887) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M028979](https://github.com/rohanarun/alpoge-rh-replay/issues/11889) | Claimed |
| [@jjjhenriksen](https://github.com/jjjhenriksen) | [M134329](https://github.com/rohanarun/alpoge-rh-replay/issues/11898) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M005701](https://github.com/rohanarun/alpoge-rh-replay/issues/11899) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M106076](https://github.com/rohanarun/alpoge-rh-replay/issues/11901) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M157213](https://github.com/rohanarun/alpoge-rh-replay/issues/11902) | Claimed |
| [@BouquetAntoine](https://github.com/BouquetAntoine) | [M050914](https://github.com/rohanarun/alpoge-rh-replay/issues/11903) | Claimed |
| [@twaldin](https://github.com/twaldin) | [P1957](https://github.com/rohanarun/alpoge-rh-replay/issues/11927) | Claimed |
| [@21Z121Z1](https://github.com/21Z121Z1) | [M123475](https://github.com/rohanarun/alpoge-rh-replay/issues/11944) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[4,129 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@ANdATIon](https://github.com/ANdATIon) | [M069939](https://github.com/rohanarun/alpoge-rh-replay/issues/11923#issuecomment-7056789357) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M157138](https://github.com/rohanarun/alpoge-rh-replay/issues/11924#issuecomment-7056789351) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M042848](https://github.com/rohanarun/alpoge-rh-replay/issues/11925#issuecomment-7056769702) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M126981](https://github.com/rohanarun/alpoge-rh-replay/issues/11926#issuecomment-7056788723) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M006946](https://github.com/rohanarun/alpoge-rh-replay/issues/11928#issuecomment-7056778024) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M006723](https://github.com/rohanarun/alpoge-rh-replay/issues/11929#issuecomment-7056779122) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M006945](https://github.com/rohanarun/alpoge-rh-replay/issues/11930#issuecomment-7056780337) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M061095](https://github.com/rohanarun/alpoge-rh-replay/issues/11931#issuecomment-7056781459) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M154584](https://github.com/rohanarun/alpoge-rh-replay/issues/11932#issuecomment-7056782619) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M101484](https://github.com/rohanarun/alpoge-rh-replay/issues/11933#issuecomment-7056783701) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M138869](https://github.com/rohanarun/alpoge-rh-replay/issues/11934#issuecomment-7056796299) | Pending review |
| [@UnityChaos](https://github.com/UnityChaos) | [M064217](https://github.com/rohanarun/alpoge-rh-replay/issues/11936#issuecomment-7056784717) | Pending review |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M132951](https://github.com/rohanarun/alpoge-rh-replay/issues/11939#issuecomment-7056777701) | Pending review |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115355](https://github.com/rohanarun/alpoge-rh-replay/issues/11941#issuecomment-7056778187) | Pending review |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M124312](https://github.com/rohanarun/alpoge-rh-replay/issues/11942#issuecomment-7056778541) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M019690](https://github.com/rohanarun/alpoge-rh-replay/issues/11943#issuecomment-7056774518) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M110233](https://github.com/rohanarun/alpoge-rh-replay/issues/11945#issuecomment-7056787304) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M116347](https://github.com/rohanarun/alpoge-rh-replay/issues/11946#issuecomment-7056788466) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M004199](https://github.com/rohanarun/alpoge-rh-replay/issues/11947#issuecomment-7056795623) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M123567](https://github.com/rohanarun/alpoge-rh-replay/issues/11948#issuecomment-7056789647) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[5,466 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M134676](https://github.com/rohanarun/alpoge-rh-replay/issues/7713#issuecomment-7054001793) | 1 | [Build evidence verified](evidence/volunteers/M134676.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M060779](https://github.com/rohanarun/alpoge-rh-replay/issues/7704#issuecomment-7054002789) | 1 | [Build evidence verified](evidence/volunteers/M060779.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M091536](https://github.com/rohanarun/alpoge-rh-replay/issues/7709#issuecomment-7053980599) | 1 | [Build evidence verified](evidence/volunteers/M091536.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M171940](https://github.com/rohanarun/alpoge-rh-replay/issues/7700#issuecomment-7053992107) | 1 | [Build evidence verified](evidence/volunteers/M171940.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M119898](https://github.com/rohanarun/alpoge-rh-replay/issues/7697#issuecomment-7054007017) | 1 | [Build evidence verified](evidence/volunteers/M119898.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M170882](https://github.com/rohanarun/alpoge-rh-replay/issues/7693#issuecomment-7054012959) | 1 | [Build evidence verified](evidence/volunteers/M170882.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M141522](https://github.com/rohanarun/alpoge-rh-replay/issues/7687#issuecomment-7053987888) | 1 | [Build evidence verified](evidence/volunteers/M141522.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M027664](https://github.com/rohanarun/alpoge-rh-replay/issues/7684#issuecomment-7053994407) | 1 | [Build evidence verified](evidence/volunteers/M027664.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M032086](https://github.com/rohanarun/alpoge-rh-replay/issues/7682#issuecomment-7053987338) | 1 | [Build evidence verified](evidence/volunteers/M032086.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M154311](https://github.com/rohanarun/alpoge-rh-replay/issues/7681#issuecomment-7053993227) | 1 | [Build evidence verified](evidence/volunteers/M154311.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M143083](https://github.com/rohanarun/alpoge-rh-replay/issues/7680#issuecomment-7054015037) | 1 | [Build evidence verified](evidence/volunteers/M143083.json) |
| [@whitegrave1917-web](https://github.com/whitegrave1917-web) | [M027471](https://github.com/rohanarun/alpoge-rh-replay/issues/7678#issuecomment-7053976717) | 1 | [Build evidence verified](evidence/volunteers/M027471.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115807](https://github.com/rohanarun/alpoge-rh-replay/issues/7677#issuecomment-7054014043) | 1 | [Build evidence verified](evidence/volunteers/M115807.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M024727](https://github.com/rohanarun/alpoge-rh-replay/issues/7671#issuecomment-7053984793) | 1 | [Build evidence verified](evidence/volunteers/M024727.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M120044](https://github.com/rohanarun/alpoge-rh-replay/issues/7675#issuecomment-7054000725) | 1 | [Build evidence verified](evidence/volunteers/M120044.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M077532](https://github.com/rohanarun/alpoge-rh-replay/issues/7665#issuecomment-7054008019) | 1 | [Build evidence verified](evidence/volunteers/M077532.json) |
| [@emsi](https://github.com/emsi) | [P1932](https://github.com/rohanarun/alpoge-rh-replay/issues/7252#issuecomment-7053957546) | 64 | [Build evidence verified](evidence/volunteers/P1932.json) |
| [@emsi](https://github.com/emsi) | [P1930](https://github.com/rohanarun/alpoge-rh-replay/issues/6862#issuecomment-7054032933) | 64 | [Build evidence verified](evidence/volunteers/P1930.json) |
| [@surfyhou](https://github.com/surfyhou) | [P1826](https://github.com/rohanarun/alpoge-rh-replay/issues/7063#issuecomment-7053958065) | 64 | [Build evidence verified](evidence/volunteers/P1826.json) |
| [@CubeJerry](https://github.com/CubeJerry) | [M031623](https://github.com/rohanarun/alpoge-rh-replay/issues/6067#issuecomment-7053967155) | 1 | [Build evidence verified](evidence/volunteers/M031623.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 18,469 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 20,145 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **55,834 / 175,187** |

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
