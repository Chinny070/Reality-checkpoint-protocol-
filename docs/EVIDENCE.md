# Evidence and Receipt Model

Each source observation is bound to checkpoint and source definitions, retrieval kind, normalized content hash, render hash (or all-zero value for non-render retrieval), normalization version, and observation status. Evidence identity excludes model rationale.

Dynamic rendered content is not compared by byte equality between validators. Each validator extracts and classifies typed facts independently; consensus compares normalized facts and decision-critical states.

Transport/render failure creates an explicit external-failure observation. It must never be re-labeled as a contradiction or as support. Receipts preserve source/claim deltas and evidence root so consumers can audit the reason for a state transition.

## Studionet verification record (2026-10-02)

Canonical contract: `0x69570326e3120c2b9EB96Cc471b235b6adE91501`.

### Initial live render

- Checkpoint creation tx: `0x116785b528e523908d9e7ade567baf2d14d5f5632de77ee7879d759bf497ffda` (checkpoint ID 2, finalized).
- Resolution tx: `0x7799c664640f661294de744ab4dfe09c9dc545436de47cd45c394bbebdb9a390` (finalized, GenVM success, `MAJORITY_AGREE`).
- WHO `WEB_RENDER_TEXT`: `https://www.who.int/about/who-we-are`; observation `OBSERVED`; content and render SHA-256 `f60fe91a4a6211e0644d9dd232c680c4898190ee65b834c4c8eec2932cb87f2e`.
- Example.com `WEB_RENDER_TEXT`: `https://example.com/`; observation `OBSERVED`; content and render SHA-256 `aa8c4320fabb468930b605f5f365b1beaf2ac42b081eed50083e26d26cb3c159`.
- Both claims were `SUPPORTED` on the initial observation, relationships `INDEPENDENT`, divergence `CONSISTENT`, and the source response declared no external failure.
- The leader receipt returned checkpoint 2 `FINALIZED` and receipt 2. Explorer: <https://explorer-studio.genlayer.com/tx/0x7799c664640f661294de744ab4dfe09c9dc545436de47cd45c394bbebdb9a390>.

### Revalidation boundary

- Revalidation tx: `0xbaffa0523d997fe27d49d73630e222d9fdf78693a329b301f504b547cb486abf` (finalized, `MAJORITY_AGREE`).
- `overall_delta=UNCHANGED`, evidence hashes unchanged, example.com remained `SUPPORTED`, but WHO became `UNKNOWN`.
- Contract output was `PRESERVED_PRIOR`, attempt receipt 3. It did not create a successor; do not describe this as a successful no-change revalidation proof.
- Explorer: <https://explorer-studio.genlayer.com/tx/0xbaffa0523d997fe27d49d73630e222d9fdf78693a329b301f504b547cb486abf>.

### Reality-fork proof

- Checkpoint creation tx: `0x4d8458b6482e4bdfb1eb131464ee6546ddd3e7265f2850ce052358fe6d4dd0d1` (checkpoint ID 1, finalized).
- Resolution tx: `0x529de2378dcb5364700a1abc5171f95c9861ba238caff2752e0950296a3be60a` (finalized, `MAJORITY_AGREE`, leader GenVM success).
- Sources: `https://postman-echo.com/get?foo1=Hello` and `https://httpbin.org/get?foo1=World`, both fetched with `WEB_GET_TEXT`, separate registrable-domain clusters, no external failure.
- The source findings were respectively `SUPPORTED` and `CONTRADICTED`; contract result was `DISPUTED` / `CONTRADICTORY_REALITY`. Portable certificate was `FRESH`; `is_checkpoint_usable(1)` returned `false`.
- Evidence content hashes: Postman `515bbcf3f68a6d70cd49651cfbad5a47594e73bf8d1f45dec8ba37d2481cfdae`; HTTPBin `cbde950e1e94443610032a791bfac168318b5a361038284e0c02ef4e8f8b8bca`.
- Explorer: <https://explorer-studio.genlayer.com/tx/0x529de2378dcb5364700a1abc5171f95c9861ba238caff2752e0950296a3be60a>.

### Out-of-scope failed transaction

An extra resolution transaction `0x06be77c3e1ba498655e7a3951808a7a85c49000d84700acfddb845b600f9d537` targeted checkpoint ID 6 instead of the newly created ID 1. It finalized with `checkpoint not found`; it is a test-driver argument error, not evidence of successful execution or a contract defect. The correctly addressed ID 1 transaction above passed.
