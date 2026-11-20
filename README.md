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

**Replay volunteers (49)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@iAndyHD3](https://github.com/iAndyHD3), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@krisyotam](https://github.com/krisyotam), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@surfyhou](https://github.com/surfyhou), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@WilmervH](https://github.com/WilmervH), [@Wronskode](https://github.com/Wronskode)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[817 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M057304](https://github.com/rohanarun/alpoge-rh-replay/issues/3415) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M158734](https://github.com/rohanarun/alpoge-rh-replay/issues/3419) | Claimed |
| [@surfyhou](https://github.com/surfyhou) | [P1781](https://github.com/rohanarun/alpoge-rh-replay/issues/3430) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M043955](https://github.com/rohanarun/alpoge-rh-replay/issues/3432) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M098814](https://github.com/rohanarun/alpoge-rh-replay/issues/3433) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M064704](https://github.com/rohanarun/alpoge-rh-replay/issues/3434) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115661](https://github.com/rohanarun/alpoge-rh-replay/issues/3435) | Claimed |
| [@SeriousRising](https://github.com/SeriousRising) | [P1750](https://github.com/rohanarun/alpoge-rh-replay/issues/3442) | Claimed |
| [@iAndyHD3](https://github.com/iAndyHD3) | [M070463](https://github.com/rohanarun/alpoge-rh-replay/issues/3447) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M005924](https://github.com/rohanarun/alpoge-rh-replay/issues/3455) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M085742](https://github.com/rohanarun/alpoge-rh-replay/issues/3457) | Claimed |
| [@dga471](https://github.com/dga471) | [M073708](https://github.com/rohanarun/alpoge-rh-replay/issues/3458) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M038296](https://github.com/rohanarun/alpoge-rh-replay/issues/3459) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M132280](https://github.com/rohanarun/alpoge-rh-replay/issues/3460) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115306](https://github.com/rohanarun/alpoge-rh-replay/issues/3461) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M006412](https://github.com/rohanarun/alpoge-rh-replay/issues/3462) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M007374](https://github.com/rohanarun/alpoge-rh-replay/issues/3464) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115319](https://github.com/rohanarun/alpoge-rh-replay/issues/3465) | Claimed |
| [@user42245](https://github.com/user42245) | [M070632](https://github.com/rohanarun/alpoge-rh-replay/issues/3466) | Claimed |
| [@emsi](https://github.com/emsi) | [P1762](https://github.com/rohanarun/alpoge-rh-replay/issues/3467) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[407 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@BenCaunt](https://github.com/BenCaunt) | [M003690](https://github.com/rohanarun/alpoge-rh-replay/issues/3436#issuecomment-7051173883) | Pending review |
| [@emsi](https://github.com/emsi) | [M002771](https://github.com/rohanarun/alpoge-rh-replay/issues/3437#issuecomment-7051179721) | Pending review |
| [@emsi](https://github.com/emsi) | [M044378](https://github.com/rohanarun/alpoge-rh-replay/issues/3438#issuecomment-7051181705) | Pending review |
| [@emsi](https://github.com/emsi) | [M100856](https://github.com/rohanarun/alpoge-rh-replay/issues/3439#issuecomment-7051183775) | Pending review |
| [@emsi](https://github.com/emsi) | [M004837](https://github.com/rohanarun/alpoge-rh-replay/issues/3440#issuecomment-7051197023) | Pending review |
| [@emsi](https://github.com/emsi) | [M100685](https://github.com/rohanarun/alpoge-rh-replay/issues/3441#issuecomment-7051198939) | Pending review |
| [@emsi](https://github.com/emsi) | [M002156](https://github.com/rohanarun/alpoge-rh-replay/issues/3443#issuecomment-7051201006) | Pending review |
| [@emsi](https://github.com/emsi) | [M003436](https://github.com/rohanarun/alpoge-rh-replay/issues/3444#issuecomment-7051192859) | Pending review |
| [@emsi](https://github.com/emsi) | [M003468](https://github.com/rohanarun/alpoge-rh-replay/issues/3445#issuecomment-7051195038) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M081522](https://github.com/rohanarun/alpoge-rh-replay/issues/3446#issuecomment-7051181166) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M004077](https://github.com/rohanarun/alpoge-rh-replay/issues/3448#issuecomment-7051190642) | Pending review |
| [@varo6](https://github.com/varo6) | [M071069](https://github.com/rohanarun/alpoge-rh-replay/issues/3449#issuecomment-7051190910) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M100886](https://github.com/rohanarun/alpoge-rh-replay/issues/3450#issuecomment-7051184291) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M082067](https://github.com/rohanarun/alpoge-rh-replay/issues/3451#issuecomment-7051192334) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M075159](https://github.com/rohanarun/alpoge-rh-replay/issues/3452#issuecomment-7051191645) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M162800](https://github.com/rohanarun/alpoge-rh-replay/issues/3453#issuecomment-7051186749) | Pending review |
| [@user42245](https://github.com/user42245) | [M070504](https://github.com/rohanarun/alpoge-rh-replay/issues/3454#issuecomment-7051188814) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M004392](https://github.com/rohanarun/alpoge-rh-replay/issues/3456#issuecomment-7051204367) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M101367](https://github.com/rohanarun/alpoge-rh-replay/issues/3463#issuecomment-7051213155) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M089389](https://github.com/rohanarun/alpoge-rh-replay/issues/3468#issuecomment-7051211735) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[1,878 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M060450](https://github.com/rohanarun/alpoge-rh-replay/issues/3026#issuecomment-7050856301) | 1 | [Build evidence verified](evidence/volunteers/M060450.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M055703](https://github.com/rohanarun/alpoge-rh-replay/issues/3018#issuecomment-7050841378) | 1 | [Build evidence verified](evidence/volunteers/M055703.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M058770](https://github.com/rohanarun/alpoge-rh-replay/issues/3016#issuecomment-7050840738) | 1 | [Build evidence verified](evidence/volunteers/M058770.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M016858](https://github.com/rohanarun/alpoge-rh-replay/issues/3015#issuecomment-7050840049) | 1 | [Build evidence verified](evidence/volunteers/M016858.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M036376](https://github.com/rohanarun/alpoge-rh-replay/issues/3014#issuecomment-7050839368) | 1 | [Build evidence verified](evidence/volunteers/M036376.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M060052](https://github.com/rohanarun/alpoge-rh-replay/issues/2994#issuecomment-7050823856) | 1 | [Build evidence verified](evidence/volunteers/M060052.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M079855](https://github.com/rohanarun/alpoge-rh-replay/issues/2993#issuecomment-7050823244) | 1 | [Build evidence verified](evidence/volunteers/M079855.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M100360](https://github.com/rohanarun/alpoge-rh-replay/issues/2988#issuecomment-7050822599) | 1 | [Build evidence verified](evidence/volunteers/M100360.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M140941](https://github.com/rohanarun/alpoge-rh-replay/issues/2986#issuecomment-7050821891) | 1 | [Build evidence verified](evidence/volunteers/M140941.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115153](https://github.com/rohanarun/alpoge-rh-replay/issues/2974#issuecomment-7050808759) | 1 | [Build evidence verified](evidence/volunteers/M115153.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M087591](https://github.com/rohanarun/alpoge-rh-replay/issues/2971#issuecomment-7050808025) | 1 | [Build evidence verified](evidence/volunteers/M087591.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M100205](https://github.com/rohanarun/alpoge-rh-replay/issues/2969#issuecomment-7050807417) | 1 | [Build evidence verified](evidence/volunteers/M100205.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M044509](https://github.com/rohanarun/alpoge-rh-replay/issues/2967#issuecomment-7050806707) | 1 | [Build evidence verified](evidence/volunteers/M044509.json) |
| [@SeriousRising](https://github.com/SeriousRising) | [P1677](https://github.com/rohanarun/alpoge-rh-replay/issues/2885#issuecomment-7051057211) | 64 | [Build evidence verified](evidence/volunteers/P1677.json) |
| [@emsi](https://github.com/emsi) | [P1722](https://github.com/rohanarun/alpoge-rh-replay/issues/2828#issuecomment-7050952950) | 64 | [Build evidence verified](evidence/volunteers/P1722.json) |
| [@emsi](https://github.com/emsi) | [P1794](https://github.com/rohanarun/alpoge-rh-replay/issues/2948#issuecomment-7051122780) | 64 | [Build evidence verified](evidence/volunteers/P1794.json) |
| [@dhudakk](https://github.com/dhudakk) | [M031586](https://github.com/rohanarun/alpoge-rh-replay/issues/2683#issuecomment-7050815484) | 1 | [Build evidence verified](evidence/volunteers/M031586.json) |
| [@emsi](https://github.com/emsi) | [P1652](https://github.com/rohanarun/alpoge-rh-replay/issues/2805#issuecomment-7050879339) | 64 | [Build evidence verified](evidence/volunteers/P1652.json) |
| [@emsi](https://github.com/emsi) | [P1562](https://github.com/rohanarun/alpoge-rh-replay/issues/2375#issuecomment-7050886506) | 64 | [Build evidence verified](evidence/volunteers/P1562.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1457](https://github.com/rohanarun/alpoge-rh-replay/issues/1140#issuecomment-7051113357) | 64 | [Build evidence verified](evidence/volunteers/P1457.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 11,393 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 10,005 |
| **Total with recorded module evidence** | **38,519 / 175,187** |

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
