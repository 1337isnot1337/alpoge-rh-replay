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

**Replay volunteers (57)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@krisyotam](https://github.com/krisyotam), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@surfyhou](https://github.com/surfyhou), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[939 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M043379](https://github.com/rohanarun/alpoge-rh-replay/issues/4273) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M027711](https://github.com/rohanarun/alpoge-rh-replay/issues/4277) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M103999](https://github.com/rohanarun/alpoge-rh-replay/issues/4278) | Claimed |
| [@dhudakk](https://github.com/dhudakk) | [M057575](https://github.com/rohanarun/alpoge-rh-replay/issues/4280) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M105880](https://github.com/rohanarun/alpoge-rh-replay/issues/4281) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115346](https://github.com/rohanarun/alpoge-rh-replay/issues/4283) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115450](https://github.com/rohanarun/alpoge-rh-replay/issues/4284) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M173233](https://github.com/rohanarun/alpoge-rh-replay/issues/4285) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M005900](https://github.com/rohanarun/alpoge-rh-replay/issues/4286) | Claimed |
| [@user42245](https://github.com/user42245) | [M043283](https://github.com/rohanarun/alpoge-rh-replay/issues/4287) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M114959](https://github.com/rohanarun/alpoge-rh-replay/issues/4289) | Claimed |
| [@user42245](https://github.com/user42245) | [M050702](https://github.com/rohanarun/alpoge-rh-replay/issues/4296) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M036447](https://github.com/rohanarun/alpoge-rh-replay/issues/4297) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115292](https://github.com/rohanarun/alpoge-rh-replay/issues/4298) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M027614](https://github.com/rohanarun/alpoge-rh-replay/issues/4301) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M037018](https://github.com/rohanarun/alpoge-rh-replay/issues/4302) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M032317](https://github.com/rohanarun/alpoge-rh-replay/issues/4304) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M056615](https://github.com/rohanarun/alpoge-rh-replay/issues/4313) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M064262](https://github.com/rohanarun/alpoge-rh-replay/issues/4315) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M065222](https://github.com/rohanarun/alpoge-rh-replay/issues/4316) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[535 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@ANdATIon](https://github.com/ANdATIon) | [M064311](https://github.com/rohanarun/alpoge-rh-replay/issues/4282#issuecomment-7051967055) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M104619](https://github.com/rohanarun/alpoge-rh-replay/issues/4288#issuecomment-7051967423) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M009607](https://github.com/rohanarun/alpoge-rh-replay/issues/4291#issuecomment-7051967368) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M000010](https://github.com/rohanarun/alpoge-rh-replay/issues/4292#issuecomment-7051970402) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M004542](https://github.com/rohanarun/alpoge-rh-replay/issues/4293#issuecomment-7051967141) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M164624](https://github.com/rohanarun/alpoge-rh-replay/issues/4294#issuecomment-7051990990) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M065555](https://github.com/rohanarun/alpoge-rh-replay/issues/4295#issuecomment-7051992674) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M164610](https://github.com/rohanarun/alpoge-rh-replay/issues/4299#issuecomment-7051995020) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M005419](https://github.com/rohanarun/alpoge-rh-replay/issues/4300#issuecomment-7051995704) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M132815](https://github.com/rohanarun/alpoge-rh-replay/issues/4305#issuecomment-7051989042) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M157471](https://github.com/rohanarun/alpoge-rh-replay/issues/4306#issuecomment-7051992868) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M155057](https://github.com/rohanarun/alpoge-rh-replay/issues/4307#issuecomment-7051995481) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M161076](https://github.com/rohanarun/alpoge-rh-replay/issues/4308#issuecomment-7051989796) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M152570](https://github.com/rohanarun/alpoge-rh-replay/issues/4309#issuecomment-7051987726) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M154087](https://github.com/rohanarun/alpoge-rh-replay/issues/4310#issuecomment-7051987695) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M057627](https://github.com/rohanarun/alpoge-rh-replay/issues/4314#issuecomment-7051989605) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M130337](https://github.com/rohanarun/alpoge-rh-replay/issues/4317#issuecomment-7051992054) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M130745](https://github.com/rohanarun/alpoge-rh-replay/issues/4318#issuecomment-7051993989) | Pending review |
| [@Trefoiler](https://github.com/Trefoiler) | [M051567](https://github.com/rohanarun/alpoge-rh-replay/issues/4319#issuecomment-7051990671) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M046311](https://github.com/rohanarun/alpoge-rh-replay/issues/4320#issuecomment-7051994116) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[2,445 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M070472](https://github.com/rohanarun/alpoge-rh-replay/issues/3698#issuecomment-7051721950) | 1 | [Build evidence verified](evidence/volunteers/M070472.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M037475](https://github.com/rohanarun/alpoge-rh-replay/issues/3694#issuecomment-7051697331) | 1 | [Build evidence verified](evidence/volunteers/M037475.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115310](https://github.com/rohanarun/alpoge-rh-replay/issues/3691#issuecomment-7051696753) | 1 | [Build evidence verified](evidence/volunteers/M115310.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M056993](https://github.com/rohanarun/alpoge-rh-replay/issues/3688#issuecomment-7051696030) | 1 | [Build evidence verified](evidence/volunteers/M056993.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M162557](https://github.com/rohanarun/alpoge-rh-replay/issues/3687#issuecomment-7051695412) | 1 | [Build evidence verified](evidence/volunteers/M162557.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M103034](https://github.com/rohanarun/alpoge-rh-replay/issues/3679#issuecomment-7051667942) | 1 | [Build evidence verified](evidence/volunteers/M103034.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M171565](https://github.com/rohanarun/alpoge-rh-replay/issues/3677#issuecomment-7051667282) | 1 | [Build evidence verified](evidence/volunteers/M171565.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M131249](https://github.com/rohanarun/alpoge-rh-replay/issues/3676#issuecomment-7051666512) | 1 | [Build evidence verified](evidence/volunteers/M131249.json) |
| [@surfyhou](https://github.com/surfyhou) | [P1752](https://github.com/rohanarun/alpoge-rh-replay/issues/3729#issuecomment-7051768394) | 64 | [Build evidence verified](evidence/volunteers/P1752.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M101521](https://github.com/rohanarun/alpoge-rh-replay/issues/3672#issuecomment-7051665863) | 1 | [Build evidence verified](evidence/volunteers/M101521.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M127929](https://github.com/rohanarun/alpoge-rh-replay/issues/3652#issuecomment-7051639754) | 1 | [Build evidence verified](evidence/volunteers/M127929.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M091584](https://github.com/rohanarun/alpoge-rh-replay/issues/3651#issuecomment-7051639108) | 1 | [Build evidence verified](evidence/volunteers/M091584.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115538](https://github.com/rohanarun/alpoge-rh-replay/issues/3650#issuecomment-7051638508) | 1 | [Build evidence verified](evidence/volunteers/M115538.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M153580](https://github.com/rohanarun/alpoge-rh-replay/issues/3647#issuecomment-7051637837) | 1 | [Build evidence verified](evidence/volunteers/M153580.json) |
| [@dhudakk](https://github.com/dhudakk) | [M081135](https://github.com/rohanarun/alpoge-rh-replay/issues/3633#issuecomment-7051855129) | 1 | [Build evidence verified](evidence/volunteers/M081135.json) |
| [@hipotures](https://github.com/hipotures) | [P1550](https://github.com/rohanarun/alpoge-rh-replay/issues/3605#issuecomment-7051654852) | 64 | [Build evidence verified](evidence/volunteers/P1550.json) |
| [@iAndyHD3](https://github.com/iAndyHD3) | [M075163](https://github.com/rohanarun/alpoge-rh-replay/issues/3508#issuecomment-7051812349) | 1 | [Build evidence verified](evidence/volunteers/M075163.json) |
| [@emsi](https://github.com/emsi) | [P1747](https://github.com/rohanarun/alpoge-rh-replay/issues/3615#issuecomment-7051725415) | 64 | [Build evidence verified](evidence/volunteers/P1747.json) |
| [@iAndyHD3](https://github.com/iAndyHD3) | [M070463](https://github.com/rohanarun/alpoge-rh-replay/issues/3447#issuecomment-7051744993) | 1 | [Build evidence verified](evidence/volunteers/M070463.json) |
| [@emsi](https://github.com/emsi) | [P1713](https://github.com/rohanarun/alpoge-rh-replay/issues/3640#issuecomment-7051840671) | 64 | [Build evidence verified](evidence/volunteers/P1713.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 12,959 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 11,517 |
| **Total with recorded module evidence** | **41,597 / 175,187** |

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
