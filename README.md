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

**Replay volunteers (53)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@krisyotam](https://github.com/krisyotam), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@surfyhou](https://github.com/surfyhou), [@TomMoeras](https://github.com/TomMoeras), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[733 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@dhudakk](https://github.com/dhudakk) | [M081135](https://github.com/rohanarun/alpoge-rh-replay/issues/3633) | Claimed |
| [@emsi](https://github.com/emsi) | [P1713](https://github.com/rohanarun/alpoge-rh-replay/issues/3640) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M153580](https://github.com/rohanarun/alpoge-rh-replay/issues/3647) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115538](https://github.com/rohanarun/alpoge-rh-replay/issues/3650) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M091584](https://github.com/rohanarun/alpoge-rh-replay/issues/3651) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M127929](https://github.com/rohanarun/alpoge-rh-replay/issues/3652) | Claimed |
| [@WorldianAI](https://github.com/WorldianAI) | [M080123](https://github.com/rohanarun/alpoge-rh-replay/issues/3657) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M101521](https://github.com/rohanarun/alpoge-rh-replay/issues/3672) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M131249](https://github.com/rohanarun/alpoge-rh-replay/issues/3676) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M171565](https://github.com/rohanarun/alpoge-rh-replay/issues/3677) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M103034](https://github.com/rohanarun/alpoge-rh-replay/issues/3679) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M162557](https://github.com/rohanarun/alpoge-rh-replay/issues/3687) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M056993](https://github.com/rohanarun/alpoge-rh-replay/issues/3688) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115310](https://github.com/rohanarun/alpoge-rh-replay/issues/3691) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M037475](https://github.com/rohanarun/alpoge-rh-replay/issues/3694) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M070472](https://github.com/rohanarun/alpoge-rh-replay/issues/3698) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M093338](https://github.com/rohanarun/alpoge-rh-replay/issues/3700) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M036427](https://github.com/rohanarun/alpoge-rh-replay/issues/3701) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M068420](https://github.com/rohanarun/alpoge-rh-replay/issues/3703) | Claimed |
| [@zediir](https://github.com/zediir) | [M080787](https://github.com/rohanarun/alpoge-rh-replay/issues/3706) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[528 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@user42245](https://github.com/user42245) | [M084887](https://github.com/rohanarun/alpoge-rh-replay/issues/3678#issuecomment-7051493273) | Pending review |
| [@TomMoeras](https://github.com/TomMoeras) | [M080712](https://github.com/rohanarun/alpoge-rh-replay/issues/3680#issuecomment-7051497566) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M000203](https://github.com/rohanarun/alpoge-rh-replay/issues/3681#issuecomment-7051497179) | Pending review |
| [@varo6](https://github.com/varo6) | [M081722](https://github.com/rohanarun/alpoge-rh-replay/issues/3682#issuecomment-7051499919) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M173234](https://github.com/rohanarun/alpoge-rh-replay/issues/3683#issuecomment-7051503092) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M174578](https://github.com/rohanarun/alpoge-rh-replay/issues/3684#issuecomment-7051512452) | Pending review |
| [@user42245](https://github.com/user42245) | [M084926](https://github.com/rohanarun/alpoge-rh-replay/issues/3686#issuecomment-7051541709) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M132950](https://github.com/rohanarun/alpoge-rh-replay/issues/3689#issuecomment-7051518908) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M082791](https://github.com/rohanarun/alpoge-rh-replay/issues/3690#issuecomment-7051519010) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M081322](https://github.com/rohanarun/alpoge-rh-replay/issues/3692#issuecomment-7051520495) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M131857](https://github.com/rohanarun/alpoge-rh-replay/issues/3693#issuecomment-7051529809) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M131755](https://github.com/rohanarun/alpoge-rh-replay/issues/3695#issuecomment-7051523454) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M004348](https://github.com/rohanarun/alpoge-rh-replay/issues/3696#issuecomment-7051526083) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M127365](https://github.com/rohanarun/alpoge-rh-replay/issues/3697#issuecomment-7051513577) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M002761](https://github.com/rohanarun/alpoge-rh-replay/issues/3699#issuecomment-7051528895) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M131253](https://github.com/rohanarun/alpoge-rh-replay/issues/3702#issuecomment-7051532323) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M154065](https://github.com/rohanarun/alpoge-rh-replay/issues/3704#issuecomment-7051546707) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M153524](https://github.com/rohanarun/alpoge-rh-replay/issues/3705#issuecomment-7051546982) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M134047](https://github.com/rohanarun/alpoge-rh-replay/issues/3707#issuecomment-7051549796) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M134269](https://github.com/rohanarun/alpoge-rh-replay/issues/3709#issuecomment-7051549326) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[2,072 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@sat3n](https://github.com/sat3n) | [M115030](https://github.com/rohanarun/alpoge-rh-replay/issues/2903#issuecomment-7051166293) | 1 | [Build evidence verified](evidence/volunteers/M115030.json) |
| [@sat3n](https://github.com/sat3n) | [M114989](https://github.com/rohanarun/alpoge-rh-replay/issues/2902#issuecomment-7051152016) | 1 | [Build evidence verified](evidence/volunteers/M114989.json) |
| [@sat3n](https://github.com/sat3n) | [M109991](https://github.com/rohanarun/alpoge-rh-replay/issues/2894#issuecomment-7051150302) | 1 | [Build evidence verified](evidence/volunteers/M109991.json) |
| [@sat3n](https://github.com/sat3n) | [M109314](https://github.com/rohanarun/alpoge-rh-replay/issues/2889#issuecomment-7051148696) | 1 | [Build evidence verified](evidence/volunteers/M109314.json) |
| [@hipotures](https://github.com/hipotures) | [P1543](https://github.com/rohanarun/alpoge-rh-replay/issues/2938#issuecomment-7051348700) | 64 | [Build evidence verified](evidence/volunteers/P1543.json) |
| [@surfyhou](https://github.com/surfyhou) | [P1570](https://github.com/rohanarun/alpoge-rh-replay/issues/2699#issuecomment-7051125724) | 64 | [Build evidence verified](evidence/volunteers/P1570.json) |
| [@dga471](https://github.com/dga471) | [M031373](https://github.com/rohanarun/alpoge-rh-replay/issues/2620#issuecomment-7050471941) | 1 | [Build evidence verified](evidence/volunteers/M031373.json) |
| [@dga471](https://github.com/dga471) | [M014616](https://github.com/rohanarun/alpoge-rh-replay/issues/2462#issuecomment-7050266514) | 1 | [Build evidence verified](evidence/volunteers/M014616.json) |
| [@dga471](https://github.com/dga471) | [M154134](https://github.com/rohanarun/alpoge-rh-replay/issues/2294#issuecomment-7050054189) | 1 | [Build evidence verified](evidence/volunteers/M154134.json) |
| [@dga471](https://github.com/dga471) | [M153640](https://github.com/rohanarun/alpoge-rh-replay/issues/2118#issuecomment-7049841570) | 1 | [Build evidence verified](evidence/volunteers/M153640.json) |
| [@dga471](https://github.com/dga471) | [M138849](https://github.com/rohanarun/alpoge-rh-replay/issues/1988#issuecomment-7049641158) | 1 | [Build evidence verified](evidence/volunteers/M138849.json) |
| [@dga471](https://github.com/dga471) | [M079958](https://github.com/rohanarun/alpoge-rh-replay/issues/1759#issuecomment-7049440060) | 1 | [Build evidence verified](evidence/volunteers/M079958.json) |
| [@dga471](https://github.com/dga471) | [M019614](https://github.com/rohanarun/alpoge-rh-replay/issues/1533#issuecomment-7049237563) | 1 | [Build evidence verified](evidence/volunteers/M019614.json) |
| [@dga471](https://github.com/dga471) | [M003761](https://github.com/rohanarun/alpoge-rh-replay/issues/1346#issuecomment-7049033648) | 1 | [Build evidence verified](evidence/volunteers/M003761.json) |
| [@dga471](https://github.com/dga471) | [M164632](https://github.com/rohanarun/alpoge-rh-replay/issues/1193#issuecomment-7048833023) | 1 | [Build evidence verified](evidence/volunteers/M164632.json) |
| [@dga471](https://github.com/dga471) | [M002710](https://github.com/rohanarun/alpoge-rh-replay/issues/1091#issuecomment-7048585822) | 1 | [Build evidence verified](evidence/volunteers/M002710.json) |
| [@dga471](https://github.com/dga471) | [M137503](https://github.com/rohanarun/alpoge-rh-replay/issues/947#issuecomment-7048371239) | 1 | [Build evidence verified](evidence/volunteers/M137503.json) |
| [@dga471](https://github.com/dga471) | [M161804](https://github.com/rohanarun/alpoge-rh-replay/issues/719#issuecomment-7048162547) | 1 | [Build evidence verified](evidence/volunteers/M161804.json) |
| [@dga471](https://github.com/dga471) | [M133853](https://github.com/rohanarun/alpoge-rh-replay/issues/519#issuecomment-7047946320) | 1 | [Build evidence verified](evidence/volunteers/M133853.json) |
| [@dga471](https://github.com/dga471) | [M113396](https://github.com/rohanarun/alpoge-rh-replay/issues/271#issuecomment-7047496567) | 1 | [Build evidence verified](evidence/volunteers/M113396.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 11,996 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 10,451 |
| **Total with recorded module evidence** | **39,568 / 175,187** |

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

## Read the evidence

1. `REPLAY_SOURCE_BUILD_PASSED` means Lake built the module containing the final theorem.
2. `REPLAY_AXIOM_AUDIT_PASSED` means the five public theorems in `Main` type-checked against their statements, which `Audit.lean` writes out with Mathlib definitions only. The audit rejects any reported axiom beyond propositional extensionality, classical choice, and quotient soundness.
3. `REPLAY_FRESH_KERNEL_PASSED` means Lean’s checker replayed the declarations imported by `Main` in a fresh environment. It uses the same Lean kernel implementation.

An optional statement check runs after these three when `REPLAY_STATEMENT_CHECK=1` is set. It compares the five theorems in `Main` with propositions elaborated in a module that imports only Mathlib, and prints `REPLAY_STATEMENT_CHECK_PASSED`. It can also be run against a completed checkout; see [audit/README.md](audit/README.md).

A completed report should include the exit status, all three outputs, the printed theorem and axioms, and a checksum for the archived transcript. A machine or storage failure leaves the mathematical claim unresolved.

## Optional determinant check

The [M115707 example](examples/M115707/README.md) compares a shorter local Gram determinant argument with the published module. This check runs separately from the volunteer replay.

## Volunteer activity

![Cumulative chart of volunteers, granted claims, and replay submissions](tracker/activity.svg)

[How the chart is counted](ACTIVITY.md) · [Event data](tracker/activity.tsv)

## License

The original replay tooling and documentation in this repository are available under the [MIT License](LICENSE). Upstream Lean source, Mathlib, and third-party artifacts retain their respective licenses.
