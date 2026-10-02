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

No deployment has been submitted from this local build.

## Required live proofs

1. Initial checkpoint with independently rendered and fetched sources; verify final receipt and certificate.
2. Semantic no-change revalidation; verify immutable predecessor and new successor.
3. Material delta; verify per-claim attribution and successor state.
4. Reality fork with supported vs contradicted sources; verify `DISPUTED` and unusable.
5. Composite of finalized children; verify deterministic result and cycle rejection.
6. Transport failure; verify prior finalized checkpoint remains readable and is not superseded.
7. Challenge/revalidation recovery; verify bounded challenge round and lineage.

Record transaction hashes, lifecycle/finality, explorer URLs, contract address, source commit/blob hash, and deployed-source parity. Do not call an accepted transaction finalized without chain evidence.
