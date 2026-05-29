---
id: woodrow-sweet-spot-p90
preset_name: "Woodrow Sweet Spot P90"
created: 2026-05-26
updated: 2026-05-27
guitar: Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)
target: "The Tweed Deluxe \"Sweet Spot\" — optimized for P-90s: vocal, mid-forward crunch that is highly touch-sensitive, woody, and raw."
tags: tweed, woodrow, blues, classic-rock, framus, p-90, compressed, mid-forward
tone-king-channel: rhythm
amp: Woodrow '55
status: tested
pickup_type: p-90
---

# Woodrow Sweet Spot (P-90 Variant)

## Target Sound

The Tweed Deluxe (UADx Woodrow '55) is the polar opposite of scooped Blackface-style amps. It is a mid-forward, woolly, and highly compressed circuit with very little clean headroom. If you push a Tweed too hard, the low end collapses, resulting in a muddy, "farting out" distortion. The magic of a Tweed lives in the **Sweet Spot**: where playing softly sounds clean, woody, and dynamic, but digging in instantly adds a glorious, organic harmonic growl.

P-90s and Tweed Deluxe amps are one of the most legendary tonal pairings in history—representing the raw, explosive blues-rock tones of Neil Young's "Old Black" or early Larry Carlton session sounds. 

Because the DiMarzio P-90s in your Framus are much hotter than standard Strat single-coils, they will push the Woodrow into heavy compression much earlier. To preserve the touch-sensitive clean-to-grit transition, we make three essential tweaks:
1.  **Lower Instrument Volume**: We set the primary Volume (Inst) to **3.0** (down from 3.5) to keep the preamp in its touch-sensitive range.
2.  **Tame the Low End**: We lower the Volume (Mic) to **2.5** (down from 3.0). The Mic channel is where the Tweed's heavy low end lives; lowering it prevents the hot P-90 neck pickup from muddying the bass.
3.  **Treble Damping**: We set the Tone control to **5.0** (noon) to smooth out the snappy transients of the swamp ash body and roundwound strings.

We pair this raw vintage head with a subtle **Galaxy Tape Echo** and a fast **LA-2A Gray compressor** to glue the echo to the Tweed's natural power-amp sag.

---

## Signal Chain

### 1. Tone King Imperial Preamp — transparent buffer front-end
*   **Status:** **ACTIVE**
*   **Purpose:** Acting as a high-quality hardware signal buffer driving the audio interface cleanly.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Cleanest available Tone King voicing |
| Volume | 2.0 | Kept very low to prevent preamp coloration |
| Attenuation | 5.0 | Moderate output |
| Bass | 5.0 | Flat EQ |
| Treble | 5.0 | Flat EQ |
| Reverb / Tremolo | Off | Bypassed |
| IR | **Bypassed** | Woodrow handles the full amp + cab simulation |

---

### 2. Guitar Track → UADx Woodrow '55

We jump the channels by running both Volume controls simultaneously above 0. Input is set to High (Input 1) for the primary gain stage.

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume (Inst) | **3.0** | The primary "bite" and gain. Kept low to preserve the clean-to-grit transition |
| Volume (Mic) | **2.5** | Adds midrange body. Rolled back to keep P-90 low-end from muddying |
| Tone | **5.0** | **CRITICAL:** Adjusts gain and high-end contour. Noon is the sweet spot for P-90s |
| Boost (Stock) | **TOGGLE OFF** | Bypasses the extra gain stage to keep the signal path pure |
| Input | **High (Input 1)** | Sets primary gain stage |
| Room | **25%** | Adds natural studio air and depth |
| Cabinet | **GB25** | **Fixed Cabinet**: Celestion Greenback + 57; provides classic mid-forward bark |

---

### 3. UADx Galaxy Tape Echo — subtle depth

Tweed amps and tape echo are a match made in heaven. The tape saturation complements the amp's vocal midrange, and a subtle slapback adds classic space.

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 1 | Single head for focused slapback |
| Echo Rate | 6.5 | **Clockwise = Shorter.** ~100ms on Head 1 for classic depth |
| Feedback | 1.5 | Set low for essentially a single ghost repeat |
| Echo Volume | 2.0 | Supportive; a subtle "shadow" behind the note |
| Tape Age | New | Keeps the repeats clean and distinct |

---

### 4. UADx LA-2A Gray Compressor — post-amp glue

Because the Woodrow is already compressing heavily in its virtual power tubes, we use the faster Gray LA-2A very lightly, just to catch any stray peaks and glue the tape echo to the amp decay.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | **30** | Slightly firmer squeeze; catches peaks and glues the sound |
| Gain | **25** | Makeup gain |
| Mode | Compress | Gentle optical compression |

---

## Starting Point Guide

- **Tasting the Tweed Magic**: Set the Framus to the **Neck/Middle position (Pos 2)**. Play a sustained chord very softly—it should sound woody, clean, and clear. Now, hit a double-stop (two notes) hard. You should hear the virtual amp "clamp down" and add a glorious, vocal, fuzzy hair to the notes.
- **Taming the Low E "Fart"**: If your low E string sounds mushy or distorted in an unpleasant way when playing hard, roll the **Volume (Mic)** down to **2.0**.
- **The Neil Young "Old Black" Vibe**: Switch the Framus to the **Bridge P-90**, push the **Volume (Inst)** up to **5.0**, and roll your physical **Guitar Volume knob** back to **7**. The amp will growl and saturate beautifully, giving you an explosive, highly organic rock-crunch that sings.

---

## Feedback History

### 2026-05-27 — tested
Tested by Mike. Amended the LA-2A Gray settings to **Peak Reduction 30** and **Gain 25** for a slightly firmer squeeze that better catches peaks and glues the tone together. Status updated to `tested`.

### 2026-05-26 — initial
Ported from single-coil Strat variant. Keeps Tone King active as a transparent buffer. Tweaks Woodrow parameters: lowers Volume (Inst) to 3.0 to protect touch-sensitivity with the hotter P-90s, lowers Volume (Mic) to 2.5 to prevent low-end mud, and sets Tone to 5.0 (noon) to smooth out the swamp ash snap.
