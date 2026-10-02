# Evidence and Receipt Model

Each source observation is bound to checkpoint and source definitions, retrieval kind, normalized content hash, render hash (or all-zero value for non-render retrieval), normalization version, and observation status. Evidence identity excludes model rationale.

Dynamic rendered content is not compared by byte equality between validators. Each validator extracts and classifies typed facts independently; consensus compares normalized facts and decision-critical states.

Transport/render failure creates an explicit external-failure observation. It must never be re-labeled as a contradiction or as support. Receipts preserve source/claim deltas and evidence root so consumers can audit the reason for a state transition.

**No live evidence transaction has yet been run.** This document describes the candidate evidence path, not a claim that real Studionet retrieval has been proven.
