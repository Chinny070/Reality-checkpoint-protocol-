# Decision Record — Reality Checkpoint Protocol

## Fixed primitive

Reality Checkpoint Protocol (RCP) creates consensus-backed certificates of bounded external state from multiple independently observable sources, detects semantic change and source disagreement over time, composes child checkpoints under frozen deterministic rules, and exposes machine-readable state for other contracts.

## Owner-portfolio collision audit

On 2026-10-03, the public GitHub REST API returned 51 repositories for Chinny070, including this now-populated target repository. I reviewed the full returned names/descriptions and read the README files for the closest seven adjacent projects: RenderWitness, DRIFT, Decision Memory Protocol, Continuum Protocol, Contradiction Protocol, ProofMesh, and Provenance Engine. This is a public portfolio audit of the API-visible list, not an assertion about private or unlisted work.

The closest overlap is **[Decision Memory Protocol](https://github.com/Chinny070/Decision-memory-protocol-)**: it also offers multi-source web evidence, semantic revalidation, immutable successors, challenges, dependencies, and a reusable reliance certificate. The distinction is the primary state object and consumer question. Decision Memory asks whether a frozen past decision remains reliable as assumptions change; RCP asks what bounded external state is currently supported, contradicted, forked, stale, or composable. The interfaces and state policy are related enough that RCP must not claim an uncontested general “evidence-backed reliance certificate” category. RCP's distinct center is its State Claim Graph, per-claim/source findings, domain-cluster evidence floor, explicit opposing-reality fork, freshness half-life, deterministic child-checkpoint composition, and portable snapshot certificate.

**[RenderWitness](https://github.com/Chinny070/RenderWitness)** overlaps direct rendered-web claim verification and challenge, but centers on proof of a webpage's current content and verdict. RCP generalizes beyond one rendered page to bounded claims over multiple retrieval types/sources, source-independence clusters, temporal successor receipts, and composite state certificates. **[DRIFT](https://github.com/Chinny070/DRIFT)** overlaps temporal semantic comparison but focuses on changes to public commitments and policy language (e.g. weakened or removed obligations); RCP tracks typed external-state findings, including unchanged, contradicted, unavailable, or divergent evidence. **[ProofMesh](https://github.com/Chinny070/proofmesh)** overlaps multi-source independence and conflict handling for public identity claims; its output is an identity/trust credential rather than a general current-state checkpoint. **[Provenance Engine](https://github.com/Chinny070/provenanceengine)** overlaps immutable evidence history, content/render hashes, source relations, and conflict status; it records claim/evidence provenance and evolution rather than composable multi-claim state snapshots with freshness policy. [Continuum Protocol](https://github.com/Chinny070/continuum-protocol), [Contradiction Protocol](https://github.com/Chinny070/contradiction-protocol), and [AgentCourt](https://github.com/Chinny070/agentcourt) address impact rewards or agreement/dispute workflows rather than a general state certificate.

This is a candid scope differentiation, not a novelty proof. The substantial Decision Memory overlap is a rejection risk; RCP should be judged on the coherent distinct state/fork/composition surface, not a broad assertion that it is the only protocol for evidence, revalidation, or certificates.

## Ecosystem collision audit

Reviewed current official GenLayer Web Access and Equivalence Principle documentation plus public GenLayer repositories surfaced by web search. GenLayer's own web-access guide explicitly discusses independent retrieval, multiple sources, provenance, rendering, and failure handling as contract design patterns ([Web Access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access), [Core Concepts: Web Data Access](https://docs.genlayer.com/understand-genlayer-protocol/core-concepts/web-data-access)). These are capabilities and patterns, not a packaged RCP contract.

Closest public implementations reviewed:

- [GenLayer Intelligent Oracle](https://github.com/genlayerlabs/intelligent-oracle): prediction-market oracle that resolves natural-language market questions against live web evidence. It is the closest product-level collision. RCP differs by making reusable checkpoint definitions, per-claim graph policy, independence floors, fork preservation, freshness, delta receipts, challenge/revalidation lineage, deterministic composition, and a portable consumer certificate the core contract surface.
- [AI Bounty Verifier](https://github.com/dimsky131/genlayer-ai-bounty-verifier): consensus-based completion evidence adjudication, usually around a submitted evidence URL and a bounty verdict. RCP represents continuing external state over time rather than completion of one task.
- [ClauseFlow](https://github.com/tanphung/ClauseFlow): validator-reviewed immutable delivery evidence for service agreements with deterministic escrow settlement. RCP has no agreement or funds workflow; its output is a broadly consumable state certificate.
- [internetcourt](https://github.com/genlayer-foundation/internetcourt): cross-chain agent dispute resolution over submitted evidence with an AI jury and escrow. RCP is a source-observation and state-revalidation primitive rather than a dispute court.

This search is not exhaustive across all GenLayer submissions or repositories. It supports a bounded differentiation claim; it does not establish novelty or exclusivity.

Additional public ecosystem projects reviewed include [Lumen](https://github.com/ldkfj/Lumen), an evidence-bound registry checking public AI performance claims against a fixed benchmark record; [GenLayer Intelligent Oracle](https://github.com/genlayerlabs/intelligent-oracle), a prediction-market resolution application; and [internetcourt](https://github.com/genlayer-foundation/internetcourt), a cross-chain evidence dispute and escrow workflow. Their unit of decision is respectively a scoped benchmark claim, a market outcome, and a submitted dispute. RCP's center is an evolving, multi-claim state graph with independent-source floors, typed forks, semantic successor receipts, deterministic composition, freshness, and a portable certificate. This is a feature-level differentiation assessment based on public descriptions, not an implementation-level exhaustive audit.

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

The current challenge contract preserves the parent and does not spend a challenge round when supplemental evidence is unavailable or fails the validator-agreed independence/floor checks. An initial `INCONCLUSIVE` or `UNAVAILABLE` result is intentionally terminal for that checkpoint ID; callers retry by creating a new checkpoint, preserving the original failed attempt as immutable history. Live challenge recovery on earlier source versions does not prove recovery of an initial failure, and is not claimed as such. Local and live status for this corrected source is recorded only after its own verification in `docs/EVIDENCE.md` and `docs/RELEASE_VERIFICATION.md`.
