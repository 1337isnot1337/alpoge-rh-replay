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

**Replay volunteers (70)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@chriswilson413](https://github.com/chriswilson413), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,051 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@rohanarun](https://github.com/rohanarun) | [M109463](https://github.com/rohanarun/alpoge-rh-replay/issues/5471) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M131813](https://github.com/rohanarun/alpoge-rh-replay/issues/5473) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M132402](https://github.com/rohanarun/alpoge-rh-replay/issues/5475) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M151460](https://github.com/rohanarun/alpoge-rh-replay/issues/5479) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M174919](https://github.com/rohanarun/alpoge-rh-replay/issues/5482) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M087939](https://github.com/rohanarun/alpoge-rh-replay/issues/5483) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M091385](https://github.com/rohanarun/alpoge-rh-replay/issues/5484) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M065033](https://github.com/rohanarun/alpoge-rh-replay/issues/5485) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M156020](https://github.com/rohanarun/alpoge-rh-replay/issues/5486) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M091727](https://github.com/rohanarun/alpoge-rh-replay/issues/5512) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M131215](https://github.com/rohanarun/alpoge-rh-replay/issues/5567) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M143417](https://github.com/rohanarun/alpoge-rh-replay/issues/5571) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M065243](https://github.com/rohanarun/alpoge-rh-replay/issues/5575) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115801](https://github.com/rohanarun/alpoge-rh-replay/issues/5580) | Claimed |
| [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel) | [P1572](https://github.com/rohanarun/alpoge-rh-replay/issues/5598) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M062536](https://github.com/rohanarun/alpoge-rh-replay/issues/5647) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M143867](https://github.com/rohanarun/alpoge-rh-replay/issues/5650) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115799](https://github.com/rohanarun/alpoge-rh-replay/issues/5655) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M099654](https://github.com/rohanarun/alpoge-rh-replay/issues/5658) | Claimed |
| [@t-choudhury](https://github.com/t-choudhury) | [M146992](https://github.com/rohanarun/alpoge-rh-replay/issues/5663) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[671 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@BenCaunt](https://github.com/BenCaunt) | [M014510](https://github.com/rohanarun/alpoge-rh-replay/issues/5662#issuecomment-7052745384) | Pending review |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M037180](https://github.com/rohanarun/alpoge-rh-replay/issues/5664#issuecomment-7052817436) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M063257](https://github.com/rohanarun/alpoge-rh-replay/issues/5666#issuecomment-7052740756) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M053889](https://github.com/rohanarun/alpoge-rh-replay/issues/5667#issuecomment-7052741106) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M036424](https://github.com/rohanarun/alpoge-rh-replay/issues/5669#issuecomment-7052739807) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M068735](https://github.com/rohanarun/alpoge-rh-replay/issues/5670#issuecomment-7052731807) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M064473](https://github.com/rohanarun/alpoge-rh-replay/issues/5671#issuecomment-7052733034) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M164146](https://github.com/rohanarun/alpoge-rh-replay/issues/5672#issuecomment-7052746709) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M164555](https://github.com/rohanarun/alpoge-rh-replay/issues/5673#issuecomment-7052736814) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M102636](https://github.com/rohanarun/alpoge-rh-replay/issues/5674#issuecomment-7052738576) | Pending review |
| [@drew2apps](https://github.com/drew2apps) | [M165943](https://github.com/rohanarun/alpoge-rh-replay/issues/5675#issuecomment-7052859020) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M058613](https://github.com/rohanarun/alpoge-rh-replay/issues/5676#issuecomment-7052739823) | Pending review |
| [@drew2apps](https://github.com/drew2apps) | [M165949](https://github.com/rohanarun/alpoge-rh-replay/issues/5677#issuecomment-7052853060) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M173290](https://github.com/rohanarun/alpoge-rh-replay/issues/5678#issuecomment-7052753822) | Pending review |
| [@zediir](https://github.com/zediir) | [M062483](https://github.com/rohanarun/alpoge-rh-replay/issues/5679#issuecomment-7052749189) | Pending review |
| [@florianmodel](https://github.com/florianmodel) | [M018812](https://github.com/rohanarun/alpoge-rh-replay/issues/5680#issuecomment-7052736061) | Pending review |
| [@zediir](https://github.com/zediir) | [M062688](https://github.com/rohanarun/alpoge-rh-replay/issues/5681#issuecomment-7052741757) | Pending review |
| [@misuadn-laplace](https://github.com/misuadn-laplace) | [M115627](https://github.com/rohanarun/alpoge-rh-replay/issues/5682#issuecomment-7052743969) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115137](https://github.com/rohanarun/alpoge-rh-replay/issues/5683#issuecomment-7052745551) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M115295](https://github.com/rohanarun/alpoge-rh-replay/issues/5684#issuecomment-7052745873) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[3,370 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115784](https://github.com/rohanarun/alpoge-rh-replay/issues/4892#issuecomment-7052558940) | 1 | [Build evidence verified](evidence/volunteers/M115784.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M077026](https://github.com/rohanarun/alpoge-rh-replay/issues/4887#issuecomment-7052558334) | 1 | [Build evidence verified](evidence/volunteers/M077026.json) |
| [@egergerfg](https://github.com/egergerfg) | [M153528](https://github.com/rohanarun/alpoge-rh-replay/issues/5000#issuecomment-7052448557) | 1 | [Build evidence verified](evidence/volunteers/M153528.json) |
| [@egergerfg](https://github.com/egergerfg) | [M174961](https://github.com/rohanarun/alpoge-rh-replay/issues/4998#issuecomment-7052448000) | 1 | [Build evidence verified](evidence/volunteers/M174961.json) |
| [@egergerfg](https://github.com/egergerfg) | [M006489](https://github.com/rohanarun/alpoge-rh-replay/issues/4996#issuecomment-7052447487) | 1 | [Build evidence verified](evidence/volunteers/M006489.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M071611](https://github.com/rohanarun/alpoge-rh-replay/issues/4797#issuecomment-7052527674) | 1 | [Build evidence verified](evidence/volunteers/M071611.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M162630](https://github.com/rohanarun/alpoge-rh-replay/issues/4794#issuecomment-7052527115) | 1 | [Build evidence verified](evidence/volunteers/M162630.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115139](https://github.com/rohanarun/alpoge-rh-replay/issues/4791#issuecomment-7052526548) | 1 | [Build evidence verified](evidence/volunteers/M115139.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M072012](https://github.com/rohanarun/alpoge-rh-replay/issues/4788#issuecomment-7052525968) | 1 | [Build evidence verified](evidence/volunteers/M072012.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M143368](https://github.com/rohanarun/alpoge-rh-replay/issues/4767#issuecomment-7052498774) | 1 | [Build evidence verified](evidence/volunteers/M143368.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M072243](https://github.com/rohanarun/alpoge-rh-replay/issues/4765#issuecomment-7052498229) | 1 | [Build evidence verified](evidence/volunteers/M072243.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M063254](https://github.com/rohanarun/alpoge-rh-replay/issues/4764#issuecomment-7052497722) | 1 | [Build evidence verified](evidence/volunteers/M063254.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M104548](https://github.com/rohanarun/alpoge-rh-replay/issues/4761#issuecomment-7052497152) | 1 | [Build evidence verified](evidence/volunteers/M104548.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M149631](https://github.com/rohanarun/alpoge-rh-replay/issues/4729#issuecomment-7052465823) | 1 | [Build evidence verified](evidence/volunteers/M149631.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M063198](https://github.com/rohanarun/alpoge-rh-replay/issues/4728#issuecomment-7052465336) | 1 | [Build evidence verified](evidence/volunteers/M063198.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M025435](https://github.com/rohanarun/alpoge-rh-replay/issues/4724#issuecomment-7052464775) | 1 | [Build evidence verified](evidence/volunteers/M025435.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115466](https://github.com/rohanarun/alpoge-rh-replay/issues/4722#issuecomment-7052464271) | 1 | [Build evidence verified](evidence/volunteers/M115466.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M151982](https://github.com/rohanarun/alpoge-rh-replay/issues/4643#issuecomment-7052482562) | 1 | [Build evidence verified](evidence/volunteers/M151982.json) |
| [@emsi](https://github.com/emsi) | [P1903](https://github.com/rohanarun/alpoge-rh-replay/issues/4680#issuecomment-7052474227) | 64 | [Build evidence verified](evidence/volunteers/P1903.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M090182](https://github.com/rohanarun/alpoge-rh-replay/issues/4252#issuecomment-7052506108) | 1 | [Build evidence verified](evidence/volunteers/M090182.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 14,955 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 13,639 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **45,814 / 175,187** |

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
