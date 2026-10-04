# Submission Status

## Positioning

**Reality Checkpoint Protocol — Consensus-backed certificates for external state.**

- Category: standalone reusable GenLayer Intelligent Contract.
- One-line thesis: consensus-backed certificates for bounded external state, with semantic drift, reality forks, composition, freshness, and immutable lineage.
- Repository: https://github.com/Chinny070/Reality-checkpoint-protocol-

RCP creates bounded state claims from independently observable evidence, uses GenLayer validators to independently classify meaning and source relationships, and derives freshness, divergence, lineage, composition, and consumer usability deterministically.

## Why GenLayer and system boundary

Ordinary deterministic contracts cannot independently render public pages, interpret natural-language claims, determine whether apparently separate publishers are syndicated, or compare semantic meaning across changing sources. In `gl.vm.run_nondet`, the leader and validator independently observe the same bounded source set and agree on typed claim states, source relationships, divergence, and semantic deltas. The deterministic contract validates the shape and bounds, allocates IDs and timestamps, applies independence/freshness/composition policies, records append-only receipts, and decides usability. Retrieval or consensus failures are `UNAVAILABLE`/`INCONCLUSIVE`; they do not prove a contradiction and do not erase a prior finalized checkpoint.

## Reuse surface and limits

Downstream contracts consume `get_certificate` and `is_checkpoint_usable`; provider admission, milestone settlement, and tool authorization are three distinct examples. The certificate covers only its bounded claim graph, sources, and validity window. Source-independence classification is validator judgment, not cryptographic proof. Owner-portfolio and ecosystem novelty searches are not exhaustive.

## Verified local gates

- Python syntax compilation: passed for contract and both test modules.
- Direct Mode: 21 passed, 0 failed. The added regression persists an admitted supplemental source for C1 while C2 remains unresolved, then proves persisted inconclusive attempts are capped.
- Protocol helper/adversarial logic tests: 27 passed, 0 failed.
- GenVM AST lint: passed (3 checks; `genvm-lint` 0.11.0).
- GenVM SDK semantic validation: passed with GenVM v0.2.16.
- Schema: extracted; 10 methods (5 read-only, 5 write).
- Direct Mode pickling check: included and passed.
- The steward-fix source `26ca41afe295bdacfded56976d99dfde3839a62d150c5b6a35e88f645740f1ee` passes all local gates at commit `cae50240f47e6e035fa577b122aad93b9c4f0fbf`. It is not yet deployed or source-parity verified. The previous deployed source remains `2ca8e459…788a37d` at `0xbEFbE69a1723E637691a7c2De76b5d01D81a41A2`; its live proofs must not be attributed to this steward-fix candidate. Deployment is waiting on Studionet wallet unlock and source-specific live proof.

## Remaining review limits

- The steward-fix candidate and updated release records are not yet pushed.
- A cross-domain hostile challenge attempt finalized MAJORITY_DISAGREE; it is explicitly excluded from passing evidence. The live same-domain challenge rejection passed.
- Owner-portfolio audit: reviewed all 51 public API-visible repositories (names/descriptions) and README-level detail for the seven closest overlaps. Decision Memory Protocol is the closest neighboring project; see `DECISION.md` for the substantive scope distinction and explicit rejection risk.
- Ecosystem collision search: compared current official GenLayer docs and several public projects, including Intelligent Oracle, Lumen, and Internetcourt. This is a bounded collision assessment, not a novelty guarantee or coverage of private/unindexed projects.

## Evidence fields

- Repository: https://github.com/Chinny070/Reality-checkpoint-protocol-
- Canonical contract: `contracts/reality_checkpoint.py`
- Contract SHA-256: recorded in `docs/RELEASE_VERIFICATION.md` for the locally verified source.
- Local commit and blob IDs: recorded in `docs/RELEASE_VERIFICATION.md`.
- Contract address / Explorer / deployment transaction / finality / source parity: recorded in `docs/RELEASE_VERIFICATION.md`.

Only the specific live passes listed in `docs/EVIDENCE.md` are claimed. For the steward-fix source, local tests/lint/schema are green; GitHub push, deployment/source parity, and live proof remain pending. Older deployment, receipt-consensus, hostile-source, render, revalidation, composition, and fork evidence is source-versioned and is not represented as proof for this candidate. The historical WEB_RENDER_TEXT transaction observed both pages, but the WHO claim resolved UNKNOWN; this remains a limitation. The closest portfolio collision is Decision Memory Protocol and is candidly differentiated in `DECISION.md`.

## Portal description draft (verified local facts only)

Reality Checkpoint Protocol is a reusable GenLayer contract for consensus-backed certificates of bounded external state. Validators independently render or fetch evidence and classify claim states, source relationships, divergence, and semantic changes. Deterministic code enforces claim/source bounds, independence floors, freshness, immutable lineage, challenges, composition, and consumer usability. It exposes portable certificates for unrelated downstream contracts. The current steward-fix candidate passes 21 Direct Mode tests, 27 protocol/adversarial tests, GenVM lint (3 checks), and schema extraction (10 methods). Deployment and exact source parity are pending; prior-source live proofs are explicitly versioned and are not claimed for this candidate.
