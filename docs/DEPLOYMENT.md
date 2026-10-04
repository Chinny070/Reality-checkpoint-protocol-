# Deployment and Live Verification

## Local preflight

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
genvm-lint check contracts/reality_checkpoint.py
python -m pytest tests/test_protocol.py -q
gltest tests/direct/test_contract.py -q
```

## Studionet

Current official GenLayer docs list Studionet RPC `https://studio.genlayer.com/api`, chain ID 61999, and Explorer `https://explorer-studio.genlayer.com` ([network reference](https://docs.genlayer.com/developers/networks)). The CLI reference uses `genlayer deploy --contract <path> --rpc <url>` ([CLI deployment](https://docs.genlayer.com/developers/intelligent-contracts/deploying/cli-deployment)).

Run `./deploy.ps1` for local GenVM lint/schema preflight. Once the GenLayer CLI is installed and authenticated, `./deploy.ps1 -Deploy` submits to the canonical Studionet RPC. A returned address/transaction is not proof of consensus finality; inspect transaction lifecycle and Explorer evidence before documenting deployment.

After a real deployment, verify finality with `genlayer receipt`, inspect the deployed schema with `genlayer schema`, and export code with `genlayer code`. Compare exported contract bytes against the local source. The Python JSON-RPC verifier below may receive HTTP 403 in restricted environments; the authenticated GenLayer CLI is the fallback used for the current verification.

```powershell
python scripts/live_verify.py --address 0x... --deployment-tx 0x...
```

It writes the raw lifecycle result, schema method comparison, and local/deployed source SHA-256 values to ignored `artifacts/live-verification.json`. It exits nonzero when source bytes or schema methods differ. It does not deploy or create protocol checkpoints; the live transaction matrix still requires independently recorded write transactions and Explorer evidence.

## Steward-fix deployment (2026-10-04)

- Canonical current source: `contracts/reality_checkpoint.py`, SHA-256 `26ca41afe295bdacfded56976d99dfde3839a62d150c5b6a35e88f645740f1ee`, Git blob `1ecd8894b4299a7586452a0dc151e3bfa5abe0f2`.
- Contract: [`0x31d3981d162BcE0E91785E9eCAa2c957639B7764`](https://explorer-studio.genlayer.com/address/0x31d3981d162BcE0E91785E9eCAa2c957639B7764).
- Deployment: [`0xf4f79ac806a81678c8bbc80384a2efd364cc466d71f3c12bbbd8085c18faca6a`](https://explorer-studio.genlayer.com/tx/0xf4f79ac806a81678c8bbc80384a2efd364cc466d71f3c12bbbd8085c18faca6a), FINALIZED, GenVM SUCCESS, MAJORITY_AGREE; all five validators agreed.
- SDK-exported source is 59,671 bytes and byte-identical to the local source. The deployed schema has the ten expected methods.
- Current-source proof transactions and their exact limits are recorded in [EVIDENCE.md](EVIDENCE.md). The admitted-source plus unresolved-second-claim attempt-accounting behavior is verified by Direct Mode regression; it is not claimed as a live transaction.

## Previous Studionet deployment (2026-10-02)

Historical deployment (source hash `dcf3c321…d4fda7`) verified in Explorer:

- Contract: `0x69570326e3120c2b9EB96Cc471b235b6adE91501`
- Deployment transaction: `0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3`
- Explorer: <https://explorer-studio.genlayer.com/tx/0x3424b0007d4631fc45215ace751c17d61a477bca4c316aba7e5eeca7322453f3>
- Explorer lifecycle: `FINALIZED`; GenVM `SUCCESS`; consensus `Accepted`.
- Local and deployed contract bytes matched at the time (SHA-256 `dcf3c321b8d598e24d2d91f6a7c4aae9e0cfd272563dcaf15eb3789e79d4fda7`).

Historical source `386103fd111f6280b94f78a9508084e1ba72503d1d7824de5189d75218f9cbf0` was deployed at `0xDc01B2807A2D9285C9F9359930b8076ac89d6688`; its prior live proofs are version-specific and do not establish corrected-source behavior.

## Corrected source deployment (2026-10-03)

- Source SHA-256: `2ca8e45982d88184b845df6441a9e6c2667af9ecc2bed88754964d8bb788a37d` (Git blob `c7b915d9a137a25646b6ca4468f5cb154c371c2b`; source commit `66d87907b04ab8b7490ace2f02403be177350a98`).
- Contract: `0xbEFbE69a1723E637691a7c2De76b5d01D81a41A2`.
- Deployment transaction: [0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd](https://explorer-studio.genlayer.com/tx/0xff8d674e59804edeeadf085a2fc122d5726e9068cc7c217a538ec1742ca88bdd), FINALIZED, GenVM SUCCESS, MAJORITY_AGREE.
- Exported source matched byte-for-byte (59,431 bytes); the live schema exposed all 10 expected methods. The Python JSON-RPC verifier returned HTTP 403; authenticated GenLayer SDK/CLI export and schema reads succeeded.
- Validator-bound receipt proof and hostile same-domain source rejection both finalized with `MAJORITY_AGREE`; the latter preserved checkpoint 2 as SUPPORTED and usable. Full transaction hashes and receipt facts are in [EVIDENCE.md](EVIDENCE.md).

## Historical live proofs on earlier source versions

1. **Historical, claim result limited:** earlier WEB_RENDER_TEXT transaction retrieved WHO and example.com. WHO claim was UNKNOWN; example.com claim SUPPORTED; overall INCONCLUSIVE. Render observations are not described as a fully supported render checkpoint.
2. **Passed:** time-cutoff revalidation created successor checkpoint 2 with `CONTRADICTION` claim delta and predecessor 1; successor was DISPUTED/unusable.
3. **Passed:** source fork with one SUPPORTED and one CONTRADICTED finding; finalized `DISPUTED` / `CONTRADICTORY_REALITY`, usability false.
4. **Passed:** composition of supported checkpoints 4 and 5 yielded checkpoint 6, SUPPORTED/CONSISTENT, FRESH and usable.
5. **Passed:** invalid future/self reference attempt finalized `checkpoint not found` without mutation; immutable composition accepts finalized children only.
6. **Passed:** unavailable external source challenge preserved checkpoint 2 and bound the failed source to claim C1 in its attempt receipt.
7. Initial `INCONCLUSIVE`/`UNAVAILABLE` is terminal for that checkpoint ID; create a replacement checkpoint to retry. A later challenge only applies to an already `FINALIZED` checkpoint.

Record transaction hashes, lifecycle/finality, explorer URLs, contract address, source commit/blob hash, and deployed-source parity. Do not call an accepted transaction finalized without chain evidence.
