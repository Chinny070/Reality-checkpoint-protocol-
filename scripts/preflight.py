"""Offline source preflight for the single deployable RCP contract."""

from __future__ import annotations

import ast
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "reality_checkpoint.py"
EXPECTED_PUBLIC = {
    "create_checkpoint", "resolve_checkpoint", "revalidate", "challenge",
    "create_composite", "get_checkpoint", "get_receipt", "get_certificate",
    "get_children", "is_checkpoint_usable",
}


def main() -> int:
    source = CONTRACT.read_bytes()
    tree = ast.parse(source, filename=str(CONTRACT))
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    deployable = [node for node in classes if node.name == "RealityCheckpoint"]
    if len(deployable) != 1:
        raise SystemExit("preflight failed: expected exactly one canonical RealityCheckpoint class")
    methods = {node.name for node in deployable[0].body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
    missing = EXPECTED_PUBLIC - methods
    if missing:
        raise SystemExit(f"preflight failed: missing API methods {sorted(missing)}")
    if "gl.nondet.web.render" not in source.decode("utf-8"):
        raise SystemExit("preflight failed: browser-render path missing")
    if "gl.vm.run_nondet" not in source.decode("utf-8"):
        raise SystemExit("preflight failed: independent validator path missing")
    print(f"preflight passed: one canonical contract, {len(EXPECTED_PUBLIC)} public API methods")
    print(f"contract sha256: {hashlib.sha256(source).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
