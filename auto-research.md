# Agent instructions for the independent RH replay

Your task is to produce reproducible evidence for one part of Alpöge’s published Lean proof. The full replay is ongoing. Only the final theorem, axiom audit, and fresh-kernel receipt can establish the full project result.

1. Clone this repository or fast-forward your checkout of main. Read CONTRIBUTING.md, STATUS.md, and the [completed-parts ledger](completed/README.md). Run `python3 tracker/tasks.py next` for currently available packets. A packet contains up to 64 same-depth modules. For narrower assignments, inspect a packet with `show` and select one open module ID.
2. Run `python3 tracker/tasks.py claim <ID>`. Each packet and every module inside it share one reservation. Wait for both the **claim-granted** label and a matching **Granted** comment from github-actions[bot]. A request without that confirmation is pending. If the bot marks a conflict, close your request and choose other work. Keep the title stable after grant. Split a packet among your own processes only while you hold its grant.
3. Prepare a clean Linux volume using `./verify.sh /path/to/empty-volume --prepare-only`. Keep the published archive immutable. The inputs are the 14 pinned SHA-256 hashes, Lean 4.33.1 and the pinned mathlib commit. Reuse artifacts only if their provenance, input digests, and toolchain match.
4. Run `python3 tracker/tasks.py build <ID> /path/to/empty-volume/lean /path/to/new-receipt --bundle`. Log resources, UTC times, and any infrastructure retries. Lake may also build prerequisites on a cold worker. Report requested targets separately from locally rebuilt imports.
5. Attach the receipt and log, and link the optional artifact bundle and checksum, on the claim issue. Submit the first diagnostic for a failure. A compiler pass, reuse check, partial kernel replay, and fresh full-project replay are different outcomes. Describe exactly what ran.
6. Keep a submitted issue open during maintainer review, and close a reservation you abandon. Maintainers update the completed ledger after reviewing evidence. A grant is a reservation for targeted volunteer work; the independent primary build continues walking the full dependency graph and may reach prerequisites before a volunteer returns.

## Maintainer checks

The claim workflow serializes reconciliation of all open issues, preserves valid grants, and rejects overlap between packet and module reservations. Verify input hashes, source and object digests, and the claimed command before accepting any external result. Keep outside artifacts and code in isolated environments. Publish a full-RH verdict only after the criteria in README.md are satisfied.
