# Deployment and Live Verification

## Local preflight

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
genvm-lint check contracts/reality_checkpoint.py
python -m pytest tests -q
```

## Studionet

Current official GenLayer docs list Studionet RPC `https://studio.genlayer.com/api`, chain ID 61999, and Explorer `https://explorer-studio.genlayer.com` ([network reference](https://docs.genlayer.com/developers/networks)). The CLI reference uses `genlayer deploy --contract <path> --rpc <url>` ([CLI deployment](https://docs.genlayer.com/developers/intelligent-contracts/deploying/cli-deployment)).

Run `./deploy.ps1` for local GenVM lint/schema preflight. Once the GenLayer CLI is installed and authenticated, `./deploy.ps1 -Deploy` submits to the canonical Studionet RPC. A returned address/transaction is not proof of consensus finality; inspect transaction lifecycle and Explorer evidence before documenting deployment.

After a real deployment, run the read-only verifier (current official RPC methods: `gen_getContractCode`, `gen_getContractSchema`, and `gen_getTransactionLifecycle`):

```powershell
python scripts/live_verify.py --address 0x... --deployment-tx 0x...
```

It writes the raw lifecycle result, schema method comparison, and local/deployed source SHA-256 values to ignored `artifacts/live-verification.json`. It exits nonzero when source bytes or schema methods differ. It does not deploy or create protocol checkpoints; the live transaction matrix still requires independently recorded write transactions and Explorer evidence.

## Previous Studionet deployment (2026-10-02)

The current canonical deployment was submitted to Studionet and verified in Explorer:

- Contract: `0x69570326e3120c2b9EB96Cc471b235b6adE91501`
- Deployment transaction: `0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3`
- Explorer: <https://explorer-studio.genlayer.com/tx/0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3>
- Explorer lifecycle: `FINALIZED`; GenVM `SUCCESS`; consensus `Accepted`.
- Local and deployed contract bytes matched at the time (SHA-256 `dcf3c321b8d598e24d2d91f6a7c4aae9e0cfd272563dcaf15eb3789e79d4fda7`).

That source passed live rendered-evidence, fork, supported-state, no-change successor, composition, and fail-closed challenge transactions. A challenge attempt receipt then revealed that an added challenge source was not bound to its claim IDs in the preserved-prior receipt. The current local candidate fixes this and includes a regression test. Its SHA-256 is `450dd5c8c25d22e9ac9922df25f3f2c454015171bab643a9b653cda209156df7`; it must be deployed, parity-checked, and run through the unavailable-source challenge before the latest source is considered live-verified. The time-bound material-delta attempt was `UNDETERMINED` after validator disagreement. See `RELEASE_VERIFICATION.md` and `EVIDENCE.md` for exact transactions. Live cycle rejection, a material-delta pass, and challenge recovery are still unverified.

## Required live proofs

1. **Passed:** finalized initial live WEB_RENDER_TEXT resolution from WHO and example.com; both content/render hashes were recorded in `EVIDENCE.md`.
2. **Not passed:** revalidation had `overall_delta=UNCHANGED`, but WHO was `UNKNOWN`; contract correctly preserved the prior. No successor claim.
3. Material delta and successor attribution: still required.
4. **Passed:** source fork with one `SUPPORTED` and one `CONTRADICTED` finding; finalized as `DISPUTED` / `CONTRADICTORY_REALITY`; usability returned `false`.
5. Composition and cycle rejection: still required.
6. Live transport failure preserving a prior finalized checkpoint: still required.
7. Live challenge/revalidation recovery: still required.

Record transaction hashes, lifecycle/finality, explorer URLs, contract address, source commit/blob hash, and deployed-source parity. Do not call an accepted transaction finalized without chain evidence.
