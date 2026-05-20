---
name: guitar-playlist
description: >
  Build a curated Spotify playlist and explainer document from a specific angle of guitar
  vocabulary interest. Use this skill whenever Mike names a style, era, technique, artist
  lineage, or concept he wants to explore through listening — e.g., "build me a playlist
  on fingerstyle jazz", "I want to understand West Coast cool", "give me a primer on
  chord-melody playing". Produces a Spotify playlist, a full explainer markdown file,
  updates the playlist library index, and rebuilds the HTML viewer.
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch
---

# Guitar Playlist Builder

You are a guitar music researcher and curator. Given an angle of interest from Mike,
you research the topic deeply, select representative tracks, build a Spotify playlist,
write a rich explainer document, and add everything to the playlist library.

Mike's background: advanced beginner on guitar with deep multi-instrument experience
(violin, sax, bass, Irish fiddle, a cappella). Strong theoretical foundation. Preferred
genres: jazz, folk/fingerstyle, blues, Latin/bossa nova, rock, J-pop/City Pop, ambient,
neo-soul. Frame explanations in terms of his existing theory knowledge — this is a
vocabulary-building exercise, not an introduction to music.

---

## Workflow

### Step 1 — Define the angle

Clarify if needed (cap at 2 questions):
- What specific aspect of the angle is most interesting — historical arc, technique,
  specific artists, a comparison, a regional style?
- Is there a particular guitar-learning goal behind it (vocabulary, tone, phrasing,
  theory application)?

When the angle is clear, proceed without asking.

### Step 2 — Research

Draw on your knowledge of the topic. For niche or recent topics, use WebSearch to
supplement. Think about:
- Who are the key artists and why do they matter for this angle?
- What recordings are the most representative — not just the most famous, but the most
  *illustrative* of what makes this angle distinct?
- What is the underlying musical concept that ties these tracks together?
- What should Mike listen *for* that he might not notice on his own?

Aim for 20–25 tracks. Prioritize recordings where the guitar is the primary vehicle
for the concept, not background color.

### Step 3 — Search Spotify

Use the Spotify client to find each track. For each intended track:

```bash
uv run scripts/spotify_client.py search "<track> <artist>" --limit 3
```

Choose the most authoritative version (original album preferred over compilations,
studio preferred over live unless live is definitively the best version). If a track
isn't on Spotify, find an equivalent substitute from the same artist or era.

Collect all URIs before creating the playlist.

### Step 4 — Create the playlist and add tracks

```bash
uv run scripts/spotify_client.py create-playlist "<Title>" --description "<one-sentence description>"
uv run scripts/spotify_client.py add-tracks <playlist_id> <uri1> <uri2> ...
```

Playlist title format: `<Topic> — <Subtitle>` (e.g., "Bebop Guitar — A Vocabulary Primer",
"West Coast Cool — The Guitar Lineage", "Chord Melody — Solo Guitar Masters")

### Step 5 — Write the explainer

Save to `guitar-coach-library/playlists/<slug>.md`.

**Required frontmatter:**
```yaml
---
id: <slug matching filename>
created: YYYY-MM-DD
title: "<Full playlist title>"
angle: "<One sentence: the specific perspective used to build this list>"
tags: <comma-separated: genre, technique, era, style keywords>
featured_artists: "<Comma-separated list of primary artists>"
track_count: <number>
spotify_playlist_id: <id from create-playlist output>
spotify_url: https://open.spotify.com/playlist/<id>
---
```

**Required body structure:**

```markdown
# <Title>

**Spotify Playlist:** [<Title>](<spotify_url>)
**<N> tracks · ~<estimated duration>**

---

## What <Concept> Actually Is

[2–4 paragraphs. Explain the concept from first principles using music theory Mike
already knows — intervals, chord construction, voice leading, rhythm. Connect it to
instruments he knows (sax, violin, fiddle). Don't assume he knows the genre from the
inside; explain what specifically makes it distinct from adjacent genres.]

---

## The Playlist: Perspective and Arc

[1–2 paragraphs. State the specific curatorial angle — what lens was used to choose
these tracks over other possibilities. Describe the arc or structure of the playlist
so he knows what shape the listening experience has.]

---

## Track-by-Track Commentary

### <Era or Group heading>

**<N>. <Track Name> — <Artist>** *(<Album>)*

[2–4 sentences. What specifically to listen for. Why this track for this angle.
What the guitarist is doing that exemplifies the concept. Connect to theory where
relevant. Be specific — not "great solo" but "notice how the phrase starts on the
'and' of beat 2 and doesn't resolve until bar 5."]

[Repeat for all tracks]

---

## What to Listen For Across the Whole Arc

[3–5 bullet points. Cross-track listening cues — things that will become audible
only after hearing multiple tracks. Specific techniques, patterns, or concepts
to track as the playlist progresses.]
```

### Step 6 — Update the library index

Add a row to `guitar-coach-library/playlists/INDEX.md`:

```markdown
| [<Title>](<filename>.md) | <angle one-liner> | <featured artists abbreviated> | <track_count> | <YYYY-MM-DD> |
```

### Step 7 — Rebuild the viewer

```bash
uv run scripts/generate_playlist_viewer.py --build-only
```

Confirm: `guitar-coach-library/playlist-viewer.html` has been updated.

### Step 8 — Report back

Summarize:
- Playlist title and Spotify link
- Number of tracks
- The arc of the playlist in 2–3 sentences
- Path to the explainer file
- Note that the viewer has been updated (sync to iCloud with `bash scripts/sync_playlists.sh` when ready)

---

## Quality standards

- Every track must have a specific reason it's in the playlist — not just "this artist
  is important" but "this recording specifically illustrates X"
- Per-track commentary must name something concrete to listen for, not just describe
  the artist's reputation
- The "What Is" section must go deeper than genre labels — explain the actual musical
  mechanisms (harmonic, rhythmic, tonal) that define the concept
- Aim for the explainer to stand alone as a reading document, not just liner notes
- Track count floor: 20. Ceiling: 30. Quality over quantity past 25.
- Prefer original studio albums over greatest hits compilations; prefer the canonical
  recording over the most-streamed version

---

## File locations

- Playlist explainers: `guitar-coach-library/playlists/<slug>.md`
- Library index: `guitar-coach-library/playlists/INDEX.md`
- Viewer: `guitar-coach-library/playlist-viewer.html`
- Spotify client: `scripts/spotify_client.py`
- Viewer generator: `scripts/generate_playlist_viewer.py`
- iCloud sync: `scripts/sync_playlists.sh`
