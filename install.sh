#!/usr/bin/env bash
# Install the Moksh Vasant context into an existing FulcrumOS / Claude Code workspace.
#
# Run from the ROOT of the workspace (the folder whose CLAUDE.md the AI reads):
#   git clone --depth 1 https://github.com/aaryapranshu/moksh-vasant-context.git /tmp/moksh-ctx \
#     && bash /tmp/moksh-ctx/install.sh && rm -rf /tmp/moksh-ctx
#
# What it does (safe to re-run; re-running updates the files):
#   1. Copies this repo into ./context/moksh-vasant/ (no nested .git).
#   2. Adds a short pointer block to ./CLAUDE.md so the AI knows the context exists.
#   3. Adds the transcript-sync SessionStart hook to ./.claude/settings.json
#      (hooks in a nested folder don't fire on their own).
# Override the target folder with: MOKSH_CONTEXT_DIR=some/path bash install.sh
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS="$(pwd)"
REL="${MOKSH_CONTEXT_DIR:-context/moksh-vasant}"
DEST="$WS/$REL"

if [ "$SRC" = "$DEST" ] || [ "$SRC" = "$WS" ]; then
  echo "Run this from your workspace root, not from inside the cloned repo." >&2
  exit 1
fi
command -v python3 >/dev/null || { echo "python3 is required." >&2; exit 1; }

echo "Installing Moksh Vasant context into $REL/"
mkdir -p "$DEST"
rsync -a --delete \
  --exclude ".git/" --exclude ".transcript-tools/" --exclude "__pycache__/" \
  --exclude "transcripts/.sync.lock" --exclude "transcripts/_sync.log" \
  "$SRC/" "$DEST/"
rm -f "$DEST/install.sh"

# 2. Pointer block in the workspace CLAUDE.md (between markers, replaced on re-run)
python3 - "$WS/CLAUDE.md" "$REL" <<'PY'
import sys, re, pathlib
path, rel = pathlib.Path(sys.argv[1]), sys.argv[2]
block = f"""<!-- moksh-context:start -->
## Moksh Vasant context

Everything Moksh has published (161 timestamped transcripts, mental models, Meteoric Boost, sales process, content playbook) lives in `{rel}/`.

- For anything about Moksh, Meteoric Boost, his clients, his content or writing in his voice: read `{rel}/CLAUDE.md` first. It routes each task to the right files.
- Quick context for any task: `{rel}/MOKSH.md` (one-file brief).
- Transcripts are the source of truth; numbers are self-reported; don't guess. Open items: `{rel}/OPEN-QUESTIONS.md`.
<!-- moksh-context:end -->
"""
text = path.read_text(encoding="utf-8") if path.exists() else ""
pat = re.compile(r"<!-- moksh-context:start -->.*?<!-- moksh-context:end -->\n?", re.S)
text = pat.sub(block, text) if pat.search(text) else (text.rstrip() + "\n\n" + block if text.strip() else block)
path.write_text(text, encoding="utf-8")
print(f"Updated {path.name}")
PY

# 3. SessionStart hook in the workspace settings (merged, never duplicated)
python3 - "$WS/.claude/settings.json" "$REL" <<'PY'
import sys, json, pathlib
path, rel = pathlib.Path(sys.argv[1]), sys.argv[2]
cmd = (f'cd "$CLAUDE_PROJECT_DIR/{rel}" && '
       '(python3 scripts/sync_transcripts.py 2>/dev/null || python scripts/sync_transcripts.py)')
path.parent.mkdir(parents=True, exist_ok=True)
try:
    cfg = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
except json.JSONDecodeError:
    sys.exit(f"{path} is not valid JSON; add the hook by hand (see {rel}/transcripts/README.md).")
groups = cfg.setdefault("hooks", {}).setdefault("SessionStart", [])
for g in groups:
    g["hooks"] = [h for h in g.get("hooks", []) if "sync_transcripts.py" not in h.get("command", "")]
groups[:] = [g for g in groups if g.get("hooks")]
groups.append({"matcher": "startup|resume",
               "hooks": [{"type": "command", "command": cmd, "timeout": 30}]})
path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
print(f"Updated .claude/{path.name}")
PY

echo "Done. Open the workspace in Claude Code and ask it anything about Moksh or Meteoric Boost."
