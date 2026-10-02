"""Compare a local contract with source exported from GenLayer RPC/CLI."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("local", type=Path)
    parser.add_argument("deployed", type=Path, help="exact exported deployed source bytes")
    args = parser.parse_args()
    local_hash, deployed_hash = digest(args.local), digest(args.deployed)
    print(f"local sha256:    {local_hash}")
    print(f"deployed sha256: {deployed_hash}")
    if local_hash != deployed_hash:
        print("SOURCE PARITY: MISMATCH")
        return 1
    print("SOURCE PARITY: MATCH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
