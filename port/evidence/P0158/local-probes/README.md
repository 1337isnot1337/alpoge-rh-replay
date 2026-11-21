# Local compatibility probes

These small target-toolchain checks explain the mechanical changes. They are not packet compilation evidence. The full-packet CI artifact records compilation of the complete modules.

- `RuleDev.lean`: expected-type propagation through `Eq.symm` before `Submodule.span_eq_bot`.
- `Coefficient.lean`: equality by `rfl` between the exact replay-pinned coefficient accessor body and the target field accessor, including the matrix product shape.
- `Product.lean`: the target finite-product bound with both original proof arguments.
- `PadicCompatibility.lean`: the four valuation proof patterns using the current multiplicity API.

All probes used Lean 4.36.0 (`611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9`) and Mathlib `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`. Log file paths retain their actual local execution locations. The source files have been copied here without changing their bytes.
