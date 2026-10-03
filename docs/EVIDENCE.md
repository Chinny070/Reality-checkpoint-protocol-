# Evidence and Receipt Model

Each source observation is bound to checkpoint and source definitions, retrieval kind, normalized content hash, render hash (or all-zero value for non-render retrieval), normalization version, and observation status. Evidence identity excludes model rationale.

Dynamic rendered content is not compared by byte equality between validators. Each validator extracts and classifies typed facts independently; consensus compares normalized facts and decision-critical states.

Transport/render failure creates an explicit external-failure observation. It must never be re-labeled as a contradiction or as support. Receipts preserve source/claim deltas and evidence root so consumers can audit the reason for a state transition.

## Studionet verification record (2026-10-02)

These transactions were run against source hash `dcf3c321b8d598e24d2d91f6a7c4aae9e0cfd272563dcaf15eb3789e79d4fda7`, which matched the deployed bytes. They remain valid evidence for that exact source version. A later transaction exposed a missing-model-finding execution error; the corrected candidate has SHA-256 `fd0969dc0d7b1d9df4b13be0c5de65c91757d5edece3884c6f15f61c4b29f7e2` and must be redeployed and live-verified before these results are attributed to it.

Contract used for the successful fork/render transactions: `0x69570326e3120c2b9EB96Cc471b235b6adE91501`.

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

The later diagnostic deployment `0xB9f9e09571679e719184b751baf600dec9d5841B` used the same previous source. Its initial rendered resolution `0x3d1106cd30d71883a61cff2a39823aef3f4faf5b057edeeb5476eb226ab7e471` is `UNDETERMINED`: Explorer shows GenVM `ERROR`, traceback `ValueError: incomplete source findings`. The validator/model omitted a source finding. The corrected code fills omissions as `UNKNOWN` and makes the aggregate claim `UNKNOWN`, which fails closed without turning expected model variability into a contract runtime exception. The fix is locally tested but not yet deployed.

## Corrected deployed source `fd0969dc…f7e2`

- Deployment: `0x743d95c1b06d18ff885461f36ee9bb989a6e65b7087c753789c93ccda576cf17`; address `0xdF1BF015f0d6a136Fc8c89020e1F9D122e9aDaEf`; FINALIZED, GenVM SUCCESS, MAJORITY_AGREE. GenLayer CLI code retrieval matched the deployed bytes exactly, and the live schema exposed 10 expected methods.
- Matching echo checkpoint 2: create `0xbee4150194ff345c8b36120c7ae874e70e31edcb6df28bff2d633021ec38eb11`; resolve `0xd5c38ff421cbfd650c417f1024e4791fbfa5f46b9855173553857326a2a819bc`. Both Postman and HTTPBin returned `foo1=Hello`, each classified `SUPPORTED`, with independent domain clusters. Finalized `SUPPORTED` / `CONSISTENT`.
- No-change revalidation: `0xd6d91b8c446817bf52f0b6e77e823538248c798445db3d077b55d46f4fbe3878`. Finalized `UNCHANGED`, created successor checkpoint 3 (predecessor 2), and retained both SUPPORTED findings.
- Second echo checkpoint 4: create `0xe510d1f99395fd41182307e72c06571e768777b5d9d07fbfdfcaaf3ce759fd16`; resolve `0xb5ceccf6506db2b4fa21f9d101782eb5e1af8fe4195da4046f0940f982e54688`; both sources SUPPORTED.
- Composition checkpoint 5: transaction `0x276905036761a8773a0147511ab6af1814c50c0377cc28da2d63022133dedb24`. Finalized `SUPPORTED` / `CONSISTENT`, child list `[3,4]`, `FRESH`, `is_checkpoint_usable=true`. Certificate fingerprint `33ceae01917dde17af9161d3c58bb7ffee442af23e7e36377cb1c77bc8016ab6`.
- Fork checkpoint 6: create `0xbc605065d4545470b02a78e56de4067e6e28bcc6d3a1755c43959ac2e5a11dab`; resolve `0xe83e278319e95b9890bc799b6c58d7a10636dc2fc0522c9333dcea799ebd650f`. Postman was SUPPORTED; HTTPBin was CONTRADICTED; result `DISPUTED` / `CONTRADICTORY_REALITY`, certificate FRESH, `is_checkpoint_usable=false`. Explorer: <https://explorer-studio.genlayer.com/tx/0xe83e278319e95b9890bc799b6c58d7a10636dc2fc0522c9333dcea799ebd650f>.
- Unavailable challenge against checkpoint 3: transaction `0x7bba240a174fa8beeba606bbdcff3062ee822a552b9dbe35331c31710f33981e`, FINALIZED; return `PRESERVED_PRIOR`, attempt receipt 5; source at `.invalid` was `EXTERNAL_FAILURE`, attempt `UNAVAILABLE`, and checkpoint 3 remained FINALIZED/usable. The attempt receipt revealed the appended source had empty `claim_ids`; the current local candidate fixes this and must be redeployed and re-proven.
- Time-bound semantic-delta attempt: checkpoint 7 resolved initially as SUPPORTED. Revalidation tx `0x5822d463ecc56d93b2cb67deeb399e0cab5d96103c5ede6bc99131f4f9998764` became UNDETERMINED after validators disagreed. No live material-delta pass is claimed.

## Current source `450dd5c8…56df7`

- Deployment tx `0x6ce1ef5652140bcb0aa34503b95c0a46be702e3642fbd7cdc664f4349ec56490`; address `0x91d0F2b43E79666c49c0000b15b98630c6Fc64Fc`; FINALIZED, GenVM SUCCESS, MAJORITY_AGREE.
- CLI-retrieved deployed source is byte-identical to `contracts/reality_checkpoint.py`, SHA-256 `450dd5c8c25d22e9ac9922df25f3f2c454015171bab643a9b653cda209156df7`; schema has the expected 10 methods.
- Supported checkpoint creation tx `0xfb18bf5fb8055f09e51a656c6e93b70c0faf8735ca9ac8cebcce712582b936af`; resolution `0x33c55f4c2681df36e42a2530d6a42b586a982e7b3c6fc59f4a3f71c019c196a8`; finalized SUPPORTED / CONSISTENT based on two independent echo endpoints.
- Unavailable-source challenge tx `0xd1dfb3b11ed349107aa60bcf21796d89a2100b3b53536878a19466dc6621b94b`; finalized `PRESERVED_PRIOR`; attempt receipt 2 is UNAVAILABLE / EXTERNAL_FAILURE and its source S3 evidence receipt has `claim_ids:["C1"]`, `observation_status:EXTERNAL_FAILURE`. Checkpoint 1 remains FINALIZED/SUPPORTED with the original two-source definition.

The live material-delta attempt against the previous source was UNDETERMINED after validator disagreement; no material-change PASS is claimed for this source.
