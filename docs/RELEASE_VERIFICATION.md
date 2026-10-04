# Release Verification Record

This record distinguishes reproducible local checks from finalized live-chain evidence. No status is inferred from an accepted transaction alone. The steward-fix candidate adds bounded accounting for every persisted inconclusive challenge attempt. Its local tests, lint, and schema gates are green; it is not yet the deployed source. A new Studionet deployment and source-specific live proof remain pending.

## Local candidate

| Gate | Result | Evidence |
|---|---|---|
| Python syntax | PASS | `python -m py_compile contracts/reality_checkpoint.py tests/test_protocol.py tests/direct/test_contract.py` |
| Offline preflight | PASS | `python scripts/preflight.py`; one canonical contract, 10 public API methods |
| Direct Mode | PASS: 21/21 | `gltest tests/direct/test_contract.py -q`; includes admitted-supplemental-source plus unresolved-second-claim receipt/budget regression |
| Protocol/adversarial tests | PASS: 27/27 | `python -m pytest tests/test_protocol.py -q` |
| GenVM AST lint | PASS: 3 checks | `genvm-lint check contracts/reality_checkpoint.py` |
| SDK semantic validation | PASS | `genvm-lint check contracts/reality_checkpoint.py`; GenVM v0.2.16 |
| ABI/schema extraction | PASS: 10 methods (5 view, 5 write) | `genvm-lint schema contracts/reality_checkpoint.py` |
| GenVM JSON-specific check | NOT RUN | Installed linter exposes no JSON-mode command |
| Local-chain integration | NOT RUN | No local Studio/GLSim node was started |

Run the suites separately: `python -m pytest tests/test_protocol.py -q` for pure protocol logic and `gltest tests/direct/test_contract.py -q` for GenLayer Direct Mode. `python -m pytest tests -q` does not substitute for the Direct Mode runner and should not be used as the project-wide command.

## Source and Git

| Item | Value |
|---|---|
| Branch | `main` |
| Remote | `https://github.com/Chinny070/Reality-checkpoint-protocol-` |
| Steward-fix candidate contract SHA-256 | `26ca41afe295bdacfded56976d99dfde3839a62d150c5b6a35e88f645740f1ee` |
| Steward-fix candidate Git blob | `1ecd8894b4299a7586452a0dc151e3bfa5abe0f2` |
| Steward-fix commit | `cae50240f47e6e035fa577b122aad93b9c4f0fbf` |
| Matching push | Pending |
| Historical deployed source hashes | `386103fd…18f9cbf0`, `fd0969dc…f7e2`, and earlier sources |
| Corrected source deployment parity | PASS: byte-identical, 59,431 bytes |
| Previous evidence-record commit | `37f670b1fc62a9fba39344ca71195e6c32dd4f77` |
| Git metadata | `.gitmeta`; explicit `--git-dir` / `--work-tree` used due inherited `.git` ownership mismatch |

## Studionet deployment

| Field | Verified value |
|---|---|
| Corrected contract | `0xbEFbE69a1723E637691a7c2De76b5d01D81a41A2` |
| Corrected deployment tx | `0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd` |
| Corrected Explorer | <https://explorer-studio.genlayer.com/tx/0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd> |
| Lifecycle | `FINALIZED` |
| GenVM | `SUCCESS` |
| Consensus | `MAJORITY_AGREE` |

Historical deployments are listed in the source-versioned evidence below. For the corrected source, Python JSON-RPC returned HTTP 403; exact SDK/CLI export and schema reads succeeded and source parity was byte-identical.

## Historical live protocol transactions (through source `386103fd…18f9cbf0`)

| Proof | Transaction(s) | Verified result |
|---|---|---|
| Fork checkpoint creation (ID 1) | `0x4d8458b6482e4bdfb1eb131464ee6546ddd3e7265f2850ce052358fe6d4dd0d1` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE |
| Fork resolution | `0x529de2378dcb5364700a1abc5171f95c9861ba238caff2752e0950296a3be60a` | FINALIZED; leader SUCCESS; 1 SUPPORTED + 1 CONTRADICTED; DISPUTED / CONTRADICTORY_REALITY |
| Render checkpoint creation (ID 2) | `0x116785b528e523908d9e7ade567baf2d14d5f5632de77ee7879d759bf497ffda` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE |
| Render resolution | `0x7799c664640f661294de744ab4dfe09c9dc545436de47cd45c394bbebdb9a390` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE; WHO + example.com WEB_RENDER_TEXT observations both supported; CONSISTENT |
| Revalidation | `0xbaffa0523d997fe27d49d73630e222d9fdf78693a329b301f504b547cb486abf` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE; overall delta UNCHANGED, but WHO UNKNOWN, output PRESERVED_PRIOR (receipt 3), no successor |
| Corrective candidate diagnostic resolution | `0x3d1106cd30d71883a61cff2a39823aef3f4faf5b057edeeb5476eb226ab7e471` | UNDETERMINED; model omitted a bound source finding; GenVM raised `incomplete source findings`. Corrected candidate now maps missing findings to UNKNOWN and forces the claim UNKNOWN; covered by regression test. This transaction is not a pass. |
| Corrected-source omitted-finding live resolution | `0x61a54c0da97e68ba2fd4e13767a5a8275aa01fc23138b5f3c0a181e1161ae252` | UNDETERMINED; contract execution SUCCESS returned INCONCLUSIVE when findings/relationships were incomplete, but validators disagreed. No protocol pass claimed. |
| Corrected-source echo initial checkpoint | `0xbee4150194ff345c8b36120c7ae874e70e31edcb6df28bff2d633021ec38eb11` | FINALIZED; checkpoint ID 2 |
| Corrected-source echo resolution | `0xd5c38ff421cbfd650c417f1024e4791fbfa5f46b9855173553857326a2a819bc` | FINALIZED; both echo findings SUPPORTED; CONSISTENT; checkpoint 2 finalized |
| Corrected-source no-change revalidation | `0xd6d91b8c446817bf52f0b6e77e823538248c798445db3d077b55d46f4fbe3878` | FINALIZED; overall/claim delta UNCHANGED; SUCCESSOR_CREATED as checkpoint 3, predecessor 2 |
| Corrected-source second echo checkpoint | `0xe510d1f99395fd41182307e72c06571e768777b5d9d07fbfdfcaaf3ce759fd16` | FINALIZED; checkpoint ID 4 |
| Corrected-source second echo resolution | `0xb5ceccf6506db2b4fa21f9d101782eb5e1af8fe4195da4046f0940f982e54688` | FINALIZED; both findings SUPPORTED; checkpoint 4 finalized |
| Live composite | `0x276905036761a8773a0147511ab6af1814c50c0377cc28da2d63022133dedb24` | FINALIZED; composite checkpoint 5 SUPPORTED/CONSISTENT; children `[3,4]`; certificate FRESH; usable `true` |
| Corrected-source fork checkpoint | `0xbc605065d4545470b02a78e56de4067e6e28bcc6d3a1755c43959ac2e5a11dab` | FINALIZED; checkpoint ID 6 |
| Corrected-source fork resolution | `0xe83e278319e95b9890bc799b6c58d7a10636dc2fc0522c9333dcea799ebd650f` | FINALIZED; opposing SUPPORTED/CONTRADICTED findings; DISPUTED/CONTRADICTORY_REALITY; usable `false` |
| Prior-source unavailable challenge | `0x7bba240a174fa8beeba606bbdcff3062ee822a552b9dbe35331c31710f33981e` | FINALIZED; challenge output PRESERVED_PRIOR; cp3 remains FINALIZED and usable. Receipt 5 exposed missing claim binding for the appended challenge source; the present candidate fixes it. |
| Material-delta revalidation attempt | `0x5822d463ecc56d93b2cb67deeb399e0cab5d96103c5ede6bc99131f4f9998764` | UNDETERMINED because validators disagreed. Not a pass; material delta remains unverified live. |
| Source-386103fd supported parent create | `0xfb18bf5fb8055f09e51a656c6e93b70c0faf8735ca9ac8cebcce712582b936af` | FINALIZED; checkpoint ID 1 |
| Source-386103fd supported parent resolve | `0x33c55f4c2681df36e42a2530d6a42b586a982e7b3c6fc59f4a3f71c019c196a8` | FINALIZED; both independent echo findings SUPPORTED; checkpoint 1 FINALIZED |
| Source-386103fd challenge failure proof | `0xd1dfb3b11ed349107aa60bcf21796d89a2100b3b53536878a19466dc6621b94b` | FINALIZED; PRESERVED_PRIOR; source S3 observation EXTERNAL_FAILURE; attempt receipt 2 contains `claim_ids=["C1"]`; checkpoint 1 remains FINALIZED/SUPPORTED |

Explorer transaction links and exact evidence hashes are in `EVIDENCE.md`. The exploratory wrong-ID transaction `0x06be77c3e1ba498655e7a3951808a7a85c49000d84700acfddb845b600f9d537` finalized as `checkpoint not found`; it is excluded from passing proofs.

## Historical candidate proofs (`386103fd…18f9cbf0`)

The exact live transaction IDs and evidence hashes are documented in [EVIDENCE.md](EVIDENCE.md). On this deployed source: time-cutoff semantic contradiction created successor 2; unavailable challenges preserved their parents, and checkpoint 8's valid retry created supported successor 9; live render retrievals were observed with WHO claim UNKNOWN and example.com SUPPORTED; composite 6 from children 4/5 was SUPPORTED/CONSISTENT, FRESH and usable; fork 7 was DISPUTED/CONTRADICTORY_REALITY and unusable; and a future/self child reference was rejected with `checkpoint not found`. Render retrieval is proven, a fully supported WHO render claim is not. Composition future/self rejection is proven; no separately constructed cycle can be submitted through the already-finalized-child API.

These proofs apply only to the source hash in this heading.

## Previously deployed corrected candidate live proofs (`2ca8e459…788a37d`)

| Proof | Transaction | Verified result |
|---|---|---|
| Deployment | [`0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd`](https://explorer-studio.genlayer.com/tx/0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd) | FINALIZED, GenVM SUCCESS, MAJORITY_AGREE; contract `0xbEFbE69a1723E637691a7c2De76b5d01D81a41A2` |
| Receipt proof checkpoint | [`0x8d054c3316f87e3eb995f6a47ad1d9bba6f118c7a5d9eb9634f5e8e4cf824c50`](https://explorer-studio.genlayer.com/tx/0x8d054c3316f87e3eb995f6a47ad1d9bba6f118c7a5d9eb9634f5e8e4cf824c50) | FINALIZED, MAJORITY_AGREE; checkpoint 1 |
| Validator-bound receipt resolution | [`0xd083cf617f7e13c38a4359b1d20b32fb235a2aff8f5c56959b15a55a062b7984`](https://explorer-studio.genlayer.com/tx/0xd083cf617f7e13c38a4359b1d20b32fb235a2aff8f5c56959b15a55a062b7984) | FINALIZED, MAJORITY_AGREE; SUPPORTED/CONSISTENT, FRESH and usable; on-chain receipt exposes two observed content hashes and consensus-bound evidence root |
| Hostile test parent | [`0x41609c283a02b654b485442f0e35224b7c1f71974da12720a36050a5a6db0a98`](https://explorer-studio.genlayer.com/tx/0x41609c283a02b654b485442f0e35224b7c1f71974da12720a36050a5a6db0a98) and [`0x224bd9fc31e5a442030185a924c978fb5678625fbc2e74cff3cc7ad13f6b1509`](https://explorer-studio.genlayer.com/tx/0x224bd9fc31e5a442030185a924c978fb5678625fbc2e74cff3cc7ad13f6b1509) | Both FINALIZED, MAJORITY_AGREE; checkpoint 2 SUPPORTED and usable before attack |
| Hostile same-domain contradictory challenge | [`0x10ce7764cfa6d0f59cba0c332b889eb19598eb824c0b7da9992923b8ac18b1b4`](https://explorer-studio.genlayer.com/tx/0x10ce7764cfa6d0f59cba0c332b889eb19598eb824c0b7da9992923b8ac18b1b4) | FINALIZED, MAJORITY_AGREE; deterministic rejection `challenge source must use a new domain cluster`; checkpoint fingerprint/state digest unchanged, no successor, no challenge-count increase, remains usable |
| Cross-domain hostile challenge diagnostic | [`0xbfbfcfa1ea2ca560c7659ffb785682f50083d838c63fba7e85302a65b915eacc`](https://explorer-studio.genlayer.com/tx/0xbfbfcfa1ea2ca560c7659ffb785682f50083d838c63fba7e85302a65b915eacc) | FINALIZED, MAJORITY_DISAGREE; not a passing proof; parent unchanged |

The Python JSON-RPC source verifier returned HTTP 403. The authenticated SDK exported the source (59,431 bytes) and it matched SHA-256 exactly; the CLI verified the 10-method schema and deployment receipt.

## Steward-fix candidate (`26ca41af…5740f1ee`)

| Gate | Status |
|---|---|
| Persisted inconclusive attempt accounting | PASS locally: every nonfinal challenge receipt increments the per-checkpoint attempt count; reverts after three. Rejected supplemental submissions persist no receipt and consume no round. |
| Admitted supplemental source with another unresolved claim | PASS locally: Direct Mode regression verifies claim-bound receipt persistence, unchanged parent state, no successor, and challenge budget exhaustion. |
| Direct Mode / protocol tests | PASS: 21 / 27 |
| Lint / schema / preflight | PASS: 3 lint checks, 10 methods, single canonical contract |
| Studionet deployment and parity | PENDING; deployment command stopped at wallet keystore decryption (`Invalid password. Attempt 2/3`). |
| Live admitted-source/unresolved-claim bounded-attempt proof | PENDING deployment of this source |

## Submission-gate status

| Gate | Status |
|---|---|
| Steward-fix candidate tests, lint, schema | GREEN: 21 Direct Mode + 27 protocol tests; GenVM lint 3 checks; 10-method schema |
| Steward-fix candidate Studionet deployment and source parity | PENDING wallet unlock; older deployed candidate parity remains verified for its own hash |
| Corrected-source live validator-bound receipt proof | GREEN: on-chain receipt facts and evidence root are included in the accepted consensus result |
| Corrected-source live hostile same-domain contradictory challenge | GREEN: deterministic rejection; parent unchanged, supported, usable |
| Cross-domain hostile challenge live consensus | NOT GREEN: finalized MAJORITY_DISAGREE; excluded from passing evidence |
| Previous byte-identical source live web-render evidence | GREEN |
| Prior-source live WEB_RENDER_TEXT | GREEN for on-chain retrieval and observation receipts; example.com claim SUPPORTED, WHO claim UNKNOWN (no fully supported WHO claim asserted) |
| Previous byte-identical source live Reality Fork Detection and unusable disputed certificate | GREEN |
| Prior-source no-change revalidation successor | GREEN on earlier source `fd0969dc…f7e2` |
| Prior-source live material semantic delta | GREEN on source `386103fd…18f9cbf0`: two independent contradictions, CONTRADICTION delta, successor created |
| Prior-source live composite checkpoint | GREEN on source `386103fd…18f9cbf0`; future/self reference rejected; see qualification above |
| Prior-source live transport failure preserving a checkpoint | GREEN on source `386103fd…18f9cbf0`; failed source binds C1; parent unchanged |
| Initial failed-checkpoint recovery | Intentional terminal semantics: initial INCONCLUSIVE/UNAVAILABLE checkpoints cannot be revived; create a replacement checkpoint |
| Supplemental challenge admission | Local safety and bounded persisted-attempt accounting GREEN; steward-specific live proof PENDING deployment of steward-fix source |
| Live WEB_RENDER_TEXT | GREEN for actual rendered-source retrieval/evidence; WHO remains UNKNOWN, so no fully supported WHO claim |
| GitHub push | GREEN: corrected implementation and release records pushed; final local/remote `main` heads were verified equal |
| Public owner portfolio audit | GREEN within scope: 51 public repo names/descriptions reviewed, seven closest README reviews; Decision Memory overlap/rejection risk disclosed in `DECISION.md` |

The project must not be marked frozen, finalized, or submission-ready while any required live proof above remains incomplete. Older challenge-recovery transaction evidence applies only to the prior deployed source and does not establish behavior of the corrected source. A failure to meet a live gate is not relabeled as an external connectivity block when the chain is reachable and the attempt yielded a protocol outcome.

## Connectivity and wallet notes

GitHub access previously allowed commit `42e3b5d4376dafb87a580c610d133010b8a61127` to be pushed. A subsequent push initially failed with a Windows socket permission error, then succeeded with the user's authorized network-permission retry. Public API access then returned the complete 51-repository owner list; the closest seven were reviewed at README level (see `DECISION.md`). Final release documentation was pushed, and `git ls-remote origin refs/heads/main` returned the same SHA as local HEAD. `gh auth status` still reported the cached token invalid; the successful push used existing Git credential-manager access. No global security policy was changed. Studionet was reachable for recorded transactions. The sandboxed helper could not read the keychain, but the same helper with approved host keychain/network access read the unlocked signer; no private key was printed or persisted.

