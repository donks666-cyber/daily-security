#!/usr/bin/env python3
"""Fast concurrent upload of blog files to GitHub via Contents API."""
import os, base64, sys, json
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TOKEN = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("Usage: python3 upload_to_github.py <token>")
    sys.exit(1)

OWNER = "donks666-cyber"
REPO = "daily-security"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
BASE = os.path.dirname(os.path.abspath(__file__))
POOL = 20

def get_sha(path):
    r = requests.get(f"{API}/{path}", headers=HEADERS, verify=False)
    return r.json().get("sha") if r.ok else None

def upload_file(path):
    full = os.path.join(BASE, path)
    with open(full, "rb") as f:
        content = f.read()
    b64 = base64.b64encode(content).decode("ascii")
    data = {"message": f"Add {path}", "content": b64}
    sha = get_sha(path)
    if sha:
        data["sha"] = sha
    r = requests.put(f"{API}/{path}", headers=HEADERS, json=data, verify=False)
    return path, r.ok, r.status_code

essential_files = [
    "pelicanconf.py", "publishconf.py", "requirements.txt",
    "generate_search_index.py", "stork-config.toml", "Makefile", ".gitignore",
]
essential_dirs = ["content", "themes/daily-security", "themes/m.css/plugins"]

files = []
for f in essential_files:
    if os.path.isfile(os.path.join(BASE, f)):
        files.append(f)
for d in essential_dirs:
    dp = os.path.join(BASE, d)
    if os.path.isdir(dp):
        for root, dirs, filenames in os.walk(dp):
            dirs[:] = [x for x in dirs if x != "__pycache__"]
            for fn in filenames:
                files.append(os.path.relpath(os.path.join(root, fn), BASE))

print(f"Uploading {len(files)} files ({POOL} concurrent)...")
ok = fail = 0
with ThreadPoolExecutor(max_workers=POOL) as ex:
    fut = {ex.submit(upload_file, f): f for f in files}
    for f in as_completed(fut):
        path, success, code = f.result()
        if success:
            ok += 1
        else:
            fail += 1
            print(f"  FAIL {path} ({code})")
        if (ok + fail) % 50 == 0:
            print(f"  Progress: {ok+fail}/{len(files)}")

print(f"Done! {ok} OK, {fail} failed")
print(f"https://github.com/{OWNER}/{REPO}")
