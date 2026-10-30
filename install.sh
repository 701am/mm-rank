#!/usr/bin/env bash
# MM Rank by Media Matchers — skills installer
# Supports Claude Code, Claude Cowork, OpenCode, OpenWork, and Grok.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -d "$HOME/.claude" ]]; then
  TARGET="$HOME/.claude/skills"
  CLIENT="Claude Code / Cowork"
elif [[ -d "$HOME/.agents" ]] || [[ -d "$HOME/.config/opencode" ]]; then
  TARGET="$HOME/.agents/skills"
  CLIENT="OpenCode / OpenWork"
elif [[ -d "$HOME/.grok" ]]; then
  TARGET="$HOME/.grok/skills"
  CLIENT="Grok"
else
  echo "No agent skills directory detected."
  echo "Create one and re-run, or copy manually:"
  echo "  Claude Code / Cowork:  mkdir -p ~/.claude/skills && cp -a * ~/.claude/skills/"
  echo "  OpenCode / OpenWork:   mkdir -p ~/.agents/skills && cp -a * ~/.agents/skills/"
  echo "  Grok:                  mkdir -p ~/.grok/skills && cp -a * ~/.grok/skills/"
  exit 1
fi

mkdir -p "$TARGET"

echo "Installing MM Rank by Media Matchers skills into $TARGET ($CLIENT)…"

for dir in "$SCRIPT_DIR"/*/; do
  name=$(basename "$dir")
  if [[ -f "$dir/SKILL.md" ]]; then
    echo "  → $name"
    rm -rf "$TARGET/$name"
    cp -a "$dir" "$TARGET/"
  fi
done

echo
echo "Done."
echo "Next: start a new chat and say:"
echo "  Run MM Rank on example.com"
