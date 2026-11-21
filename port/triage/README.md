# Port triage

Depth-0 and unblocked Depth-1 live modules compiled **unchanged** on `leanprover/lean4:v4.36.0` with Mathlib `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`, one Lean process per module (with landed Depth-0 `.olean`s built for Depth 1), on Google Cloud.

| Status | Modules |
|---|---:|
| ok | 4,100 |
| fail / timeout | 684 |
| **total triaged** | **4,784** |

`results.json` lists each module's status, compile time and, for failures, the first compiler output (`excerpt`).
`ok` modules have already been landed as `port/patches/<ID>.json` with `"notes": "unchanged"`. Start porting from the remaining unported failures in [failing.md](failing.md) (**215** live modules currently failing).
