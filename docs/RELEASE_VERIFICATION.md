# Release Verification Record

This record distinguishes reproducible local checks from finalized live-chain evidence. No status is inferred from an accepted transaction alone.

## Local candidate

| Gate | Result | Evidence |
|---|---|---|
| Python syntax | PASS | `python -m py_compile contracts/reality_checkpoint.py tests/test_protocol.py tests/direct/test_contract.py` |
| Offline preflight | PASS | `python scripts/preflight.py`; one canonical contract, 10 public API methods |
| Direct Mode | PASS: 14/14 | `gltest tests/direct/test_contract.py -q` |
| Protocol/adversarial tests | PASS: 18/18 | `pytest tests/test_protocol.py -q` |
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
| Contract SHA-256 | `dcf3c321b8d598e24d2d91f6a7c4aae9e0cfd272563dcaf15eb3789e79d4fda7` |
| Deployment source parity | Exact local/deployed byte match verified before live transactions |
| Current local commit | See final verification record after the evidence-document commit |
| Git metadata | `.gitmeta`; explicit `--git-dir` / `--work-tree` used due inherited `.git` ownership mismatch |

## Studionet deployment

| Field | Verified value |
|---|---|
| Contract | `0x69570326e3120c2b9EB96Cc471b235b6adE91501` |
| Deployment tx | `0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3` |
| Explorer | <https://explorer-studio.genlayer.com/tx/0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3> |
| Lifecycle | `FINALIZED` |
| GenVM | `SUCCESS` |
| Consensus | `Accepted` |

## Live protocol transactions

| Proof | Transaction(s) | Verified result |
|---|---|---|
| Fork checkpoint creation (ID 1) | `0x4d8458b6482e4bdfb1eb131464ee6546ddd3e7265f2850ce052358fe6d4dd0d1` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE |
| Fork resolution | `0x529de2378dcb5364700a1abc5171f95c9861ba238caff2752e0950296a3be60a` | FINALIZED; leader SUCCESS; 1 SUPPORTED + 1 CONTRADICTED; DISPUTED / CONTRADICTORY_REALITY |
| Render checkpoint creation (ID 2) | `0x116785b528e523908d9e7ade567baf2d14d5f5632de77ee7879d759bf497ffda` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE |
| Render resolution | `0x7799c664640f661294de744ab4dfe09c9dc545436de47cd45c394bbebdb9a390` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE; WHO + example.com WEB_RENDER_TEXT observations both supported; CONSISTENT |
| Revalidation | `0xbaffa0523d997fe27d49d73630e222d9fdf78693a329b301f504b547cb486abf` | FINALIZED; GenVM SUCCESS; MAJORITY_AGREE; overall delta UNCHANGED, but WHO UNKNOWN, output PRESERVED_PRIOR (receipt 3), no successor |

Explorer transaction links and exact evidence hashes are in `EVIDENCE.md`. The exploratory wrong-ID transaction `0x06be77c3e1ba498655e7a3951808a7a85c49000d84700acfddb845b600f9d537` finalized as `checkpoint not found`; it is excluded from passing proofs.

## Submission-gate status

| Gate | Status |
|---|---|
| Local tests, lint, schema | GREEN |
| Studionet deployment and source parity | GREEN |
| Live web-render evidence | GREEN |
| Live Reality Fork Detection and unusable disputed certificate | GREEN |
| Live no-change revalidation successor | NOT GREEN: prior preserved because WHO classified UNKNOWN |
| Live material semantic delta | NOT RUN |
| Live composite checkpoint and cycle rejection | NOT RUN |
| Live transport failure preserving a prior checkpoint | NOT RUN |
| Live challenge recovery | NOT RUN |
| GitHub push of final evidence documentation | Pending final commit/push attempt |

The project must not be marked frozen, finalized, or submission-ready while any required live proof above remains incomplete. A failure to meet a live gate is not relabeled as an external connectivity block when the chain is reachable and the attempt yielded a protocol outcome.

## Connectivity and wallet notes

Earlier independent retries showed GitHub HTTPS transport denied by the Windows/network sandbox and an expired saved `gh` token. GitHub connectivity/authentication should be retried separately before final push. Studionet became reachable with the permitted elevated network call. The local keystore was unlocked by the user through GenLayer CLI's secure prompt; no wallet secret was copied into chat or the repository.

