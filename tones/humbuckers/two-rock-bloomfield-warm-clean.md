---
amp: "Two-Rock Bloomfield"
created: 2026-05-08
guitar: "Gibson Les Paul Studio (490R neck pickup)"
id: two-rock-bloomfield-warm-clean
pickup_type: humbucker
preset_name: "Two-Rock Bloomfield Boutique Clean HB"
status: tested
tags: "boutique, clean, warm, les-paul, humbucker, two-rock, jazz-blues, neo-soul, bloomfield"
target: "High-end boutique clean through the Two Rock Bloomfield Drive — late-night blues, sophisticated jazz-blues, and neo-soul warmth; hi-fi and polished where Fender is glassy and Marshall is aggressive"
tone-king-channel: bypassed
updated: 2026-05-16
preset_data:
  amp_platform: mixwave
  amp_settings:
    Bass: 5
    Bright: false
    Deep: false
    Gain: 5
    Lead: false
    Master: 5
    Mid: false
    Middle: 5.5
    Presence: 5
    Reverb: 0
    Tone Stack Bypass: false
    Treble: 4.5
    Vibe: 5
  hitsville:
    decay: 2.0
    mix: 1.0
    pre_delay: 8.0
  la2a:
    gain: 28
    peak_reduction: 35
---

# Two Rock Bloomfield — Boutique Warm Clean

## Target Sound

The MixWave Two Rock Bloomfield Drive is named after Mike Bloomfield — the blues guitarist from Paul Butterfield Blues Band and Bob Dylan's Highway 61 Revisited era, whose tone sat in a warm, expressive, "studio quality" space that distinguished him from the grittier British blues players of the same period. The Two Rock amplifiers he inspired are high-end boutique amps known for extraordinary note separation, very touch-sensitive dynamics, and a warmth that's distinct from both Fender's characteristic glassiness and Marshall's midrange aggression.

The goal here is not "jazz clean" in the Showtime '64 sense — the Two Rock is not a neutral platform. It has a character: warm, polished, hi-fi. Where the Showtime '64 disappears behind the guitar, the Two Rock adds its own flavor — a refined, smooth quality that sounds like an expensive studio recording even when you're just noodling at home. With the LP Studio 490R neck pickup, the result is a late-night, smoky-lounge blues clean that works equally well for:

- Sophisticated jazz-blues (later Miles Davis collaborators' guitar work)  
- Neo-soul (D'Angelo's "Really Love," John Mayer acoustic-electric crossover)
- Nashville session recording clean
- Slack moments inside any clean tone set

**Gain Staging & Noise Floor Note:** This 100-watt boutique amp sim has an authentic, high modeled noise floor. A built-in noise gate at threshold `0.500` handles the idle hum. Current signal path: guitar direct into iD14 instrument input (no Tone King Imperial Preamp), iD14 gain at 0, Guitar bus set to Mono.

**Compare against Jazz Clean — Intimate Les Paul (Showtime '64):** Both use Gibson LP Studio 490R neck pickup and LA-2A Silver compression. The Showtime is specifically chosen to be transparent — it doesn't add its own color. The Two Rock *does* add color: slightly more warmth in the low-mids, more of an "amp in the room" quality, less "glass" in the top end. Both are valid jazz/clean platforms; the Two Rock has a personality the Showtime deliberately lacks.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. MixWave Two Rock Bloomfield Drive — boutique character source

The Two Rock Bloomfield Drive is a "powerful and high headroom amplifier" known for "rich cleans, harmonic overdrive, and smooth transitions between tones." The plugin has two channels: a clean channel (Gain + Master) and a separate lead channel (Lead Switch, Lead Gain, Lead Master). For this toneprint the lead channel stays off. Small EQ adjustments have noticeable effects — start neutral and listen.

**Switches and Configuration**

| Control | Setting | Purpose |
|---------|---------|---------|
| EQ Selection | **EQ 1** | Explicitly the clean-tone EQ choice: "lower gain structure with enhanced headroom," extended midrange, fuller bass |
| Bright Switch | Off | LP 490R neck humbucker is already warm; Bright boosts highs and would push this combination toward glassy |
| Mid Switch | Off | Start neutral; engage if the tone feels thin and lacks body |
| Deep Switch | Off | Deep boosts lower bass and smooths mids — LP neck already has substantial low end |
| Tone Stack Bypass | Off | Keep the EQ knobs active |
| Lead Switch | Off | Clean channel only |
| Tube Select | **6L6** | Maximum headroom for clean tones; 6V6 breaks up earlier and runs warmer |
| Full/Half Power | **Full (100w)** | Full power = most headroom; Half (50w) compresses slightly earlier |

**Amp Controls**

| Control | Setting | Purpose |
|---------|---------|---------|
| Gain | ~5 | Clean to barely-touching-breakup; at 5 this amp stays clean but a hard attack gives a slight bloom — that's the touch sensitivity character |
| Treble | 4.5 | Pulled back slightly from neutral to tame any high-end glass, ensuring a smokier, polished top end |
| Middle | 5.5 | Pushed slightly above neutral to highlight the Two Rock's signature midrange bloom and add body to the clean tone |
| Bass | 5 | Neutral; LP neck already has substantial low end; don't add more here |
| Presence | 5 | "Adjusts the contour of the high-frequency response" — subtle; raise slightly for more air, lower for a rounder, smoother quality |
| Master | ~5 | Clean channel output level; adjust relative to the full signal chain level |
| Reverb | 0 | Off — Hitsville handles the space |
| Vibe | 5 | "Affects top end harmonics" — reduce toward 3–4 for a warmer, more polished top end |

**Plugin I/O Trims**

| Control | Setting | Purpose |
|---------|---------|---------|
| Input Trim | −8.0 dB | Manages the hot boutique amp model; pads before the virtual circuit |
| Output Trim | −6.25 dB | Normalizes output to −12 dBFS target |

**Note on Built-in Processing:** Leave the plugin's integrated **Input/Output EQ** and **Compression** sections **bypassed**. We are relying on the external LA-2A for dynamics.

**Cabinet and Mic**

Cabinet: 2x12 Two-Rock Vertical (the only available cabinet). 

Use two mics: **Ribbon 84** on the Bottom speaker (for warmth and natural HF roll-off) and **Dynamic 57** on the Top speaker (for presence and definition). Blend to taste. 

**Built-in Overdrive Pedal**

The plugin includes an integrated overdrive section (Drive, Balance, Tone, Dry/Wet). Leave it **bypassed** for this toneprint — the Tim TONEX stomp listed below is the documented option for pushing this amp. Use one or the other, not both.

**Tone sensitivity note:** The Two Rock Bloomfield is not an amp that rewards aggressive setting changes. If the tone sounds slightly off, first try rolling the guitar's volume knob back to 7–8 — the Two Rock's response to guitar volume rolloff is exceptionally smooth and may already give you what you're looking for without touching any plugin settings.

---

### 3. UADx LA-2A Silver Compressor — organic glue

The Two Rock + LA-2A Silver optical combination is the studio-clean signature for this class of boutique amp. Because the MixWave plugin input is padded, the compressor requires a higher Peak Reduction setting to engage.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 35 | Targets `1–3dB` of gain reduction on firm strums; provides the "kiss" of optical smoothing and bloom the Two Rock is known for |
| Gain | 28 | Makeup gain adjusted for a smooth, healthy output level |
| Mode | Compress (3:1) | Gentle optical compression; not Limit mode |

---

### 4. UADx Hitsville Reverb Chambers — intimate room

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Bright, present character — cuts through well for guitar |
| Speaker | **Bozak 800** | The classic Chamber 1 speaker setup |
| Mic | **Unidyne 545** | Predecessor to the SM57; the most familiar-sounding mic for guitar reverb |
| Mix | **Wet Solo (100%)** | Plugin used on an Aux bus; balance controlled via send/fader |
| Decay | **9:00** | Shortened room reflection; provides depth without washing out the rhythm |
| Pre-Delay | 8 ms | Separation between dry note and room |

**Bus Configuration (Aux 2)**

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −12 dB | Gain-staged send from the main guitar track |
| Bus Fader | −8 dB | Final reverb level in the mix |

---

## Optional TONEX Stomp (pre-Tone King)

| Capture | Character | Why it works here |
|---------|-----------|-------------------|
| **Tim (Paul Cochrane)** (~52 captures) | Versatile OD designed for high-end amplifiers — stays musical at any gain level, very amp-friendly | The Tim is famously well-matched to boutique amps like the Two Rock; it pushes the amp into a warm, slightly-driven territory without imposing its own color; multiple captures at different knob positions — look for "low gain" or "clean boost" settings |

*Default: stomp bypassed. The Two Rock clean tone is complete without a pedal. Engage the Tim if you want to push into a warm, barely-driven territory — the Two Rock + Tim combination is well-documented in boutique blues contexts.*

---

## Starting Point Guide

- **The LA-2A Silver is not optional:** Don't skip it. The Two Rock's touch sensitivity, while a feature, benefits significantly from the optical smoothing at Peak Reduction 35. Without it, the tone may feel too "raw" or the dynamics too wide for the refined character this amp is known for.
- **Guitar volume rolloff exploration:** The Two Rock is known for cleaning up very gracefully. Roll the Les Paul's volume knob back to 7 — the tone should still be full and balanced, just slightly softer. At 5, it may become a delicate, fingerpicking-appropriate touch. Document what you find in Feedback History.
- **The Two Rock vs. Showtime '64 comparison:** Both are clean LP neck tones. The Showtime disappears; the Two Rock has presence and warmth. If you feel like "this is just a slightly different Jazz Clean," that might be the correct assessment — or it might mean the Two Rock's character is so well-integrated that it sounds natural. Play the same chord progressions through both and trust your ears.
- **Neo-soul direction:** For John Mayer's "Slow Dancing in a Burning Room" / "Gravity" aesthetic, add the Tim TONEX stomp at low gain and raise the Presence control slightly. The combination produces the "singing clean" that defines that genre.

---

## Feedback History

### 2026-05-08 — initial
Built to explore the Two Rock Bloomfield Drive's boutique clean character. LP Studio 490R neck, LA-2A Silver at Peak Reduction 35 (integral, not optional), Hitsville 2648 chamber. Tim TONEX stomp as optional neo-soul push. Signal chain originally used placeholder control names pending UI verification.

### 2026-05-08 — tested
Verified in DAW session. LP Studio 490R neck → Tone King (Vol 3) → MixWave Two Rock. Key findings: Plugin is extremely hot; **Input dialled to -9.0** and **Noise Gate at 0.500** are mandatory to manage gain staging and noise floor. LA-2A Silver updated to **Peak Reduction 55** and **Gain 40** to compensate for the input pad while achieving 3dB of musical compression. Hitsville Decay pulled back to **2.5 (9:30)** for rhythm clarity. Opinionated EQ (Treble 4.5, Mid 5.5) confirmed. End-to-end levels: ~ -22.7dB in / -12.1dB out. Status updated to `tested`.

### 2026-05-16 — gain staging calibration (direct to iD14)
Signal path changed: guitar now routes direct into iD14 instrument input (Tone King Imperial Preamp bypassed pending its own calibration pass). iD14 gain set to **0**. Guitar bus changed to **Mono** (was Stereo when driven by TKIP). MixWave Two Rock I/O trims set: **Input −8.0 dB / Output −6.25 dB**. LA-2A recalibrated: **Peak Reduction 35 / Gain 28** (down from PR 55 / Gain 40 — previous values were compensating for the padded input that no longer applies). Hitsville reverb send updated to **−12 dB** (was −20 dB); bus fader unchanged at −8 dB.

### 2026-05-13 — reverb bus update
Moved Hitsville Reverb to a dedicated Aux bus (Aux 2). Set plugin to **Wet Solo**, updated Decay to **9:00**. Configured send at **-20dB** and bus fader at **-8dB** for better spatial control and session organization.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
