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

**Replay volunteers (80)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@ljagiello](https://github.com/ljagiello), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,045 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115155](https://github.com/rohanarun/alpoge-rh-replay/issues/6811) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M175183](https://github.com/rohanarun/alpoge-rh-replay/issues/6813) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M149533](https://github.com/rohanarun/alpoge-rh-replay/issues/6814) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115457](https://github.com/rohanarun/alpoge-rh-replay/issues/6815) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M060235](https://github.com/rohanarun/alpoge-rh-replay/issues/6817) | Claimed |
| [@emsi](https://github.com/emsi) | [P2038](https://github.com/rohanarun/alpoge-rh-replay/issues/6818) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M154816](https://github.com/rohanarun/alpoge-rh-replay/issues/6821) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M169268](https://github.com/rohanarun/alpoge-rh-replay/issues/6822) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M024666](https://github.com/rohanarun/alpoge-rh-replay/issues/6823) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M162558](https://github.com/rohanarun/alpoge-rh-replay/issues/6824) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M104593](https://github.com/rohanarun/alpoge-rh-replay/issues/6827) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M120450](https://github.com/rohanarun/alpoge-rh-replay/issues/6829) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M157217](https://github.com/rohanarun/alpoge-rh-replay/issues/6831) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M092903](https://github.com/rohanarun/alpoge-rh-replay/issues/6832) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M120677](https://github.com/rohanarun/alpoge-rh-replay/issues/6833) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M087539](https://github.com/rohanarun/alpoge-rh-replay/issues/6834) | Claimed |
| [@ANdATIon](https://github.com/ANdATIon) | [M127906](https://github.com/rohanarun/alpoge-rh-replay/issues/6836) | Claimed |
| [@ANdATIon](https://github.com/ANdATIon) | [M127919](https://github.com/rohanarun/alpoge-rh-replay/issues/6840) | Claimed |
| [@ANdATIon](https://github.com/ANdATIon) | [M170799](https://github.com/rohanarun/alpoge-rh-replay/issues/6841) | Claimed |
| [@emsi](https://github.com/emsi) | [P1930](https://github.com/rohanarun/alpoge-rh-replay/issues/6862) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[661 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@Trefoiler](https://github.com/Trefoiler) | [M076919](https://github.com/rohanarun/alpoge-rh-replay/issues/6842#issuecomment-7053431504) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115221](https://github.com/rohanarun/alpoge-rh-replay/issues/6843#issuecomment-7053428772) | Pending review |
| [@emsi](https://github.com/emsi) | [M100911](https://github.com/rohanarun/alpoge-rh-replay/issues/6844#issuecomment-7053441980) | Pending review |
| [@emsi](https://github.com/emsi) | [M101001](https://github.com/rohanarun/alpoge-rh-replay/issues/6845#issuecomment-7053443741) | Pending review |
| [@emsi](https://github.com/emsi) | [M080617](https://github.com/rohanarun/alpoge-rh-replay/issues/6846#issuecomment-7053434962) | Pending review |
| [@emsi](https://github.com/emsi) | [M095823](https://github.com/rohanarun/alpoge-rh-replay/issues/6847#issuecomment-7053436832) | Pending review |
| [@emsi](https://github.com/emsi) | [M140107](https://github.com/rohanarun/alpoge-rh-replay/issues/6848#issuecomment-7053438592) | Pending review |
| [@emsi](https://github.com/emsi) | [M046761](https://github.com/rohanarun/alpoge-rh-replay/issues/6849#issuecomment-7053440229) | Pending review |
| [@emsi](https://github.com/emsi) | [M004494](https://github.com/rohanarun/alpoge-rh-replay/issues/6850#issuecomment-7053445440) | Pending review |
| [@emsi](https://github.com/emsi) | [M062111](https://github.com/rohanarun/alpoge-rh-replay/issues/6851#issuecomment-7053447287) | Pending review |
| [@egergerfg](https://github.com/egergerfg) | [M175010](https://github.com/rohanarun/alpoge-rh-replay/issues/6852#issuecomment-7053428007) | Pending review |
| [@emsi](https://github.com/emsi) | [M101068](https://github.com/rohanarun/alpoge-rh-replay/issues/6853#issuecomment-7053449081) | Pending review |
| [@emsi](https://github.com/emsi) | [M003636](https://github.com/rohanarun/alpoge-rh-replay/issues/6854#issuecomment-7053450687) | Pending review |
| [@emsi](https://github.com/emsi) | [M044619](https://github.com/rohanarun/alpoge-rh-replay/issues/6855#issuecomment-7053452453) | Pending review |
| [@emsi](https://github.com/emsi) | [M003937](https://github.com/rohanarun/alpoge-rh-replay/issues/6856#issuecomment-7053454115) | Pending review |
| [@emsi](https://github.com/emsi) | [M004240](https://github.com/rohanarun/alpoge-rh-replay/issues/6857#issuecomment-7053455872) | Pending review |
| [@emsi](https://github.com/emsi) | [M039162](https://github.com/rohanarun/alpoge-rh-replay/issues/6858#issuecomment-7053457679) | Pending review |
| [@emsi](https://github.com/emsi) | [M080088](https://github.com/rohanarun/alpoge-rh-replay/issues/6859#issuecomment-7053459467) | Pending review |
| [@emsi](https://github.com/emsi) | [M100680](https://github.com/rohanarun/alpoge-rh-replay/issues/6860#issuecomment-7053461375) | Pending review |
| [@Trefoiler](https://github.com/Trefoiler) | [M077692](https://github.com/rohanarun/alpoge-rh-replay/issues/6861#issuecomment-7053442101) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[4,417 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@emsi](https://github.com/emsi) | [P1806](https://github.com/rohanarun/alpoge-rh-replay/issues/4918#issuecomment-7053120180) | 64 | [Build evidence verified](evidence/volunteers/P1806.json) |
| [@whitegrave1917-web](https://github.com/whitegrave1917-web) | [M014782](https://github.com/rohanarun/alpoge-rh-replay/issues/4731#issuecomment-7053284382) | 1 | [Build evidence verified](evidence/volunteers/M014782.json) |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [P1661](https://github.com/rohanarun/alpoge-rh-replay/issues/4732#issuecomment-7053186653) | 64 | [Build evidence verified](evidence/volunteers/P1661.json) |
| [@dga471](https://github.com/dga471) | [M009606](https://github.com/rohanarun/alpoge-rh-replay/issues/4679#issuecomment-7053191219) | 1 | [Build evidence verified](evidence/volunteers/M009606.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1610](https://github.com/rohanarun/alpoge-rh-replay/issues/3280#issuecomment-7053213380) | 64 | [Build evidence verified](evidence/volunteers/P1610.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1591](https://github.com/rohanarun/alpoge-rh-replay/issues/3208#issuecomment-7053226927) | 64 | [Build evidence verified](evidence/volunteers/P1591.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1563](https://github.com/rohanarun/alpoge-rh-replay/issues/3155#issuecomment-7053201513) | 64 | [Build evidence verified](evidence/volunteers/P1563.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1537](https://github.com/rohanarun/alpoge-rh-replay/issues/2916#issuecomment-7053229855) | 64 | [Build evidence verified](evidence/volunteers/P1537.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1655](https://github.com/rohanarun/alpoge-rh-replay/issues/2496#issuecomment-7053204427) | 64 | [Build evidence verified](evidence/volunteers/P1655.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1516](https://github.com/rohanarun/alpoge-rh-replay/issues/1271#issuecomment-7053221449) | 64 | [Build evidence verified](evidence/volunteers/P1516.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1515](https://github.com/rohanarun/alpoge-rh-replay/issues/1265#issuecomment-7053204315) | 64 | [Build evidence verified](evidence/volunteers/P1515.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1514](https://github.com/rohanarun/alpoge-rh-replay/issues/1262#issuecomment-7053210098) | 64 | [Build evidence verified](evidence/volunteers/P1514.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1513](https://github.com/rohanarun/alpoge-rh-replay/issues/1258#issuecomment-7053193171) | 64 | [Build evidence verified](evidence/volunteers/P1513.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1507](https://github.com/rohanarun/alpoge-rh-replay/issues/1255#issuecomment-7053218077) | 64 | [Build evidence verified](evidence/volunteers/P1507.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1506](https://github.com/rohanarun/alpoge-rh-replay/issues/1251#issuecomment-7053195820) | 64 | [Build evidence verified](evidence/volunteers/P1506.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1487](https://github.com/rohanarun/alpoge-rh-replay/issues/1237#issuecomment-7053198892) | 64 | [Build evidence verified](evidence/volunteers/P1487.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1478](https://github.com/rohanarun/alpoge-rh-replay/issues/1226#issuecomment-7053223976) | 64 | [Build evidence verified](evidence/volunteers/P1478.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1476](https://github.com/rohanarun/alpoge-rh-replay/issues/1222#issuecomment-7053215616) | 64 | [Build evidence verified](evidence/volunteers/P1476.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1474](https://github.com/rohanarun/alpoge-rh-replay/issues/1217#issuecomment-7053207398) | 64 | [Build evidence verified](evidence/volunteers/P1474.json) |
| [@angusbarry](https://github.com/angusbarry) | [P1606](https://github.com/rohanarun/alpoge-rh-replay/issues/664#issuecomment-7053324238) | 64 | [Build evidence verified](evidence/volunteers/P1606.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 16,731 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 17,458 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **51,409 / 175,187** |

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
