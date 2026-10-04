# Evidence and Receipt Model

## Steward-requested persisted-attempt bound (2026-10-04)

The current local candidate (`contracts/reality_checkpoint.py`, SHA-256 `26ca41afe295bdacfded56976d99dfde3839a62d150c5b6a35e88f645740f1ee`) increments a per-checkpoint challenge-attempt counter whenever it persists a nonfinal challenge receipt. This includes the case where an added source is admitted for the challenged claim but another claim leaves the overall result inconclusive. After three persisted inconclusive attempts, a further attempt reverts before storage. A supplemental source rejected for domain, availability, independence, claim-binding, or floor reasons still writes no receipt and consumes no attempt.

Direct Mode regression: `test_admitted_supplemental_source_with_unresolved_claim_persists_and_consumes_bounded_attempt` passes. It verifies S3 is claim-bound to C1 in the persisted receipt while C2 remains unresolved, the prior checkpoint digest and successor pointer are unchanged, and the persisted-attempt bound is enforced. This is local evidence only. The Studionet deployment command for this source reached wallet decryption and reported `Invalid password. Attempt 2/3`; no new deployment or live proof is claimed yet.

Each source observation is bound to checkpoint and source definitions, retrieval kind, normalized content hash, render hash (or all-zero value for non-render retrieval), normalization version, and observation status. Evidence identity excludes model rationale.

Every validator independently retrieves evidence and compares receipt source binding, retrieval kind, render/content hashes, normalization version, and observation status against its own fetch before those hashes enter a consensus-bound evidence root. Dynamic content that changes between observations therefore fails equivalence. Classifier rationale is not part of evidence identity.

Transport/render failure creates an explicit external-failure observation. It must never be re-labeled as a contradiction or as support. Receipts preserve source/claim deltas and evidence root so consumers can audit the reason for a state transition.

## Studionet verification record (2026-10-02)

Transactions below are versioned evidence for the source hashes and addresses shown; none is proof for a later contract version. The currently corrected candidate requires its own deployment parity and live proofs before its behavior can be attributed to the network.

Contract used for the successful fork/render transactions: `0x69570326e3120c2b9EB96Cc471b235b6adE91501`.

### Initial live render

- Checkpoint creation tx: `0x116785b528e523908d9e7ade567baf2d14d5f5632de77ee7879d759bf497ffda` (checkpoint ID 2, finalized).
- Resolution tx: `0x7799c664640f661294de744ab4dfe09c9dc545436de47cd45c394bbebdb9a390` (finalized, GenVM success, `MAJORITY_AGREE`).
- WHO `WEB_RENDER_TEXT`: `https://www.who.int/about/who-we-are`; observation `OBSERVED`; content and render SHA-256 `f60fe91a4a6211e0644d9dd232c680c4898190ee65b834c4c8eec2932cb87f2e`.
- Example.com `WEB_RENDER_TEXT`: `https://example.com/`; observation `OBSERVED`; content and render SHA-256 `aa8c4320fabb468930b605f5f365b1beaf2ac42b081eed50083e26d26cb3c159`.
- Both claims were `SUPPORTED` on the initial observation, relationships `INDEPENDENT`, divergence `CONSISTENT`, and the source response declared no external failure.
- The leader receipt returned checkpoint 2 `FINALIZED` and receipt 2. Explorer: <https://explorer-studio.genlayer.com/tx/0x7799c664640f661294de744ab4dfe09c9dc545436de47cd45c394bbebdb9a390>.

## Corrected candidate: receipt binding and challenge admission (2026-10-03)

Contract SHA-256: `2ca8e45982d88184b845df6441a9e6c2667af9ecc2bed88754964d8bb788a37d`; Git blob `c7b915d9a137a25646b6ca4468f5cb154c371c2b`; source commit `66d87907b04ab8b7490ace2f02403be177350a98`. Studionet contract: `0xbEFbE69a1723E637691a7c2De76b5d01D81a41A2`; deployment transaction [0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd](https://explorer-studio.genlayer.com/tx/0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd) finalized `MAJORITY_AGREE`, GenVM `SUCCESS`, with all five deployment validators agreeing. The deployed source export is 59,431 bytes and byte-identical to the local source (SHA-256 above). The deployed schema exposes the same 10 expected methods. The direct JSON-RPC verifier returned HTTP 403; exact code export and schema verification succeeded through the authenticated GenLayer SDK/CLI.

### Validator-bound receipt proof

- Checkpoint creation: [0x8d054c3316f87e3eb995f6a47ad1d9bba6f118c7a5d9eb9634f5e8e4cf824c50](https://explorer-studio.genlayer.com/tx/0x8d054c3316f87e3eb995f6a47ad1d9bba6f118c7a5d9eb9634f5e8e4cf824c50), finalized `MAJORITY_AGREE`, checkpoint 1.
- Resolution: [0xd083cf617f7e13c38a4359b1d20b32fb235a2aff8f5c56959b15a55a062b7984](https://explorer-studio.genlayer.com/tx/0xd083cf617f7e13c38a4359b1d20b32fb235a2aff8f5c56959b15a55a062b7984), finalized `MAJORITY_AGREE`; checkpoint 1 became `FINALIZED / SUPPORTED / CONSISTENT`, certificate `FRESH`, usable `true`.
- Receipt 1 binds S1 `https://example.com/` to `WEB_GET_TEXT`, content SHA-256 `25ddf2c883e0d1958ea971d279a7e4f0fd446724ee3db7db19dadabd4a62e484`, zero render hash, `rcp-v1`, and `OBSERVED`.
- It binds S2 `https://www.iana.org/domains/reserved` to `WEB_GET_TEXT`, content SHA-256 `4a836e33450dce1f57ecc81bf9a5695279798adba4777a22271f321b6ab70010`, zero render hash, `rcp-v1`, and `OBSERVED`.
- Exact evidence root: `adead5629676257065931d0d6d1af183c782dbb40cb4540b7426fbaabcdcaa9a`; consensus digest: `5eb5d761b66f215a9980c67a323aaf7082fb928f1e7431fcd747c6dbed8efe10`; checkpoint fingerprint: `c5a960dd0fbffc94d595fc085dd522873f25ae179517d62f679b24ddad4959ed`.
- `MAJORITY_AGREE` means the network accepted the validator-equivalent result. It does not publish each validator's raw web-fetch log; the protocol commits the common receipt facts and hashes.

### Live hostile source-cluster proof

- Parent checkpoint 2 was created at [0x41609c283a02b654b485442f0e35224b7c1f71974da12720a36050a5a6db0a98](https://explorer-studio.genlayer.com/tx/0x41609c283a02b654b485442f0e35224b7c1f71974da12720a36050a5a6db0a98) and resolved at [0x224bd9fc31e5a442030185a924c978fb5678625fbc2e74cff3cc7ad13f6b1509](https://explorer-studio.genlayer.com/tx/0x224bd9fc31e5a442030185a924c978fb5678625fbc2e74cff3cc7ad13f6b1509). It was `FINALIZED / SUPPORTED`, certificate usable `true`. C1 was grounded in `https://httpbin.org/html`.
- The hostile source at `https://httpbin.org/base64/...` returned text explicitly contradicting C1 but shares the existing `httpbin.org` cluster.
- Challenge transaction [0x10ce7764cfa6d0f59cba0c332b889eb19598eb824c0b7da9992923b8ac18b1b4](https://explorer-studio.genlayer.com/tx/0x10ce7764cfa6d0f59cba0c332b889eb19598eb824c0b7da9992923b8ac18b1b4) finalized `MAJORITY_AGREE`. Leader and validators returned the deterministic error `challenge source must use a new domain cluster`; no nondeterministic source observation was admitted.
- Afterward checkpoint 2 retained fingerprint `5a6a3deb6aba76339c1ff8ad73bb814adff99931604bdcc7e760004b796d1245`, consensus digest `d2505477c50c1381ac6dbac8652a2c2563fd0f1419f6746375469a954d10ceea`, and state digest `380ca50cb263eed4dd4bcd345fbb9e87eb6e5f3a7a66697a06a934616c40b378`; `challenge_count=0`, `successor_id=0`, `state_status=SUPPORTED`, and usability remained `true`.
- A separate cross-domain hostile attempt [0xbfbfcfa1ea2ca560c7659ffb785682f50083d838c63fba7e85302a65b915eacc](https://explorer-studio.genlayer.com/tx/0xbfbfcfa1ea2ca560c7659ffb785682f50083d838c63fba7e85302a65b915eacc) finalized `MAJORITY_DISAGREE`. Its leader returned `PRESERVED_PRIOR`, but validators did not reach consensus. This is recorded as a failed live attempt, not a passing proof; checkpoint 1 remained unchanged and usable.

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

## Historical source `386103fd…18f9cbf0`

Canonical source SHA-256: `386103fd111f6280b94f78a9508084e1ba72503d1d7824de5189d75218f9cbf0`. Deployment tx `0xc953efe708125c4bec7669398e368c9f84184e1fb392638b80cec279073166c6` finalized with MAJORITY_AGREE / GenVM SUCCESS at `0xDc01B2807A2D9285C9F9359930b8076ac89d6688`. CLI-exported source is byte-identical (53,413 bytes), and live schema has 10 methods. Explorer: <https://explorer-studio.genlayer.com/tx/0xc953efe708125c4bec7669398e368c9f84184e1fb392638b80cec279073166c6>.

### Live material delta / successor

- Supported clock checkpoint 1: create `0xdd8c25be9cbb8d3a201248cbe7fdc6725ad9ce06a5d0597d283e342c6938dea0`; resolve `0x337a8f02c29c8634f2504c794e8db238c367f380b9a2453c15bdf8123c3e9dd8`. Both finalized MAJORITY_AGREE / GenVM SUCCESS; resolved SUPPORTED before cutoff.
- Post-cutoff revalidation: `0x65d8fbcad50b90d3391a00234d6696d57f2e25d0e182b822ea0c77192f3185d5`, FINALIZED / MAJORITY_AGREE / leader SUCCESS. Returned `SUCCESSOR_CREATED`, receipt 2, successor checkpoint 2 with predecessor 1. Both sources were OBSERVED and independently clustered. Prior SUPPORTED state became current CONTRADICTED; per-claim and overall delta were `CONTRADICTION`. Successor status DISPUTED, divergence CONSISTENT, FRESH, and unusable. This is a material state-change/successor proof; the two evidence hashes were Postman `ca0c2a3b4c84dded98938ad45b7070d1bfc57396a31c2a5ad536a65ff6a5eccd` and TimeAPI `87e6de1e6f3481a9e4fbf9b29faffa80060b2cdbcfb31990482950d7dc0607fe`.
- Explorer: <https://explorer-studio.genlayer.com/tx/0x65d8fbcad50b90d3391a00234d6696d57f2e25d0e182b822ea0c77192f3185d5>.

### Fail-closed challenge

- Challenge against checkpoint 2: `0xbe0babe0a18ec648717b870b5a24ae0cc19ddc19e86948efc33f1898016922ca`, FINALIZED. The `.invalid` source produced attempt status UNAVAILABLE / challenge result EXTERNAL_FAILURE. Attempt receipt 3 binds source S3 to claim C1 and marks observation EXTERNAL_FAILURE; `prior_checkpoint_preserved=true`. Re-read confirmed parent checkpoint 2 unchanged (DISPUTED, version 2, original source set only). No recovery success is claimed.
- Explorer: <https://explorer-studio.genlayer.com/tx/0xbe0babe0a18ec648717b870b5a24ae0cc19ddc19e86948efc33f1898016922ca>.

### WEB_RENDER_TEXT evidence

- Checkpoint 3 create `0x39da9b59be73c918ce42a498862e4b1c9b3779c4d187a69622c40904fc2baa06`; resolution `0xd919e2688908de351a3af48312e4d87ad91ff709f164d31bd097bb5db7173e05`, FINALIZED / MAJORITY_AGREE / GenVM SUCCESS.
- WHO page and example.com were actually retrieved with WEB_RENDER_TEXT; observations were OBSERVED and externalFailure=false. WHO claim C1 was UNKNOWN; example.com claim C2 SUPPORTED. Overall checkpoint was INCONCLUSIVE with `INSUFFICIENT_INDEPENDENCE`; this verifies live render retrieval and bound evidence, not a fully supported render checkpoint.
- WHO content/render hash `f60fe91a4a6211e0644d9dd232c680c4898190ee65b834c4c8eec2932cb87f2e`; example.com content/render hash `aa8c4320fabb468930b605f5f365b1beaf2ac42b081eed50083e26d26cb3c159`.
- Explorer: <https://explorer-studio.genlayer.com/tx/0xd919e2688908de351a3af48312e4d87ad91ff709f164d31bd097bb5db7173e05>.

### Composition and fork

- Echo checkpoint 4 create/resolve: `0xf10fae4ec18337d73572d2203328c5b55d90bb67b8f7be7375e91606c05e58c0` / `0x0a6366e5c94f5a42af08362323daf565f94bb3a6ad368c2018548c835d68349a`.
- Echo checkpoint 5 create/resolve: `0x6034417efc8cb2309eb458807ccfadbc75c40daef5f2a96b78a82de3467dc763` / `0x2d6d02262118b706de07c084af9abf7ffad7632195f95ee6587b040a8aa326cc`. Both child checkpoints finalized SUPPORTED / CONSISTENT and usable.
- Composite transaction `0x7d37cda9b0f430dd4a146034b2539c75d3e4d0fa1ea954833956485c888b289d`, FINALIZED. Checkpoint 6 references children and ancestors `[4,5]`, state SUPPORTED / CONSISTENT, certificate FRESH, usable true. Explorer: <https://explorer-studio.genlayer.com/tx/0x7d37cda9b0f430dd4a146034b2539c75d3e4d0fa1ea954833956485c888b289d>.
- Fork checkpoint 7 create `0x346f529e2a417a61bbeb5009c56f9715edcef8e9d2fcd1fe97e40c07df3b1a33`; resolve `0xedf6a826f58965418d9a4ccd06e6b04f0a88fd87f8a003ad04ab755ddf143707`, FINALIZED / MAJORITY_AGREE. Postman `foo1=Hello` was SUPPORTED (hash `515bbcf3f68a6d70cd49651cfbad5a47594e73bf8d1f45dec8ba37d2481cfdae`); HTTPBin `foo1=World` was CONTRADICTED (hash `02a3d81585ed25ca306a8e4cb5306be454b97c5e3743702811784528b969e958`). Result DISPUTED / CONTRADICTORY_REALITY, certificate FRESH, unusable, no external failure. Explorer: <https://explorer-studio.genlayer.com/tx/0xedf6a826f58965418d9a4ccd06e6b04f0a88fd87f8a003ad04ab755ddf143707>.

### Future/self reference rejection

- Attempted to create a composite with prospective checkpoint ID 8 in its child list when only seven checkpoints existed: `0x3d35610730955ccc5653ae28c2e762f12782ff896b074ae5bb74ecacb436da6e`, FINALIZED / MAJORITY_AGREE with validator execution ERROR `checkpoint not found`. It created no checkpoint and changed no state. This demonstrates rejection of a future/self reference; it is not reported as a separate explicit graph-cycle detector test.

### Challenge failure and recovery

- A dedicated standalone checkpoint 8 was created by `0x4cc3633342e477e1ca469beebb86cf7eb30650bbf464cfc013f6e95bbfb43d8e` (FINALIZED / MAJORITY_AGREE). Its first resolution `0x6ece50d6bb3dc02dfbda75d649d60a41de2e5522bbd8df550e578b92534eaf89` finalized MAJORITY_DISAGREE after validators disagreed on an INCONCLUSIVE proposal; it did not change state, and checkpoint 8 remained SEALED. Retry `0xeb163e7d2840b2af37c3c1406927636762a2f6f203346540a9dc4671a4c8cd47` finalized MAJORITY_AGREE and created initial receipt 9, SUPPORTED / CONSISTENT with two OBSERVED independent sources. Postman hash `515bbcf3f68a6d70cd49651cfbad5a47594e73bf8d1f45dec8ba37d2481cfdae`; HTTPBin hash `388df268ef27dfac7967b7eb3c11935642723cf19ec3400b8fcf9943cb352678`. Explorer: [create](https://explorer-studio.genlayer.com/tx/0x4cc3633342e477e1ca469beebb86cf7eb30650bbf464cfc013f6e95bbfb43d8e), [first resolution (disagreement)](https://explorer-studio.genlayer.com/tx/0x6ece50d6bb3dc02dfbda75d649d60a41de2e5522bbd8df550e578b92534eaf89), [successful retry](https://explorer-studio.genlayer.com/tx/0xeb163e7d2840b2af37c3c1406927636762a2f6f203346540a9dc4671a4c8cd47).
- Failed challenge against checkpoint 8: `0xdb384cee09f9b3dda86c6a4ebe9fb59faf0db2e9d4bec852ab532239cd91d3d1`, FINALIZED / MAJORITY_AGREE. Attempt receipt 10 is UNAVAILABLE / EXTERNAL_FAILURE; S3 at `.invalid` is bound to C1 and marked EXTERNAL_FAILURE. `prior_checkpoint_preserved=true`; checkpoint 8 remained SUPPORTED / FINALIZED with its original sources and initial receipt 9. Explorer: <https://explorer-studio.genlayer.com/tx/0xdb384cee09f9b3dda86c6a4ebe9fb59faf0db2e9d4bec852ab532239cd91d3d1>.
- Valid retry against checkpoint 8: `0x68831f4a6e6c3c8e60f544e751aac4a1774f166d3832d322041038e5127bac45`, FINALIZED / MAJORITY_AGREE. Receipt 11 returned `UPHELD`, `UNCHANGED`, SUPPORTED, predecessor 8; it created checkpoint 9 as the immutable successor. Checkpoint 8 is SUPERSEDED, checkpoint 9 is FINALIZED / SUPPORTED / CONSISTENT / FRESH, and `is_checkpoint_usable(9)` returned true. Explorer: <https://explorer-studio.genlayer.com/tx/0x68831f4a6e6c3c8e60f544e751aac4a1774f166d3832d322041038e5127bac45>.
- An earlier independent unavailable challenge against checkpoint 4 finalized as `0x64eefd200c19ebebc0f7ec1afffa45712e8a0a200eb4dab3f935b231ea3daf0f` (MAJORITY_AGREE), receipt 8, EXTERNAL_FAILURE; the parent remained unchanged. Afterward the existing composite checkpoint 6 still returned usable=true. Explorer: <https://explorer-studio.genlayer.com/tx/0x64eefd200c19ebebc0f7ec1afffa45712e8a0a200eb4dab3f935b231ea3daf0f>.

## Current proof boundary

The transaction matrix is source-version-specific. Source `386103fd…18f9cbf0` passed successor semantic contradiction, fail-closed challenge preservation, live WEB_RENDER_TEXT retrieval, supported composition, fork detection, and future/self-reference rejection. The corrected source `2ca8e459…788a37d` passed the validator-bound receipt proof and hostile same-domain source-cluster rejection recorded above. The WHO semantic claim remained UNKNOWN in the historical render proof. Do not upgrade that render limitation to a fully supported claim or transfer any proof across source versions.

## Revised source `133bec360911bb5cc4cfdef32330bcadb13e61c74a92b1f3bd9641d04c49bace`

- Commit: `52395adef1f12655c74500e639b694fca2774b40`; pushed to `main`.
- Deployment transaction `0xcac440da626a08a2c709340f10ef6f7d9008ff36c097d2ae6821de381d82e943`; contract `0x2dFBBB86bcfc85493732AcA9e028e570a41D6a7A`; FINALIZED, GenVM SUCCESS, MAJORITY_AGREE. Explorer: <https://explorer-studio.genlayer.com/tx/0xcac440da626a08a2c709340f10ef6f7d9008ff36c097d2ae6821de381d82e943>.
- CLI-exported contract source is byte-identical: 53,501 bytes; local and deployed SHA-256 `133bec360911bb5cc4cfdef32330bcadb13e61c74a92b1f3bd9641d04c49bace`. The live schema contains the expected ten methods.
- Time-bound checkpoint 1 creation `0xac1447bf2ddd6215c7e29c34f69ba89a138d20893f042f512cdc44cfe8611b43` and initial resolution `0x21348e9703d2f043ebaa9b30c191f4f163e050c9c7eae153fee230c05b23047c` both FINALIZED, GenVM SUCCESS, MAJORITY_AGREE. Resolution returned FINALIZED, state SUPPORTED, divergence CONSISTENT, receipt 1. Postman Echo and TimeAPI were OBSERVED and independently clustered as `domain:postman-echo.com` and `domain:timeapi.io`; their evidence content hashes are `648bd36c011fc4544afff92818a644d2f2ed31e94f7ff13b8b9a84e97ef5c313` and `fb1e3b9b90b84c1612ee82f71a950043ba4df2a75a10d0c9bba090d3607cf5dc`.
- The matching post-cutoff revalidation has not yet been submitted; no material-delta or successor pass is claimed here.

## Prior deployed source `c184f679…b340c4`: material-delta diagnostic

- Initial clock checkpoint create `0x37bddeb00c4a963b76071880613f96f7cc4320307fc463d4207d9cd8b076f358` and resolve `0x7ad1a11086390b66f1cdf26ab30a5b08e455221321277827d98b08f3d0910fbe` finalized; checkpoint 1 was SUPPORTED/CONSISTENT with both clock sources observed.
- Post-cutoff revalidation `0xdac1f12388515850381e83b6d9fd65660397275dd4691cc8698e8e51ffe1e783` finalized MAJORITY_AGREE. Receipt 2 had both independent findings CONTRADICTED and claim delta CONTRADICTION, but the model's `INSUFFICIENT_EVIDENCE` divergence label led the contract to preserve prior as INCONCLUSIVE. This exposed the summary-label precedence issue fixed in source `133bec…` and covered by a regression test. It is not a material-delta success.
- Explorer: <https://explorer-studio.genlayer.com/tx/0xdac1f12388515850381e83b6d9fd65660397275dd4691cc8698e8e51ffe1e783>.
