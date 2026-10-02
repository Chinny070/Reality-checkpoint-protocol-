# Protocol Invariants

- **RC1 — Finalized immutability:** finalized definition, source set, state digest, certificate fingerprint, and evidence receipt are never rewritten. Changes create successors; creating a composite does not mutate its children.
- **RC2 — Independent observation:** the leader and each validator execute retrieval/classification independently for decision-critical evidence.
- **RC3 — Model boundary:** model output is limited to typed claim states, source relationship classifications, divergence, and semantic delta. It cannot choose IDs, hashes, timestamps, thresholds, freshness, lineage, or usability.
- **RC4 — Deterministic usability:** only contract logic derives usability from finalized status, supported state, allowed divergence, freshness, and successor status.
- **RC5 — Failure separation:** retrieval failure is unavailable/inconclusive, never contradiction or support.
- **RC6 — Independence honesty:** URLs do not count as independent clusters unless validators classify them as independent; deterministic code counts unique clusters.
- **RC7 — Reality fork preservation:** opposite supported/contradicted source findings force `DISPUTED` regardless of the model's divergence label.
- **RC8 — Composition determinism:** composite state derives from child certificates and fixed policy fields.
- **RC9 — Cycle freedom:** claim dependencies and composite ancestry are bounded and cycle-checked.
- **RC10 — Bounded work:** definitions, strings, claims, sources, composition depth/width, page sizes, and decisive or inconclusive challenge attempts have explicit caps.
- **RC11 — Lineage integrity:** successor creation marks the prior checkpoint superseded but does not change its receipt or state digest.
- **RC12 — Freshness honesty:** timestamps and windows are deterministic; a fresh contradiction remains a contradiction.
- **RC13 — Challenge immutability:** a challenge creates a new consensus observation and, when decisive, a successor; it never rewrites the challenged receipt.
- **RC14 — Evidence identity separation:** evidence IDs/hashes are deterministic and exclude free-form model rationale.
- **RC15 — Protocol uncertainty separation:** an inconclusive attempt records an attempt receipt and preserves the prior finalized checkpoint.
