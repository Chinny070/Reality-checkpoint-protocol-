# Release Verification Record

This record distinguishes reproducible local checks from finalized live-chain evidence. No status is inferred from an accepted transaction alone.

## Local candidate

| Gate | Result | Evidence |
|---|---|---|
| Python syntax | PASS | `python -m py_compile contracts/reality_checkpoint.py tests/test_protocol.py tests/direct/test_contract.py` |
| Offline preflight | PASS | `python scripts/preflight.py`; one canonical contract, 10 public API methods |
| Direct Mode | PASS: 15/15 | `gltest tests/direct/test_contract.py -q` |
| Protocol/adversarial tests | PASS: 19/19 | `pytest tests/test_protocol.py -q` |
| GenVM AST lint | PASS: 3 checks | `genvm-lint check contracts/reality_checkpoint.py` |
| SDK semantic validation | PASS | `genvm-lint check contracts/reality_checkpoint.py`; GenVM v0.2.16 |
| ABI/schema extraction | PASS: 10 methods (5 view, 5 write) | `genvm-lint schema contracts/reality_checkpoint.py` |
| GenVM JSON-specific check | NOT RUN | Installed linter exposes no JSON-mode command |
| Local-chain integration | NOT RUN | No local Studio/GLSim node was started |

The first broad `pytest tests -q` invocation is not a valid Direct Mode command: it bypassed the GenLayer `gltest` fixture and failed 13 fixture-dependent Direct tests. Running the prescribed `gltest` command passed all 14 Direct tests; the protocol suite passed all 18 tests. Do not count the failed invocation as a candidate regression.

## Source and Git

| Item | Value |
|---|---|
| Branch | `main` |
| Remote | `https://github.com/Chinny070/Reality-checkpoint-protocol-` |
| Current candidate contract SHA-256 | `450dd5c8c25d22e9ac9922df25f3f2c454015171bab643a9b653cda209156df7` |
| Deployed source hashes | `fd0969dc0d7b1d9df4b13be0c5de65c91757d5edece3884c6f15f61c4b29f7e2` and earlier `dcf3c321b8d598e24d2d91f6a7c4aae9e0cfd272563dcaf15eb3789e79d4fda7` |
| Current source deployment parity | Pending: current source adds challenge-attempt source binding and must be redeployed |
| Previous evidence-record commit | `37f670b1fc62a9fba39344ca71195e6c32dd4f77` |
| Git metadata | `.gitmeta`; explicit `--git-dir` / `--work-tree` used due inherited `.git` ownership mismatch |

## Studionet deployment

| Field | Verified value |
|---|---|
| Previously verified contract (source `dcf3…fda7`) | `0x69570326e3120c2b9EB96Cc471b235b6adE91501` |
| Previous deployment tx | `0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3` |
| Previous Explorer | <https://explorer-studio.genlayer.com/tx/0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3> |
| Lifecycle | `FINALIZED` |
| GenVM | `SUCCESS` |
| Consensus | `Accepted` |

The source at SHA-256 `fd0969dc…f7e2` was deployed at `0xdF1BF015f0d6a136Fc8c89020e1F9D122e9aDaEf` via `0x743d95c1b06d18ff885461f36ee9bb989a6e65b7087c753789c93ccda576cf17` (FINALIZED, GenVM SUCCESS, MAJORITY_AGREE); GenLayer CLI source retrieval was byte-identical, and schema contained the expected 10 methods. The current source hash `450dd5c8…56df7` is a follow-up evidence-binding correction and has not yet been deployed.

## Live protocol transactions

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
| Corrected-source unavailable challenge | `0x7bba240a174fa8beeba606bbdcff3062ee822a552b9dbe35331c31710f33981e` | FINALIZED; challenge output PRESERVED_PRIOR; cp3 remains FINALIZED and usable. Receipt 5 exposed missing claim binding for the appended challenge source; current candidate fixes this and needs re-deployment/live check. |
| Material-delta revalidation attempt | `0x5822d463ecc56d93b2cb67deeb399e0cab5d96103c5ede6bc99131f4f9998764` | UNDETERMINED because validators disagreed. Not a pass; material delta remains unverified live. |

Explorer transaction links and exact evidence hashes are in `EVIDENCE.md`. The exploratory wrong-ID transaction `0x06be77c3e1ba498655e7a3951808a7a85c49000d84700acfddb845b600f9d537` finalized as `checkpoint not found`; it is excluded from passing proofs.

## Submission-gate status

| Gate | Status |
|---|---|
| Current candidate tests, lint, schema | GREEN |
| Current candidate Studionet deployment and source parity | NOT YET VERIFIED |
| Previous byte-identical source live web-render evidence | GREEN |
| Previous byte-identical source live Reality Fork Detection and unusable disputed certificate | GREEN |
| Live no-change revalidation successor | GREEN on source `fd0969dc…f7e2` |
| Live material semantic delta | NOT GREEN: latest attempt UNDETERMINED |
| Live composite checkpoint | GREEN on source `fd0969dc…f7e2`; live cycle rejection still not tested |
| Live transport failure preserving a prior checkpoint | GREEN on source `fd0969dc…f7e2`, via challenge. Added-source claim binding now regression-tested and awaits deployment/live repeat |
| Live challenge recovery | Not yet demonstrated; only fail-closed preservation was verified |
| GitHub push | Previous evidence documentation commit pushed; corrected candidate changes require a new push |

The project must not be marked frozen, finalized, or submission-ready while any required live proof above remains incomplete. A failure to meet a live gate is not relabeled as an external connectivity block when the chain is reachable and the attempt yielded a protocol outcome.

## Connectivity and wallet notes

Earlier independent retries showed GitHub HTTPS transport denied by the Windows/network sandbox and an expired saved `gh` token. GitHub connectivity/authentication should be retried separately before final push. Studionet became reachable with the permitted elevated network call. The local keystore was unlocked by the user through GenLayer CLI's secure prompt; no wallet secret was copied into chat or the repository.
