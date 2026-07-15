#!/usr/bin/env python3
"""Push repo via Git Data API — creates single commit with all files."""
import os, base64, json, sys, subprocess
import requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TOKEN = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("Usage: python3 push_repo.py <token>")
    sys.exit(1)

OWNER = "donks666-cyber"
REPO = "daily-security"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"
H = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
S = requests.Session()
S.verify = False
BASE = os.path.dirname(os.path.abspath(__file__))

def gh(method, url, data=None):
    r = S.request(method, url, headers=H, json=data)
    if r.status_code >= 400:
        print(f"  HTTP {r.status_code}: {r.text[:150]}")
        r.raise_for_status()
    return r.json() if r.text else {}

# List tracked files (skip .gitmodules, submodule pointer)
res = subprocess.run(["git", "ls-files"], capture_output=True, text=True, cwd=BASE)
files = [f for f in res.stdout.strip().split("\n") if f and f != ".gitmodules"]
print(f"Creating blobs for {len(files)} files...")

tree_entries = []
for i, fp in enumerate(files):
    fpath = os.path.join(BASE, fp)
    if not os.path.isfile(fpath):
        continue
    with open(fpath, "rb") as f:
        content = f.read()
    try:
        text = content.decode("utf-8")
        enc = "utf-8"
    except UnicodeDecodeError:
        text = base64.b64encode(content).decode("ascii")
        enc = "base64"
    blob = gh("POST", f"{API}/git/blobs", {"content": text, "encoding": enc})
    tree_entries.append({"path": fp, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    if (i + 1) % 50 == 0:
        print(f"  blobs {i+1}/{len(files)}")

# Add submodule
res = subprocess.run(["git", "ls-tree", "HEAD", "themes/m.css"],
                     capture_output=True, text=True, cwd=BASE)
parts = res.stdout.strip().split()
if len(parts) >= 3:
    tree_entries.append({"path": "themes/m.css", "mode": "160000", "type": "commit", "sha": parts[2]})
    print(f"  submodule themes/m.css @ {parts[2][:8]}")

print(f"Creating tree with {len(tree_entries)} entries...")
tree = gh("POST", f"{API}/git/trees", {"tree": tree_entries})
print(f"  tree {tree['sha'][:8]}")

print("Creating commit...")
commit = gh("POST", f"{API}/git/commits", {
    "message": "Initial commit: Pelican blog",
    "tree": tree["sha"],
    "parents": [],
})
print(f"  commit {commit['sha'][:8]}")

print("Updating main branch...")
try:
    ref = gh("PATCH", f"{API}/git/refs/heads/main", {"sha": commit["sha"], "force": True})
    print(f"  ref updated to {ref['object']['sha'][:8]}")
except Exception:
    gh("POST", f"{API}/git/refs", {"ref": "refs/heads/main", "sha": commit["sha"]})
    print(f"  ref created")

print(f"Done! https://github.com/{OWNER}/{REPO}")
