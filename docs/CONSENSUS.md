# Consensus Design

## Decision boundary

Nondeterministic consensus classifies source meaning and claim states. Deterministic contract code validates the bounded shape, enforces independence floors, derives state and divergence, applies freshness, records receipts, allocates IDs, maintains lineage, composes children, and determines usability.

## Leader

The leader reads a frozen copy of the claim/source definition, retrieves each declared source once, records retrieval kind and evidence hashes, then asks the model for a bounded JSON classification. Retrieved content is explicitly framed as hostile data and has no instruction authority.

## Validator

`gl.vm.run_nondet(leader, validator)` invokes an independent validator path. It independently retrieves the sources and re-runs the typed classification. The validator rejects unknown/forged IDs and malformed decision fields, then compares normalized claim state, per-source findings, source relationship, deterministic domain cluster, divergence, delta, failure status, and every evidence-receipt fact. Receipt source ID, URL, retrieval kind, render/content hashes, normalization version, and observation status must exactly match the validator's own fetch. Missing, extra, malformed, or changed receipt data fails equivalence. Missing source findings are inserted as `UNKNOWN` and force the affected claim to `UNKNOWN`; they cannot be omitted to claim support or hide a fork. Confirmed retrieval failures are then deterministically marked `UNAVAILABLE`. The model's arbitrary cluster labels are discarded. Rationale prose is discarded. Dynamic pages can therefore fail closed when they change between leader and validator retrieval.

## Equivalence

The agreement test is strict on the small decision fields that affect protocol state. It allows no equivalence between supported and contradicted claims, consistent and contradictory reality, sufficient and insufficient independence, no-change and critical-change, or reachable and unreachable when reachability is encoded as a claim.

## Evidence snapshot

Each validator execution performs one retrieval per source, normalizes that result once, and classifies from the same captured content. Browser-rendered sources use the current SDK `gl.nondet.web.render(url, mode="text"|"html")`; direct fetch uses `gl.nondet.web.get`. Render-backed evidence is labeled accordingly; raw fetches are never represented as browser-render proof.

## Errors

Transport/render exceptions become source-level unavailable evidence. An external-failure proposal cannot become positive or contradictory state. GenLayer transaction errors remain distinct from protocol-level `INCONCLUSIVE` and `UNAVAILABLE` outcomes.

## Current limitation

Direct Mode, pickling, GenVM lint, schema, and local semantic validation have passed for this candidate. The live deployment and transaction evidence are recorded in `RELEASE_VERIFICATION.md`; deployment finality and contract execution success are checked separately because the CLI success banner alone is insufficient.
