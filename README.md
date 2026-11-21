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

**Replay volunteers (81)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@aulafy](https://github.com/aulafy), [@BenCaunt](https://github.com/BenCaunt), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@ljagiello](https://github.com/ljagiello), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@maxime-fleury](https://github.com/maxime-fleury), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[1,069 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M143292](https://github.com/rohanarun/alpoge-rh-replay/issues/7162) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M042464](https://github.com/rohanarun/alpoge-rh-replay/issues/7163) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M134630](https://github.com/rohanarun/alpoge-rh-replay/issues/7166) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M082605](https://github.com/rohanarun/alpoge-rh-replay/issues/7167) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M062742](https://github.com/rohanarun/alpoge-rh-replay/issues/7168) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M108286](https://github.com/rohanarun/alpoge-rh-replay/issues/7170) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M065514](https://github.com/rohanarun/alpoge-rh-replay/issues/7172) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M092766](https://github.com/rohanarun/alpoge-rh-replay/issues/7176) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M016669](https://github.com/rohanarun/alpoge-rh-replay/issues/7177) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M171591](https://github.com/rohanarun/alpoge-rh-replay/issues/7179) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M025854](https://github.com/rohanarun/alpoge-rh-replay/issues/7180) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115564](https://github.com/rohanarun/alpoge-rh-replay/issues/7181) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M137992](https://github.com/rohanarun/alpoge-rh-replay/issues/7182) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M084499](https://github.com/rohanarun/alpoge-rh-replay/issues/7184) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M115168](https://github.com/rohanarun/alpoge-rh-replay/issues/7185) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M077751](https://github.com/rohanarun/alpoge-rh-replay/issues/7187) | Claimed |
| [@rayy3535](https://github.com/rayy3535) | [M002449](https://github.com/rohanarun/alpoge-rh-replay/issues/7188) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M150279](https://github.com/rohanarun/alpoge-rh-replay/issues/7189) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M150343](https://github.com/rohanarun/alpoge-rh-replay/issues/7193) | Claimed |
| [@RobertBarnettProjects](https://github.com/RobertBarnettProjects) | [M141277](https://github.com/rohanarun/alpoge-rh-replay/issues/7195) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[767 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@ANdATIon](https://github.com/ANdATIon) | [M043033](https://github.com/rohanarun/alpoge-rh-replay/issues/7150#issuecomment-7053625872) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M160580](https://github.com/rohanarun/alpoge-rh-replay/issues/7154#issuecomment-7053624853) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M012918](https://github.com/rohanarun/alpoge-rh-replay/issues/7157#issuecomment-7053625311) | Pending review |
| [@ANdATIon](https://github.com/ANdATIon) | [M164028](https://github.com/rohanarun/alpoge-rh-replay/issues/7160#issuecomment-7053634903) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M160709](https://github.com/rohanarun/alpoge-rh-replay/issues/7164#issuecomment-7053627490) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M115537](https://github.com/rohanarun/alpoge-rh-replay/issues/7165#issuecomment-7053627775) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M101535](https://github.com/rohanarun/alpoge-rh-replay/issues/7169#issuecomment-7053629982) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M116148](https://github.com/rohanarun/alpoge-rh-replay/issues/7171#issuecomment-7053629723) | Pending review |
| [@egergerfg](https://github.com/egergerfg) | [M163962](https://github.com/rohanarun/alpoge-rh-replay/issues/7173#issuecomment-7053631241) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M114950](https://github.com/rohanarun/alpoge-rh-replay/issues/7174#issuecomment-7053635445) | Pending review |
| [@matan1905](https://github.com/matan1905) | [M106058](https://github.com/rohanarun/alpoge-rh-replay/issues/7175#issuecomment-7053636286) | Pending review |
| [@drew2apps](https://github.com/drew2apps) | [M165948](https://github.com/rohanarun/alpoge-rh-replay/issues/7178#issuecomment-7053635483) | Pending review |
| [@galakurpi](https://github.com/galakurpi) | [M130212](https://github.com/rohanarun/alpoge-rh-replay/issues/7183#issuecomment-7053634291) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M154834](https://github.com/rohanarun/alpoge-rh-replay/issues/7186#issuecomment-7053633970) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M114951](https://github.com/rohanarun/alpoge-rh-replay/issues/7190#issuecomment-7053641096) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M002739](https://github.com/rohanarun/alpoge-rh-replay/issues/7191#issuecomment-7053635300) | Pending review |
| [@rayy3535](https://github.com/rayy3535) | [M121518](https://github.com/rohanarun/alpoge-rh-replay/issues/7192#issuecomment-7053636694) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M115803](https://github.com/rohanarun/alpoge-rh-replay/issues/7194#issuecomment-7053640075) | Pending review |
| [@egergerfg](https://github.com/egergerfg) | [M164644](https://github.com/rohanarun/alpoge-rh-replay/issues/7196#issuecomment-7053636383) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M115551](https://github.com/rohanarun/alpoge-rh-replay/issues/7197#issuecomment-7053640264) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[4,913 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M143919](https://github.com/rohanarun/alpoge-rh-replay/issues/6935#issuecomment-7053646605) | 1 | [Build evidence verified](evidence/volunteers/M143919.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M092227](https://github.com/rohanarun/alpoge-rh-replay/issues/6933#issuecomment-7053646032) | 1 | [Build evidence verified](evidence/volunteers/M092227.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M114977](https://github.com/rohanarun/alpoge-rh-replay/issues/6932#issuecomment-7053645453) | 1 | [Build evidence verified](evidence/volunteers/M114977.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M143839](https://github.com/rohanarun/alpoge-rh-replay/issues/6920#issuecomment-7053634596) | 1 | [Build evidence verified](evidence/volunteers/M143839.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115776](https://github.com/rohanarun/alpoge-rh-replay/issues/6916#issuecomment-7053634090) | 1 | [Build evidence verified](evidence/volunteers/M115776.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115220](https://github.com/rohanarun/alpoge-rh-replay/issues/6914#issuecomment-7053633501) | 1 | [Build evidence verified](evidence/volunteers/M115220.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M043813](https://github.com/rohanarun/alpoge-rh-replay/issues/6912#issuecomment-7053632932) | 1 | [Build evidence verified](evidence/volunteers/M043813.json) |
| [@t-choudhury](https://github.com/t-choudhury) | [M135054](https://github.com/rohanarun/alpoge-rh-replay/issues/6909#issuecomment-7053673063) | 1 | [Build evidence verified](evidence/volunteers/M135054.json) |
| [@misuadn-laplace](https://github.com/misuadn-laplace) | [M115276](https://github.com/rohanarun/alpoge-rh-replay/issues/7037#issuecomment-7053625382) | 1 | [Build evidence verified](evidence/volunteers/M115276.json) |
| [@hipotures](https://github.com/hipotures) | [P1649](https://github.com/rohanarun/alpoge-rh-replay/issues/6876#issuecomment-7053636337) | 64 | [Build evidence verified](evidence/volunteers/P1649.json) |
| [@JamCh01](https://github.com/JamCh01) | [P1706](https://github.com/rohanarun/alpoge-rh-replay/issues/6638#issuecomment-7053719176) | 64 | [Build evidence verified](evidence/volunteers/P1706.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1818](https://github.com/rohanarun/alpoge-rh-replay/issues/6538#issuecomment-7053712856) | 64 | [Build evidence verified](evidence/volunteers/P1818.json) |
| [@dga471](https://github.com/dga471) | [M073054](https://github.com/rohanarun/alpoge-rh-replay/issues/6615#issuecomment-7053689604) | 1 | [Build evidence verified](evidence/volunteers/M073054.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1862](https://github.com/rohanarun/alpoge-rh-replay/issues/6356#issuecomment-7053662850) | 64 | [Build evidence verified](evidence/volunteers/P1862.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1705](https://github.com/rohanarun/alpoge-rh-replay/issues/6269#issuecomment-7053665264) | 64 | [Build evidence verified](evidence/volunteers/P1705.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M126616](https://github.com/rohanarun/alpoge-rh-replay/issues/6209#issuecomment-7053725465) | 1 | [Build evidence verified](evidence/volunteers/M126616.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M034297](https://github.com/rohanarun/alpoge-rh-replay/issues/5214#issuecomment-7053675234) | 1 | [Build evidence verified](evidence/volunteers/M034297.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M036241](https://github.com/rohanarun/alpoge-rh-replay/issues/5184#issuecomment-7053674491) | 1 | [Build evidence verified](evidence/volunteers/M036241.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M169425](https://github.com/rohanarun/alpoge-rh-replay/issues/5118#issuecomment-7053726366) | 1 | [Build evidence verified](evidence/volunteers/M169425.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1634](https://github.com/rohanarun/alpoge-rh-replay/issues/2442#issuecomment-7053700738) | 64 | [Build evidence verified](evidence/volunteers/P1634.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 17,831 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 19,025 |
| Worker target kernel replay reviewed | 99 |
| **Total with recorded module evidence** | **54,076 / 175,187** |

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
