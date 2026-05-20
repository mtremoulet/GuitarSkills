#!/usr/bin/env bash
# macOS Spotify desktop controller using AppleScript (osascript).
# Suppress stdout/stderr if needed, and cleanly control Spotify.

set -euo pipefail

# Ensure Spotify is running
check_running() {
  if ! pgrep -x "Spotify" >/dev/null; then
    echo "Starting Spotify..."
    open -a "Spotify"
    sleep 3
  fi
}

cmd_now() {
  if ! pgrep -x "Spotify" >/dev/null; then
    echo "Spotify is not running"
    return
  fi
  osascript -e '
    tell application "Spotify"
      if player state is playing or player state is paused then
        set ctrack to current track
        set tname to name of ctrack
        set tartist to artist of ctrack
        set talbum to album of ctrack
        set tpos to player position
        set tstate to player state as string
        return tname & " — " & tartist & " [" & talbum & "] (" & tstate & ", " & round(tpos) & "s)"
      else
        return "Spotify is open but idle"
      end if
    end tell
  '
}

cmd_play_uri() {
  check_running
  local uri="$1"
  osascript -e "tell application \"Spotify\" to play track \"$uri\""
}

cmd_play_search() {
  local artist="$1"
  local title="$2"
  local query="artist:$artist track:$title"
  echo "Searching and playing: $artist — $title"
  
  # Try to use the python script to search and get a URI
  # If it works, play that URI. If not, open search in Spotify.
  local proj_root
  proj_root="$(cd "$(dirname "$0")/.." && pwd)"
  
  if [[ -f "$proj_root/.spotify_cache" ]]; then
    local search_res
    search_res=$(uv run "$proj_root/scripts/spotify_client.py" search "$query" --limit 1 --type track 2>/dev/null)
    local uri
    uri=$(echo "$search_res" | grep -o '"uri": "[^"]*"' | head -n 1 | cut -d'"' -f4)
    if [[ -n "$uri" ]]; then
      cmd_play_uri "$uri"
      return
    fi
  fi
  
  # Fallback: Open search in Spotify desktop
  check_running
  open "spotify:search:$(echo "$query" | awk '{print $0}' | tr ' ' '+')"
}

case "${1:-}" in
  play)
    if [[ $# -lt 3 ]]; then
      echo "Usage: $0 play \"artist\" \"title\"" >&2
      exit 1
    fi
    cmd_play_search "$2" "$3"
    ;;
  play-uri)
    if [[ $# -lt 2 ]]; then
      echo "Usage: $0 play-uri spotify:track:..." >&2
      exit 1
    fi
    cmd_play_uri "$2"
    ;;
  pause)
    check_running
    osascript -e 'tell application "Spotify" to pause'
    ;;
  resume)
    check_running
    osascript -e 'tell application "Spotify" to play'
    ;;
  toggle)
    check_running
    osascript -e 'tell application "Spotify" to playpause'
    ;;
  next)
    check_running
    osascript -e 'tell application "Spotify" to next track'
    ;;
  prev)
    check_running
    osascript -e 'tell application "Spotify" to previous track'
    ;;
  now)
    cmd_now
    ;;
  vol)
    check_running
    if [[ $# -eq 2 ]]; then
      osascript -e "tell application \"Spotify\" to set sound volume to $2"
    else
      osascript -e 'tell application "Spotify" to get sound volume'
    fi
    ;;
  open)
    if [[ $# -lt 2 ]]; then
      echo "Usage: $0 open \"query\"" >&2
      exit 1
    fi
    check_running
    open "spotify:search:$(echo "$2" | tr ' ' '+')"
    ;;
  *)
    echo "Usage: $0 {play|play-uri|pause|resume|toggle|next|prev|now|vol|open}" >&2
    exit 1
    ;;
esac
