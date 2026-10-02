# Semantic Delta Engine

Revalidation compares typed prior claim states and receipt facts with current independent observations. Model delta values are bounded to unchanged, cosmetic, minor, material, critical, contradiction, and unavailable classes. The contract controls successor creation, state, freshness, and lineage.

Each claim returns a typed semantic delta. Per-claim receipts retain prior/current state plus that delta. Deterministic rules override an underreported delta when the typed claim state changed, and mark a supported/contradicted flip as `CONTRADICTION`. When state is unchanged, the agreed claim-level semantic class is retained. Evidence hashes and typed deltas are included in state/evidence digests. Textual page differences alone do not constitute material change.

Insufficient evidence and external failure create nonfinal attempt receipts and preserve the prior finalized checkpoint. A decisive new observation creates a successor and marks the old checkpoint superseded without rewriting its historical receipt.
