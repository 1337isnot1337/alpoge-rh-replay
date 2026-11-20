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

**Replay volunteers (79)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,009 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M173262](https://github.com/rohanarun/alpoge-rh-replay/issues/6611) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M078773](https://github.com/rohanarun/alpoge-rh-replay/issues/6614) | Claimed |
| [@dga471](https://github.com/dga471) | [M073054](https://github.com/rohanarun/alpoge-rh-replay/issues/6615) | Claimed |
| [@chriswilson413](https://github.com/chriswilson413) | [M066023](https://github.com/rohanarun/alpoge-rh-replay/issues/6620) | Claimed |
| [@chriswilson413](https://github.com/chriswilson413) | [M067602](https://github.com/rohanarun/alpoge-rh-replay/issues/6621) | Claimed |
| [@WorldianAI](https://github.com/WorldianAI) | [M115076](https://github.com/rohanarun/alpoge-rh-replay/issues/6623) | Claimed |
| [@emsi](https://github.com/emsi) | [P1950](https://github.com/rohanarun/alpoge-rh-replay/issues/6629) | Claimed |
| [@emsi](https://github.com/emsi) | [P1977](https://github.com/rohanarun/alpoge-rh-replay/issues/6632) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M111010](https://github.com/rohanarun/alpoge-rh-replay/issues/6634) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M088241](https://github.com/rohanarun/alpoge-rh-replay/issues/6637) | Claimed |
| [@JamCh01](https://github.com/JamCh01) | [P1706](https://github.com/rohanarun/alpoge-rh-replay/issues/6638) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M059217](https://github.com/rohanarun/alpoge-rh-replay/issues/6639) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M074316](https://github.com/rohanarun/alpoge-rh-replay/issues/6641) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M044743](https://github.com/rohanarun/alpoge-rh-replay/issues/6646) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M174459](https://github.com/rohanarun/alpoge-rh-replay/issues/6690) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M172317](https://github.com/rohanarun/alpoge-rh-replay/issues/6692) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M070263](https://github.com/rohanarun/alpoge-rh-replay/issues/6693) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M071674](https://github.com/rohanarun/alpoge-rh-replay/issues/6695) | Claimed |
| [@rishabh-16](https://github.com/rishabh-16) | [M071164](https://github.com/rohanarun/alpoge-rh-replay/issues/6705) | Claimed |
| [@WilmervH](https://github.com/WilmervH) | [P1700](https://github.com/rohanarun/alpoge-rh-replay/issues/6711) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[920 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@egergerfg](https://github.com/egergerfg) | [M101536](https://github.com/rohanarun/alpoge-rh-replay/issues/6684#issuecomment-7053307705) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115385](https://github.com/rohanarun/alpoge-rh-replay/issues/6685#issuecomment-7053321328) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115014](https://github.com/rohanarun/alpoge-rh-replay/issues/6686#issuecomment-7053323096) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M110997](https://github.com/rohanarun/alpoge-rh-replay/issues/6687#issuecomment-7053324925) | Pending review |
| [@sp20262026](https://github.com/sp20262026) | [M166263](https://github.com/rohanarun/alpoge-rh-replay/issues/6688#issuecomment-7053333124) | Pending review |
| [@drew2apps](https://github.com/drew2apps) | [M165934](https://github.com/rohanarun/alpoge-rh-replay/issues/6689#issuecomment-7053311165) | Pending review |
| [@jjjhenriksen](https://github.com/jjjhenriksen) | [M059622](https://github.com/rohanarun/alpoge-rh-replay/issues/6691#issuecomment-7053311604) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M164769](https://github.com/rohanarun/alpoge-rh-replay/issues/6694#issuecomment-7053309119) | Pending review |
| [@matan1905](https://github.com/matan1905) | [M133247](https://github.com/rohanarun/alpoge-rh-replay/issues/6696#issuecomment-7053321383) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M129905](https://github.com/rohanarun/alpoge-rh-replay/issues/6698#issuecomment-7053311086) | Pending review |
| [@egergerfg](https://github.com/egergerfg) | [M164584](https://github.com/rohanarun/alpoge-rh-replay/issues/6699#issuecomment-7053312174) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M002081](https://github.com/rohanarun/alpoge-rh-replay/issues/6701#issuecomment-7053311649) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M028060](https://github.com/rohanarun/alpoge-rh-replay/issues/6702#issuecomment-7053313792) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M108253](https://github.com/rohanarun/alpoge-rh-replay/issues/6703#issuecomment-7053311018) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M102992](https://github.com/rohanarun/alpoge-rh-replay/issues/6706#issuecomment-7053309827) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M102993](https://github.com/rohanarun/alpoge-rh-replay/issues/6707#issuecomment-7053311308) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M103001](https://github.com/rohanarun/alpoge-rh-replay/issues/6708#issuecomment-7053312515) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M001454](https://github.com/rohanarun/alpoge-rh-replay/issues/6709#issuecomment-7053315767) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M104909](https://github.com/rohanarun/alpoge-rh-replay/issues/6710#issuecomment-7053317674) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M013216](https://github.com/rohanarun/alpoge-rh-replay/issues/6712#issuecomment-7053325526) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[4,053 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@loremcdmx](https://github.com/loremcdmx) | [M109922](https://github.com/rohanarun/alpoge-rh-replay/issues/4875#issuecomment-7052932496) | 1 | [Build evidence verified](evidence/volunteers/M109922.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M080875](https://github.com/rohanarun/alpoge-rh-replay/issues/4873#issuecomment-7052931408) | 1 | [Build evidence verified](evidence/volunteers/M080875.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M051488](https://github.com/rohanarun/alpoge-rh-replay/issues/4866#issuecomment-7052929865) | 1 | [Build evidence verified](evidence/volunteers/M051488.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M036482](https://github.com/rohanarun/alpoge-rh-replay/issues/4868#issuecomment-7052930321) | 1 | [Build evidence verified](evidence/volunteers/M036482.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M058574](https://github.com/rohanarun/alpoge-rh-replay/issues/4870#issuecomment-7052930956) | 1 | [Build evidence verified](evidence/volunteers/M058574.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M110078](https://github.com/rohanarun/alpoge-rh-replay/issues/4864#issuecomment-7052929250) | 1 | [Build evidence verified](evidence/volunteers/M110078.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M115106](https://github.com/rohanarun/alpoge-rh-replay/issues/4861#issuecomment-7052928198) | 1 | [Build evidence verified](evidence/volunteers/M115106.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M053806](https://github.com/rohanarun/alpoge-rh-replay/issues/4859#issuecomment-7052927621) | 1 | [Build evidence verified](evidence/volunteers/M053806.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M078102](https://github.com/rohanarun/alpoge-rh-replay/issues/4857#issuecomment-7052927274) | 1 | [Build evidence verified](evidence/volunteers/M078102.json) |
| [@loremcdmx](https://github.com/loremcdmx) | [M086645](https://github.com/rohanarun/alpoge-rh-replay/issues/4856#issuecomment-7052926729) | 1 | [Build evidence verified](evidence/volunteers/M086645.json) |
| [@SeriousRising](https://github.com/SeriousRising) | [P1871](https://github.com/rohanarun/alpoge-rh-replay/issues/3145#issuecomment-7052980497) | 64 | [Build evidence verified](evidence/volunteers/P1871.json) |
| [@SeriousRising](https://github.com/SeriousRising) | [P1639](https://github.com/rohanarun/alpoge-rh-replay/issues/2408#issuecomment-7053111166) | 64 | [Build evidence verified](evidence/volunteers/P1639.json) |
| [@mu-mei](https://github.com/mu-mei) | [P1690](https://github.com/rohanarun/alpoge-rh-replay/issues/1993#issuecomment-7053059135) | 64 | [Build evidence verified](evidence/volunteers/P1690.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1607](https://github.com/rohanarun/alpoge-rh-replay/issues/2040#issuecomment-7053033048) | 64 | [Build evidence verified](evidence/volunteers/P1607.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1490](https://github.com/rohanarun/alpoge-rh-replay/issues/1241#issuecomment-7052985077) | 64 | [Build evidence verified](evidence/volunteers/P1490.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1501](https://github.com/rohanarun/alpoge-rh-replay/issues/1246#issuecomment-7053002728) | 64 | [Build evidence verified](evidence/volunteers/P1501.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1485](https://github.com/rohanarun/alpoge-rh-replay/issues/1232#issuecomment-7052998540) | 64 | [Build evidence verified](evidence/volunteers/P1485.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1423](https://github.com/rohanarun/alpoge-rh-replay/issues/1080#issuecomment-7052995666) | 64 | [Build evidence verified](evidence/volunteers/P1423.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1411](https://github.com/rohanarun/alpoge-rh-replay/issues/1075#issuecomment-7052989781) | 64 | [Build evidence verified](evidence/volunteers/P1411.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1421](https://github.com/rohanarun/alpoge-rh-replay/issues/1078#issuecomment-7052992759) | 64 | [Build evidence verified](evidence/volunteers/P1421.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 16,109 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 15,771 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **49,100 / 175,187** |

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
