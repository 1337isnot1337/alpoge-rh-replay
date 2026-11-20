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

**Replay volunteers (54)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@krisyotam](https://github.com/krisyotam), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@surfyhou](https://github.com/surfyhou), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[790 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@BenCaunt](https://github.com/BenCaunt) | [M102733](https://github.com/rohanarun/alpoge-rh-replay/issues/3896) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M102182](https://github.com/rohanarun/alpoge-rh-replay/issues/3897) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M151715](https://github.com/rohanarun/alpoge-rh-replay/issues/3903) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M157489](https://github.com/rohanarun/alpoge-rh-replay/issues/3904) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M091932](https://github.com/rohanarun/alpoge-rh-replay/issues/3905) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115020](https://github.com/rohanarun/alpoge-rh-replay/issues/3906) | Claimed |
| [@user42245](https://github.com/user42245) | [M087813](https://github.com/rohanarun/alpoge-rh-replay/issues/3907) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M060065](https://github.com/rohanarun/alpoge-rh-replay/issues/3908) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M142764](https://github.com/rohanarun/alpoge-rh-replay/issues/3910) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M001317](https://github.com/rohanarun/alpoge-rh-replay/issues/3912) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M083045](https://github.com/rohanarun/alpoge-rh-replay/issues/3913) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M170827](https://github.com/rohanarun/alpoge-rh-replay/issues/3914) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M120115](https://github.com/rohanarun/alpoge-rh-replay/issues/3915) | Claimed |
| [@emsi](https://github.com/emsi) | [P1784](https://github.com/rohanarun/alpoge-rh-replay/issues/3918) | Claimed |
| [@user42245](https://github.com/user42245) | [M087815](https://github.com/rohanarun/alpoge-rh-replay/issues/3919) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M175178](https://github.com/rohanarun/alpoge-rh-replay/issues/3920) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M173277](https://github.com/rohanarun/alpoge-rh-replay/issues/3921) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M109976](https://github.com/rohanarun/alpoge-rh-replay/issues/3922) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M053741](https://github.com/rohanarun/alpoge-rh-replay/issues/3923) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M142327](https://github.com/rohanarun/alpoge-rh-replay/issues/3924) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[488 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M066446](https://github.com/rohanarun/alpoge-rh-replay/issues/3857#issuecomment-7051680712) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M164487](https://github.com/rohanarun/alpoge-rh-replay/issues/3862#issuecomment-7051712412) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M134233](https://github.com/rohanarun/alpoge-rh-replay/issues/3864#issuecomment-7051679719) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M132658](https://github.com/rohanarun/alpoge-rh-replay/issues/3865#issuecomment-7051679113) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M074788](https://github.com/rohanarun/alpoge-rh-replay/issues/3868#issuecomment-7051682713) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M099434](https://github.com/rohanarun/alpoge-rh-replay/issues/3869#issuecomment-7051683414) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M051003](https://github.com/rohanarun/alpoge-rh-replay/issues/3876#issuecomment-7051686468) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M131252](https://github.com/rohanarun/alpoge-rh-replay/issues/3878#issuecomment-7051680611) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M174626](https://github.com/rohanarun/alpoge-rh-replay/issues/3889#issuecomment-7051695921) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M164600](https://github.com/rohanarun/alpoge-rh-replay/issues/3890#issuecomment-7051699360) | Pending review |
| [@jjjhenriksen](https://github.com/jjjhenriksen) | [M083549](https://github.com/rohanarun/alpoge-rh-replay/issues/3894#issuecomment-7051703185) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M104440](https://github.com/rohanarun/alpoge-rh-replay/issues/3898#issuecomment-7051709242) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M002752](https://github.com/rohanarun/alpoge-rh-replay/issues/3899#issuecomment-7051699113) | Pending review |
| [@egergerfg](https://github.com/egergerfg) | [M164574](https://github.com/rohanarun/alpoge-rh-replay/issues/3900#issuecomment-7051721752) | Pending review |
| [@egergerfg](https://github.com/egergerfg) | [M156208](https://github.com/rohanarun/alpoge-rh-replay/issues/3901#issuecomment-7051722142) | Pending review |
| [@egergerfg](https://github.com/egergerfg) | [M101500](https://github.com/rohanarun/alpoge-rh-replay/issues/3902#issuecomment-7051722535) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M005063](https://github.com/rohanarun/alpoge-rh-replay/issues/3909#issuecomment-7051731975) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M138393](https://github.com/rohanarun/alpoge-rh-replay/issues/3911#issuecomment-7051720768) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M090571](https://github.com/rohanarun/alpoge-rh-replay/issues/3916#issuecomment-7051731100) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M101479](https://github.com/rohanarun/alpoge-rh-replay/issues/3917#issuecomment-7051733270) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[2,266 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@sat3n](https://github.com/sat3n) | [M065178](https://github.com/rohanarun/alpoge-rh-replay/issues/3328#issuecomment-7051473002) | 1 | [Build evidence verified](evidence/volunteers/M065178.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M024505](https://github.com/rohanarun/alpoge-rh-replay/issues/3327#issuecomment-7051409860) | 1 | [Build evidence verified](evidence/volunteers/M024505.json) |
| [@sat3n](https://github.com/sat3n) | [M064938](https://github.com/rohanarun/alpoge-rh-replay/issues/3326#issuecomment-7051471274) | 1 | [Build evidence verified](evidence/volunteers/M064938.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M072200](https://github.com/rohanarun/alpoge-rh-replay/issues/3324#issuecomment-7051409155) | 1 | [Build evidence verified](evidence/volunteers/M072200.json) |
| [@sat3n](https://github.com/sat3n) | [M064785](https://github.com/rohanarun/alpoge-rh-replay/issues/3323#issuecomment-7051469739) | 1 | [Build evidence verified](evidence/volunteers/M064785.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115328](https://github.com/rohanarun/alpoge-rh-replay/issues/3322#issuecomment-7051408381) | 1 | [Build evidence verified](evidence/volunteers/M115328.json) |
| [@sat3n](https://github.com/sat3n) | [M064035](https://github.com/rohanarun/alpoge-rh-replay/issues/3320#issuecomment-7051468443) | 1 | [Build evidence verified](evidence/volunteers/M064035.json) |
| [@emsi](https://github.com/emsi) | [P1792](https://github.com/rohanarun/alpoge-rh-replay/issues/3406#issuecomment-7051436538) | 64 | [Build evidence verified](evidence/volunteers/P1792.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M006425](https://github.com/rohanarun/alpoge-rh-replay/issues/3317#issuecomment-7051407701) | 1 | [Build evidence verified](evidence/volunteers/M006425.json) |
| [@sat3n](https://github.com/sat3n) | [M064014](https://github.com/rohanarun/alpoge-rh-replay/issues/3314#issuecomment-7051464671) | 1 | [Build evidence verified](evidence/volunteers/M064014.json) |
| [@sat3n](https://github.com/sat3n) | [M063921](https://github.com/rohanarun/alpoge-rh-replay/issues/3312#issuecomment-7051463508) | 1 | [Build evidence verified](evidence/volunteers/M063921.json) |
| [@sat3n](https://github.com/sat3n) | [M063710](https://github.com/rohanarun/alpoge-rh-replay/issues/3311#issuecomment-7051462033) | 1 | [Build evidence verified](evidence/volunteers/M063710.json) |
| [@sat3n](https://github.com/sat3n) | [M063330](https://github.com/rohanarun/alpoge-rh-replay/issues/3300#issuecomment-7051460770) | 1 | [Build evidence verified](evidence/volunteers/M063330.json) |
| [@sat3n](https://github.com/sat3n) | [M063242](https://github.com/rohanarun/alpoge-rh-replay/issues/3299#issuecomment-7051456651) | 1 | [Build evidence verified](evidence/volunteers/M063242.json) |
| [@sat3n](https://github.com/sat3n) | [M063176](https://github.com/rohanarun/alpoge-rh-replay/issues/3294#issuecomment-7051455179) | 1 | [Build evidence verified](evidence/volunteers/M063176.json) |
| [@sat3n](https://github.com/sat3n) | [M063083](https://github.com/rohanarun/alpoge-rh-replay/issues/3288#issuecomment-7051453847) | 1 | [Build evidence verified](evidence/volunteers/M063083.json) |
| [@emsi](https://github.com/emsi) | [P1762](https://github.com/rohanarun/alpoge-rh-replay/issues/3467#issuecomment-7051402445) | 64 | [Build evidence verified](evidence/volunteers/P1762.json) |
| [@emsi](https://github.com/emsi) | [P1742](https://github.com/rohanarun/alpoge-rh-replay/issues/2381#issuecomment-7050631359) | 64 | [Build evidence verified](evidence/volunteers/P1742.json) |
| [@surfyhou](https://github.com/surfyhou) | [P1099](https://github.com/rohanarun/alpoge-rh-replay/issues/245#issuecomment-7051553309) | 64 | [Build evidence verified](evidence/volunteers/P1099.json) |
| [@emsi](https://github.com/emsi) | [P1309](https://github.com/rohanarun/alpoge-rh-replay/issues/572#issuecomment-7050566180) | 64 | [Build evidence verified](evidence/volunteers/P1309.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 12,448 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 11,086 |
| **Total with recorded module evidence** | **40,655 / 175,187** |

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
