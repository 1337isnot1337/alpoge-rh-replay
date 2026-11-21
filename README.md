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

**Replay volunteers (82)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@21Z121Z1](https://github.com/21Z121Z1), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@aulafy](https://github.com/aulafy), [@BenCaunt](https://github.com/BenCaunt), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@ljagiello](https://github.com/ljagiello), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,044 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@BenCaunt](https://github.com/BenCaunt) | [M043352](https://github.com/rohanarun/alpoge-rh-replay/issues/7821) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M045901](https://github.com/rohanarun/alpoge-rh-replay/issues/7843) | Claimed |
| [@user42245](https://github.com/user42245) | [M115645](https://github.com/rohanarun/alpoge-rh-replay/issues/7852) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M046303](https://github.com/rohanarun/alpoge-rh-replay/issues/7854) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M061571](https://github.com/rohanarun/alpoge-rh-replay/issues/7855) | Claimed |
| [@emsi](https://github.com/emsi) | [P2026](https://github.com/rohanarun/alpoge-rh-replay/issues/7856) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M046348](https://github.com/rohanarun/alpoge-rh-replay/issues/7858) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M047089](https://github.com/rohanarun/alpoge-rh-replay/issues/7870) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M051020](https://github.com/rohanarun/alpoge-rh-replay/issues/7889) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M042552](https://github.com/rohanarun/alpoge-rh-replay/issues/7896) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M064298](https://github.com/rohanarun/alpoge-rh-replay/issues/7898) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M142754](https://github.com/rohanarun/alpoge-rh-replay/issues/7900) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115790](https://github.com/rohanarun/alpoge-rh-replay/issues/7903) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M051305](https://github.com/rohanarun/alpoge-rh-replay/issues/7907) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M051652](https://github.com/rohanarun/alpoge-rh-replay/issues/7920) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M026517](https://github.com/rohanarun/alpoge-rh-replay/issues/7932) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M172756](https://github.com/rohanarun/alpoge-rh-replay/issues/7934) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M072667](https://github.com/rohanarun/alpoge-rh-replay/issues/7942) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M160583](https://github.com/rohanarun/alpoge-rh-replay/issues/7947) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M061610](https://github.com/rohanarun/alpoge-rh-replay/issues/7981) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[790 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M027495](https://github.com/rohanarun/alpoge-rh-replay/issues/7965#issuecomment-7053949541) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M127198](https://github.com/rohanarun/alpoge-rh-replay/issues/7967#issuecomment-7054040105) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115813](https://github.com/rohanarun/alpoge-rh-replay/issues/7968#issuecomment-7053976373) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M072249](https://github.com/rohanarun/alpoge-rh-replay/issues/7970#issuecomment-7053978776) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M142490](https://github.com/rohanarun/alpoge-rh-replay/issues/7971#issuecomment-7053981413) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M104075](https://github.com/rohanarun/alpoge-rh-replay/issues/7972#issuecomment-7054040707) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M091659](https://github.com/rohanarun/alpoge-rh-replay/issues/7973#issuecomment-7053983753) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M170081](https://github.com/rohanarun/alpoge-rh-replay/issues/7974#issuecomment-7054041249) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115849](https://github.com/rohanarun/alpoge-rh-replay/issues/7976#issuecomment-7053986195) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M115011](https://github.com/rohanarun/alpoge-rh-replay/issues/7977#issuecomment-7054041797) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M170200](https://github.com/rohanarun/alpoge-rh-replay/issues/7978#issuecomment-7053988537) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115113](https://github.com/rohanarun/alpoge-rh-replay/issues/7979#issuecomment-7053991114) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M143280](https://github.com/rohanarun/alpoge-rh-replay/issues/7980#issuecomment-7053993839) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M115455](https://github.com/rohanarun/alpoge-rh-replay/issues/7982#issuecomment-7054042424) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M115365](https://github.com/rohanarun/alpoge-rh-replay/issues/7983#issuecomment-7054043013) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M141501](https://github.com/rohanarun/alpoge-rh-replay/issues/7985#issuecomment-7054044249) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M115509](https://github.com/rohanarun/alpoge-rh-replay/issues/7986#issuecomment-7054045908) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M163886](https://github.com/rohanarun/alpoge-rh-replay/issues/7987#issuecomment-7053967825) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M115757](https://github.com/rohanarun/alpoge-rh-replay/issues/7988#issuecomment-7053976732) | Pending review |
| [@loremcdmx](https://github.com/loremcdmx) | [M115003](https://github.com/rohanarun/alpoge-rh-replay/issues/7989#issuecomment-7054048309) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[5,319 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115540](https://github.com/rohanarun/alpoge-rh-replay/issues/7443#issuecomment-7053837270) | 1 | [Build evidence verified](evidence/volunteers/M115540.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M142025](https://github.com/rohanarun/alpoge-rh-replay/issues/7440#issuecomment-7053836597) | 1 | [Build evidence verified](evidence/volunteers/M142025.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M037584](https://github.com/rohanarun/alpoge-rh-replay/issues/7438#issuecomment-7053836046) | 1 | [Build evidence verified](evidence/volunteers/M037584.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M091452](https://github.com/rohanarun/alpoge-rh-replay/issues/7432#issuecomment-7053835524) | 1 | [Build evidence verified](evidence/volunteers/M091452.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M045662](https://github.com/rohanarun/alpoge-rh-replay/issues/7519#issuecomment-7053832858) | 1 | [Build evidence verified](evidence/volunteers/M045662.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M142315](https://github.com/rohanarun/alpoge-rh-replay/issues/7253#issuecomment-7053833070) | 1 | [Build evidence verified](evidence/volunteers/M142315.json) |
| [@hipotures](https://github.com/hipotures) | [P1673](https://github.com/rohanarun/alpoge-rh-replay/issues/7351#issuecomment-7053892970) | 64 | [Build evidence verified](evidence/volunteers/P1673.json) |
| [@TomMoeras](https://github.com/TomMoeras) | [P1894](https://github.com/rohanarun/alpoge-rh-replay/issues/6970#issuecomment-7053908608) | 64 | [Build evidence verified](evidence/volunteers/P1894.json) |
| [@rishabh-16](https://github.com/rishabh-16) | [M072668](https://github.com/rohanarun/alpoge-rh-replay/issues/6734#issuecomment-7053900103) | 1 | [Build evidence verified](evidence/volunteers/M072668.json) |
| [@rishabh-16](https://github.com/rishabh-16) | [M071673](https://github.com/rohanarun/alpoge-rh-replay/issues/6720#issuecomment-7053899781) | 1 | [Build evidence verified](evidence/volunteers/M071673.json) |
| [@dhudakk](https://github.com/dhudakk) | [M086046](https://github.com/rohanarun/alpoge-rh-replay/issues/6868#issuecomment-7053904756) | 1 | [Build evidence verified](evidence/volunteers/M086046.json) |
| [@rishabh-16](https://github.com/rishabh-16) | [M071391](https://github.com/rohanarun/alpoge-rh-replay/issues/6715#issuecomment-7053899423) | 1 | [Build evidence verified](evidence/volunteers/M071391.json) |
| [@rishabh-16](https://github.com/rishabh-16) | [M071164](https://github.com/rohanarun/alpoge-rh-replay/issues/6705#issuecomment-7053899073) | 1 | [Build evidence verified](evidence/volunteers/M071164.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1700](https://github.com/rohanarun/alpoge-rh-replay/issues/6711#issuecomment-7053858376) | 64 | [Build evidence verified](evidence/volunteers/P1700.json) |
| [@emsi](https://github.com/emsi) | [P1977](https://github.com/rohanarun/alpoge-rh-replay/issues/6632#issuecomment-7053836863) | 64 | [Build evidence verified](evidence/volunteers/P1977.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1796](https://github.com/rohanarun/alpoge-rh-replay/issues/6447#issuecomment-7053860855) | 64 | [Build evidence verified](evidence/volunteers/P1796.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M130271](https://github.com/rohanarun/alpoge-rh-replay/issues/6263#issuecomment-7053871617) | 1 | [Build evidence verified](evidence/volunteers/M130271.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M108909](https://github.com/rohanarun/alpoge-rh-replay/issues/6077#issuecomment-7053898253) | 1 | [Build evidence verified](evidence/volunteers/M108909.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M173228](https://github.com/rohanarun/alpoge-rh-replay/issues/5896#issuecomment-7053840352) | 1 | [Build evidence verified](evidence/volunteers/M173228.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M101446](https://github.com/rohanarun/alpoge-rh-replay/issues/5884#issuecomment-7053839504) | 1 | [Build evidence verified](evidence/volunteers/M101446.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 18,325 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 19,809 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **55,354 / 175,187** |

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
