#!/usr/bin/env bash
# Publish the archive to a review branch of the existing repository.
# Requires authenticated Git push access. Never changes the default branch.
set -euo pipefail

REPO="${DABOOK_REPO:-zitterbewegung/dabook}"
BRANCH="${DABOOK_BRANCH:-archive/research-families-2026-11-25}"
BASE="${DABOOK_BASE:-main}"
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

for cmd in git rsync; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    printf 'Required command missing: %s\n' "$cmd" >&2
    exit 1
  fi
done

PYTHON_BIN="${DABOOK_PYTHON:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN=python3
  elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN=python
  else
    printf 'Required executable missing: Python 3\n' >&2
    exit 1
  fi
fi

"$PYTHON_BIN" "$SOURCE/scripts/check_catalog.py"
(cd "$SOURCE" && "$PYTHON_BIN" -m unittest discover -s tests -v)

git clone "https://github.com/$REPO.git" "$WORK/remote"
git -C "$WORK/remote" switch "$BASE"
if git -C "$WORK/remote" ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  printf 'Remote branch %s already exists. No changes published.\n' "$BRANCH" >&2
  exit 1
fi
git -C "$WORK/remote" switch -c "$BRANCH"

# Preserve all existing repository files, its license, and its .gitignore.
# No --delete: do not remove unrelated files from the remote repo.
rsync -a \
  --exclude='.git/' \
  --exclude='__pycache__/' \
  --exclude='.gitignore' \
  "$SOURCE/" "$WORK/remote/"

git -C "$WORK/remote" add --all
if git -C "$WORK/remote" diff --cached --quiet; then
  printf 'Nothing new to publish.\n'
  exit 0
fi
git -C "$WORK/remote" commit -m "Archive daBook mathematical results and proof-status ledger"
git -C "$WORK/remote" push -u origin "$BRANCH"

printf '\nReview branch published: https://github.com/%s/tree/%s\n' "$REPO" "$BRANCH"
if command -v gh >/dev/null 2>&1; then
  gh pr create --repo "$REPO" --head "$BRANCH" --base "$BASE" --draft \
    --title "Archive daBook mathematical results, proofs, and open gaps" \
    --body "Source-limited audit of eight research families and 40 indexed claims. Includes exact proofs, counterexamples, prior-art notes, and unresolved gaps. Not refereed; please review before merging."
else
  printf 'To open a draft PR, use: https://github.com/%s/compare/%s...%s?expand=1\n' "$REPO" "$BASE" "$BRANCH"
fi
