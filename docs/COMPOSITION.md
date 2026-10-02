# Checkpoint Composition

Composites accept 2–8 finalized children, a critical-child set, a maximum degraded-child count, a freshness requirement, and a divergence tolerance. Composite state is derived in contract code; the model is not asked to decide a composite.

- A critical child that is blocked, disputed, inconclusive, unavailable, or stale blocks the composite.
- Disallowed child divergence rejects composition.
- Noncritical degraded/nonusable children consume the frozen degradation allowance.
- Composite expiry is the earliest child expiry.
- Parent ancestry is bounded to eight levels and checked to prevent cycles.

The same child certificate is immutable; composition records only its references and deterministic digest.
