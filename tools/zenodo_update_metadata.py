"""
zenodo_update_metadata.py — Update metadata on already-published Zenodo records.

Workflow:
  1. POST /api/deposit/depositions/{id}/actions/edit  (unlock for editing)
  2. PUT  /api/deposit/depositions/{id}               (update metadata)
  3. POST /api/deposit/depositions/{id}/actions/publish (re-publish, same DOI)

Usage:
  python tools/zenodo_update_metadata.py \
    --record-id 20269435 \
    --metadata for_qc_v2_paper/zenodo_metadata.json \
    [--sandbox] [--dry-run]
"""

from __future__ import annotations
import argparse, json, os, pathlib, sys
import requests


def _clean_token(raw: str) -> str:
    if raw.startswith("﻿"):
        raw = raw[1:]
    return raw.strip()


def load_token(sandbox: bool) -> str:
    env_name = "ZENODO_SANDBOX_TOKEN" if sandbox else "ZENODO_TOKEN"
    if os.environ.get(env_name):
        return _clean_token(os.environ[env_name])
    p = pathlib.Path.home() / (".zenodo_sandbox_token" if sandbox else ".zenodo_token")
    if p.exists():
        raw = p.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raw = raw[3:]
        return _clean_token(raw.decode("utf-8"))
    raise RuntimeError(f"No token found ({env_name} env or {p})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record-id", type=int, required=True, help="Zenodo record/deposit ID")
    ap.add_argument("--metadata", required=True, help="JSON file with updated metadata")
    ap.add_argument("--sandbox", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    base = "https://sandbox.zenodo.org/api" if args.sandbox else "https://zenodo.org/api"
    token = load_token(args.sandbox)
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    with open(args.metadata, "r", encoding="utf-8") as f:
        meta = json.load(f)

    rid = args.record_id
    if args.dry_run:
        print(f"[DRY-RUN] Would update record {rid}")
        print(f"  Title: {meta.get('title','?')[:80]}...")
        print(f"  Creators: {meta.get('creators')}")
        return

    # Step 1: Edit (unlock)
    print(f"[1/3] Unlock record {rid} for editing...")
    r = requests.post(f"{base}/deposit/depositions/{rid}/actions/edit", headers=headers)
    if r.status_code not in (200, 201):
        # 403 with "already_locked" may mean already in edit mode — try update directly
        if r.status_code == 403 and "already" in r.text.lower():
            print(f"  Already unlocked (re-using existing draft).")
        else:
            print(f"  ERROR {r.status_code}: {r.text[:300]}", file=sys.stderr)
            r.raise_for_status()
    else:
        print(f"  OK")

    # Step 2: Update metadata
    print(f"[2/3] Update metadata...")
    r = requests.put(f"{base}/deposit/depositions/{rid}",
                     headers=headers, json={"metadata": meta})
    if r.status_code >= 400:
        print(f"  ERROR {r.status_code}: {r.text[:500]}", file=sys.stderr)
        r.raise_for_status()
    print(f"  OK")

    # Step 3: Re-publish
    print(f"[3/3] Re-publish...")
    r = requests.post(f"{base}/deposit/depositions/{rid}/actions/publish", headers=headers)
    if r.status_code >= 400:
        print(f"  ERROR {r.status_code}: {r.text[:500]}", file=sys.stderr)
        r.raise_for_status()
    result = r.json()
    print(f"  OK — DOI: {result.get('doi','?')}")
    print(f"\n  Record URL: https://{'sandbox.' if args.sandbox else ''}zenodo.org/records/{rid}")


if __name__ == "__main__":
    main()
