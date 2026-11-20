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

**Replay volunteers (48)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@aapolipponen](https://github.com/aapolipponen), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@BenCaunt](https://github.com/BenCaunt), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@gabeldev](https://github.com/gabeldev), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@hipotures](https://github.com/hipotures), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jjjhenriksen](https://github.com/jjjhenriksen), [@juanfers1](https://github.com/juanfers1), [@krisyotam](https://github.com/krisyotam), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@maddoxjack](https://github.com/maddoxjack), [@maxime-fleury](https://github.com/maxime-fleury), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@roonastgames](https://github.com/roonastgames), [@sat3n](https://github.com/sat3n), [@SeriousRising](https://github.com/SeriousRising), [@shardmods](https://github.com/shardmods), [@surfyhou](https://github.com/surfyhou), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@unhingedpanda](https://github.com/unhingedpanda), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@WilmervH](https://github.com/WilmervH), [@Wronskode](https://github.com/Wronskode)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[832 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@sat3n](https://github.com/sat3n) | [M068440](https://github.com/rohanarun/alpoge-rh-replay/issues/3366) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M027309](https://github.com/rohanarun/alpoge-rh-replay/issues/3367) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M068547](https://github.com/rohanarun/alpoge-rh-replay/issues/3372) | Claimed |
| [@mu-mei](https://github.com/mu-mei) | [M003042](https://github.com/rohanarun/alpoge-rh-replay/issues/3375) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M164814](https://github.com/rohanarun/alpoge-rh-replay/issues/3376) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M068582](https://github.com/rohanarun/alpoge-rh-replay/issues/3377) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M165614](https://github.com/rohanarun/alpoge-rh-replay/issues/3378) | Claimed |
| [@egergerfg](https://github.com/egergerfg) | [M152569](https://github.com/rohanarun/alpoge-rh-replay/issues/3379) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M068717](https://github.com/rohanarun/alpoge-rh-replay/issues/3380) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M068728](https://github.com/rohanarun/alpoge-rh-replay/issues/3381) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M049979](https://github.com/rohanarun/alpoge-rh-replay/issues/3382) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M069120](https://github.com/rohanarun/alpoge-rh-replay/issues/3387) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M036422](https://github.com/rohanarun/alpoge-rh-replay/issues/3389) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M013570](https://github.com/rohanarun/alpoge-rh-replay/issues/3390) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M069195](https://github.com/rohanarun/alpoge-rh-replay/issues/3392) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115101](https://github.com/rohanarun/alpoge-rh-replay/issues/3393) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M171772](https://github.com/rohanarun/alpoge-rh-replay/issues/3396) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M069345](https://github.com/rohanarun/alpoge-rh-replay/issues/3397) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M109259](https://github.com/rohanarun/alpoge-rh-replay/issues/3398) | Claimed |
| [@sat3n](https://github.com/sat3n) | [M069410](https://github.com/rohanarun/alpoge-rh-replay/issues/3399) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[489 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@mu-mei](https://github.com/mu-mei) | [M003068](https://github.com/rohanarun/alpoge-rh-replay/issues/3316#issuecomment-7051067058) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M079463](https://github.com/rohanarun/alpoge-rh-replay/issues/3318#issuecomment-7051065226) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M125795](https://github.com/rohanarun/alpoge-rh-replay/issues/3319#issuecomment-7051068082) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M099076](https://github.com/rohanarun/alpoge-rh-replay/issues/3321#issuecomment-7051073945) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M002505](https://github.com/rohanarun/alpoge-rh-replay/issues/3325#issuecomment-7051076329) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M066867](https://github.com/rohanarun/alpoge-rh-replay/issues/3332#issuecomment-7051070000) | Pending review |
| [@emsi](https://github.com/emsi) | [M100654](https://github.com/rohanarun/alpoge-rh-replay/issues/3333#issuecomment-7051079744) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M069962](https://github.com/rohanarun/alpoge-rh-replay/issues/3340#issuecomment-7051085645) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M080091](https://github.com/rohanarun/alpoge-rh-replay/issues/3350#issuecomment-7051092771) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M162720](https://github.com/rohanarun/alpoge-rh-replay/issues/3351#issuecomment-7051090648) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M080170](https://github.com/rohanarun/alpoge-rh-replay/issues/3356#issuecomment-7051093848) | Pending review |
| [@roonastgames](https://github.com/roonastgames) | [M164705](https://github.com/rohanarun/alpoge-rh-replay/issues/3358#issuecomment-7051135697) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M171498](https://github.com/rohanarun/alpoge-rh-replay/issues/3360#issuecomment-7051091141) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M173779](https://github.com/rohanarun/alpoge-rh-replay/issues/3368#issuecomment-7051111045) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M000179](https://github.com/rohanarun/alpoge-rh-replay/issues/3370#issuecomment-7051114733) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M099231](https://github.com/rohanarun/alpoge-rh-replay/issues/3371#issuecomment-7051114567) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M002536](https://github.com/rohanarun/alpoge-rh-replay/issues/3373#issuecomment-7051130098) | Pending review |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M101474](https://github.com/rohanarun/alpoge-rh-replay/issues/3385#issuecomment-7051120528) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M080270](https://github.com/rohanarun/alpoge-rh-replay/issues/3391#issuecomment-7051120191) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M004947](https://github.com/rohanarun/alpoge-rh-replay/issues/3394#issuecomment-7051125890) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[1,716 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115289](https://github.com/rohanarun/alpoge-rh-replay/issues/2773#issuecomment-7050579940) | 1 | [Build evidence verified](evidence/volunteers/M115289.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M138584](https://github.com/rohanarun/alpoge-rh-replay/issues/2765#issuecomment-7050566108) | 1 | [Build evidence verified](evidence/volunteers/M138584.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M031851](https://github.com/rohanarun/alpoge-rh-replay/issues/2763#issuecomment-7050565396) | 1 | [Build evidence verified](evidence/volunteers/M031851.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M038270](https://github.com/rohanarun/alpoge-rh-replay/issues/2761#issuecomment-7050564695) | 1 | [Build evidence verified](evidence/volunteers/M038270.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M129538](https://github.com/rohanarun/alpoge-rh-replay/issues/2760#issuecomment-7050563930) | 1 | [Build evidence verified](evidence/volunteers/M129538.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M065301](https://github.com/rohanarun/alpoge-rh-replay/issues/2751#issuecomment-7050550737) | 1 | [Build evidence verified](evidence/volunteers/M065301.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115447](https://github.com/rohanarun/alpoge-rh-replay/issues/2750#issuecomment-7050550008) | 1 | [Build evidence verified](evidence/volunteers/M115447.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M170729](https://github.com/rohanarun/alpoge-rh-replay/issues/2748#issuecomment-7050549107) | 1 | [Build evidence verified](evidence/volunteers/M170729.json) |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115793](https://github.com/rohanarun/alpoge-rh-replay/issues/2746#issuecomment-7050548295) | 1 | [Build evidence verified](evidence/volunteers/M115793.json) |
| [@Paulee314](https://github.com/Paulee314) | [M032434](https://github.com/rohanarun/alpoge-rh-replay/issues/2717#issuecomment-7050632504) | 1 | [Build evidence verified](evidence/volunteers/M032434.json) |
| [@SeriousRising](https://github.com/SeriousRising) | [P1653](https://github.com/rohanarun/alpoge-rh-replay/issues/2481#issuecomment-7050556540) | 64 | [Build evidence verified](evidence/volunteers/P1653.json) |
| [@hipotures](https://github.com/hipotures) | [P1524](https://github.com/rohanarun/alpoge-rh-replay/issues/2370#issuecomment-7050597794) | 64 | [Build evidence verified](evidence/volunteers/P1524.json) |
| [@123454321bobbob-tech](https://github.com/123454321bobbob-tech) | [M000522](https://github.com/rohanarun/alpoge-rh-replay/issues/2096#issuecomment-7050750353) | 1 | [Build evidence verified](evidence/volunteers/M000522.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1456](https://github.com/rohanarun/alpoge-rh-replay/issues/1138#issuecomment-7050718529) | 64 | [Build evidence verified](evidence/volunteers/P1456.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1451](https://github.com/rohanarun/alpoge-rh-replay/issues/1130#issuecomment-7050564980) | 64 | [Build evidence verified](evidence/volunteers/P1451.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1445](https://github.com/rohanarun/alpoge-rh-replay/issues/1122#issuecomment-7050579377) | 64 | [Build evidence verified](evidence/volunteers/P1445.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1403](https://github.com/rohanarun/alpoge-rh-replay/issues/1072#issuecomment-7050569409) | 64 | [Build evidence verified](evidence/volunteers/P1403.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1438](https://github.com/rohanarun/alpoge-rh-replay/issues/1120#issuecomment-7050560075) | 64 | [Build evidence verified](evidence/volunteers/P1438.json) |
| [@WilmervH](https://github.com/WilmervH) | [P1311](https://github.com/rohanarun/alpoge-rh-replay/issues/891#issuecomment-7050782691) | 64 | [Build evidence verified](evidence/volunteers/P1311.json) |
| [@dgahelper](https://github.com/dgahelper) | [P1145](https://github.com/rohanarun/alpoge-rh-replay/issues/341#issuecomment-7050766163) | 64 | [Build evidence verified](evidence/volunteers/P1145.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 10,596 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 9,465 |
| **Total with recorded module evidence** | **37,182 / 175,187** |

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
