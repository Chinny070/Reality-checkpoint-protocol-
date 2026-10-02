# Decision Record — Reality Checkpoint Protocol

## Fixed primitive

Reality Checkpoint Protocol (RCP) creates consensus-backed certificates of bounded external state from multiple independently observable sources, detects semantic change and source disagreement over time, composes child checkpoints under frozen deterministic rules, and exposes machine-readable state for other contracts.

## Owner-portfolio collision audit

The target GitHub repository was confirmed empty through its public page. A public web-index search for `Chinny070` plus GenLayer/Reality Checkpoint did not surface related projects, but the complete owner repository list could not be queried: authenticated GitHub API access is unavailable and direct outbound GitHub API sockets are blocked. Therefore this is a partial owner collision audit, not a claim that the owner's full portfolio was reviewed.

## Ecosystem collision audit

Reviewed current official GenLayer Web Access and Equivalence Principle documentation plus public GenLayer repositories surfaced by web search. GenLayer's own web-access guide explicitly discusses independent retrieval, multiple sources, provenance, rendering, and failure handling as contract design patterns ([Web Access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access), [Core Concepts: Web Data Access](https://docs.genlayer.com/understand-genlayer-protocol/core-concepts/web-data-access)). These are capabilities and patterns, not a packaged RCP contract.

Closest public implementations reviewed:

- [GenLayer Intelligent Oracle](https://github.com/genlayerlabs/intelligent-oracle): prediction-market oracle that resolves natural-language market questions against live web evidence. It is the closest product-level collision. RCP differs by making reusable checkpoint definitions, per-claim graph policy, independence floors, fork preservation, freshness, delta receipts, challenge/revalidation lineage, deterministic composition, and a portable consumer certificate the core contract surface.
- [AI Bounty Verifier](https://github.com/dimsky131/genlayer-ai-bounty-verifier): consensus-based completion evidence adjudication, usually around a submitted evidence URL and a bounty verdict. RCP represents continuing external state over time rather than completion of one task.
- [ClauseFlow](https://github.com/tanphung/ClauseFlow): validator-reviewed immutable delivery evidence for service agreements with deterministic escrow settlement. RCP has no agreement or funds workflow; its output is a broadly consumable state certificate.
- [internetcourt](https://github.com/genlayer-foundation/internetcourt): cross-chain agent dispute resolution over submitted evidence with an AI jury and escrow. RCP is a source-observation and state-revalidation primitive rather than a dispute court.

This search is not exhaustive across all GenLayer submissions or repositories. It supports a bounded differentiation claim; it does not establish novelty or exclusivity.

## Closest primitives and differentiation

| Primitive | Core question | RCP distinction |
|---|---|---|
| Provenance Engine | What is the evidence identity/authenticity/history? | What external state is defensible now, do independent sources agree, and how did state change? |
| Decision Memory Protocol | Can an old decision still be relied on? | What is the current externally evidenced state, how fresh is it, and what changed from the prior checkpoint? |
| Historical Truth Reconstruction | What was true at time T? | Forward-going live observation and successor checkpoints with freshness and current usability. |
| Generic oracle / Intelligent Oracle | What value or market outcome follows from external sources? | An append-only state history with explicit claim policy, independence, forks, semantic drift, deterministic composition, freshness, and a portable certificate. |

## Three-consumer proof

1. **Provider launch gate:** compose service operation, region support, and policy permission checkpoints before a deployment contract accepts a provider.
2. **Real-world milestone settlement:** use claims about independently evidenced event completion and dispute status to gate a downstream settlement contract.
3. **Agent/tool authorization:** combine live security posture, terms, incident state, and behavior conformance into a fresh certificate consumed by a permissions contract.

These are different consumers of the same reusable state-certificate interface, not three user interfaces for one application.

## Delete-GenLayer answer

Without GenLayer, one backend operator chooses the sources, performs the semantic comparison, determines source independence, decides whether change is material, and authors the final state. With GenLayer, each validator independently retrieves evidence and classifies decision-critical meaning; consensus checks the leader proposal. Deterministic code controls thresholds, freshness, lineage, usability, and composition.

## Hardest implementation risk

The hardest risk is obtaining stable substantive agreement from independently rendered, dynamic pages while keeping source-independence classification honest. The contract therefore compares typed claim/source relationship fields and does not require identical prose or rendered HTML hashes.

## Status and limits

The local GenVM static validation passed for the current candidate; no live Studionet consensus or deployment has been performed. This is not an exhaustive novelty or owner-portfolio finding. See `SUBMISSION.md` for external gates.
