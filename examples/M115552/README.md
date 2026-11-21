# Lifting a residue-field basis

Module M115552 constructs a basis of the residue field of a nonarchimedean local field over `ZMod l`, lifts its basis vectors to the valuation ring, and proves their linear independence over the l-adic numbers when the algebra map is continuous. The revision uses Mathlib's valuation-ring and residue-field notation and the local `ZMod`-algebra instance. This lets Lean infer the ring, field and module structures that the archive spells out in full. It retains the two private proofs that lift residue-field independence and place the p-adic integers inside the valuation ring.

`AuditAll.lean` checks all ten public declarations by `rfl`, including the values of the four definitions and the propositions proved by the six theorems. It checks the declaration lists of both modules against the ten pairs, compares binder names, binder visibility and universes, and audits both sides with `collectAxioms`. The reference module is the pinned original with its declaration namespace renamed. Both versions import `Mathlib`.

| Metric | Published | Revised |
| --- | ---: | ---: |
| Source lines | 5,746 | 123 |
| Heartbeats across the 10 public declarations | 31,750 | 10,916 |
| Heartbeats including both private helpers | 47,087 | 26,238 |

Both columns use the same `Mathlib` import and compiler flags on x86-64 Windows. The ten public declarations use **65.6% fewer heartbeats**; including the private proofs, the reduction is **44.3%**. See the [receipt](receipt.json) for source and diff digests and the [compiler transcript](transcript.txt) for each declaration and the three successful kernel replays.

## Reproduce

Start in the `lean/` directory of a prepared original replay volume (Lean 4.33.1, Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`). Run the example script through that project's Lake environment.

```bash
lake env python3 /path/to/alpoge-rh-replay/examples/M115552/replay.py "$PWD"
```

The script checks source and diff digests, compiles the two modules and the audit in a temporary directory, replays all three with `leanchecker`, then instruments each of the twelve declarations with `#count_heartbeats` under `-j1 -DElab.async=false`. It reports totals both with and without the two private helpers. Use `make_diff.py "$PWD" -o mem-of-closed.patch` to regenerate the diff, or `make_diff.py "$PWD" --check` to check its SHA-256.
