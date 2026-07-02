---
amp: "Dream '65 (UADx)"
created: 2026-05-08
guitar: "Gibson Les Paul Studio (490R neck pickup)"
id: dream-65-blackface-jazz
pickup_type: humbucker
preset_name: "Dream 65 Blackface Jazz HB"
status: tested
tags: "jazz, clean, warm, les-paul, humbucker, dream-65, blackface, comparison"
target: "Warm jazz clean through the Dream '65 — Blackface character comparison to the Showtime-based Jazz Clean Intimate; how does the Deluxe Reverb's mid-scoop and spring reverb change the LP neck's jazz voice?"
tone-king-channel: bypassed
updated: 2026-06-28
preset_data:
  amp_platform: uad_paradise
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  amp_settings:
    Bass: 5
    Bright: false
    Reverb: 2
    Treble: 5
    Volume: 2.5
  hitsville:
    decay: 2.0
    mix: 0.08
    pre_delay: 6.0
  la2a:
    gain: 25
    peak_reduction: 32
---

# Dream '65 — Blackface Jazz

## Target Sound

The Jazz Clean — Intimate Les Paul toneprint uses the Showtime '64 specifically because it does *not* impose Fender color — its high headroom and neutral character lets the 490R neck pickup speak for itself. This toneprint asks the inverse question: what does the Dream '65's Blackface character do to the same guitar in the same musical context?

The Dream '65 (Fender Blackface Deluxe Reverb '65) has a natural mid-scoop, sparkly top end, and built-in spring reverb — none of which are part of the Showtime '64's signal. Through a humbucker neck pickup, some of that brightness will be absorbed, but the Blackface personality will still be audible.

**Gain Staging & Character Note:** The Deluxe Reverb is famously loud and breaks up early. In testing, the amp was set to **Volume 2.5** to maintain clean headroom. This preset leans naturally towards "country twang" and "bright jangle" — to push it toward jazz, roll the guitar's physical tone knob back to 6 or 7. End-to-end levels: ~ `-19.8dB` at track input and ~ `-13.3dB` at stereo output.

**Compare against Jazz Clean — Intimate Les Paul (Showtime '64):** Both use Gibson LP Studio 490R neck pickup and LA-2A Silver compression. The Showtime is specifically chosen to be transparent — it doesn't add its own color. The Dream '65 adds a distinct mid-scoop and high-end sparkle that confirms the Showtime as the superior neutral jazz platform, while the Dream serves better for country/soul/R&B contexts.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

**Pre-FX / Pre-Amp Stompbox Option**

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 2. UADx Dream '65 Reverb Amp — Blackface character source

Normal channel and Stock mod preserve as much of the LP's natural voice as possible while still letting the Dream '65's Blackface character come through.

| Control | Setting | Purpose |
|---------|---------|---------|
| Bright / Normal | **Normal** | LP 490R neck + Normal channel = warm and smooth |
| Mod Circuit | **Stock** | Most neutral version of the Dream '65 |
| Volume | 2.5 | Set low to preserve clean headroom and prevent early breakup |
| Treble | 5 | Neutral; roll back to 3.5 or 4 if the "twang" is too prominent |
| Bass | 5 | Neutral |
| Reverb | 2 | Very light spring reverb — just a hint |
| Tremolo | Off | — |
| Input Trim | −8.0 dB | Plugin-level pad; calibrated 2026-05-16 for direct-to-iD14 path |
| Output Trim | +10.0 dB | Makeup gain to restore −12 dBFS after amp model |
| Noise Gate | 20.0 | Threshold to kill the modeled idle hum |

**Cab and mic:** Try the 1x12 internal first. 

---

### 3. UADx LA-2A Silver Compressor — optical sustain

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 32 | Light optical compression; set low to prevent makeup gain from amplifying the amp's modeled idle noise during note decay |
| Gain | 25 | Makeup gain for a healthy final output |
| Mode | Compress (3:1) | Preserve dynamics |

---

### 4. UADx Hitsville Reverb Chambers — intimate room

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Bright, present character; close and intimate |
| Speaker | **Bozak 800** | Standard setup |
| Mic | **Unidyne 545** | SM57-style character |
| Mix | −22 dB (~8% wet) | Minimal physical space |
| Decay | 2.0 (9:00) | Shortened room reflection for clarity |
| Pre-Delay | 6 ms | Dry note attack first |

**Optimization Note:** Keep as an inline insert for now; eventually move to a dedicated Aux Reverb Bus for better template organization.

---

## Starting Point Guide

- **First comparison:** Load this and Jazz Clean — Intimate side by side in the same session. Play the same phrase through each. The Blackface mid-scoop should be audible on the LP neck — if it makes the 490R sound thin or scooped, that confirms why the Showtime was the right choice for jazz. If it sounds warm and musical, it's a second valid platform.
- **The spring reverb difference:** Even at Reverb 2, the Dream '65's spring reverb adds a quality that Hitsville chamber alone doesn't. If you prefer the result with the spring reverb, raise it to 3. If it feels out of place in a jazz context, pull it to 1 or off.
- **Treble lever:** If the LP sounds too scooped in the low-mids (notes feeling thin), raise Treble to 6 to compensate for the Blackface mid-scoop's effect on humbucker output. If it sounds balanced, leave at 5.
- **Unexpected direction:** If the Dream '65 + LP neck ends up sounding more Country/Soul than jazz (the mid-scoop and sparkle pulling it that direction), note that in Feedback History and consider using the Blackface Jazz toneprint for those styles instead of jazz proper.

---

## Feedback History

### 2026-05-16 — gain staging calibration (direct to iD14)
Signal path changed: guitar now routes direct into iD14 instrument input (Tone King Imperial Preamp bypassed pending its own calibration pass). iD14 gain set to **0**. Guitar bus changed to **Mono** (was Stereo). Dream '65 plugin I/O trims set: **Input −8.0 dB / Output +10.0 dB** (the Deluxe Reverb model drops significant level; the +10 output trim compensates). LA-2A adjusted: **Peak Reduction 32 / Gain 25**.

### 2026-05-08 — tested
Verified in DAW session. Key findings: The Deluxe Reverb is extremely sensitive; **Volume 2.5** is necessary for clean headroom. The preset leans bright/twangy; roll back guitar tone to 6 for jazz. **LA-2A at Peak Reduction 40 / Gain 20** yields minimal reduction but prevents "noise floor fizz" on decay. **Hitsville Decay 2.0** confirmed. End-to-end: ~ -19.8dB in / -13.3dB out. Status updated to `tested`.

### 2026-05-08 — initial
Built as a deliberate comparison to Jazz Clean — Intimate Les Paul (Showtime '64). Signal chain parallels the Jazz Clean Intimate with matched Tone King settings and Hitsville chamber, so the only variable is the amp. Stock mod and Normal channel chosen to minimize imposed character while still testing what the Blackface voice does to the LP neck in a jazz context. Spring reverb at Reverb 2 — light enough to be a hint rather than a feature. No optional TONEX stomp; keep this clean for the comparison to mean something.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
