#!/usr/bin/env python3
"""Push repo to GitHub via Git Data API + curl with retry."""
import os, sys, subprocess, json, base64, time

GH = "https://api.github.com/repos/donks666-cyber/daily-security"
TMP = "/tmp/_gh_push.json"

def curl(method, url, data=None, desc=""):
    for attempt in range(5):
        cmd = ["curl", "-sk", "-X", method, url,
               "-H", f"Authorization: token {TOKEN}",
               "-H", "Accept: application/vnd.github.v3+json"]
        if data is not None:
            with open(TMP, "w") as f:
                f.write(data)
            cmd += ["-d", f"@{TMP}"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0 and r.stdout.strip():
            return json.loads(r.stdout)
        print(f"  retry {attempt+1}/5 ({desc}) rc={r.returncode}", flush=True)
        time.sleep(2)
    print(f"  FAILED ({desc}) rc={r.returncode} stderr={r.stderr[:200]}")
    sys.exit(1)

TOKEN = sys.argv[1] if len(sys.argv) > 1 else os.environ["GITHUB_TOKEN"]
BASE = os.path.dirname(os.path.abspath(__file__))

res = subprocess.run(["git", "ls-files"], capture_output=True, text=True, cwd=BASE)
files = [f for f in res.stdout.strip().split("\n") if f]
print(f"Creating {len(files)} blobs...", flush=True)

tree = []
for i, fp in enumerate(files, 1):
    fpath = os.path.join(BASE, fp)
    if not os.path.isfile(fpath):
        continue
    with open(fpath, "rb") as f:
        content = f.read()
    try:
        blob = json.dumps({"content": content.decode("utf-8"), "encoding": "utf-8"})
    except UnicodeDecodeError:
        blob = json.dumps({"content": base64.b64encode(content).decode(), "encoding": "base64"})
    result = curl("POST", f"{GH}/git/blobs", blob, f"blob {fp}")
    tree.append({"path": fp, "mode": "100644", "type": "blob", "sha": result["sha"]})
    if i % 50 == 0:
        print(f"  {i}/{len(files)}", flush=True)

res = subprocess.run(["git", "ls-tree", "HEAD", "themes/m.css"], capture_output=True, text=True, cwd=BASE)
parts = res.stdout.strip().split()
if len(parts) >= 3:
    tree.append({"path": "themes/m.css", "mode": "160000", "type": "commit", "sha": parts[2]})
    print(f"  submodule @ {parts[2][:8]}", flush=True)

print(f"Creating tree ({len(tree)} entries)...", flush=True)
result = curl("POST", f"{GH}/git/trees", json.dumps({"tree": tree}), "tree")
tree_sha = result["sha"]
print(f"  tree {tree_sha[:8]}", flush=True)

print("Creating commit...", flush=True)
result = curl("POST", f"{GH}/git/commits",
    json.dumps({"message": "Initial commit: Pelican blog", "tree": tree_sha, "parents": []}), "commit")
commit_sha = result["sha"]
print(f"  commit {commit_sha[:8]}", flush=True)

print("Updating branch...", flush=True)
try:
    curl("PATCH", f"{GH}/git/refs/heads/main",
        json.dumps({"sha": commit_sha, "force": True}), "ref")
    print("  ref updated", flush=True)
except Exception:
    curl("POST", f"{GH}/git/refs",
        json.dumps({"ref": "refs/heads/main", "sha": commit_sha}), "ref create")
    print("  ref created", flush=True)

for f in [TMP]:
    try: os.remove(f)
    except: pass

print(f"Done! https://github.com/donks666-cyber/daily-security", flush=True)
