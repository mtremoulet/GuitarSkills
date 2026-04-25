# Spotify Integration (macOS)

Control Spotify playback directly from the terminal using AppleScript — no API
keys, no tokens, no OAuth. Just the Spotify desktop app installed on your Mac.

---

## Quick Start

```bash
# Play a track by searching artist + title
./scripts/spotify-mac.sh play "Miles Davis" "So What"

# Pause / resume / skip
./scripts/spotify-mac.sh pause
./scripts/spotify-mac.sh resume
./scripts/spotify-mac.sh next

# See what's playing
./scripts/spotify-mac.sh now

# Set volume (0-100)
./scripts/spotify-mac.sh vol 60
```

---

## How It Works

The script uses macOS `osascript` to send commands to the Spotify desktop app.
Spotify exposes a scripting dictionary that allows:
- Play / pause / next / previous
- Play a specific track by URI
- Open search queries
- Read current track metadata (name, artist, album, position)
- Control volume

No network API calls are made. Everything runs locally.

---

## Commands Reference

| Command                              | Description                       |
|--------------------------------------|-----------------------------------|
| `play "artist" "title"`             | Search & play a track             |
| `play-uri spotify:track:...`        | Play a specific Spotify URI       |
| `pause`                              | Pause playback                    |
| `resume`                             | Resume playback                   |
| `toggle`                             | Toggle play/pause                 |
| `next`                               | Skip to next track                |
| `prev`                               | Go to previous track              |
| `now`                                | Show current track info           |
| `vol [0-100]`                        | Get or set volume                 |
| `open "query"`                       | Open a search in Spotify          |

---

## Playlists

Playlists are stored as local JSON files in `~/guitar-coach-library/playlists/`.
Each session generates a playlist file like:

```json
{
  "name": "Jazz ii-V-I Turnarounds",
  "date": "2026-03-18",
  "tracks": [
    {
      "artist": "Miles Davis",
      "title": "So What",
      "key": "Dm",
      "bpm": 136,
      "focus": "verse — D dorian modal vamp",
      "difficulty": "moderate"
    }
  ]
}
```

To play through a playlist file sequentially, you can use the play commands
in the session's `session.md` file, or manually run:

```bash
./scripts/spotify-mac.sh play "Miles Davis" "So What"
# ... listen, practice ...
./scripts/spotify-mac.sh play "John Coltrane" "Giant Steps"
```

---

## Requirements

- **macOS** (uses AppleScript / `osascript`)
- **Spotify desktop app** installed (not the web player)
- Spotify must be logged in — the script will launch it if not running

---

## Troubleshooting

| Issue                          | Fix                                                |
|--------------------------------|----------------------------------------------------|
| "Spotify is not running"       | Script auto-launches Spotify; wait a few seconds   |
| Search plays wrong track       | Use `open "query"` to search manually, then play   |
| No sound                       | Check `vol` level and macOS system volume           |
| Permission denied              | Run `chmod +x scripts/spotify-mac.sh`              |
| Not on macOS                   | This script requires macOS; use search links instead|
