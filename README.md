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

**Replay volunteers (81)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@aulafy](https://github.com/aulafy), [@BenCaunt](https://github.com/BenCaunt), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@ljagiello](https://github.com/ljagiello), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,033 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M107476](https://github.com/rohanarun/alpoge-rh-replay/issues/7075) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M132031](https://github.com/rohanarun/alpoge-rh-replay/issues/7077) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M171138](https://github.com/rohanarun/alpoge-rh-replay/issues/7080) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M091295](https://github.com/rohanarun/alpoge-rh-replay/issues/7084) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M140073](https://github.com/rohanarun/alpoge-rh-replay/issues/7087) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M073259](https://github.com/rohanarun/alpoge-rh-replay/issues/7088) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M120532](https://github.com/rohanarun/alpoge-rh-replay/issues/7090) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M072886](https://github.com/rohanarun/alpoge-rh-replay/issues/7091) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M170921](https://github.com/rohanarun/alpoge-rh-replay/issues/7095) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M060456](https://github.com/rohanarun/alpoge-rh-replay/issues/7098) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M139204](https://github.com/rohanarun/alpoge-rh-replay/issues/7100) | Claimed |
| [@chriswilson413](https://github.com/chriswilson413) | [M098658](https://github.com/rohanarun/alpoge-rh-replay/issues/7101) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M072377](https://github.com/rohanarun/alpoge-rh-replay/issues/7102) | Claimed |
| [@chriswilson413](https://github.com/chriswilson413) | [M101272](https://github.com/rohanarun/alpoge-rh-replay/issues/7103) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M146405](https://github.com/rohanarun/alpoge-rh-replay/issues/7104) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M090355](https://github.com/rohanarun/alpoge-rh-replay/issues/7105) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M116319](https://github.com/rohanarun/alpoge-rh-replay/issues/7106) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M101534](https://github.com/rohanarun/alpoge-rh-replay/issues/7108) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M061418](https://github.com/rohanarun/alpoge-rh-replay/issues/7109) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M018173](https://github.com/rohanarun/alpoge-rh-replay/issues/7110) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[719 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@aulafy](https://github.com/aulafy) | [M009606](https://github.com/rohanarun/alpoge-rh-replay/issues/7051#issuecomment-7053536155) | Pending review |
| [@sp20262026](https://github.com/sp20262026) | [M030278](https://github.com/rohanarun/alpoge-rh-replay/issues/7053#issuecomment-7053610036) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M163928](https://github.com/rohanarun/alpoge-rh-replay/issues/7071#issuecomment-7053589025) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M037221](https://github.com/rohanarun/alpoge-rh-replay/issues/7073#issuecomment-7053589685) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M114983](https://github.com/rohanarun/alpoge-rh-replay/issues/7074#issuecomment-7053599906) | Pending review |
| [@drew2apps](https://github.com/drew2apps) | [M165947](https://github.com/rohanarun/alpoge-rh-replay/issues/7076#issuecomment-7053593184) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M092323](https://github.com/rohanarun/alpoge-rh-replay/issues/7078#issuecomment-7053589770) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M155858](https://github.com/rohanarun/alpoge-rh-replay/issues/7079#issuecomment-7053590318) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M155953](https://github.com/rohanarun/alpoge-rh-replay/issues/7081#issuecomment-7053591543) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M142961](https://github.com/rohanarun/alpoge-rh-replay/issues/7082#issuecomment-7053593437) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M057456](https://github.com/rohanarun/alpoge-rh-replay/issues/7083#issuecomment-7053592783) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M164179](https://github.com/rohanarun/alpoge-rh-replay/issues/7085#issuecomment-7053594022) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M127925](https://github.com/rohanarun/alpoge-rh-replay/issues/7086#issuecomment-7053605177) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M173416](https://github.com/rohanarun/alpoge-rh-replay/issues/7089#issuecomment-7053604883) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M171122](https://github.com/rohanarun/alpoge-rh-replay/issues/7092#issuecomment-7053604449) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M099262](https://github.com/rohanarun/alpoge-rh-replay/issues/7093#issuecomment-7053595785) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M142807](https://github.com/rohanarun/alpoge-rh-replay/issues/7094#issuecomment-7053600755) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M013841](https://github.com/rohanarun/alpoge-rh-replay/issues/7096#issuecomment-7053596398) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115187](https://github.com/rohanarun/alpoge-rh-replay/issues/7097#issuecomment-7053600967) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M069187](https://github.com/rohanarun/alpoge-rh-replay/issues/7099#issuecomment-7053601019) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[4,602 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115607](https://github.com/rohanarun/alpoge-rh-replay/issues/6490#issuecomment-7053392434) | 1 | [Build evidence verified](evidence/volunteers/M115607.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M140907](https://github.com/rohanarun/alpoge-rh-replay/issues/6489#issuecomment-7053391783) | 1 | [Build evidence verified](evidence/volunteers/M140907.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M037373](https://github.com/rohanarun/alpoge-rh-replay/issues/6487#issuecomment-7053391138) | 1 | [Build evidence verified](evidence/volunteers/M037373.json) |
| [@surfyhou](https://github.com/surfyhou) | [P1802](https://github.com/rohanarun/alpoge-rh-replay/issues/6546#issuecomment-7053519620) | 64 | [Build evidence verified](evidence/volunteers/P1802.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M129915](https://github.com/rohanarun/alpoge-rh-replay/issues/6230#issuecomment-7053387838) | 1 | [Build evidence verified](evidence/volunteers/M129915.json) |
| [@TomMoeras](https://github.com/TomMoeras) | [P1782](https://github.com/rohanarun/alpoge-rh-replay/issues/6252#issuecomment-7053472951) | 64 | [Build evidence verified](evidence/volunteers/P1782.json) |
| [@emsi](https://github.com/emsi) | [P2020](https://github.com/rohanarun/alpoge-rh-replay/issues/6228#issuecomment-7053411894) | 64 | [Build evidence verified](evidence/volunteers/P2020.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M123537](https://github.com/rohanarun/alpoge-rh-replay/issues/6193#issuecomment-7053475805) | 1 | [Build evidence verified](evidence/volunteers/M123537.json) |
| [@emsi](https://github.com/emsi) | [P1884](https://github.com/rohanarun/alpoge-rh-replay/issues/6205#issuecomment-7053492380) | 64 | [Build evidence verified](evidence/volunteers/P1884.json) |
| [@dhudakk](https://github.com/dhudakk) | [M038875](https://github.com/rohanarun/alpoge-rh-replay/issues/6114#issuecomment-7053372089) | 1 | [Build evidence verified](evidence/volunteers/M038875.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M110996](https://github.com/rohanarun/alpoge-rh-replay/issues/6110#issuecomment-7053476616) | 1 | [Build evidence verified](evidence/volunteers/M110996.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M109037](https://github.com/rohanarun/alpoge-rh-replay/issues/6090#issuecomment-7053345175) | 1 | [Build evidence verified](evidence/volunteers/M109037.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M103985](https://github.com/rohanarun/alpoge-rh-replay/issues/5979#issuecomment-7053431293) | 1 | [Build evidence verified](evidence/volunteers/M103985.json) |
| [@hipotures](https://github.com/hipotures) | [P1637](https://github.com/rohanarun/alpoge-rh-replay/issues/5876#issuecomment-7053386673) | 64 | [Build evidence verified](evidence/volunteers/P1637.json) |
| [@emsi](https://github.com/emsi) | [P1982](https://github.com/rohanarun/alpoge-rh-replay/issues/5841#issuecomment-7053462043) | 64 | [Build evidence verified](evidence/volunteers/P1982.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M073999](https://github.com/rohanarun/alpoge-rh-replay/issues/5453#issuecomment-7053344057) | 1 | [Build evidence verified](evidence/volunteers/M073999.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M040857](https://github.com/rohanarun/alpoge-rh-replay/issues/5242#issuecomment-7053432236) | 1 | [Build evidence verified](evidence/volunteers/M040857.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M169422](https://github.com/rohanarun/alpoge-rh-replay/issues/5102#issuecomment-7053388913) | 1 | [Build evidence verified](evidence/volunteers/M169422.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1749](https://github.com/rohanarun/alpoge-rh-replay/issues/2702#issuecomment-7053477459) | 64 | [Build evidence verified](evidence/volunteers/P1749.json) |
| [@dgahelper](https://github.com/dgahelper) | [P1472](https://github.com/rohanarun/alpoge-rh-replay/issues/1196#issuecomment-7053406439) | 64 | [Build evidence verified](evidence/volunteers/P1472.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 17,209 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 18,147 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **52,576 / 175,187** |

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
