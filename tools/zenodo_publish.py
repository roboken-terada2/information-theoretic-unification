"""
zenodo_publish.py — End-to-end Zenodo publication automation.

Workflow:
  1. Create deposit on Zenodo (sandbox or production).
  2. Upload metadata (title, description, authors, license, keywords, related identifiers).
  3. Upload paper ZIP file.
  4. Publish and obtain DOI.
  5. Optionally: substitute DOI placeholder in local paper files.
  6. Optionally: git add + commit + tag + push.
  7. Print summary.

Usage:
  python tools/zenodo_publish.py \
    --metadata for_qc_v2_paper/zenodo_metadata.json \
    --zip ITU_Tier1plus_01_QC_mKQEC_v1.0.0.zip \
    --package-dir for_qc_v2_paper \
    --git-subdir papers/qc-deep \
    --git-tag qc-deep-paper-v1.0.0 \
    --git-commit-message "Add Tier 1+ #1 mKQEC ..." \
    [--sandbox] \
    [--dry-run] \
    [--skip-git]

Env vars:
  ZENODO_TOKEN          — production token
  ZENODO_SANDBOX_TOKEN  — sandbox token (when --sandbox)

Reads token from env first; falls back to ~/.zenodo_token (chmod 600).
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import time
from typing import Any, Optional

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library not installed. Run: python -m pip install requests")
    sys.exit(1)


# ---------- API endpoints ----------

PROD_BASE = "https://zenodo.org/api"
SANDBOX_BASE = "https://sandbox.zenodo.org/api"


# ---------- Token loading ----------

def _clean_token(raw: str) -> str:
    """Strip whitespace, BOM, and any non-ASCII control chars."""
    # Remove UTF-8 BOM if present
    if raw.startswith("﻿"):
        raw = raw[1:]
    return raw.strip()


def load_token(sandbox: bool) -> str:
    env_name = "ZENODO_SANDBOX_TOKEN" if sandbox else "ZENODO_TOKEN"
    token = os.environ.get(env_name)
    if token:
        return _clean_token(token)

    # Fallback to ~/.zenodo_token (sandbox.zenodo_token)
    home = pathlib.Path.home()
    fname = ".zenodo_sandbox_token" if sandbox else ".zenodo_token"
    p = home / fname
    if p.exists():
        # Read as bytes first to handle BOM cleanly
        raw_bytes = p.read_bytes()
        if raw_bytes.startswith(b"\xef\xbb\xbf"):
            raw_bytes = raw_bytes[3:]
        return _clean_token(raw_bytes.decode("utf-8"))

    raise RuntimeError(
        f"No Zenodo token found. Set {env_name} env var or create {p}\n"
        f"  Get token at: https://{'sandbox.' if sandbox else ''}zenodo.org/account/settings/applications/tokens/new/"
    )


# ---------- Zenodo API wrapper ----------

class ZenodoClient:
    def __init__(self, token: str, sandbox: bool = False, dry_run: bool = False):
        self.token = token
        self.base = SANDBOX_BASE if sandbox else PROD_BASE
        self.dry_run = dry_run
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    def _request(self, method: str, path: str, **kwargs):
        url = f"{self.base}{path}"
        if self.dry_run:
            print(f"[DRY-RUN] {method} {url}")
            if "json" in kwargs:
                print(f"  Body keys: {list(kwargs['json'].keys()) if isinstance(kwargs['json'], dict) else 'list'}")
            # Return mock response object
            class MockResp:
                status_code = 200
                def json(self): return {"id": 99999999, "links": {"self": url, "publish": url, "bucket": "mock-bucket"}, "doi": "10.5281/zenodo.DRYRUN", "record_id": 99999999}
                def raise_for_status(self): pass
                text = "DRY-RUN"
            return MockResp()
        r = self.session.request(method, url, **kwargs)
        if r.status_code >= 400:
            print(f"ERROR {r.status_code}: {r.text[:500]}", file=sys.stderr)
        r.raise_for_status()
        return r

    def create_deposition(self) -> dict:
        """Step 1: POST empty deposit."""
        r = self._request("POST", "/deposit/depositions", json={})
        return r.json()

    def update_metadata(self, deposit_id: int, metadata: dict) -> dict:
        """Step 2: PUT metadata."""
        r = self._request("PUT", f"/deposit/depositions/{deposit_id}",
                          json={"metadata": metadata})
        return r.json()

    def upload_file(self, bucket_url: str, file_path: str) -> dict:
        """Step 3: PUT file to bucket."""
        path = pathlib.Path(file_path)
        if not path.exists():
            raise FileNotFoundError(file_path)
        if self.dry_run:
            print(f"[DRY-RUN] PUT {bucket_url}/{path.name} ({path.stat().st_size} bytes)")
            return {"key": path.name, "size": path.stat().st_size}
        with open(path, "rb") as fp:
            # Bucket upload uses different auth context (no Content-Type JSON)
            headers = {"Authorization": f"Bearer {self.token}"}
            r = requests.put(f"{bucket_url}/{path.name}", data=fp, headers=headers)
            if r.status_code >= 400:
                print(f"ERROR {r.status_code}: {r.text[:500]}", file=sys.stderr)
            r.raise_for_status()
        return r.json()

    def publish(self, deposit_id: int) -> dict:
        """Step 4: POST publish action."""
        r = self._request("POST", f"/deposit/depositions/{deposit_id}/actions/publish")
        return r.json()


# ---------- Post-DOI helpers ----------

def substitute_doi(package_dir: str, placeholder: str, doi: str, dry_run: bool = False) -> list:
    """Replace placeholder DOI in all package files."""
    updated = []
    pkg = pathlib.Path(package_dir)
    for p in pkg.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in (".md", ".cff", ".py", ".txt", ".json", ".yaml", ".yml"):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if placeholder in text:
            if not dry_run:
                new_text = text.replace(placeholder, doi)
                p.write_text(new_text, encoding="utf-8")
            updated.append(str(p))
    return updated


def git_workflow(git_repo: str, git_subdir: str, package_dir: str, tag: str,
                 message: str, dry_run: bool = False) -> None:
    """Copy package to GitHub subdir, commit, tag, push."""
    repo = pathlib.Path(git_repo)
    target = repo / git_subdir
    target.mkdir(parents=True, exist_ok=True)
    src = pathlib.Path(package_dir)
    # Copy contents
    if dry_run:
        print(f"[DRY-RUN] Copy {src}/* → {target}/")
    else:
        for item in src.iterdir():
            if item.is_file():
                target_path = target / item.name
                target_path.write_bytes(item.read_bytes())
        print(f"  Copied {src} → {target}")

    def run(cmd: list[str]):
        if dry_run:
            print(f"[DRY-RUN] {' '.join(cmd)} (cwd={repo})")
            return ""
        proc = subprocess.run(cmd, cwd=repo, capture_output=True, text=True)
        if proc.returncode != 0:
            print(f"git ERROR ({' '.join(cmd)}):\n{proc.stderr}", file=sys.stderr)
            raise SystemExit(proc.returncode)
        return proc.stdout

    run(["git", "add", git_subdir])
    run(["git", "commit", "-m", message])
    run(["git", "tag", "-a", tag, "-m", f"{tag} — auto-published by zenodo_publish.py"])
    run(["git", "push", "origin", "main"])
    run(["git", "push", "origin", tag])
    print(f"  Pushed commit + tag {tag} to origin/main")


# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--metadata", required=True, help="JSON file with Zenodo metadata")
    ap.add_argument("--zip", required=True, help="Path to ZIP file to upload")
    ap.add_argument("--package-dir", required=True, help="Directory with source files (for DOI substitution)")
    ap.add_argument("--doi-placeholder", default="10.5281/zenodo.XXXXX", help="DOI placeholder string to substitute")
    ap.add_argument("--git-repo", default="for_github", help="Local git repo path (relative to cwd)")
    ap.add_argument("--git-subdir", help="Subdirectory under <repo>/papers/ to copy files (e.g. papers/qc-deep)")
    ap.add_argument("--git-tag", help="Git tag to create (e.g. qc-deep-paper-v1.0.0)")
    ap.add_argument("--git-commit-message", help="Commit message")
    ap.add_argument("--skip-git", action="store_true", help="Skip git workflow")
    ap.add_argument("--sandbox", action="store_true", help="Use Zenodo sandbox instead of production")
    ap.add_argument("--dry-run", action="store_true", help="Print API calls but do not execute")
    args = ap.parse_args()

    # Load metadata
    with open(args.metadata, "r", encoding="utf-8") as f:
        metadata = json.load(f)
    # Auto-inject default ORCID for Terada Munehiro if missing
    DEFAULT_ORCID = "0009-0008-0191-5831"
    for creator in metadata.get("creators", []):
        if creator.get("name", "").startswith("Terada") and "orcid" not in creator:
            creator["orcid"] = DEFAULT_ORCID
            print(f"[auto] Injected default ORCID for Terada: {DEFAULT_ORCID}")
    print(f"Loaded metadata: '{metadata.get('title', '<no title>')[:80]}...'")

    # Load token
    try:
        token = load_token(args.sandbox)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"Token loaded ({'sandbox' if args.sandbox else 'production'}, length={len(token)})")

    # Initialize client
    client = ZenodoClient(token, sandbox=args.sandbox, dry_run=args.dry_run)

    # Step 1: Create deposition
    print("\n[1/5] Creating deposit ...")
    deposit = client.create_deposition()
    deposit_id = deposit["id"]
    bucket = deposit["links"].get("bucket")
    print(f"  Deposit ID: {deposit_id}")
    print(f"  Bucket: {bucket}")

    # Step 2: Update metadata
    print("\n[2/5] Setting metadata ...")
    client.update_metadata(deposit_id, metadata)
    print(f"  Title: {metadata.get('title', '?')[:80]}...")

    # Step 3: Upload file
    print(f"\n[3/5] Uploading {args.zip} ...")
    client.upload_file(bucket, args.zip)
    print(f"  File uploaded.")

    # Step 4: Publish
    print("\n[4/5] Publishing ...")
    published = client.publish(deposit_id)
    doi = published.get("doi") or published.get("metadata", {}).get("doi", "10.5281/zenodo.UNKNOWN")
    record_id = published.get("record_id", deposit_id)
    print(f"  DOI: {doi}")
    print(f"  Record URL: https://{'sandbox.' if args.sandbox else ''}zenodo.org/records/{record_id}")

    # Step 5: Post-publish substitutions and git
    print("\n[5/5] Post-publish workflow ...")
    updated = substitute_doi(args.package_dir, args.doi_placeholder, doi, dry_run=args.dry_run)
    print(f"  DOI substituted in {len(updated)} files:")
    for u in updated[:8]:
        print(f"    {u}")
    if len(updated) > 8:
        print(f"    ... and {len(updated) - 8} more")

    if not args.skip_git and args.git_subdir and args.git_tag and args.git_commit_message:
        print(f"\n  Git workflow ({args.git_subdir} → tag {args.git_tag}) ...")
        git_workflow(args.git_repo, args.git_subdir, args.package_dir,
                     args.git_tag, args.git_commit_message, dry_run=args.dry_run)

    print("\n" + "=" * 70)
    print(f"  SUCCESS — DOI: {doi}")
    print("=" * 70)
    return doi


if __name__ == "__main__":
    main()
