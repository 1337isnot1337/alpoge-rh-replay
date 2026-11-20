# Independent replay of Alpöge’s RH release

Levent Alpöge announced a Lean proof of the Riemann Hypothesis on November 20, 2026. This repository records an independent attempt to check his published archive. Credit for the claimed proof belongs to Alpöge and his collaborators. [Original announcement](https://alpo.ge/remark.pdf)

## Current status

**Full replay in progress.** No full RH verification receipt has been produced by this project. The [two-worker pilot](evidence/pilot-receipt.json) transferred 150 previously unbuilt modules; the primary reused them and kernel-checked one downstream module.

Current cloud progress is recorded in the [worker status report](STATUS.md).

## Contributors

Choose any of **175,187 module tasks** or one of **2,858 work packets**. Each module has a source digest, direct dependencies, import depth, and a coordinator snapshot state. Use the [contributor guide](CONTRIBUTING.md) to find an available packet, claim it, build it, and return evidence. Browse the [packet index](tracker/packets.tsv), [snapshot totals](tracker/summary.json), or [open volunteer claims](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue%20is%3Aopen%20in%3Atitle%20Claim).

Start with the [agent instructions](auto-research.md) to claim work and submit replay evidence. Start your evidence comment with `Replay submission` to be credited automatically. Maintainers review the evidence before marking a task complete.

### Submitted for review

<!-- pending-volunteers-start -->

| Contributor | Task | Review |
|---|---|---|
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0020](https://github.com/rohanarun/alpoge-rh-replay/issues/2#issuecomment-7044751121) | Pending review |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0021](https://github.com/rohanarun/alpoge-rh-replay/issues/3#issuecomment-7044905860) | Pending review |
| [@surfyhou](https://github.com/surfyhou) | [M170887](https://github.com/rohanarun/alpoge-rh-replay/issues/5#issuecomment-7044980759) | Pending review |

<!-- pending-volunteers-end -->

### Reviewed builds

<!-- volunteers-start -->

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0012](https://github.com/rohanarun/alpoge-rh-replay/issues/1#issuecomment-7044609913) | 64 | [Build evidence verified](evidence/volunteers/P0012.json) |

<!-- volunteers-end -->

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 2,851 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 0 |
| Volunteer build evidence reviewed | 64 |
| **Total with recorded module evidence** | **3,066 / 175,187** |

[See each completed part and its evidence](completed/README.md) · [Machine-readable ledger](tracker/completed.tsv)

<!-- completed-end -->

## Give this prompt to an agent

> Help independently replay the claimed RH proof using https://github.com/rohanarun/alpoge-rh-replay. Read auto-research.md and fast-forward to the latest main commit. Run `python3 tracker/tasks.py next` and inspect an open packet. Claim exactly one open packet or module. Wait for the claim-granted label and matching bot comment before starting. Reproduce the pinned inputs, build the assigned targets and their required imports, and attach the receipt, log, and artifact hashes to your issue. If you stop, release the claim. Report exactly what passed and leave the full-RH verdict to the final audit.

[Full instructions for agents](auto-research.md) · [Claims and conflicts](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+in%3Atitle+Claim)

## Reproduce the check

On Linux, install the elan launcher and ensure its `lean` and `lake` commands are on your PATH. The script also requires Bash, Git, curl, GNU tar, sha256sum, a C toolchain, network access, and a large writable build volume. Run from this repository with a fresh output directory.

```bash
./verify.sh /path/to/empty/replay-directory
```

The script compares every archive part with its SHA-256 digest, checks the toolchain and mathlib revision, builds the final module from source, and writes the transcript to `replay.log` in the output directory. The pinned Lean compiler is 4.33.1 and the mathlib commit is `0df444a360eaa60ab8c11dca51a86af692955474`.

## Read the evidence

1. `REPLAY_SOURCE_BUILD_PASSED` means Lake built the module containing the final theorem.
2. `REPLAY_AXIOM_AUDIT_PASSED` means the declarations type-checked against the targets in `Audit.lean`. The audit rejects any reported axiom beyond propositional extensionality, classical choice, and quotient soundness.
3. `REPLAY_FRESH_KERNEL_PASSED` means Lean’s checker replayed the declarations imported by `Main` in a fresh environment. It uses the same Lean kernel implementation.

A completed report should include the exit status, all three outputs, the printed theorem and axioms, and a checksum for the archived transcript. A machine or storage failure leaves the mathematical claim unresolved.

## License

The original replay tooling and documentation in this repository are available under the [MIT License](LICENSE). Upstream Lean source, Mathlib, and third-party artifacts retain their respective licenses.
