# /// script
# dependencies = ["markdown", "python-dotenv"]
# ///
"""
Generate a self-contained HTML viewer for the guitar playlist library.

Reads all .md files (except INDEX.md) from guitar-coach-library/playlists/,
parses frontmatter + body, and produces guitar-coach-library/playlist-viewer.html.

Usage:
    uv run scripts/generate_playlist_viewer.py             # generate + open in browser
    uv run scripts/generate_playlist_viewer.py --build-only  # generate only (for skill use)
"""

import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime
import markdown as md_lib

PROJ_ROOT = Path(__file__).parent.parent
PLAYLISTS_DIR = PROJ_ROOT / "guitar-coach-library" / "playlists"
OUTPUT_HTML = PROJ_ROOT / "guitar-coach-library" / "playlist-viewer.html"


# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}, text
    data = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            data[k.strip()] = v.strip().strip('"')
    return data, text[m.end():]


def load_playlists():
    playlists = []
    for path in sorted(PLAYLISTS_DIR.glob("*.md")):
        if path.name == "INDEX.md":
            continue
        text = path.read_text()
        meta, body = parse_frontmatter(text)
        if not meta:
            continue
        playlists.append({
            "path": path,
            "meta": meta,
            "body": body,
            "html_body": md_lib.markdown(body, extensions=["tables", "fenced_code"]),
        })
    playlists.sort(key=lambda p: p["meta"].get("created", ""), reverse=True)
    return playlists


# ── HTML generation ───────────────────────────────────────────────────────────

CSS = """
:root {
    --bg:               #0f0f0f;
    --bg-elevated:      #1a1a1a;
    --bg-hover:         #1e1e1e;
    --border:           #2a2a2a;
    --text:             #e8e8e8;
    --text-sub:         #ccc;
    --text-secondary:   #999;
    --text-muted:       #666;
    --text-faint:       #777;
    --text-heading:     #fff;
    --pill-bg:          #252525;
    --pill-border:      #333;
    --pill-text:        #aaa;
    --pill-green-bg:    #0d2b18;
    --pill-green-text:  #1db954;
    --pill-green-border:#1a5c30;
    --table-header-bg:  #1e1e1e;
    --code-bg:          #1e1e1e;
    --hr:               #2a2a2a;
    --back-btn-border:  #333;
    --back-btn-text:    #aaa;
}

@media (prefers-color-scheme: light) {
    :root {
        --bg:               #f4f4f4;
        --bg-elevated:      #ffffff;
        --bg-hover:         #fafafa;
        --border:           #e0e0e0;
        --text:             #1a1a1a;
        --text-sub:         #333;
        --text-secondary:   #555;
        --text-muted:       #888;
        --text-faint:       #666;
        --text-heading:     #000;
        --pill-bg:          #eeeeee;
        --pill-border:      #d4d4d4;
        --pill-text:        #555;
        --pill-green-bg:    #e6f7ee;
        --pill-green-text:  #1a7a3c;
        --pill-green-border:#a8dbb9;
        --table-header-bg:  #f5f5f5;
        --code-bg:          #efefef;
        --hr:               #e0e0e0;
        --back-btn-border:  #d0d0d0;
        --back-btn-text:    #555;
    }
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
}
header {
    background: var(--bg-elevated);
    border-bottom: 1px solid var(--border);
    padding: 20px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
header h1 { font-size: 1.2rem; font-weight: 600; color: var(--text-heading); letter-spacing: 0.02em; }
header span { font-size: 0.8rem; color: var(--text-muted); }

/* Index view */
#index-view { padding: 32px; max-width: 1100px; margin: 0 auto; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 24px; }
.card {
    background: var(--bg-elevated);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 22px;
    cursor: pointer;
    transition: border-color 0.15s, background 0.15s;
}
.card:hover { border-color: #1db954; background: var(--bg-hover); }
.card-title { font-size: 1rem; font-weight: 600; color: var(--text-heading); margin-bottom: 8px; line-height: 1.3; }
.card-angle { font-size: 0.8rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 12px; }
.card-meta { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 12px; }
.pill {
    font-size: 0.7rem;
    padding: 2px 8px;
    border-radius: 99px;
    background: var(--pill-bg);
    color: var(--pill-text);
    border: 1px solid var(--pill-border);
}
.pill.green { background: var(--pill-green-bg); color: var(--pill-green-text); border-color: var(--pill-green-border); }
.card-artists { font-size: 0.75rem; color: var(--text-faint); margin-top: 6px; line-height: 1.4; }
.card-date { font-size: 0.75rem; color: var(--text-muted); margin-top: 10px; }

/* Detail view */
#detail-view { display: none; padding: 32px; max-width: 820px; margin: 0 auto; }
.back-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: none;
    border: 1px solid var(--back-btn-border);
    color: var(--back-btn-text);
    padding: 6px 14px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.85rem;
    margin-bottom: 28px;
    transition: border-color 0.15s, color 0.15s;
}
.back-btn:hover { border-color: #1db954; color: #1db954; }
.spotify-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #1db954;
    color: #000;
    padding: 8px 18px;
    border-radius: 99px;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none;
    margin-bottom: 32px;
    transition: background 0.15s;
}
.spotify-btn:hover { background: #1ed760; }
#detail-body { line-height: 1.75; }
#detail-body h1 { font-size: 1.8rem; font-weight: 700; color: var(--text-heading); margin-bottom: 8px; }
#detail-body h2 { font-size: 1.2rem; font-weight: 600; color: var(--text-heading); margin: 32px 0 12px; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
#detail-body h3 { font-size: 1rem; font-weight: 600; color: var(--text-sub); margin: 24px 0 8px; }
#detail-body p { margin-bottom: 14px; color: var(--text-sub); font-size: 0.95rem; }
#detail-body strong { color: var(--text); }
#detail-body em { color: var(--text-secondary); }
#detail-body ul, #detail-body ol { margin: 0 0 14px 22px; color: var(--text-sub); font-size: 0.95rem; }
#detail-body li { margin-bottom: 4px; }
#detail-body table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 0.85rem; }
#detail-body th { text-align: left; padding: 8px 12px; background: var(--table-header-bg); color: var(--text-secondary); border-bottom: 1px solid var(--border); }
#detail-body td { padding: 8px 12px; border-bottom: 1px solid var(--border); color: var(--text-sub); vertical-align: top; }
#detail-body tr:last-child td { border-bottom: none; }
#detail-body code { background: var(--code-bg); padding: 2px 6px; border-radius: 4px; font-size: 0.85em; color: var(--text-secondary); }
#detail-body blockquote { border-left: 3px solid #1db954; margin: 0 0 14px; padding: 4px 16px; color: var(--text-secondary); font-style: italic; }
#detail-body hr { border: none; border-top: 1px solid var(--hr); margin: 32px 0; }
#detail-body a { color: #1db954; text-decoration: none; }
#detail-body a:hover { text-decoration: underline; }

.detail-meta { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px; }
"""

JS = """
const playlists = PLAYLISTS_DATA;

function showIndex() {
    document.getElementById('index-view').style.display = 'block';
    document.getElementById('detail-view').style.display = 'none';
    document.title = 'Guitar Playlist Library';
}

function showDetail(id) {
    const p = playlists.find(x => x.id === id);
    if (!p) return;
    document.getElementById('index-view').style.display = 'none';
    const dv = document.getElementById('detail-view');
    dv.style.display = 'block';

    const tags = (p.tags || '').split(',').map(t => t.trim()).filter(Boolean);
    const tagPills = tags.map(t => `<span class="pill">${t}</span>`).join('');
    const spotifyBtn = p.spotify_url
        ? `<a class="spotify-btn" href="${p.spotify_url}" target="_blank">
             <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
               <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
             </svg>
             Open in Spotify
           </a>`
        : '';

    dv.innerHTML = `
        <button class="back-btn" onclick="showIndex()">← All Playlists</button>
        <div class="detail-meta">${tagPills}</div>
        ${spotifyBtn}
        <div id="detail-body">${p.html_body}</div>
    `;
    document.title = p.title || 'Playlist';
    window.scrollTo(0, 0);
}

function renderIndex() {
    const grid = document.getElementById('playlist-grid');
    grid.innerHTML = playlists.map(p => {
        const tags = (p.tags || '').split(',').map(t => t.trim()).filter(Boolean).slice(0, 4);
        const tagPills = tags.map(t => `<span class="pill">${t}</span>`).join('');
        return `
        <div class="card" onclick="showDetail('${p.id}')">
            <div class="card-title">${p.title || p.id}</div>
            <div class="card-angle">${p.angle || ''}</div>
            <div class="card-meta">${tagPills}<span class="pill green">${p.track_count || '?'} tracks</span></div>
            <div class="card-artists">${p.featured_artists || ''}</div>
            <div class="card-date">${p.created || ''}</div>
        </div>`;
    }).join('');
}

renderIndex();
"""


def build_html(playlists):
    import json

    playlist_data = []
    for p in playlists:
        playlist_data.append({
            "id": p["meta"].get("id", p["path"].stem),
            "title": p["meta"].get("title", ""),
            "angle": p["meta"].get("angle", ""),
            "tags": p["meta"].get("tags", ""),
            "featured_artists": p["meta"].get("featured_artists", ""),
            "track_count": p["meta"].get("track_count", ""),
            "spotify_url": p["meta"].get("spotify_url", ""),
            "created": p["meta"].get("created", ""),
            "html_body": p["html_body"],
        })

    js = JS.replace("PLAYLISTS_DATA", json.dumps(playlist_data, ensure_ascii=False))
    count = len(playlists)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guitar Playlist Library</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>Guitar Playlist Library</h1>
  <span>{count} playlist{"s" if count != 1 else ""} · generated {now}</span>
</header>

<div id="index-view">
  <div style="max-width:1100px;margin:0 auto;padding:0">
    <p style="color:#666;font-size:0.85rem;margin-top:20px">
      Curated listening curricula — each built around a specific angle of guitar vocabulary.
      Click any card to read the full explainer and open on Spotify.
    </p>
    <div class="grid" id="playlist-grid"></div>
  </div>
</div>

<div id="detail-view"></div>

<script>{js}</script>
</body>
</html>"""


def main():
    build_only = "--build-only" in sys.argv
    playlists = load_playlists()
    if not playlists:
        print("No playlist files found.", file=sys.stderr)
        return 1

    html = build_html(playlists)
    OUTPUT_HTML.write_text(html)
    print(f"Generated {OUTPUT_HTML} ({len(playlists)} playlist{'s' if len(playlists) != 1 else ''})")

    if not build_only:
        subprocess.run(["open", str(OUTPUT_HTML)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
