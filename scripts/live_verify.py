"""Read-only Studionet code/schema/lifecycle and source-parity verification."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


RPC = "https://studio.genlayer.com/api"
EXPECTED_METHODS = {
    "challenge", "create_checkpoint", "create_composite", "get_certificate",
    "get_checkpoint", "get_children", "get_receipt", "is_checkpoint_usable",
    "resolve_checkpoint", "revalidate",
}


def rpc_call(endpoint: str, method: str, params: dict) -> object:
    request = Request(endpoint, data=json.dumps({
        "jsonrpc": "2.0", "method": method, "params": [params], "id": 1,
    }).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"{method} network request failed: {type(exc).__name__}: {exc}") from exc
    if "error" in payload:
        raise RuntimeError(f"{method} RPC error: {payload['error']}")
    if "result" not in payload:
        raise RuntimeError(f"{method} response missing result")
    return payload["result"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rpc", default=RPC)
    parser.add_argument("--address", required=True)
    parser.add_argument("--deployment-tx", required=True)
    parser.add_argument("--source", type=Path, default=Path("contracts/reality_checkpoint.py"))
    parser.add_argument("--output", type=Path, default=Path("artifacts/live-verification.json"))
    args = parser.parse_args()

    try:
        code_b64 = rpc_call(args.rpc, "gen_getContractCode", {"address": args.address, "status": "finalized"})
        if not isinstance(code_b64, str):
            raise RuntimeError("gen_getContractCode returned a non-string result")
        deployed = base64.b64decode(code_b64, validate=True)
        schema = rpc_call(args.rpc, "gen_getContractSchema", {"code": code_b64})
        lifecycle = rpc_call(args.rpc, "gen_getTransactionLifecycle", {"txId": args.deployment_tx})
    except (RuntimeError, ValueError) as exc:
        raise SystemExit(str(exc))

    local = args.source.read_bytes()
    methods = set(schema.get("methods", {})) if isinstance(schema, dict) else set()
    record = {
        "network": "studionet", "rpc": args.rpc, "chain_id": 61999,
        "contract_address": args.address,
        "explorer_url": f"https://explorer-studio.genlayer.com/address/{args.address}",
        "deployment_tx": args.deployment_tx,
        "lifecycle": lifecycle,
        "schema_method_names": sorted(methods),
        "schema_methods_match_expected": methods == EXPECTED_METHODS,
        "local_source_sha256": hashlib.sha256(local).hexdigest(),
        "deployed_source_sha256": hashlib.sha256(deployed).hexdigest(),
        "deployed_source_parity": local == deployed,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))
    if not record["schema_methods_match_expected"] or not record["deployed_source_parity"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
