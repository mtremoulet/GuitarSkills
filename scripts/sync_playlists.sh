#!/usr/bin/env bash
# One-directional sync: playlist .md files and HTML viewer to iCloud.
# Run from project root.

set -euo pipefail

PROJ_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLAYLISTS_SRC="$PROJ_ROOT/guitar-coach-library/playlists"
HTML_SRC="$PROJ_ROOT/guitar-coach-library/playlist-viewer.html"
DEST="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Guitar/Playlists"

if [[ ! -d "$PLAYLISTS_SRC" ]]; then
  echo "ERROR: Playlists directory not found at $PLAYLISTS_SRC" >&2
  exit 1
fi

mkdir -p "$DEST"

# Rebuild the viewer before syncing
echo "Rebuilding playlist viewer..."
uv run "$PROJ_ROOT/scripts/generate_playlist_viewer.py" --build-only

# Sync markdown files
rsync -av --delete \
  --include="*/" \
  --include="*.md" \
  --exclude="*" \
  "$PLAYLISTS_SRC/" "$DEST/"

# Sync the HTML viewer
if [[ -f "$HTML_SRC" ]]; then
  cp -v "$HTML_SRC" "$DEST/"
fi

echo ""
echo "Synced playlist library to $DEST"
