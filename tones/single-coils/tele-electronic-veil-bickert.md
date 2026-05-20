---
id: tele-electronic-veil-bickert
created: 2026-05-02
updated: 2026-05-10
guitar: Fender Player II Telecaster (Neck position, Flatwounds)
target: "Ed Bickert \"Electronic Veil\" \u2014 Extremely dark, warm, and intimate.\
  \ Simulates a traditional jazz box on a solid-body platform."
tags: jazz, telecaster, dark, warm, bickert, flatwounds
tone-king-channel: rhythm
amp: Showtime '64
status: tested
pickup_type: single-coil
---

# The Electronic Veil (Ed Bickert Style)

## Target Sound
The goal is the quintessential "dark Tele" sound pioneered by Ed Bickert. By rolling off the physical tone knob and using high-headroom, neutral amplification, we create a thick, warm, "veiled" tone that softens the guitar's natural transients and emphasizes its electronic character. It should sound intimate, woody, and almost like a hollowbody jazz box, but with the steady, even sustain of a solid-body Telecaster.

## Signal Chain

**Routing**: Logic Pro mono input only — **do not use stereo input** (signal is mono; stereo mode only carries signal on the left channel).

This tone works well in either physical routing:
- **Direct**: Guitar → iD14 JFET instrument input
- **Through preamp**: Guitar → Tonex → Tone King Imperial Preamp → iD14 JFET instrument input

Character differs between the two (see Feedback History), but both are usable without any plugin changes.

### 1. Tone King Imperial Preamp — physical front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Clean Blackface foundation; used as a warm tube buffer |
| Volume | 6 | Sets output level into the interface |
| Attenuation | 7 | Controls preamp drive; compensates for pickup strength |
| Bass | 5 | Neutral |
| Treble | 2 | Significant treble rolloff; darkens the preamp path to match direct character |
| IR | Bypassed | UAD Showtime '64 handles the cab |

### 2. UADx Showtime '64 Tube Amp — clean platform

Chosen for its extreme headroom and neutral character. Unlike a Deluxe Reverb, it doesn't impose a mid-scoop, allowing the "woodiness" of the neck pickup to stay forward.

| Control | Setting | Purpose |
|---------|---------|---------|
| In | HI-Z | |
| Bright / Normal | **Normal** | Removes the bright cap; essential for the dark veil |
| Volume | 3 | Deep clean territory |
| Treble | 3 | Pulled back to further soften the top end |
| Middle | 5 | Neutral; keeps the midrange present |
| Bass | 4 | Controlled; flatwounds already provide plenty of body |
| Vibrato | Off | |
| Room | Off | Reverb handled by Hitsville Chambers |
| Mic | **Ribbon 160** | Ribbon mic; warm and dark with natural HF roll-off (Ribbon 121 not available in plugin) |
| Noise Gate | Off | Gate masks the buzz symptom without fixing it; source noise resolved at TKIP/interface instead |
| Input Trim | 0 dB | |
| Output Trim | +12 dB | Compensates for quiet signal into Showtime |

### 3. Logic Channel EQ — surgical shaping

| Band | Frequency | Gain | Slope / Q | Purpose |
|------|-----------|------|-----------|---------|
| High-cut | 4.0 kHz | 24 dB/oct | — | The "Veil" — removes all digital/electric "fizz" and air |
| Peak | 250 Hz | +2 dB | Q: 0.8 | Enhances the "woody" resonance of the neck pickup |

### 4. UADx LA-2A Gray Compressor — optical glue

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 32 | Moderate optical compression (~3 dB reduction) |
| Gain | 25 | Makeup gain |
| Mode | **Compress** | Slower attack/release enhances the "bloom" and sustain of the notes |

### 5. UADx Hitsville Reverb Chambers — intimate space

Placed on **Bus 2** (Reverb bus). Channel send: **−20 dB**.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | 2644 | Smoother, more intimate chamber |
| Mix | 5% | Extremely subtle; provides physical air without a tail |
| Decay | **9:00** | Short decay; keeps reverb intimate rather than washy |
| **Wet Solo** | **ON** | Correct for a send/bus setup — outputs only the wet signal |
| All other controls | Default | No further shaping needed at this mix level |

---

## Gain Staging Reference

With TKIP in chain at the settings above, guitar tone at ~30%, guitar volume at ~90%:

| Point | Level |
|-------|-------|
| Input to chain | −21 dBFS |
| Output (stereo bus) | −12 dBFS |

If input drifts significantly from −21, adjust TKIP Attenuation first (lower = more output), then Volume.

---

## Starting Point Guide

- **Physical Tone Knob**: This is the most important control. Start with it at **3**. If it sounds too muffled, move to **4**. If you want more "veil," roll back to **2**.
- **Compression Bloom**: If the notes feel too "plucky," increase Peak Reduction on the LA-2A Gray. The goal is a smooth, even sustain where the attack is rounded off.
- **Midrange Body**: If the tone feels too thin, increase the **Middle** control on the Showtime '64 or slightly increase the **250Hz** bump in the Logic EQ.

---

## Feedback History

### 2026-05-02 — initial
Built for the BRG Player II Telecaster with flatwounds. Targets the Ed Bickert "Electronic Veil" using Showtime '64 for neutral headroom and LA-2A Gray for slow optical sustain. Reverb kept minimal with Hitsville Chambers.

### 2026-05-03 — tested
Confirmed working. Hitsville on Bus 2, send at −12 dB. Ribbon 160 substituted for Ribbon 121 (not available in plugin). Wet Solo must be turned OFF (on by default). Decay at Max is fine at this send/mix level. Tone King Attenuation adjusted to taste per guitar.

### 2026-05-10 — routing confirmed dual-path; reverb and treble adjusted
Both direct (JFET only) and through-preamp (Tonex → TKIP → JFET) confirmed working without plugin changes. TKIP Treble pulled to 2 to darken the preamp path. Bus send reduced from −12 dB to −20 dB — less echo, more intimate air. Character note: through-preamp sounds more articulate and bright; direct sounds more gelled and darker. Likely the tube harmonics and TKIP tone stack coloration vs. a flat JFET path, rather than strictly a Fender mid-scoop.

### 2026-05-10 — gain staging overhaul
Resolved persistent zzZZZ buzz: source was Tonex/TKIP pedal chain interaction, not a ground loop. Switched Logic input to MONO (stereo input only carried signal on left channel). TKIP settings dialed in: Attenuation 7, Volume 6, Bass 5, Treble 4. LA-2A backed off to PR 32 / Gain 25 — gentler compression with no noise lifting. Showtime noise gate turned off (gate was masking the symptom; source fixed at hardware). Reverb corrected: Wet Solo ON (correct for bus setup), Decay to 9:00 for a shorter, more intimate tail. Gain staging now −21 to −12 dBFS E2E.
