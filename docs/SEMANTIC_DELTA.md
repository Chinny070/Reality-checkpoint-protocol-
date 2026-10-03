# Semantic Delta Engine

Revalidation compares typed prior claim states and receipt facts with current independent observations. Model delta values are bounded to unchanged, cosmetic, minor, material, critical, contradiction, and unavailable classes. The contract controls successor creation, state, freshness, and lineage.

Each claim returns a typed semantic delta. Per-claim receipts retain prior/current state plus that delta. Deterministic rules override an underreported delta when the typed claim state changed, and mark a supported/contradicted flip as `CONTRADICTION`. When state is unchanged, the agreed claim-level semantic class is retained. Evidence hashes and typed deltas are included in state/evidence digests. Textual page differences alone do not constitute material change.

Insufficient evidence and external failure create nonfinal attempt receipts and preserve the prior finalized checkpoint. A decisive new observation creates a successor and marks the old checkpoint superseded without rewriting its historical receipt.

Summary fields such as `INSUFFICIENT_EVIDENCE` or `CONTRADICTORY_REALITY` cannot override deterministic floors derived from complete, bound source findings. Unanimous independent contradictions can support a material state change without an opposing-source fork. Unknown or unavailable observations remain non-decisive and fail closed.

On source `386103fd…18f9cbf0`, a live checkpoint was supported before a declared time cutoff; later revalidation returned two independent contradictory observations, recorded `CONTRADICTION`, and created successor checkpoint 2 with predecessor 1. The prior remained in immutable history and the successor was `DISPUTED` and unusable. Exact transactions are listed in [EVIDENCE.md](EVIDENCE.md).
