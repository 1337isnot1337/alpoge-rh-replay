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

**Replay volunteers (59)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@krisyotam](https://github.com/krisyotam), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@surfyhou](https://github.com/surfyhou), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[953 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@loremcdmx](https://github.com/loremcdmx) | [M067688](https://github.com/rohanarun/alpoge-rh-replay/issues/4988) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M072976](https://github.com/rohanarun/alpoge-rh-replay/issues/4989) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115133](https://github.com/rohanarun/alpoge-rh-replay/issues/4990) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M090667](https://github.com/rohanarun/alpoge-rh-replay/issues/4991) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115446](https://github.com/rohanarun/alpoge-rh-replay/issues/4992) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M102165](https://github.com/rohanarun/alpoge-rh-replay/issues/4993) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115386](https://github.com/rohanarun/alpoge-rh-replay/issues/4994) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115434](https://github.com/rohanarun/alpoge-rh-replay/issues/4995) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M006489](https://github.com/rohanarun/alpoge-rh-replay/issues/4996) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M058578](https://github.com/rohanarun/alpoge-rh-replay/issues/4997) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M174961](https://github.com/rohanarun/alpoge-rh-replay/issues/4998) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115166](https://github.com/rohanarun/alpoge-rh-replay/issues/4999) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M153528](https://github.com/rohanarun/alpoge-rh-replay/issues/5000) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115143](https://github.com/rohanarun/alpoge-rh-replay/issues/5001) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115246](https://github.com/rohanarun/alpoge-rh-replay/issues/5002) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M114972](https://github.com/rohanarun/alpoge-rh-replay/issues/5003) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M081199](https://github.com/rohanarun/alpoge-rh-replay/issues/5004) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M064573](https://github.com/rohanarun/alpoge-rh-replay/issues/5005) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115443](https://github.com/rohanarun/alpoge-rh-replay/issues/5006) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115354](https://github.com/rohanarun/alpoge-rh-replay/issues/5007) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[763 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M059692](https://github.com/rohanarun/alpoge-rh-replay/issues/4909#issuecomment-7052422346) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M166929](https://github.com/rohanarun/alpoge-rh-replay/issues/4910#issuecomment-7052389803) | Pending review |
| [@jjjhenriksen](https://github.com/jjjhenriksen) | [M164633](https://github.com/rohanarun/alpoge-rh-replay/issues/4921#issuecomment-7052372470) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M036449](https://github.com/rohanarun/alpoge-rh-replay/issues/4924#issuecomment-7052383734) | Pending review |
| [@zediir](https://github.com/zediir) | [M063421](https://github.com/rohanarun/alpoge-rh-replay/issues/4930#issuecomment-7052378055) | Pending review |
| [@zediir](https://github.com/zediir) | [M063741](https://github.com/rohanarun/alpoge-rh-replay/issues/4933#issuecomment-7052380569) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M025738](https://github.com/rohanarun/alpoge-rh-replay/issues/4938#issuecomment-7052380794) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M027038](https://github.com/rohanarun/alpoge-rh-replay/issues/4943#issuecomment-7052383865) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M060177](https://github.com/rohanarun/alpoge-rh-replay/issues/4948#issuecomment-7052383827) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M024880](https://github.com/rohanarun/alpoge-rh-replay/issues/4950#issuecomment-7052387688) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M028266](https://github.com/rohanarun/alpoge-rh-replay/issues/4959#issuecomment-7052384322) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M045633](https://github.com/rohanarun/alpoge-rh-replay/issues/4964#issuecomment-7052412567) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M164618](https://github.com/rohanarun/alpoge-rh-replay/issues/4965#issuecomment-7052395780) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M061520](https://github.com/rohanarun/alpoge-rh-replay/issues/4966#issuecomment-7052415724) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M101362](https://github.com/rohanarun/alpoge-rh-replay/issues/4967#issuecomment-7052402518) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M103637](https://github.com/rohanarun/alpoge-rh-replay/issues/4971#issuecomment-7052421857) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M002192](https://github.com/rohanarun/alpoge-rh-replay/issues/4974#issuecomment-7052414363) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M006018](https://github.com/rohanarun/alpoge-rh-replay/issues/4977#issuecomment-7052420101) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M051438](https://github.com/rohanarun/alpoge-rh-replay/issues/4981#issuecomment-7052410493) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M027354](https://github.com/rohanarun/alpoge-rh-replay/issues/4987#issuecomment-7052426844) | Pending review |

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
