# Consensus Design

## Decision boundary

Nondeterministic consensus classifies source meaning and claim states. Deterministic contract code validates the bounded shape, enforces independence floors, derives state and divergence, applies freshness, records receipts, allocates IDs, maintains lineage, composes children, and determines usability.

## Leader

The leader reads a frozen copy of the claim/source definition, retrieves each declared source once, records retrieval kind and evidence hashes, then asks the model for a bounded JSON classification. Retrieved content is explicitly framed as hostile data and has no instruction authority.

## Validator

`gl.vm.run_nondet(leader, validator)` invokes an independent validator path. It independently retrieves the sources and re-runs the typed classification. The validator rejects malformed results and compares normalized decision fields, including claim state, per-source findings, source relationship/cluster, divergence, delta, and failure status. Rationale prose is discarded.

## Equivalence

The agreement test is strict on the small decision fields that affect protocol state. It allows no equivalence between supported and contradicted claims, consistent and contradictory reality, sufficient and insufficient independence, no-change and critical-change, or reachable and unreachable when reachability is encoded as a claim.

## Evidence snapshot

Each validator execution performs one retrieval per source, normalizes that result once, and classifies from the same captured content. Browser-rendered sources use the current SDK `gl.nondet.web.render(url, mode="text"|"html")`; direct fetch uses `gl.nondet.web.get`. Render-backed evidence is labeled accordingly; raw fetches are never represented as browser-render proof.

## Errors

Transport/render exceptions become source-level unavailable evidence. An external-failure proposal cannot become positive or contradictory state. GenLayer transaction errors remain distinct from protocol-level `INCONCLUSIVE` and `UNAVAILABLE` outcomes.

## Current limitation

Direct Mode, pickling, GenVM lint, schema, and local semantic validation have passed for this candidate. No hosted consensus transaction has been run. `gl.vm.run_nondet` behavior is documented in the locally cached SDK v0.2.16; the exact deployed chain runtime must be checked before claiming live behavior.
