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
| Initial implementation commit | `b78f4b7bb4282fcda6350a67a62a99bd6ea62691` |
| Local branch | `main` |
| Remote | `https://github.com/Chinny070/Reality-checkpoint-protocol-` |
| Starting HEAD | Empty local repository; no prior commit |
| Commit SHA | `b78f4b7bb4282fcda6350a67a62a99bd6ea62691` (implementation commit) |
| Contract Git blob SHA | `164cdc7cc3804ed00dd9960a1d3af21f3bcb75b7` |
| Contract SHA-256 | `ade566d3dea6b78ce316da3755d9f21957824efd8163266f3daec6781be7d1f5` |
| Working tree after implementation commit | Clean |
| Push | Not completed; exact transport error below |

Git metadata lives in `.gitmeta` within the authorized project directory because the inherited `.git` metadata has an ownership mismatch and cannot safely be rewritten in this session. Git commands use explicit `--git-dir=.gitmeta --work-tree=.`. No global `safe.directory` setting was changed.

## Hosted external gates

| Gate | Result | Evidence |
|---|---|---|
| GitHub API/push | BLOCKED | Independent connection failure below; no remote write claimed |
| Studionet deploy | BLOCKED | Studionet transport denied; CLI also requires local keystore unlock (no transaction submitted) |
| Consensus transactions | NOT RUN | Requires a deployed Studionet contract |
| Explorer verification | BLOCKED / NOT RUN | Explorer HTTPS TCP probe failed; also requires an actual deployment and transaction |
| Deployed-source parity | NOT RUN | Requires deployed code/source data |
| Real live web-render evidence | NOT RUN | Requires a Studionet consensus transaction |

## Independent connectivity retry

Final independent retry on 2026-10-02 (UTC; work carried out in `C:\Users\USERpc\OneDrive\Desktop\Reality checkpoint`):

- GitHub `git ls-remote origin HEAD`: `fatal: unable to access 'https://github.com/Chinny070/Reality-checkpoint-protocol-/': Failed to connect to github.com port 443 after 138 ms: Could not connect to server`.
- GitHub REST API request: `SocketException: An attempt was made to access a socket in a way forbidden by its access permissions. (api.github.com:443)`.
- GitHub push attempt: same connection failure, after 74 ms. No refs were pushed.
- `gh auth status`: account `Chinny070` is active in the CLI, but its saved default token is invalid; CLI recommends `gh auth login -h github.com`. Web login was not attempted because HTTPS transport is blocked.
- Studionet JSON-RPC probe via `scripts/live_verify.py`: `gen_getContractCode network request failed: URLError: <urlopen error [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions>`.
- `Test-NetConnection studio.genlayer.com -Port 443`: DNS resolved `172.67.210.182` and `104.21.53.84`; TCP connect failed to both, `TcpTestSucceeded: False`.
- Studionet Explorer `explorer-studio.genlayer.com`: DNS resolved the same Cloudflare addresses; `Test-NetConnection` TCP 443 failed to both (`TcpTestSucceeded: False`).
- GenLayer CLI availability: `genlayer` is installed. `deploy.ps1 -Deploy` passed lint and schema extraction and reached the CLI's keystore prompt; the local unlock attempt returned `Invalid password. Attempt 2/3`. No transaction hash was returned or submitted. The wallet must be unlocked through the local secure CLI flow; no password or key was copied into chat or the repository.

Do not paste a token or private key into this document. If GitHub token refresh is needed, use `gh auth login --web` after connectivity returns.

## Clean checkout portability

The initial clean local bundle clone exposed Windows checkout line-ending conversion for the Python contract. `.gitattributes` now pins LF for protocol source and documentation. A fresh bundle clone must reproduce the contract SHA-256 exactly before release; see the final local verification below.
