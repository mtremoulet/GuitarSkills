---
id: "dream-65-blackface-sparkle"
preset_name: Dream 65 Blackface Sparkle SC
created: "2026-05-08"
updated: "2026-05-08"
guitar: "Fender Player II Telecaster (bridge pickup, roundwound strings)"
target: "Classic Blackface sparkle and country spank — chicken-picking, surf, 60s soul/R&B, and yacht rock shimmer through the Dream '65 Deluxe Reverb"
tags: "blackface, country, surf, sparkle, telecaster, single-coil, dream-65, spring-reverb"
tone-king-channel: rhythm
amp: "Dream '65"
status: tested
pickup_type: "single-coil"
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 2
    Treble: 5
    Bass: 5
    Bright: false
  la2a:
    peak_reduction: 40
    gain: 20
---

# Dream '65 — Blackface Sparkle

## Target Sound

The Dream '65 (Fender Blackface Deluxe Reverb '65) is the country-and-clean amp in the UADx collection — a 22-watt combo with its own built-in spring reverb, bias tremolo, and a distinctly characterful Blackface voice. Where the Showtime '64 has been used throughout this rig as a neutral, transparent platform, the Dream '65 *imposes* itself: mid-scoop, sparkly highs, and a warmth that compresses and blooms earlier than the Showman/Twin. This toneprint is about leaning into that character rather than working around it.

The D-Tex mod circuit adds harmonic richness that keeps the Blackface sparkle musical rather than glassy — "Texas" warmth on top of American chime. This is the SRV clean-space, the chicken-picking country spank, the yacht rock shimmer. The Tele bridge pickup and the Deluxe Reverb are a natural pairing: the snap and articulation of the bridge single-coil through a low-headroom combo with spring reverb is one of the most iconic clean tones in American music.

**This tone vs. similar toneprints:** Woodrow Sweet Spot (Tweed, mid-forward, low headroom, compresses into grit) is blues/rock territory. This is cleaner, more articulate, and brighter — country and pop clean territory. The Showtime-based toneprints are intentionally colorless; this one isn't.

**Gain Staging & Future Optimization Note:** In testing, end-to-end levels were ~ `-19.8dB` input and ~ `-13.3dB` output. To manage the modeled noise floor, set the **Amp Volume to 2.5**. The inline reverb (Space Designer) should eventually be moved to a shared Aux 1 (Reverb Bus) with "100% Wet" to standardize the DAW template.

**Note — Tele bridge vs. Strat adjustments:** If using the Squier Stratocaster instead, enable the Bright switch on the Dream '65 and raise Treble to 6. The Strat's lower-output single coils handle the added brightness without getting ice-picky. Strat bridge + middle ("quack" position) is the classic alternate pairing.

---

## Signal Chain

### 1. Tone King Imperial Preamp — passive front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Cleanest available voicing |
| Volume | 2 | Tele bridge has more output than Strat — keep TK in transparent buffer territory |
| Attenuation | 5 | Moderate; let Dream '65 set the level |
| Bass | 5 | Flat — Dream '65 handles its own EQ character |
| Treble | 5 | Flat |
| Reverb | Off | Dream '65 has its own spring reverb — avoid doubling |
| Tremolo | Off | — |
| IR | **Bypassed** | Dream '65 handles the cab simulation |

---

### 2. UADx Dream '65 Reverb Amp — character source

The Dream '65 is a low-headroom amp — the sweet spot for this tone is Vol 2.5–3. Light touch stays clean; harder attack gets a small bloom of harmonic color.

| Control | Setting | Purpose |
|---------|---------|---------|
| Bright / Normal | **Normal** | Tele bridge is already bright |
| Mod Circuit | **D-Tex** | Adds harmonic richness and warmth to the Blackface voice |
| Volume | 2.5 | Set low to maximize clean headroom and prevent fizz |
| Treble | 4–5 | Pulled back from noon |
| Bass | 5 | Neutral |
| Reverb | 3 | Moderate spring reverb — present but not "surfboard" |
| Tremolo Speed | 4 | Default off; when engaged: slow, lapping-wave rate |
| Tremolo Depth | 3 | Subtle when on |
| Input/Output | 0.0 dB | Neutral plugin gain |
| Noise Gate | 20.0 | Threshold to kill the modeled idle hum |

**Cab and mic selection:** Start with the 1x12 internal option. 

---

### 3. UADx LA-2A Silver Compressor — dynamics control

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 40 | Yields `0 to 1dB` of reduction; prevents makeup gain from amplifying the amp's idle fizz during note decay |
| Gain | 20 | Makeup gain for a healthy final output |
| Mode | Compress (3:1) | Preserve picking dynamics |

---

### 4. Logic Space Designer — room supplement

| Control | Setting | Purpose |
|---------|---------|---------|
| IR | Small studio room or small hall | Complements the spring reverb |
| Pre-Delay | 5 ms | Keep the dry attack first |
| Size | 65% | Short, tight room |
| Dry | 0.0 dB | Unity |
| Wet | −22 dB | ~8% — barely perceptible |

**Optimization Note:** Eventually move to a dedicated Aux Reverb Bus with "100% Wet".

---

## Optional TONEX Stomp (pre-Tone King)

Both options sit *before* the Tone King in the signal chain — either as the TONEX ONE hardware pedal on the pedalboard, or as a TONEX plugin instance on the Logic channel before the Tone King routing.

| Capture | Character | Why it works here |
|---------|-----------|-------------------|
| **Nobels ODR-1** (~8 captures) | SRV's actual boost pedal — slight mid-push, transparent body | Adds the front-end push SRV used into his Vibroverb without changing the amp's clean voice; good for slight blues-country grit |
| **Tumnus Germanium DLX** (~78 captures) | Klon-variant with germanium character, very transparent | Cleanest boost option — adds shimmer and sustain without mid-hump; good for yacht rock and soul where you want more presence, not more grit |

*Default: stomp bypassed. The Dream '65 clean tone stands alone; engage only when you want intentional front-end push.*

---

## Starting Point Guide

- **Tremolo default:** Off. Turn on for any 60s country or soul vibe — keep Speed at 4 and Depth at 3 for a lapping-wave feel, not a warble.
- **Spring reverb lever:** Reverb 3 is the home base. Pull to 2 for a more "studio" sound; push to 5–6 for full surf character. If it sounds like you're playing underwater, you've gone too far.
- **Tele bridge vs. neck:** This toneprint is calibrated for bridge pickup. The neck pickup of the Tele will be noticeably warmer and rounder — push Treble to 6 and consider enabling Bright switch for neck pickup use.
- **Compare to Woodrow Sweet Spot:** Both are "single-coil Strat/Tele" tones, but the Woodrow compresses and blooms into grit; this one stays cleaner and more articulate. If you want dynamics to drive grit, reach for the Woodrow. If you want clean sparkle that stays clean under hard playing, this is it.

---

## Feedback History

### 2026-05-08 — tested
Verified in DAW session. Key findings: **Volume 2.5** on the amp is necessary for clean headroom. **LA-2A at Peak Reduction 40 / Gain 20** yields minimal reduction but prevents "noise floor fizz" on decay. End-to-end: ~ -19.8dB in / -13.3dB out. Status updated to `tested`.

### 2026-05-08 — initial
Designed around the Dream '65's Blackface character as a country/sparkle platform — filling the gap left by using Showtime '64 as a neutral amp for all clean work. Tele bridge specified as primary guitar; Strat noted as alternate with Bright switch and Treble 6. D-Tex mod circuit chosen for its harmonic warmth over Stock. Spring reverb retained as a feature, not fought against. TONEX ODR-1 and Tumnus Germanium DLX listed as optional pre-amp boosts.
