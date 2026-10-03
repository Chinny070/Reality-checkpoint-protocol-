# Checkpoint Composition

Composites accept 2–8 finalized children, a critical-child set, a maximum degraded-child count, a freshness requirement, and a divergence tolerance. Composite state is derived in contract code; the model is not asked to decide a composite.

- A critical child that is blocked, disputed, inconclusive, unavailable, or stale blocks the composite.
- Disallowed child divergence rejects composition.
- Noncritical degraded/nonusable children consume the frozen degradation allowance.
- Composite expiry is the earliest child expiry.
- Parent ancestry is bounded to eight levels and checked to prevent cycles.

The same child certificate is immutable; composition records only its references and deterministic digest. On historical source `386103fd…18f9cbf0`, live composition checkpoint 6 used finalized supported children `[4,5]`, returned `SUPPORTED` / `CONSISTENT`, was fresh and usable, and exposed ancestors `[4,5]`. A separate live attempt to reference future/self ID 8 while only seven checkpoints existed finalized with `checkpoint not found`; no state was created or changed. Composition can reference only already-finalized children and stores an append-only forward DAG, preventing future references from adding a back-edge. This is not asserted as a proof for the corrected source. See [EVIDENCE.md](EVIDENCE.md) for transaction IDs.
