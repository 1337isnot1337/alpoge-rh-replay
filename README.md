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

**Replay volunteers (93)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@21Z121Z1](https://github.com/21Z121Z1), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@aulafy](https://github.com/aulafy), [@BenCaunt](https://github.com/BenCaunt), [@BouquetAntoine](https://github.com/BouquetAntoine), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@ChristosMaglaras](https://github.com/ChristosMaglaras), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@HaqtanEfe](https://github.com/HaqtanEfe), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@ljagiello](https://github.com/ljagiello), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@mdpmcc](https://github.com/mdpmcc), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RhizoNymph](https://github.com/RhizoNymph), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@Scratch-net](https://github.com/Scratch-net), [@SeriousRising](https://github.com/SeriousRising), [@Sethumathavanpk](https://github.com/Sethumathavanpk), [@shardmods](https://github.com/shardmods), [@Sigomi](https://github.com/Sigomi), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@TOTOGT](https://github.com/TOTOGT), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@UnityChaos](https://github.com/UnityChaos), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@yingluom](https://github.com/yingluom), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,134 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@mu-mei](https://github.com/mu-mei) | [M101147](https://github.com/rohanarun/alpoge-rh-replay/issues/15661) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M101868](https://github.com/rohanarun/alpoge-rh-replay/issues/15662) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M004276](https://github.com/rohanarun/alpoge-rh-replay/issues/15663) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M005362](https://github.com/rohanarun/alpoge-rh-replay/issues/15666) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M034380](https://github.com/rohanarun/alpoge-rh-replay/issues/15667) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M038946](https://github.com/rohanarun/alpoge-rh-replay/issues/15668) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M109831](https://github.com/rohanarun/alpoge-rh-replay/issues/15669) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M021541](https://github.com/rohanarun/alpoge-rh-replay/issues/15670) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M103638](https://github.com/rohanarun/alpoge-rh-replay/issues/15672) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M079749](https://github.com/rohanarun/alpoge-rh-replay/issues/15674) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M120322](https://github.com/rohanarun/alpoge-rh-replay/issues/15675) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M100701](https://github.com/rohanarun/alpoge-rh-replay/issues/15676) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M101804](https://github.com/rohanarun/alpoge-rh-replay/issues/15678) | Claimed |
| [@amrehan](https://github.com/amrehan) | [M161051](https://github.com/rohanarun/alpoge-rh-replay/issues/15679) | Claimed |
| [@emsi](https://github.com/emsi) | [P1772](https://github.com/rohanarun/alpoge-rh-replay/issues/15680) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M119705](https://github.com/rohanarun/alpoge-rh-replay/issues/15681) | Claimed |
| [@dga471](https://github.com/dga471) | [M164986](https://github.com/rohanarun/alpoge-rh-replay/issues/15682) | Claimed |
| [@dga471](https://github.com/dga471) | [M165004](https://github.com/rohanarun/alpoge-rh-replay/issues/15683) | Claimed |
| [@dga471](https://github.com/dga471) | [M165021](https://github.com/rohanarun/alpoge-rh-replay/issues/15684) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M128308](https://github.com/rohanarun/alpoge-rh-replay/issues/15685) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[2,662 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M052295](https://github.com/rohanarun/alpoge-rh-replay/issues/15553#issuecomment-7058703404) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M055962](https://github.com/rohanarun/alpoge-rh-replay/issues/15554#issuecomment-7058737769) | Pending review |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M128260](https://github.com/rohanarun/alpoge-rh-replay/issues/15555#issuecomment-7058703826) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M061607](https://github.com/rohanarun/alpoge-rh-replay/issues/15556#issuecomment-7058740861) | Pending review |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M133296](https://github.com/rohanarun/alpoge-rh-replay/issues/15557#issuecomment-7058704180) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M061653](https://github.com/rohanarun/alpoge-rh-replay/issues/15558#issuecomment-7058729666) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M003047](https://github.com/rohanarun/alpoge-rh-replay/issues/15562#issuecomment-7058708902) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M061855](https://github.com/rohanarun/alpoge-rh-replay/issues/15563#issuecomment-7058732775) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M061857](https://github.com/rohanarun/alpoge-rh-replay/issues/15566#issuecomment-7058733397) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M061950](https://github.com/rohanarun/alpoge-rh-replay/issues/15568#issuecomment-7058739576) | Pending review |
| [@t-choudhury](https://github.com/t-choudhury) | [M128745](https://github.com/rohanarun/alpoge-rh-replay/issues/15570#issuecomment-7058689729) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M061952](https://github.com/rohanarun/alpoge-rh-replay/issues/15571#issuecomment-7058740204) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M003175](https://github.com/rohanarun/alpoge-rh-replay/issues/15572#issuecomment-7058705805) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M062308](https://github.com/rohanarun/alpoge-rh-replay/issues/15574#issuecomment-7058732179) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M029492](https://github.com/rohanarun/alpoge-rh-replay/issues/15577#issuecomment-7058705966) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M003148](https://github.com/rohanarun/alpoge-rh-replay/issues/15578#issuecomment-7058706417) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M069186](https://github.com/rohanarun/alpoge-rh-replay/issues/15579#issuecomment-7058731576) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M064251](https://github.com/rohanarun/alpoge-rh-replay/issues/15592#issuecomment-7058796086) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M061896](https://github.com/rohanarun/alpoge-rh-replay/issues/15594#issuecomment-7058796311) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M036005](https://github.com/rohanarun/alpoge-rh-replay/issues/15596#issuecomment-7058796269) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[10,276 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@MLEARNER701](https://github.com/MLEARNER701) | [M016856](https://github.com/rohanarun/alpoge-rh-replay/issues/1715#issuecomment-7056544018) | 1 | [Build evidence verified](evidence/volunteers/M016856.json) |
| [@shardmods](https://github.com/shardmods) | [P1604](https://github.com/rohanarun/alpoge-rh-replay/issues/1532#issuecomment-7057500955) | 64 | [Build evidence verified](evidence/volunteers/P1604.json) |
| [@shardmods](https://github.com/shardmods) | [P1793](https://github.com/rohanarun/alpoge-rh-replay/issues/1531#issuecomment-7057496510) | 64 | [Build evidence verified](evidence/volunteers/P1793.json) |
| [@shardmods](https://github.com/shardmods) | [P1518](https://github.com/rohanarun/alpoge-rh-replay/issues/1530#issuecomment-7057491827) | 64 | [Build evidence verified](evidence/volunteers/P1518.json) |
| [@shardmods](https://github.com/shardmods) | [P1600](https://github.com/rohanarun/alpoge-rh-replay/issues/1319#issuecomment-7057481797) | 64 | [Build evidence verified](evidence/volunteers/P1600.json) |
| [@shardmods](https://github.com/shardmods) | [P1533](https://github.com/rohanarun/alpoge-rh-replay/issues/1318#issuecomment-7057477129) | 64 | [Build evidence verified](evidence/volunteers/P1533.json) |
| [@shardmods](https://github.com/shardmods) | [P1725](https://github.com/rohanarun/alpoge-rh-replay/issues/1144#issuecomment-7057473087) | 64 | [Build evidence verified](evidence/volunteers/P1725.json) |
| [@shardmods](https://github.com/shardmods) | [P1475](https://github.com/rohanarun/alpoge-rh-replay/issues/1143#issuecomment-7057468102) | 64 | [Build evidence verified](evidence/volunteers/P1475.json) |
| [@shardmods](https://github.com/shardmods) | [P1636](https://github.com/rohanarun/alpoge-rh-replay/issues/1137#issuecomment-7057464256) | 64 | [Build evidence verified](evidence/volunteers/P1636.json) |
| [@shardmods](https://github.com/shardmods) | [P1422](https://github.com/rohanarun/alpoge-rh-replay/issues/1042#issuecomment-7057460059) | 64 | [Build evidence verified](evidence/volunteers/P1422.json) |
| [@shardmods](https://github.com/shardmods) | [P1399](https://github.com/rohanarun/alpoge-rh-replay/issues/1020#issuecomment-7057452337) | 64 | [Build evidence verified](evidence/volunteers/P1399.json) |
| [@shardmods](https://github.com/shardmods) | [P1605](https://github.com/rohanarun/alpoge-rh-replay/issues/764#issuecomment-7057447557) | 64 | [Build evidence verified](evidence/volunteers/P1605.json) |
| [@shardmods](https://github.com/shardmods) | [P1305](https://github.com/rohanarun/alpoge-rh-replay/issues/763#issuecomment-7057440975) | 64 | [Build evidence verified](evidence/volunteers/P1305.json) |
| [@shardmods](https://github.com/shardmods) | [P1680](https://github.com/rohanarun/alpoge-rh-replay/issues/670#issuecomment-7057435685) | 64 | [Build evidence verified](evidence/volunteers/P1680.json) |
| [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen) | [M015310](https://github.com/rohanarun/alpoge-rh-replay/issues/602#issuecomment-7054670291) | 1 | [Build evidence verified](evidence/volunteers/M015310.json) |
| [@shardmods](https://github.com/shardmods) | [P1526](https://github.com/rohanarun/alpoge-rh-replay/issues/669#issuecomment-7057431603) | 64 | [Build evidence verified](evidence/volunteers/P1526.json) |
| [@shardmods](https://github.com/shardmods) | [P1633](https://github.com/rohanarun/alpoge-rh-replay/issues/1320#issuecomment-7057487253) | 64 | [Build evidence verified](evidence/volunteers/P1633.json) |
| [@shardmods](https://github.com/shardmods) | [P1630](https://github.com/rohanarun/alpoge-rh-replay/issues/557#issuecomment-7057427211) | 64 | [Build evidence verified](evidence/volunteers/P1630.json) |
| [@MLTQ](https://github.com/MLTQ) | [P1489](https://github.com/rohanarun/alpoge-rh-replay/issues/491#issuecomment-7055905601) | 64 | [Build evidence verified](evidence/volunteers/P1489.json) |
| [@shardmods](https://github.com/shardmods) | [P1503](https://github.com/rohanarun/alpoge-rh-replay/issues/1041#issuecomment-7057456328) | 64 | [Build evidence verified](evidence/volunteers/P1503.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 18,437 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 36,998 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **72,655 / 175,187** |

[See each completed part and its evidence](completed/README.md) · [Machine-readable ledger](tracker/completed.tsv)

<!-- completed-end -->

## Give this prompt to an agent

> Help independently replay the claimed RH proof using https://github.com/rohanarun/alpoge-rh-replay. Read auto-research.md and fast-forward to the latest main commit. Use `python3 tracker/tasks.py next` to find a fully open shallow packet of up to 64 modules. Prefer a packet if its import depth and your resources make it feasible. On a cold or constrained worker, start with one target from `next --cold`. For a partial packet, choose an open module and claim it individually.
>
> Wait for the claim-granted label and matching bot comment before building. Use the pinned inputs, build the targets and their required imports, and submit the receipt, log, and artifact hashes on the claim issue. Publish each claim's assets in its own release (GitHub caps a release at 1,000 assets), and before posting, download every link and confirm its SHA-256 and that the log has a build or replay line for every claimed target. Keep submitted claims open for review. If you have capacity after submitting, refresh the queue and use the same prepared checkout for a new grant. Release claims you abandon. Report exactly what passed and leave the full-RH verdict to the final audit.

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
