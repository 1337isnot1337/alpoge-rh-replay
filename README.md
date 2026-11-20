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

**Replay volunteers (66)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@chriswilson413](https://github.com/chriswilson413), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

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
| [@rohanarun](https://github.com/rohanarun) | [M022527](https://github.com/rohanarun/alpoge-rh-replay/issues/5314) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M073911](https://github.com/rohanarun/alpoge-rh-replay/issues/5315) | Claimed |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M099810](https://github.com/rohanarun/alpoge-rh-replay/issues/5316) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M087955](https://github.com/rohanarun/alpoge-rh-replay/issues/5318) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M124715](https://github.com/rohanarun/alpoge-rh-replay/issues/5320) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M075091](https://github.com/rohanarun/alpoge-rh-replay/issues/5323) | Claimed |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M138874](https://github.com/rohanarun/alpoge-rh-replay/issues/5325) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M108154](https://github.com/rohanarun/alpoge-rh-replay/issues/5326) | Claimed |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M155017](https://github.com/rohanarun/alpoge-rh-replay/issues/5327) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M032091](https://github.com/rohanarun/alpoge-rh-replay/issues/5329) | Claimed |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M164826](https://github.com/rohanarun/alpoge-rh-replay/issues/5330) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M139680](https://github.com/rohanarun/alpoge-rh-replay/issues/5331) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M056634](https://github.com/rohanarun/alpoge-rh-replay/issues/5332) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M174409](https://github.com/rohanarun/alpoge-rh-replay/issues/5334) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M138998](https://github.com/rohanarun/alpoge-rh-replay/issues/5335) | Claimed |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M150251](https://github.com/rohanarun/alpoge-rh-replay/issues/5336) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M027061](https://github.com/rohanarun/alpoge-rh-replay/issues/5338) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M152580](https://github.com/rohanarun/alpoge-rh-replay/issues/5340) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M140258](https://github.com/rohanarun/alpoge-rh-replay/issues/5341) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M104599](https://github.com/rohanarun/alpoge-rh-replay/issues/5342) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[610 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@ANdATIon](https://github.com/ANdATIon) | [M074904](https://github.com/rohanarun/alpoge-rh-replay/issues/5273#issuecomment-7052574080) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M000573](https://github.com/rohanarun/alpoge-rh-replay/issues/5274#issuecomment-7052557169) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115370](https://github.com/rohanarun/alpoge-rh-replay/issues/5276#issuecomment-7052577079) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M069412](https://github.com/rohanarun/alpoge-rh-replay/issues/5278#issuecomment-7052577859) | Pending review |
| [@twaldin](https://github.com/twaldin) | [M015403](https://github.com/rohanarun/alpoge-rh-replay/issues/5282#issuecomment-7052578549) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115631](https://github.com/rohanarun/alpoge-rh-replay/issues/5283#issuecomment-7052579929) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M055718](https://github.com/rohanarun/alpoge-rh-replay/issues/5285#issuecomment-7052581281) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M042504](https://github.com/rohanarun/alpoge-rh-replay/issues/5286#issuecomment-7052558355) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M061186](https://github.com/rohanarun/alpoge-rh-replay/issues/5292#issuecomment-7052559835) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M062385](https://github.com/rohanarun/alpoge-rh-replay/issues/5295#issuecomment-7052561281) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M101522](https://github.com/rohanarun/alpoge-rh-replay/issues/5300#issuecomment-7052562739) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M005622](https://github.com/rohanarun/alpoge-rh-replay/issues/5308#issuecomment-7052564950) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M005683](https://github.com/rohanarun/alpoge-rh-replay/issues/5311#issuecomment-7052567340) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M105089](https://github.com/rohanarun/alpoge-rh-replay/issues/5312#issuecomment-7052568633) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115744](https://github.com/rohanarun/alpoge-rh-replay/issues/5317#issuecomment-7052582949) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115427](https://github.com/rohanarun/alpoge-rh-replay/issues/5324#issuecomment-7052584085) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115173](https://github.com/rohanarun/alpoge-rh-replay/issues/5328#issuecomment-7052586298) | Pending review |
| [@jjjhenriksen](https://github.com/jjjhenriksen) | [M109861](https://github.com/rohanarun/alpoge-rh-replay/issues/5333#issuecomment-7052570864) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M164718](https://github.com/rohanarun/alpoge-rh-replay/issues/5337#issuecomment-7052582349) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M119785](https://github.com/rohanarun/alpoge-rh-replay/issues/5339#issuecomment-7052575304) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[3,137 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M017453](https://github.com/rohanarun/alpoge-rh-replay/issues/4333#issuecomment-7052260218) | 1 | [Build evidence verified](evidence/volunteers/M017453.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M037018](https://github.com/rohanarun/alpoge-rh-replay/issues/4302#issuecomment-7052234542) | 1 | [Build evidence verified](evidence/volunteers/M037018.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M027614](https://github.com/rohanarun/alpoge-rh-replay/issues/4301#issuecomment-7052233986) | 1 | [Build evidence verified](evidence/volunteers/M027614.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115292](https://github.com/rohanarun/alpoge-rh-replay/issues/4298#issuecomment-7052233423) | 1 | [Build evidence verified](evidence/volunteers/M115292.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M036447](https://github.com/rohanarun/alpoge-rh-replay/issues/4297#issuecomment-7052232870) | 1 | [Build evidence verified](evidence/volunteers/M036447.json) |
| [@emsi](https://github.com/emsi) | [P1809](https://github.com/rohanarun/alpoge-rh-replay/issues/4385#issuecomment-7052399032) | 64 | [Build evidence verified](evidence/volunteers/P1809.json) |
| [@dhudakk](https://github.com/dhudakk) | [M057575](https://github.com/rohanarun/alpoge-rh-replay/issues/4280#issuecomment-7052400056) | 1 | [Build evidence verified](evidence/volunteers/M057575.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M103999](https://github.com/rohanarun/alpoge-rh-replay/issues/4278#issuecomment-7052255771) | 1 | [Build evidence verified](evidence/volunteers/M103999.json) |
| [@hipotures](https://github.com/hipotures) | [P1595](https://github.com/rohanarun/alpoge-rh-replay/issues/4345#issuecomment-7052383770) | 64 | [Build evidence verified](evidence/volunteers/P1595.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M075081](https://github.com/rohanarun/alpoge-rh-replay/issues/4245#issuecomment-7052380502) | 1 | [Build evidence verified](evidence/volunteers/M075081.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M064695](https://github.com/rohanarun/alpoge-rh-replay/issues/3940#issuecomment-7052234226) | 1 | [Build evidence verified](evidence/volunteers/M064695.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M057323](https://github.com/rohanarun/alpoge-rh-replay/issues/3929#issuecomment-7052235157) | 1 | [Build evidence verified](evidence/volunteers/M057323.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M103998](https://github.com/rohanarun/alpoge-rh-replay/issues/3888#issuecomment-7052294215) | 1 | [Build evidence verified](evidence/volunteers/M103998.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M064847](https://github.com/rohanarun/alpoge-rh-replay/issues/3874#issuecomment-7052355344) | 1 | [Build evidence verified](evidence/volunteers/M064847.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M169364](https://github.com/rohanarun/alpoge-rh-replay/issues/3855#issuecomment-7052327588) | 1 | [Build evidence verified](evidence/volunteers/M169364.json) |
| [@TomMoeras](https://github.com/TomMoeras) | [P1874](https://github.com/rohanarun/alpoge-rh-replay/issues/3711#issuecomment-7052308411) | 64 | [Build evidence verified](evidence/volunteers/P1874.json) |
| [@SeriousRising](https://github.com/SeriousRising) | [P1767](https://github.com/rohanarun/alpoge-rh-replay/issues/3802#issuecomment-7052259365) | 64 | [Build evidence verified](evidence/volunteers/P1767.json) |
| [@TomMoeras](https://github.com/TomMoeras) | [P1896](https://github.com/rohanarun/alpoge-rh-replay/issues/3712#issuecomment-7052412151) | 64 | [Build evidence verified](evidence/volunteers/P1896.json) |
| [@emsi](https://github.com/emsi) | [P1565](https://github.com/rohanarun/alpoge-rh-replay/issues/3120#issuecomment-7052319401) | 64 | [Build evidence verified](evidence/volunteers/P1565.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1547](https://github.com/rohanarun/alpoge-rh-replay/issues/1732#issuecomment-7052255184) | 64 | [Build evidence verified](evidence/volunteers/P1547.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 14,353 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 13,280 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **44,853 / 175,187** |

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
