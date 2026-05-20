# /// script
# dependencies = ["spotipy", "python-dotenv"]
# ///
"""
One-time Spotify OAuth setup. Run this once to authenticate and cache your token.
Usage: uv run scripts/spotify_setup.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(Path(__file__).parent.parent / ".env")

SCOPES = [
    "playlist-modify-public",
    "playlist-modify-private",
    "playlist-read-private",
    "playlist-read-collaborative",
]

def main():
    required = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
        print("Copy .env.example to .env and fill in your credentials.")
        return 1

    cache_path = Path(__file__).parent.parent / ".spotify_cache"

    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=" ".join(SCOPES),
        cache_path=str(cache_path),
        open_browser=True,
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)
    user = sp.current_user()
    print(f"Authenticated as: {user['display_name']} ({user['id']})")
    print(f"Token cached at: {cache_path}")
    print("Setup complete. You won't need to do this again unless you revoke access.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
