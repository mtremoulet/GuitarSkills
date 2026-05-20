#!/usr/bin/env python3
# /// script
# dependencies = ["spotipy", "python-dotenv"]
# ///
"""
Script to create the "Vox AC30 & Humbucker Velvet Chime" playlist.
Searches for tracks displaying the iconic Les Paul/humbucker into Vox AC30 character,
creates the playlist on Spotify, and syncs everything locally and to iCloud.
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

# Tracks spec: (artist, title, description)
TRACKS_SPEC = [
    # ─── THE BEATLES (LATER ELECTRIFIED ERA) ───
    ("The Beatles", "Revolution - 1969 Stereo Mix", "The ultimate fuzzy, compressed humbucker AC30 grit. Conversational, thick, and saturated."),
    ("The Beatles", "Sgt. Pepper's Lonely Hearts Club Band - Remastered 2009", "Thick, throat-like humbucker overdrive pushing the Class A power section."),
    ("The Beatles", "Getting Better - Remastered 2009", "Chimey, staccato rhythm tracks with that characteristic 'papery' AC30 compression."),
    
    # ─── QUEEN (BRIAN MAY SATURATED ORCHESTRAL VOICE) ───
    ("Queen", "Killer Queen - Remastered 2011", "Exquisite, vocal multitracked lead harmonies. Thick humbucker-like serial tone with sharp treble boost chime."),
    ("Queen", "Bohemian Rhapsody - Remastered 2011", "The legendary solo. Creamy, compressed velvet crunch with endless sustain and mid-focus."),
    ("Queen", "Tie Your Mother Down - Remastered 2011", "Aggressive, biting slide and driving riffs — demonstrating the high-gain capacity of Class A tubes."),
    
    # ─── U2 (THE EDGE'S WARM ARENA SHIMMER) ───
    ("U2", "Pride (In The Name Of Love) - Remastered 2008", "Gibson Explorer humbuckers running into a 1964 AC30, swimming in warm analog tape delay."),
    ("U2", "Where The Streets Have No Name - Remastered 2007", "The ultimate clean-chime reference. Glassy top-end detail balancing warm mid-range sustain."),
    ("U2", "Bad - Remastered 2009", "Expressive, dynamic single-note lines showcasing the early optical compression of the LA-2A + AC30 interaction."),
    
    # ─── RADIOHEAD (COMPLEX INDIE-ROCK CHIME) ───
    ("Radiohead", "Airbag", "Jonny Greenwood's aggressive, mid-heavy crunch and Thom Yorke's chimey rhythm parts running into AC30s."),
    ("Radiohead", "Let Down", "Interlocking, glassy arpeggios showing the clean articulation of humbuckers through Celestion Blues."),
    ("Radiohead", "Bodysnatchers", "Blistering, raw, high-gain indie crunch. The sound of dual-humbuckers fully saturating an EL84 power section."),
    
    # ─── BRITPOP & ALTERNATIVE WALL OF CRUNCH ───
    ("Oasis", "Supersonic", "Noel Gallagher's Gibson Les Paul/SG into a Vox AC30, building a thick, massive wall of British crunch."),
    ("Oasis", "Don't Look Back In Anger", "Classic, warm rhythm track and singing, melodic guitar solos with throat-like humbucker character."),
    ("R.E.M.", "What's The Frequency, Kenneth?", "Peter Buck running humbucker-equipped semi-hollows into hot Vox amps for a thick, jangly alternative grind."),
    ("Foo Fighters", "Everlong", "Rich, saturated drop-D rhythm tracks blending humbucker thickness with Class A upper-mid definition.")
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
        results = sp.search(q=query, limit=1, type="track")
        items = results["tracks"]["items"]
        
        if not items:
            # Loose query
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
        
    playlist_name = "Vox AC30 & Humbucker Velvet Chime"
    playlist_desc = "The rich, touch-sensitive pairing of humbucker guitars (Les Pauls, SGs, Explorers) and the hot, chimey Vox AC30 (Ruby '63). Inspiration for the Class A Velvet Crunch toneprint."
    
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
    sp.playlist_add_items(playlist_id, track_uris)
    print("Tracks added!")
    
    # Save local markdown reference
    playlists_dir = proj_root / "guitar-coach-library" / "playlists"
    playlists_dir.mkdir(parents=True, exist_ok=True)
    
    md_path = playlists_dir / "vox-ac30-humbucker-chime.md"
    
    with open(md_path, "w") as f:
        f.write(f"# Playlist: {playlist_name}\n\n")
        f.write(f"**Spotify URL:** [Open in Spotify]({playlist['external_urls']['spotify']})\n")
        f.write(f"**URI:** `{playlist['uri']}`\n")
        f.write(f"**Description:** {playlist_desc}\n\n")
        f.write("## Track List & Inspiration Commentary\n\n")
        f.write("| # | Artist & Title | Tone Focus & Inspiration | Play Command |\n")
        f.write("|---|----------------|--------------------------|--------------|\n")
        for i, detail in enumerate(found_details, 1):
            f.write(f"| {i} | {detail['artist']} — \"{detail['title']}\" | {detail['desc']} | `./scripts/spotify-mac.sh play-uri {detail['uri']}` |\n")
            
    print(f"\nMarkdown reference saved to: {md_path}")
    
    # Rebuild playlist viewer
    print("Rebuilding HTML playlist viewer...")
    os.system(f"uv run {proj_root}/scripts/generate_playlist_viewer.py --build-only")
    
    # Sync playlist
    print("Syncing playlist...")
    os.system(f"bash {proj_root}/scripts/sync_playlists.sh")

if __name__ == "__main__":
    main()
