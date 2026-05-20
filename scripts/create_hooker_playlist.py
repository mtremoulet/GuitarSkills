#!/usr/bin/env python3
# /// script
# dependencies = ["spotipy", "python-dotenv"]
# ///
"""
Script to create the "John Lee Hooker & The Boogie Legacy" playlist.
Searches for core canon tracks and descendants, creates the playlist, and adds tracks.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment
proj_root = Path(__file__).parent.parent
load_dotenv(proj_root / ".env")

SCOPES = [
    "playlist-modify-public",
    "playlist-modify-private",
    "playlist-read-private",
]
CACHE_PATH = proj_root / ".spotify_cache"

def get_client():
    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=" ".join(SCOPES),
        cache_path=str(CACHE_PATH),
        open_browser=False,
    )
    return spotipy.Spotify(auth_manager=auth_manager)

# Tracks to search for: (artist, title, description)
TRACKS_SPEC = [
    # ─── CORE CANON: JOHN LEE HOOKER ───
    ("John Lee Hooker", "Boogie Chillen", "The 1948 solo breakthrough. Hypnotic open G drone with stomping foot rhythm."),
    ("John Lee Hooker", "Crawlin' King Snake", "Slow, dark, and brooding country-blues showcase of his modal tension."),
    ("John Lee Hooker", "I'm In The Mood", "Multi-tracked vocals and driving, swampy solo boogie beat."),
    ("John Lee Hooker", "Dimples", "The Vee-Jay records classic featuring Eddie Taylor on guitar — UK Blues boom blueprint."),
    ("John Lee Hooker", "Boom Boom", "His signature stop-time blues masterpiece, driving band groove."),
    ("John Lee Hooker", "It Serves You Right to Suffer", "Slow, smoky, jazz-modal blues from the legendary Impulse! album."),
    
    # ─── COLLABORATORS & THE BRITISH BOOM ───
    ("John Lee Hooker Carlos Santana", "The Healer", "Grammy-winning collaboration blending Latin polyrhythm with his boogie drone."),
    ("John Lee Hooker Canned Heat", "Whiskey and Womena", "From the benchmark 1971 'Hooker 'n Heat' album, with Alan Wilson's genius harmonica."),
    ("The Animals", "Boom Boom", "Eric Burdon's baritone vocal and raw band drive showing Hooker's UK influence."),
    ("Canned Heat", "On the Road Again", "Hypnotic, single-chord drone blues-rock direct from the Hooker playbook."),
    
    # ─── AMERICAN BOOGIE & BLUES-ROCK ───
    ("ZZ Top", "La Grange", "Billy Gibbons' ultimate tribute to Hooker's boogie beat, using the 'Boogie Chillen' groove."),
    ("Johnny Winter", "I'm Yours and I'm Hers", "High-energy slide-heavy Texas blues tracing back to the raw stomping speed."),
    ("Carlos Santana John Lee Hooker", "Chill Out (Things Gonna Change)", "Ethereal, ambient-inflected blues groove led by Santana's soaring guitar."),
    
    # ─── NORTH MISSISSIPPI HILL COUNTRY & MODERN DESCENDANTS ───
    ("Junior Kimbrough", "Meet Me in the City", "Hypnotic, modal, single-chord drone blues — the direct sonic child of Hooker."),
    ("R.L. Burnside", "Poor Black Mattie", "Driving, repetitive groove, heavy downbeats, raw solo fingerstyle."),
    ("The Black Keys", "Do the Rump", "Primal guitar-and-drums cover of R.L. Burnside, direct link to the hill country boogie."),
    ("The White Stripes", "Death Letter", "Jack White's blistering slide tribute to Son House, fueled by Hooker-style raw drive."),
    ("Gary Clark Jr.", "Bright Lights", "Modern guitar hero blending low-end growls and heavy boogie drones for today.")
]

def main():
    sp = get_client()
    user = sp.current_user()
    print(f"Logged in as: {user['display_name']} ({user['id']})")
    
    track_uris = []
    found_details = []
    
    print("\nSearching for tracks...")
    for artist, title, desc in TRACKS_SPEC:
        query = f"artist:{artist} track:{title}"
        # Fallback if specific fails
        results = sp.search(q=query, limit=1, type="track")
        items = results["tracks"]["items"]
        
        if not items:
            # Try looser query
            query_loose = f"{artist} {title}"
            results = sp.search(q=query_loose, limit=1, type="track")
            items = results["tracks"]["items"]
            
        if items:
            track = items[0]
            track_uris.append(track["uri"])
            track_name = track["name"]
            track_artist = ", ".join(a["name"] for a in track["artists"])
            print(f"  ✓ Found: {track_artist} — \"{track_name}\" ({track['uri']})")
            found_details.append({
                "artist": track_artist,
                "title": track_name,
                "uri": track["uri"],
                "desc": desc
            })
        else:
            print(f"  X Could not find track: {artist} — \"{title}\"")
            
    if not track_uris:
        print("No tracks found. Exiting.")
        sys.exit(1)
        
    playlist_name = "John Lee Hooker & The Boogie Legacy"
    playlist_desc = "Core canon of John Lee Hooker, tracing his hypnotic one-chord boogie and modal drone through Canned Heat, ZZ Top, to hill country blues and modern rock."
    
    print(f"\nCreating playlist: {playlist_name}...")
    playlist = sp.user_playlist_create(
        user=user["id"],
        name=playlist_name,
        public=True,
        description=playlist_desc
    )
    
    playlist_id = playlist["id"]
    print(f"Playlist created successfully! ID: {playlist_id}")
    
    print("Adding tracks...")
    # Add in batches of 100
    sp.playlist_add_items(playlist_id, track_uris)
    print("Tracks added!")
    
    # Save the playlist metadata as local markdown file in guitar-coach-library/playlists/
    playlists_dir = proj_root / "guitar-coach-library" / "playlists"
    playlists_dir.mkdir(parents=True, exist_ok=True)
    
    md_path = playlists_dir / "john-lee-hooker-legacy.md"
    
    with open(md_path, "w") as f:
        f.write(f"# Playlist: {playlist_name}\n\n")
        f.write(f"**Spotify URL:** [Open in Spotify]({playlist['external_urls']['spotify']})\n")
        f.write(f"**URI:** `{playlist['uri']}`\n")
        f.write(f"**Description:** {playlist_desc}\n\n")
        f.write("## Track List & Influence Commentary\n\n")
        f.write("| # | Artist & Title | Focus & Historical Context | Play Command |\n")
        f.write("|---|----------------|---------------------------|--------------|\n")
        for i, detail in enumerate(found_details, 1):
            f.write(f"| {i} | {detail['artist']} — \"{detail['title']}\" | {detail['desc']} | `./scripts/spotify-mac.sh play-uri {detail['uri']}` |\n")
            
    print(f"\nMarkdown reference saved to: {md_path}")
    
    # Rebuild playlist viewer
    print("Rebuilding HTML playlist viewer...")
    os.system(f"uv run {proj_root}/scripts/generate_playlist_viewer.py --build-only")
    
    print("\nSyncing playlist...")
    os.system(f"bash {proj_root}/scripts/sync_playlists.sh")

if __name__ == "__main__":
    main()
