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

[1,118 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@BenCaunt](https://github.com/BenCaunt) | [M051652](https://github.com/rohanarun/alpoge-rh-replay/issues/7920) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M026517](https://github.com/rohanarun/alpoge-rh-replay/issues/7932) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M172756](https://github.com/rohanarun/alpoge-rh-replay/issues/7934) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M072667](https://github.com/rohanarun/alpoge-rh-replay/issues/7942) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M160583](https://github.com/rohanarun/alpoge-rh-replay/issues/7947) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M143225](https://github.com/rohanarun/alpoge-rh-replay/issues/7951) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115307](https://github.com/rohanarun/alpoge-rh-replay/issues/7954) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115302](https://github.com/rohanarun/alpoge-rh-replay/issues/7956) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115135](https://github.com/rohanarun/alpoge-rh-replay/issues/7959) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115367](https://github.com/rohanarun/alpoge-rh-replay/issues/7962) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M127198](https://github.com/rohanarun/alpoge-rh-replay/issues/7967) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M104075](https://github.com/rohanarun/alpoge-rh-replay/issues/7972) | Claimed |
| [@galakurpi](https://github.com/galakurpi) | [M091659](https://github.com/rohanarun/alpoge-rh-replay/issues/7973) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M170081](https://github.com/rohanarun/alpoge-rh-replay/issues/7974) | Claimed |
| [@galakurpi](https://github.com/galakurpi) | [M115849](https://github.com/rohanarun/alpoge-rh-replay/issues/7976) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M115011](https://github.com/rohanarun/alpoge-rh-replay/issues/7977) | Claimed |
| [@galakurpi](https://github.com/galakurpi) | [M170200](https://github.com/rohanarun/alpoge-rh-replay/issues/7978) | Claimed |
| [@galakurpi](https://github.com/galakurpi) | [M115113](https://github.com/rohanarun/alpoge-rh-replay/issues/7979) | Claimed |
| [@galakurpi](https://github.com/galakurpi) | [M143280](https://github.com/rohanarun/alpoge-rh-replay/issues/7980) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M061610](https://github.com/rohanarun/alpoge-rh-replay/issues/7981) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[915 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@rayy3535](https://github.com/rayy3535) | [M069657](https://github.com/rohanarun/alpoge-rh-replay/issues/7940#issuecomment-7053940875) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M025484](https://github.com/rohanarun/alpoge-rh-replay/issues/7941#issuecomment-7053944175) | Pending review |
| [@ljagiello](https://github.com/ljagiello) | [M093235](https://github.com/rohanarun/alpoge-rh-replay/issues/7944#issuecomment-7053944015) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M102345](https://github.com/rohanarun/alpoge-rh-replay/issues/7945#issuecomment-7053949007) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115721](https://github.com/rohanarun/alpoge-rh-replay/issues/7946#issuecomment-7053953978) | Pending review |
| [@zediir](https://github.com/zediir) | [M162236](https://github.com/rohanarun/alpoge-rh-replay/issues/7948#issuecomment-7053950565) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M102200](https://github.com/rohanarun/alpoge-rh-replay/issues/7949#issuecomment-7053958491) | Pending review |
| [@zediir](https://github.com/zediir) | [M061228](https://github.com/rohanarun/alpoge-rh-replay/issues/7950#issuecomment-7053943409) | Pending review |
| [@zediir](https://github.com/zediir) | [M061246](https://github.com/rohanarun/alpoge-rh-replay/issues/7952#issuecomment-7053952580) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M071176](https://github.com/rohanarun/alpoge-rh-replay/issues/7953#issuecomment-7053952153) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M072246](https://github.com/rohanarun/alpoge-rh-replay/issues/7955#issuecomment-7053948399) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M012976](https://github.com/rohanarun/alpoge-rh-replay/issues/7957#issuecomment-7053945668) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M079702](https://github.com/rohanarun/alpoge-rh-replay/issues/7958#issuecomment-7053971357) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M076736](https://github.com/rohanarun/alpoge-rh-replay/issues/7960#issuecomment-7053950692) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M059343](https://github.com/rohanarun/alpoge-rh-replay/issues/7961#issuecomment-7053973946) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M115708](https://github.com/rohanarun/alpoge-rh-replay/issues/7963#issuecomment-7053949492) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M027495](https://github.com/rohanarun/alpoge-rh-replay/issues/7965#issuecomment-7053949541) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115813](https://github.com/rohanarun/alpoge-rh-replay/issues/7968#issuecomment-7053976373) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M072249](https://github.com/rohanarun/alpoge-rh-replay/issues/7970#issuecomment-7053978776) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M142490](https://github.com/rohanarun/alpoge-rh-replay/issues/7971#issuecomment-7053981413) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[5,121 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115168](https://github.com/rohanarun/alpoge-rh-replay/issues/7185#issuecomment-7053772819) | 1 | [Build evidence verified](evidence/volunteers/M115168.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115564](https://github.com/rohanarun/alpoge-rh-replay/issues/7181#issuecomment-7053767505) | 1 | [Build evidence verified](evidence/volunteers/M115564.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M171591](https://github.com/rohanarun/alpoge-rh-replay/issues/7179#issuecomment-7053744936) | 1 | [Build evidence verified](evidence/volunteers/M171591.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M092766](https://github.com/rohanarun/alpoge-rh-replay/issues/7176#issuecomment-7053771046) | 1 | [Build evidence verified](evidence/volunteers/M092766.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M108286](https://github.com/rohanarun/alpoge-rh-replay/issues/7170#issuecomment-7053742935) | 1 | [Build evidence verified](evidence/volunteers/M108286.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M082605](https://github.com/rohanarun/alpoge-rh-replay/issues/7167#issuecomment-7053756365) | 1 | [Build evidence verified](evidence/volunteers/M082605.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M143292](https://github.com/rohanarun/alpoge-rh-replay/issues/7162#issuecomment-7053766531) | 1 | [Build evidence verified](evidence/volunteers/M143292.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M026341](https://github.com/rohanarun/alpoge-rh-replay/issues/7155#issuecomment-7053759002) | 1 | [Build evidence verified](evidence/volunteers/M026341.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M163029](https://github.com/rohanarun/alpoge-rh-replay/issues/7151#issuecomment-7053750912) | 1 | [Build evidence verified](evidence/volunteers/M163029.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M078126](https://github.com/rohanarun/alpoge-rh-replay/issues/7137#issuecomment-7053763810) | 1 | [Build evidence verified](evidence/volunteers/M078126.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115529](https://github.com/rohanarun/alpoge-rh-replay/issues/7141#issuecomment-7053747999) | 1 | [Build evidence verified](evidence/volunteers/M115529.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M062553](https://github.com/rohanarun/alpoge-rh-replay/issues/7132#issuecomment-7053753646) | 1 | [Build evidence verified](evidence/volunteers/M062553.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M073443](https://github.com/rohanarun/alpoge-rh-replay/issues/7125#issuecomment-7053778431) | 1 | [Build evidence verified](evidence/volunteers/M073443.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M141686](https://github.com/rohanarun/alpoge-rh-replay/issues/7128#issuecomment-7053761815) | 1 | [Build evidence verified](evidence/volunteers/M141686.json) |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M104696](https://github.com/rohanarun/alpoge-rh-replay/issues/7144#issuecomment-7053757266) | 1 | [Build evidence verified](evidence/volunteers/M104696.json) |
| [@chriswilson413](https://github.com/chriswilson413) | [M101272](https://github.com/rohanarun/alpoge-rh-replay/issues/7103#issuecomment-7053813690) | 1 | [Build evidence verified](evidence/volunteers/M101272.json) |
| [@chriswilson413](https://github.com/chriswilson413) | [M098658](https://github.com/rohanarun/alpoge-rh-replay/issues/7101#issuecomment-7053811995) | 1 | [Build evidence verified](evidence/volunteers/M098658.json) |
| [@emsi](https://github.com/emsi) | [P1777](https://github.com/rohanarun/alpoge-rh-replay/issues/6537#issuecomment-7053826735) | 64 | [Build evidence verified](evidence/volunteers/P1777.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M101355](https://github.com/rohanarun/alpoge-rh-replay/issues/5932#issuecomment-7053791539) | 1 | [Build evidence verified](evidence/volunteers/M101355.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M091727](https://github.com/rohanarun/alpoge-rh-replay/issues/5512#issuecomment-7053792392) | 1 | [Build evidence verified](evidence/volunteers/M091727.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 18,092 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 19,296 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **54,608 / 175,187** |

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
