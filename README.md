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

[788 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M024814](https://github.com/rohanarun/alpoge-rh-replay/issues/3175) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115066](https://github.com/rohanarun/alpoge-rh-replay/issues/3177) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M079732](https://github.com/rohanarun/alpoge-rh-replay/issues/3179) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M074357](https://github.com/rohanarun/alpoge-rh-replay/issues/3180) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M130222](https://github.com/rohanarun/alpoge-rh-replay/issues/3183) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M150232](https://github.com/rohanarun/alpoge-rh-replay/issues/3185) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M173736](https://github.com/rohanarun/alpoge-rh-replay/issues/3186) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M168044](https://github.com/rohanarun/alpoge-rh-replay/issues/3187) | Claimed |
| [@dgahelper](https://github.com/dgahelper) | [P1598](https://github.com/rohanarun/alpoge-rh-replay/issues/3191) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M028351](https://github.com/rohanarun/alpoge-rh-replay/issues/3201) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M170860](https://github.com/rohanarun/alpoge-rh-replay/issues/3202) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M108516](https://github.com/rohanarun/alpoge-rh-replay/issues/3203) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M012814](https://github.com/rohanarun/alpoge-rh-replay/issues/3204) | Claimed |
| [@emsi](https://github.com/emsi) | [P1768](https://github.com/rohanarun/alpoge-rh-replay/issues/3205) | Claimed |
| [@WilmervH](https://github.com/WilmervH) | [P1591](https://github.com/rohanarun/alpoge-rh-replay/issues/3208) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M162450](https://github.com/rohanarun/alpoge-rh-replay/issues/3212) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M028353](https://github.com/rohanarun/alpoge-rh-replay/issues/3213) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M115232](https://github.com/rohanarun/alpoge-rh-replay/issues/3214) | Claimed |
| [@vivekshivarajkumar](https://github.com/vivekshivarajkumar) | [M027726](https://github.com/rohanarun/alpoge-rh-replay/issues/3216) | Claimed |
| [@user42245](https://github.com/user42245) | [M057888](https://github.com/rohanarun/alpoge-rh-replay/issues/3217) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[385 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@user42245](https://github.com/user42245) | [M055511](https://github.com/rohanarun/alpoge-rh-replay/issues/3182#issuecomment-7050904849) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M058898](https://github.com/rohanarun/alpoge-rh-replay/issues/3184#issuecomment-7050918644) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M055997](https://github.com/rohanarun/alpoge-rh-replay/issues/3188#issuecomment-7050927257) | Pending review |
| [@user42245](https://github.com/user42245) | [M055678](https://github.com/rohanarun/alpoge-rh-replay/issues/3189#issuecomment-7050908777) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M057684](https://github.com/rohanarun/alpoge-rh-replay/issues/3190#issuecomment-7050933687) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M034816](https://github.com/rohanarun/alpoge-rh-replay/issues/3192#issuecomment-7050927877) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M017675](https://github.com/rohanarun/alpoge-rh-replay/issues/3193#issuecomment-7050944788) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M044523](https://github.com/rohanarun/alpoge-rh-replay/issues/3194#issuecomment-7050934607) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M161184](https://github.com/rohanarun/alpoge-rh-replay/issues/3195#issuecomment-7050930600) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M000131](https://github.com/rohanarun/alpoge-rh-replay/issues/3196#issuecomment-7050930711) | Pending review |
| [@maxime-fleury](https://github.com/maxime-fleury) | [M002399](https://github.com/rohanarun/alpoge-rh-replay/issues/3197#issuecomment-7050942776) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M100733](https://github.com/rohanarun/alpoge-rh-replay/issues/3198#issuecomment-7050930699) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M044943](https://github.com/rohanarun/alpoge-rh-replay/issues/3199#issuecomment-7050950827) | Pending review |
| [@mu-mei](https://github.com/mu-mei) | [M100814](https://github.com/rohanarun/alpoge-rh-replay/issues/3200#issuecomment-7050931837) | Pending review |
| [@maddoxjack](https://github.com/maddoxjack) | [M068539](https://github.com/rohanarun/alpoge-rh-replay/issues/3206#issuecomment-7050946861) | Pending review |
| [@varo6](https://github.com/varo6) | [M056073](https://github.com/rohanarun/alpoge-rh-replay/issues/3207#issuecomment-7050959358) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M057892](https://github.com/rohanarun/alpoge-rh-replay/issues/3209#issuecomment-7050948701) | Pending review |
| [@nicu-chiciuc](https://github.com/nicu-chiciuc) | [M060036](https://github.com/rohanarun/alpoge-rh-replay/issues/3210#issuecomment-7050951968) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M103614](https://github.com/rohanarun/alpoge-rh-replay/issues/3211#issuecomment-7050953853) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M103883](https://github.com/rohanarun/alpoge-rh-replay/issues/3215#issuecomment-7050961844) | Pending review |

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
