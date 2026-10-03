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

After a real deployment, verify finality with `genlayer receipt`, inspect the deployed schema with `genlayer schema`, and export code with `genlayer code`. Compare exported contract bytes against the local source. The Python JSON-RPC verifier below may receive HTTP 403 in restricted environments; the authenticated GenLayer CLI is the fallback used for the current verification.

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

Earlier source versions provided initial render, fork, supported-state, successor, composition, and challenge-preservation evidence. Current canonical source `386103fd111f6280b94f78a9508084e1ba72503d1d7824de5189d75218f9cbf0` is deployed at `0xDc01B2807A2D9285C9F9359930b8076ac89d6688` via finalized transaction `0xc953efe708125c4bec7669398e368c9f84184e1fb392638b80cec279073166c6`; source parity is byte-identical (53,413 bytes), and the live schema exposes ten methods. Its live time-cutoff successor, fail-closed challenge, render retrieval, composition, fork, and future/self-reference rejection proofs are recorded in [EVIDENCE.md](EVIDENCE.md) and [RELEASE_VERIFICATION.md](RELEASE_VERIFICATION.md). Challenge recovery after a failed attempt has not been proven; no live cycle can be formed through the finalized-child-only API.

## Required live proofs

1. **Observed, claim result limited:** current source WEB_RENDER_TEXT transaction retrieved WHO and example.com. WHO claim was UNKNOWN; example.com claim SUPPORTED; overall INCONCLUSIVE. Render observations are not described as a fully supported render checkpoint.
2. **Passed:** time-cutoff revalidation created successor checkpoint 2 with `CONTRADICTION` claim delta and predecessor 1; successor was DISPUTED/unusable.
3. **Passed:** source fork with one SUPPORTED and one CONTRADICTED finding; finalized `DISPUTED` / `CONTRADICTORY_REALITY`, usability false.
4. **Passed:** composition of supported checkpoints 4 and 5 yielded checkpoint 6, SUPPORTED/CONSISTENT, FRESH and usable.
5. **Passed:** invalid future/self reference attempt finalized `checkpoint not found` without mutation; immutable composition accepts finalized children only.
6. **Passed:** unavailable external source challenge preserved checkpoint 2 and bound the failed source to claim C1 in its attempt receipt.
7. Challenge recovery after failure is not demonstrated. It is distinct from the verified fail-closed preservation behavior.

Record transaction hashes, lifecycle/finality, explorer URLs, contract address, source commit/blob hash, and deployed-source parity. Do not call an accepted transaction finalized without chain evidence.
