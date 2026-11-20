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

**Replay volunteers (64)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@chriswilson413](https://github.com/chriswilson413), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[987 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@BenCaunt](https://github.com/BenCaunt) | [M111006](https://github.com/rohanarun/alpoge-rh-replay/issues/5097) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M132432](https://github.com/rohanarun/alpoge-rh-replay/issues/5098) | Claimed |
| [@dhudakk](https://github.com/dhudakk) | [M013837](https://github.com/rohanarun/alpoge-rh-replay/issues/5099) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M169422](https://github.com/rohanarun/alpoge-rh-replay/issues/5102) | Claimed |
| [@surfyhou](https://github.com/surfyhou) | [P1828](https://github.com/rohanarun/alpoge-rh-replay/issues/5105) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M140540](https://github.com/rohanarun/alpoge-rh-replay/issues/5106) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115451](https://github.com/rohanarun/alpoge-rh-replay/issues/5108) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115812](https://github.com/rohanarun/alpoge-rh-replay/issues/5112) | Claimed |
| [@TomMoeras](https://github.com/TomMoeras) | [P1827](https://github.com/rohanarun/alpoge-rh-replay/issues/5114) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M026409](https://github.com/rohanarun/alpoge-rh-replay/issues/5115) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M025319](https://github.com/rohanarun/alpoge-rh-replay/issues/5116) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M169425](https://github.com/rohanarun/alpoge-rh-replay/issues/5118) | Claimed |
| [@t-choudhury](https://github.com/t-choudhury) | [M146660](https://github.com/rohanarun/alpoge-rh-replay/issues/5121) | Claimed |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M043800](https://github.com/rohanarun/alpoge-rh-replay/issues/5122) | Claimed |
| [@TomMoeras](https://github.com/TomMoeras) | [P1804](https://github.com/rohanarun/alpoge-rh-replay/issues/5128) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M002045](https://github.com/rohanarun/alpoge-rh-replay/issues/5131) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M002977](https://github.com/rohanarun/alpoge-rh-replay/issues/5136) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M003992](https://github.com/rohanarun/alpoge-rh-replay/issues/5140) | Claimed |
| [@emsi](https://github.com/emsi) | [P1924](https://github.com/rohanarun/alpoge-rh-replay/issues/5148) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M004106](https://github.com/rohanarun/alpoge-rh-replay/issues/5150) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[848 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M042973](https://github.com/rohanarun/alpoge-rh-replay/issues/5111#issuecomment-7052488657) | Pending review |
| [@zediir](https://github.com/zediir) | [M000921](https://github.com/rohanarun/alpoge-rh-replay/issues/5119#issuecomment-7052469526) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M023687](https://github.com/rohanarun/alpoge-rh-replay/issues/5120#issuecomment-7052469898) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M025703](https://github.com/rohanarun/alpoge-rh-replay/issues/5123#issuecomment-7052478138) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M051376](https://github.com/rohanarun/alpoge-rh-replay/issues/5126#issuecomment-7052477948) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115060](https://github.com/rohanarun/alpoge-rh-replay/issues/5129#issuecomment-7052492765) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M101448](https://github.com/rohanarun/alpoge-rh-replay/issues/5132#issuecomment-7052475622) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M019700](https://github.com/rohanarun/alpoge-rh-replay/issues/5133#issuecomment-7052484139) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M018377](https://github.com/rohanarun/alpoge-rh-replay/issues/5134#issuecomment-7052478303) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M061967](https://github.com/rohanarun/alpoge-rh-replay/issues/5137#issuecomment-7052486039) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M164582](https://github.com/rohanarun/alpoge-rh-replay/issues/5138#issuecomment-7052481066) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M057820](https://github.com/rohanarun/alpoge-rh-replay/issues/5139#issuecomment-7052485543) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M020940](https://github.com/rohanarun/alpoge-rh-replay/issues/5141#issuecomment-7052479416) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M101542](https://github.com/rohanarun/alpoge-rh-replay/issues/5142#issuecomment-7052494930) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M039000](https://github.com/rohanarun/alpoge-rh-replay/issues/5143#issuecomment-7052480064) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M101472](https://github.com/rohanarun/alpoge-rh-replay/issues/5144#issuecomment-7052482649) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M072980](https://github.com/rohanarun/alpoge-rh-replay/issues/5145#issuecomment-7052495991) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M000565](https://github.com/rohanarun/alpoge-rh-replay/issues/5147#issuecomment-7052477938) | Pending review |
| [@zediir](https://github.com/zediir) | [M006328](https://github.com/rohanarun/alpoge-rh-replay/issues/5149#issuecomment-7052481960) | Pending review |
| [@zediir](https://github.com/zediir) | [M006415](https://github.com/rohanarun/alpoge-rh-replay/issues/5151#issuecomment-7052490038) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[2,807 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M150852](https://github.com/rohanarun/alpoge-rh-replay/issues/4170#issuecomment-7052105476) | 1 | [Build evidence verified](evidence/volunteers/M150852.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M066359](https://github.com/rohanarun/alpoge-rh-replay/issues/4150#issuecomment-7052086830) | 1 | [Build evidence verified](evidence/volunteers/M066359.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M076682](https://github.com/rohanarun/alpoge-rh-replay/issues/4146#issuecomment-7052086147) | 1 | [Build evidence verified](evidence/volunteers/M076682.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115078](https://github.com/rohanarun/alpoge-rh-replay/issues/4143#issuecomment-7052085488) | 1 | [Build evidence verified](evidence/volunteers/M115078.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M007084](https://github.com/rohanarun/alpoge-rh-replay/issues/4141#issuecomment-7052084849) | 1 | [Build evidence verified](evidence/volunteers/M007084.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M132068](https://github.com/rohanarun/alpoge-rh-replay/issues/4173#issuecomment-7052061003) | 1 | [Build evidence verified](evidence/volunteers/M132068.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M131987](https://github.com/rohanarun/alpoge-rh-replay/issues/4171#issuecomment-7052061442) | 1 | [Build evidence verified](evidence/volunteers/M131987.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M060559](https://github.com/rohanarun/alpoge-rh-replay/issues/4121#issuecomment-7052070570) | 1 | [Build evidence verified](evidence/volunteers/M060559.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115216](https://github.com/rohanarun/alpoge-rh-replay/issues/4119#issuecomment-7052069892) | 1 | [Build evidence verified](evidence/volunteers/M115216.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M066731](https://github.com/rohanarun/alpoge-rh-replay/issues/4117#issuecomment-7052069338) | 1 | [Build evidence verified](evidence/volunteers/M066731.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M067516](https://github.com/rohanarun/alpoge-rh-replay/issues/4114#issuecomment-7052068567) | 1 | [Build evidence verified](evidence/volunteers/M067516.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M169272](https://github.com/rohanarun/alpoge-rh-replay/issues/3959#issuecomment-7052180922) | 1 | [Build evidence verified](evidence/volunteers/M169272.json) |
| [@emsi](https://github.com/emsi) | [P1795](https://github.com/rohanarun/alpoge-rh-replay/issues/4122#issuecomment-7052129483) | 64 | [Build evidence verified](evidence/volunteers/P1795.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M142327](https://github.com/rohanarun/alpoge-rh-replay/issues/3924#issuecomment-7052166707) | 1 | [Build evidence verified](evidence/volunteers/M142327.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M105275](https://github.com/rohanarun/alpoge-rh-replay/issues/3893#issuecomment-7052198741) | 1 | [Build evidence verified](evidence/volunteers/M105275.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M036336](https://github.com/rohanarun/alpoge-rh-replay/issues/3867#issuecomment-7052080846) | 1 | [Build evidence verified](evidence/volunteers/M036336.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M168826](https://github.com/rohanarun/alpoge-rh-replay/issues/3845#issuecomment-7052165729) | 1 | [Build evidence verified](evidence/volunteers/M168826.json) |
| [@dga471](https://github.com/dga471) | [M073708](https://github.com/rohanarun/alpoge-rh-replay/issues/3458#issuecomment-7052095498) | 1 | [Build evidence verified](evidence/volunteers/M073708.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1519](https://github.com/rohanarun/alpoge-rh-replay/issues/1702#issuecomment-7052192362) | 64 | [Build evidence verified](evidence/volunteers/P1519.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M151980](https://github.com/rohanarun/alpoge-rh-replay/issues/1136#issuecomment-7052130021) | 1 | [Build evidence verified](evidence/volunteers/M151980.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 14,108 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 12,383 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **43,711 / 175,187** |

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
