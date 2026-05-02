---
id: tele-electronic-veil-bickert
created: 2026-05-02
updated: 2026-05-02
guitar: Fender Player II Telecaster (Neck position, Flatwounds)
target: Ed Bickert "Electronic Veil" — Extremely dark, warm, and intimate. Simulates a traditional jazz box on a solid-body platform.
tags: jazz, telecaster, dark, warm, bickert, flatwounds
tone-king-channel: rhythm
status: initial
---

# The Electronic Veil (Ed Bickert Style)

## Target Sound
The goal is the quintessential "dark Tele" sound pioneered by Ed Bickert. By rolling off the physical tone knob and using high-headroom, neutral amplification, we create a thick, warm, "veiled" tone that softens the guitar's natural transients and emphasizes its electronic character. It should sound intimate, woody, and almost like a hollowbody jazz box, but with the steady, even sustain of a solid-body Telecaster.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Clean Blackface foundation; used as a warm tube buffer |
| Volume | 2.5 | Very low; keeps the signal pristine and uncolored |
| Attenuation | 5 | Nominal output level |
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
| Mic | **Ribbon 121** | Warm, dark, and smooth; rolls off highs naturally |

### 3. Logic Channel EQ — surgical shaping

| Band | Frequency | Gain | Slope / Q | Purpose |
|------|-----------|------|-----------|---------|
| High-cut | 4.0 kHz | 24 dB/oct | — | The "Veil" — removes all digital/electric "fizz" and air |
| Peak | 250 Hz | +2 dB | Q: 0.8 | Enhances the "woody" resonance of the neck pickup |

### 4. UADx LA-2A Gray Compressor — optical glue

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 40 | Moderate optical compression |
| Gain | 50 | Makeup gain |
| Mode | **Compress** | Slower attack/release enhances the "bloom" and sustain of the notes |

### 5. UADx Hitsville Reverb Chambers — intimate space

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | 2644 | Smoother, more intimate chamber |
| Mix | 5% | Extremely subtle; provides physical air without a tail |

---

## Starting Point Guide

- **Physical Tone Knob**: This is the most important control. Start with it at **3**. If it sounds too muffled, move to **4**. If you want more "veil," roll back to **2**.
- **Compression Bloom**: If the notes feel too "plucky," increase Peak Reduction on the LA-2A Gray. The goal is a smooth, even sustain where the attack is rounded off.
- **Midrange Body**: If the tone feels too thin, increase the **Middle** control on the Showtime '64 or slightly increase the **250Hz** bump in the Logic EQ.

---

## Feedback History

### 2026-05-02 — initial
Built for the BRG Player II Telecaster with flatwounds. Targets the Ed Bickert "Electronic Veil" using Showtime '64 for neutral headroom and LA-2A Gray for slow optical sustain. Reverb kept minimal with Hitsville Chambers.
