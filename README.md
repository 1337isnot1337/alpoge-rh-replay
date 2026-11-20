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

[871 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M036447](https://github.com/rohanarun/alpoge-rh-replay/issues/4297) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115292](https://github.com/rohanarun/alpoge-rh-replay/issues/4298) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M027614](https://github.com/rohanarun/alpoge-rh-replay/issues/4301) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M037018](https://github.com/rohanarun/alpoge-rh-replay/issues/4302) | Claimed |
| [@surfyhou](https://github.com/surfyhou) | [P1780](https://github.com/rohanarun/alpoge-rh-replay/issues/4327) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M017453](https://github.com/rohanarun/alpoge-rh-replay/issues/4333) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M070275](https://github.com/rohanarun/alpoge-rh-replay/issues/4336) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M070299](https://github.com/rohanarun/alpoge-rh-replay/issues/4340) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M076255](https://github.com/rohanarun/alpoge-rh-replay/issues/4343) | Claimed |
| [@hipotures](https://github.com/hipotures) | [P1595](https://github.com/rohanarun/alpoge-rh-replay/issues/4345) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115330](https://github.com/rohanarun/alpoge-rh-replay/issues/4383) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M143575](https://github.com/rohanarun/alpoge-rh-replay/issues/4384) | Claimed |
| [@emsi](https://github.com/emsi) | [P1809](https://github.com/rohanarun/alpoge-rh-replay/issues/4385) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M081935](https://github.com/rohanarun/alpoge-rh-replay/issues/4386) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115052](https://github.com/rohanarun/alpoge-rh-replay/issues/4387) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115601](https://github.com/rohanarun/alpoge-rh-replay/issues/4419) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M013541](https://github.com/rohanarun/alpoge-rh-replay/issues/4421) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M082499](https://github.com/rohanarun/alpoge-rh-replay/issues/4423) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115015](https://github.com/rohanarun/alpoge-rh-replay/issues/4424) | Claimed |
| [@iAndyHD3](https://github.com/iAndyHD3) | [M057466](https://github.com/rohanarun/alpoge-rh-replay/issues/4449) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[571 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M173168](https://github.com/rohanarun/alpoge-rh-replay/issues/4429#issuecomment-7052088634) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M099166](https://github.com/rohanarun/alpoge-rh-replay/issues/4430#issuecomment-7052092943) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M104686](https://github.com/rohanarun/alpoge-rh-replay/issues/4431#issuecomment-7052094143) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M168662](https://github.com/rohanarun/alpoge-rh-replay/issues/4432#issuecomment-7052095362) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M146691](https://github.com/rohanarun/alpoge-rh-replay/issues/4433#issuecomment-7052091258) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M003177](https://github.com/rohanarun/alpoge-rh-replay/issues/4434#issuecomment-7052095625) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115118](https://github.com/rohanarun/alpoge-rh-replay/issues/4435#issuecomment-7052095536) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M090585](https://github.com/rohanarun/alpoge-rh-replay/issues/4436#issuecomment-7052097093) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M164535](https://github.com/rohanarun/alpoge-rh-replay/issues/4437#issuecomment-7052091070) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M088351](https://github.com/rohanarun/alpoge-rh-replay/issues/4439#issuecomment-7052093423) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M160855](https://github.com/rohanarun/alpoge-rh-replay/issues/4440#issuecomment-7052092375) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M167887](https://github.com/rohanarun/alpoge-rh-replay/issues/4441#issuecomment-7052092530) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M031214](https://github.com/rohanarun/alpoge-rh-replay/issues/4442#issuecomment-7052092661) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M143916](https://github.com/rohanarun/alpoge-rh-replay/issues/4443#issuecomment-7052093805) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M173803](https://github.com/rohanarun/alpoge-rh-replay/issues/4444#issuecomment-7052095002) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M164780](https://github.com/rohanarun/alpoge-rh-replay/issues/4445#issuecomment-7052099835) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M027381](https://github.com/rohanarun/alpoge-rh-replay/issues/4446#issuecomment-7052100523) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M035974](https://github.com/rohanarun/alpoge-rh-replay/issues/4447#issuecomment-7052094345) | Pending review |
| [@agi-for-my-llama](https://github.com/agi-for-my-llama) | [M166512](https://github.com/rohanarun/alpoge-rh-replay/issues/4448#issuecomment-7052099958) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M164628](https://github.com/rohanarun/alpoge-rh-replay/issues/4450#issuecomment-7052103974) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[2,597 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@BenCaunt](https://github.com/BenCaunt) | [M053741](https://github.com/rohanarun/alpoge-rh-replay/issues/3923#issuecomment-7051948867) | 1 | [Build evidence verified](evidence/volunteers/M053741.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M060065](https://github.com/rohanarun/alpoge-rh-replay/issues/3908#issuecomment-7051901000) | 1 | [Build evidence verified](evidence/volunteers/M060065.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115020](https://github.com/rohanarun/alpoge-rh-replay/issues/3906#issuecomment-7051900270) | 1 | [Build evidence verified](evidence/volunteers/M115020.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M091932](https://github.com/rohanarun/alpoge-rh-replay/issues/3905#issuecomment-7051899565) | 1 | [Build evidence verified](evidence/volunteers/M091932.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M001317](https://github.com/rohanarun/alpoge-rh-replay/issues/3912#issuecomment-7051919998) | 1 | [Build evidence verified](evidence/volunteers/M001317.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M151715](https://github.com/rohanarun/alpoge-rh-replay/issues/3903#issuecomment-7051898779) | 1 | [Build evidence verified](evidence/volunteers/M151715.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M157489](https://github.com/rohanarun/alpoge-rh-replay/issues/3904#issuecomment-7052016033) | 1 | [Build evidence verified](evidence/volunteers/M157489.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M142764](https://github.com/rohanarun/alpoge-rh-replay/issues/3910#issuecomment-7051911650) | 1 | [Build evidence verified](evidence/volunteers/M142764.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M102733](https://github.com/rohanarun/alpoge-rh-replay/issues/3896#issuecomment-7051867886) | 1 | [Build evidence verified](evidence/volunteers/M102733.json) |
| [@hipotures](https://github.com/hipotures) | [P1552](https://github.com/rohanarun/alpoge-rh-replay/issues/3895#issuecomment-7051983940) | 64 | [Build evidence verified](evidence/volunteers/P1552.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M056687](https://github.com/rohanarun/alpoge-rh-replay/issues/3885#issuecomment-7051903477) | 1 | [Build evidence verified](evidence/volunteers/M056687.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M119810](https://github.com/rohanarun/alpoge-rh-replay/issues/3882#issuecomment-7051880403) | 1 | [Build evidence verified](evidence/volunteers/M119810.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M119625](https://github.com/rohanarun/alpoge-rh-replay/issues/3881#issuecomment-7051879648) | 1 | [Build evidence verified](evidence/volunteers/M119625.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M024456](https://github.com/rohanarun/alpoge-rh-replay/issues/3880#issuecomment-7051878801) | 1 | [Build evidence verified](evidence/volunteers/M024456.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M005509](https://github.com/rohanarun/alpoge-rh-replay/issues/3877#issuecomment-7051878110) | 1 | [Build evidence verified](evidence/volunteers/M005509.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M091375](https://github.com/rohanarun/alpoge-rh-replay/issues/3883#issuecomment-7051861102) | 1 | [Build evidence verified](evidence/volunteers/M091375.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M166382](https://github.com/rohanarun/alpoge-rh-replay/issues/3858#issuecomment-7051950876) | 1 | [Build evidence verified](evidence/volunteers/M166382.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M168825](https://github.com/rohanarun/alpoge-rh-replay/issues/3842#issuecomment-7051902658) | 1 | [Build evidence verified](evidence/volunteers/M168825.json) |
| [@emsi](https://github.com/emsi) | [P1784](https://github.com/rohanarun/alpoge-rh-replay/issues/3918#issuecomment-7052017528) | 64 | [Build evidence verified](evidence/volunteers/P1784.json) |
| [@emsi](https://github.com/emsi) | [P1816](https://github.com/rohanarun/alpoge-rh-replay/issues/3726#issuecomment-7051885847) | 64 | [Build evidence verified](evidence/volunteers/P1816.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 13,360 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 11,921 |
| **Total with recorded module evidence** | **42,402 / 175,187** |

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
