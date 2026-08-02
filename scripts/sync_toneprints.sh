#!/usr/bin/env bash
# One-directional sync: all toneprint .md files and the HTML viewer to iCloud
# Run from project root.

set -euo pipefail

# Define paths
PROJ_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TONES_SRC="$PROJ_ROOT/tones"
HTML_SRC="$PROJ_ROOT/tone-advisor/tone-viewer.html"
DEST="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Guitar/Toneprints"

# Ensure source exists
if [[ ! -d "$TONES_SRC" ]]; then
  echo "ERROR: Tones directory not found at $TONES_SRC" >&2
  exit 1
fi

mkdir -p "$DEST"

# Sync Markdown files from tones/
# We use --delete to keep the destination clean of removed tones.
# Note: This will delete the HTML file from the destination if it was there,
# so we copy it back in the next step.
rsync -av --delete \
  --include="*/" \
  --include="*.md" \
  --include="*.thrl6p" \
  --exclude="*" \
  "$TONES_SRC/" "$DEST/"

# Sync the HTML viewer and guides
if [[ -f "$HTML_SRC" ]]; then
  cp -v "$HTML_SRC" "$DEST/"
fi
if [[ -f "$PROJ_ROOT/tone-advisor/eq-visualizer.html" ]]; then
  cp -v "$PROJ_ROOT/tone-advisor/eq-visualizer.html" "$DEST/"
fi
if [[ -f "$PROJ_ROOT/tone-advisor/tonex-stomp-viewer.html" ]]; then
  cp -v "$PROJ_ROOT/tone-advisor/tonex-stomp-viewer.html" "$DEST/"
fi
if [[ -f "$PROJ_ROOT/tone-advisor/tonex-amp-viewer.html" ]]; then
  cp -v "$PROJ_ROOT/tone-advisor/tonex-amp-viewer.html" "$DEST/"
fi
if [[ -f "$PROJ_ROOT/tone-advisor/dual-tone-viewer.html" ]]; then
  cp -v "$PROJ_ROOT/tone-advisor/dual-tone-viewer.html" "$DEST/"
fi
if [[ -f "$PROJ_ROOT/tone-advisor/PARALLEL_AMP_GUIDE.md" ]]; then
  cp -v "$PROJ_ROOT/tone-advisor/PARALLEL_AMP_GUIDE.md" "$DEST/"
fi
if [[ -f "$PROJ_ROOT/tone-advisor/universal-template-guide.md" ]]; then
  cp -v "$PROJ_ROOT/tone-advisor/universal-template-guide.md" "$DEST/"
fi
if [[ -f "$PROJ_ROOT/tone-advisor/universal-template-guide.html" ]]; then
  cp -v "$PROJ_ROOT/tone-advisor/universal-template-guide.html" "$DEST/"
fi

echo ""
echo "Synced toneprint files to $DEST"
