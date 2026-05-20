# /// script
# dependencies = ["spotipy", "python-dotenv"]
# ///
"""
Spotify playlist management CLI for GuitarSkills.

Commands:
  search <query> [--limit N] [--type track|artist|album]
  create-playlist <name> [--description TEXT] [--public]
  add-tracks <playlist_id> <uri> [<uri> ...]
  remove-tracks <playlist_id> <uri> [<uri> ...]
  list-playlists
  show-playlist <playlist_id_or_name>
  find-playlist <name>

Usage examples:
  uv run scripts/spotify_client.py search "Wes Montgomery" --limit 5
  uv run scripts/spotify_client.py search "artist:Jim Hall track:Concierto" --limit 10
  uv run scripts/spotify_client.py create-playlist "Jazz Guitar — Wes Montgomery" --description "Hard bop and soul jazz vocabulary"
  uv run scripts/spotify_client.py add-tracks 3abc...xyz spotify:track:abc123 spotify:track:def456
  uv run scripts/spotify_client.py list-playlists
  uv run scripts/spotify_client.py find-playlist "Jazz Guitar"
"""

import argparse
import json
import os
import sys
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

CACHE_PATH = Path(__file__).parent.parent / ".spotify_cache"


def get_client():
    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=" ".join(SCOPES),
        cache_path=str(CACHE_PATH),
        open_browser=False,
    )
    if not auth_manager.get_cached_token():
        print("No cached token found. Run `uv run scripts/spotify_setup.py` first.", file=sys.stderr)
        sys.exit(1)
    return spotipy.Spotify(auth_manager=auth_manager)


def cmd_search(sp, args):
    results = sp.search(q=args.query, limit=args.limit, type=args.type)
    key = args.type + "s"
    items = results[key]["items"]
    output = []
    for item in items:
        if args.type == "track":
            output.append({
                "name": item["name"],
                "artist": ", ".join(a["name"] for a in item["artists"]),
                "album": item["album"]["name"],
                "uri": item["uri"],
                "id": item["id"],
                "duration_ms": item["duration_ms"],
                "popularity": item["popularity"],
            })
        elif args.type == "artist":
            output.append({
                "name": item["name"],
                "uri": item["uri"],
                "id": item["id"],
                "genres": item.get("genres", []),
                "popularity": item["popularity"],
            })
        elif args.type == "album":
            output.append({
                "name": item["name"],
                "artist": ", ".join(a["name"] for a in item["artists"]),
                "uri": item["uri"],
                "id": item["id"],
                "release_date": item["release_date"],
            })
    print(json.dumps(output, indent=2))


def cmd_create_playlist(sp, args):
    user = sp.current_user()
    playlist = sp.user_playlist_create(
        user=user["id"],
        name=args.name,
        public=args.public,
        description=args.description or "",
    )
    print(json.dumps({
        "id": playlist["id"],
        "name": playlist["name"],
        "uri": playlist["uri"],
        "url": playlist["external_urls"]["spotify"],
        "public": playlist["public"],
    }, indent=2))


def cmd_add_tracks(sp, args):
    sp.playlist_add_items(args.playlist_id, args.uris)
    print(json.dumps({"status": "ok", "added": len(args.uris), "playlist_id": args.playlist_id}))


def cmd_remove_tracks(sp, args):
    sp.playlist_remove_all_occurrences_of_items(args.playlist_id, args.uris)
    print(json.dumps({"status": "ok", "removed": len(args.uris), "playlist_id": args.playlist_id}))


def cmd_list_playlists(sp, args):
    user = sp.current_user()
    playlists = []
    results = sp.user_playlists(user["id"], limit=50)
    while results:
        for p in results["items"]:
            playlists.append({
                "id": p["id"],
                "name": p["name"],
                "tracks": p["tracks"]["total"],
                "public": p["public"],
                "uri": p["uri"],
            })
        results = sp.next(results) if results["next"] else None
    print(json.dumps(playlists, indent=2))


def cmd_show_playlist(sp, args):
    playlist = sp.playlist(args.playlist_id)
    tracks = []
    results = playlist["tracks"]
    while results:
        for item in results["items"]:
            t = item.get("track")
            if t:
                tracks.append({
                    "name": t["name"],
                    "artist": ", ".join(a["name"] for a in t["artists"]),
                    "album": t["album"]["name"],
                    "uri": t["uri"],
                    "added_at": item.get("added_at"),
                })
        results = sp.next(results) if results["next"] else None
    print(json.dumps({
        "id": playlist["id"],
        "name": playlist["name"],
        "description": playlist["description"],
        "tracks": tracks,
        "total": playlist["tracks"]["total"],
        "url": playlist["external_urls"]["spotify"],
    }, indent=2))


def cmd_find_playlist(sp, args):
    user = sp.current_user()
    results = sp.user_playlists(user["id"], limit=50)
    matches = []
    while results:
        for p in results["items"]:
            if args.name.lower() in p["name"].lower():
                matches.append({
                    "id": p["id"],
                    "name": p["name"],
                    "tracks": p["tracks"]["total"],
                    "uri": p["uri"],
                })
        results = sp.next(results) if results["next"] else None
    print(json.dumps(matches, indent=2))


def main():
    parser = argparse.ArgumentParser(description="GuitarSkills Spotify client")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=10)
    p_search.add_argument("--type", default="track", choices=["track", "artist", "album"])

    p_create = sub.add_parser("create-playlist")
    p_create.add_argument("name")
    p_create.add_argument("--description", default="")
    p_create.add_argument("--public", action="store_true", default=False)

    p_add = sub.add_parser("add-tracks")
    p_add.add_argument("playlist_id")
    p_add.add_argument("uris", nargs="+")

    p_remove = sub.add_parser("remove-tracks")
    p_remove.add_argument("playlist_id")
    p_remove.add_argument("uris", nargs="+")

    sub.add_parser("list-playlists")

    p_show = sub.add_parser("show-playlist")
    p_show.add_argument("playlist_id")

    p_find = sub.add_parser("find-playlist")
    p_find.add_argument("name")

    args = parser.parse_args()
    sp = get_client()

    commands = {
        "search": cmd_search,
        "create-playlist": cmd_create_playlist,
        "add-tracks": cmd_add_tracks,
        "remove-tracks": cmd_remove_tracks,
        "list-playlists": cmd_list_playlists,
        "show-playlist": cmd_show_playlist,
        "find-playlist": cmd_find_playlist,
    }
    commands[args.command](sp, args)


if __name__ == "__main__":
    main()
