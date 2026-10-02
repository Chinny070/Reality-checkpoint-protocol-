# Release Verification Record

This document separates locally reproducible checks from hosted-network facts. No external result is inferred from a local test.

## Local candidate

| Gate | Result | Evidence |
|---|---|---|
| Python syntax | PASS | `python -m py_compile contracts/reality_checkpoint.py tests/test_protocol.py tests/direct/test_contract.py` |
| Offline preflight | PASS | `python scripts/preflight.py` |
| Direct Mode | PASS: 14/14 | `gltest tests/direct/test_contract.py -q` |
| Protocol/adversarial tests | PASS: 15/15 | `pytest tests/test_protocol.py -q` |
| Pickling | PASS | Direct test `test_nondeterministic_closures_are_picklable` |
| GenVM AST lint | PASS: 3 checks | `genvm-lint check contracts/reality_checkpoint.py`; genvm-lint 0.11.0 |
| SDK semantic validation | PASS | `genvm-lint check contracts/reality_checkpoint.py`; GenVM v0.2.16 |
| ABI/schema extraction | PASS: 10 methods (5 view, 5 write) | `genvm-lint schema contracts/reality_checkpoint.py` |
| GenVM JSON-specific check | NOT RUN | No JSON-mode command is defined by the installed linter's local CLI |
| Supplemental type check | NOT RUN | Not required by the installed GenVM workflow |
| Local-chain integration | NOT RUN | No local Studio/GLSim network started |

Python: 3.12.10. `genlayer-test`: 0.29.2. `genlayer-py`: 0.16.3.

## Hashes and Git

| Item | Value |
|---|---|
| Local branch | `main` |
| Remote | `https://github.com/Chinny070/Reality-checkpoint-protocol-` |
| Commit SHA | Pending final local commit |
| Contract Git blob SHA | `164cdc7cc3804ed00dd9960a1d3af21f3bcb75b7` |
| Contract SHA-256 | `ade566d3dea6b78ce316da3755d9f21957824efd8163266f3daec6781be7d1f5` |
| Working tree | Pending final commit check |

Git metadata lives in `.gitmeta` within the authorized project directory because the inherited `.git` metadata has an ownership mismatch and cannot safely be rewritten in this session. Git commands use explicit `--git-dir=.gitmeta --work-tree=.`. No global `safe.directory` setting was changed.

## Hosted external gates

| Gate | Result | Evidence |
|---|---|---|
| GitHub API/push | BLOCKED | Pending independent connectivity retry below; no remote write claimed |
| Studionet deploy | BLOCKED / NOT RUN | Pending independent connectivity retry below |
| Consensus transactions | NOT RUN | Requires a deployed Studionet contract |
| Explorer verification | NOT RUN | Requires an actual deployment and transaction |
| Deployed-source parity | NOT RUN | Requires deployed code/source data |
| Real live web-render evidence | NOT RUN | Requires a Studionet consensus transaction |

## Independent connectivity retry

Record the final retry results here with command, timestamp, and exact error:

- GitHub HTTPS/API:
- `gh auth status`:
- Studionet RPC `https://studio.genlayer.com/api`:
- Studionet Explorer `https://explorer-studio.genlayer.com`:

Do not paste a token or private key into this document. If GitHub token refresh is needed, use `gh auth login --web` after connectivity returns.
