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
- Direct Mode: 17 passed, 0 failed.
- Protocol helper/adversarial logic tests: 23 passed, 0 failed.
- GenVM AST lint: passed (3 checks; `genvm-lint` 0.11.0).
- GenVM SDK semantic validation: passed with GenVM v0.2.16.
- Schema: extracted; 10 methods (5 read-only, 5 write).
- Direct Mode pickling check: included and passed.
- Current source `386103fd…18f9cbf0` is deployed with byte-identical parity. On this exact source, live semantic revalidation created a contradiction successor, unavailable challenge preserved its parent, render retrievals were recorded (WHO claim UNKNOWN), composition was fresh/usable, and a reality fork was disputed/unusable. Exact proof bounds and transaction evidence are in `docs/EVIDENCE.md`.

## Remaining review limits

- Latest documentation and helper changes are pushed to GitHub `main`; the final remote-head SHA is verified in the release verification record.
- Live future/self reference rejection finalized with `checkpoint not found`; immutable finalized-child DAG prevents back-edge insertion. On current source, an unavailable challenge preserved checkpoint 8 and a valid retry created supported successor 9, FRESH and usable.
- Owner-portfolio audit: reviewed all 51 public API-visible repositories (names/descriptions) and README-level detail for the seven closest overlaps. Decision Memory Protocol is the closest neighboring project; see `DECISION.md` for the substantive scope distinction and explicit rejection risk.
- Ecosystem collision search: compared current official GenLayer docs and several public projects, including Intelligent Oracle, Lumen, and Internetcourt. This is a bounded collision assessment, not a novelty guarantee or coverage of private/unindexed projects.

## Evidence fields

- Repository: https://github.com/Chinny070/Reality-checkpoint-protocol-
- Canonical contract: `contracts/reality_checkpoint.py`
- Contract SHA-256: recorded in `docs/RELEASE_VERIFICATION.md` for the locally verified source.
- Local commit and blob IDs: recorded in `docs/RELEASE_VERIFICATION.md`.
- Contract address / Explorer / deployment transaction / finality / source parity: recorded in `docs/RELEASE_VERIFICATION.md`.

Only the specific live passes listed in `docs/EVIDENCE.md` are claimed. The required local, deployment, source-parity, live protocol, public owner-audit, and GitHub push gates are verified. The live WEB_RENDER_TEXT transaction observed both pages, but the WHO claim resolved UNKNOWN; this is recorded as a limitation rather than a supported fact. The closest portfolio collision is Decision Memory Protocol and is candidly differentiated in `DECISION.md`.

## Portal description draft (verified local facts only)

Reality Checkpoint Protocol is a reusable GenLayer contract for consensus-backed certificates of bounded external state. Validators independently render or fetch evidence and classify claim states, source relationships, divergence, and semantic changes. Deterministic code enforces claim/source bounds, independence floors, freshness, immutable lineage, challenges, composition, and consumer usability. It exposes portable certificates for unrelated downstream contracts. Local verification: 17 Direct Mode tests and 23 protocol/adversarial tests passed; GenVM lint (3 checks), schema extraction (10 methods), and SDK semantic validation passed. Current source `386103fd…18f9cbf0` is deployed and parity-verified. Source-specific live evidence is summarized in `docs/EVIDENCE.md`.
