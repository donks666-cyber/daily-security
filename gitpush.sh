#!/bin/bash
# Push git repo to GitHub via API using curl with retries and no temp files.
set -euo pipefail

TOKEN="$1"
OWNER="donks666-cyber"
REPO="daily-security"
API="https://api.github.com/repos/$OWNER/$REPO"
BASE="$(cd "$(dirname "$0")" && pwd)"

CURL="curl -sk --retry 5 --retry-delay 3"

# Get list of tracked files
FILES=($(git -C "$BASE" ls-files))
TOTAL=${#FILES[@]}
echo "Creating $TOTAL blobs..."

TREE_JSON="["
FIRST=true
IDX=0

for FP in "${FILES[@]}"; do
  F="$BASE/$FP"
  [ -f "$F" ] || continue

  # Read file and encode
  if file --mime-encoding "$F" 2>/dev/null | grep -q binary; then
    ENC="base64"
    CONTENT=$(base64 < "$F" | tr -d '\n')
  else
    ENC="utf-8"
    CONTENT=$(python3 -c "
import json, sys
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    print(json.dumps(f.read()))
" "$F")
  fi

  # Create blob - send JSON via stdin pipe (no temp file)
  BLOB=$($CURL -X POST "$API/git/blobs" \
    -H "Authorization: token $TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    -d "{\"content\":$CONTENT,\"encoding\":\"$ENC\"}" 2>/dev/null |
    python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")

  # Escape path for JSON
  P=$(python3 -c "import json,sys; print(json.dumps(sys.argv[1]))" "$FP")

  if $FIRST; then FIRST=false; else TREE_JSON+=","; fi
  TREE_JSON+="{\"path\":$P,\"mode\":\"100644\",\"type\":\"blob\",\"sha\":\"$BLOB\"}"

  IDX=$((IDX + 1))
  [ $((IDX % 50)) -eq 0 ] && echo "  $IDX/$TOTAL"
done

# Submodule
SM=$(git -C "$BASE" ls-tree HEAD themes/m.css 2>/dev/null)
if [ -n "$SM" ]; then
  SM_SHA=$(echo "$SM" | awk '{print $3}')
  $FIRST || TREE_JSON+=","
  TREE_JSON+="{\"path\":\"themes/m.css\",\"mode\":\"160000\",\"type\":\"commit\",\"sha\":\"$SM_SHA\"}"
  echo "  submodule @ ${SM_SHA:0:8}"
fi
TREE_JSON+="]"

echo "Creating tree..."
TREE_SHA=$(echo "$TREE_JSON" | $CURL -X POST "$API/git/trees" \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d @- 2>/dev/null | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
echo "  tree ${TREE_SHA:0:8}"

echo "Creating commit..."
COMMIT_SHA=$($CURL -X POST "$API/git/commits" \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d "{\"message\":\"Initial commit: Pelican blog\",\"tree\":\"$TREE_SHA\",\"parents\":[]}" 2>/dev/null |
  python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
echo "  commit ${COMMIT_SHA:0:8}"

echo "Updating main branch..."
if $CURL -X PATCH "$API/git/refs/heads/main" \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d "{\"sha\":\"$COMMIT_SHA\",\"force\":true}" -o /dev/null -w "%{http_code}" 2>/dev/null | grep -q 200; then
  echo "  ref updated"
else
  $CURL -X POST "$API/git/refs" \
    -H "Authorization: token $TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    -d "{\"ref\":\"refs/heads/main\",\"sha\":\"$COMMIT_SHA"}" -o /dev/null 2>/dev/null
  echo "  ref created"
fi

echo "Done! https://github.com/$OWNER/$REPO"
