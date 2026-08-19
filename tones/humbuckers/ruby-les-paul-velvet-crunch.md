---
amp: "Ruby '63 (UADx)"
created: 2026-05-20
guitar: "Gibson Les Paul Studio (490R neck / 490T bridge humbuckers)"
id: ruby-les-paul-velvet-crunch
pickup_type: humbucker
preset_name: "Ruby LP Velvet Crunch HB"
status: archived
tags: "vox, ac30, ruby-63, les-paul, humbucker, edge-of-breakup, chime, velvet-crunch, classic-rock, indie-rock"
target: 'Warm, vocal Class A chime and creamy velvet crunch; a rich, touch-sensitive pairing of Les Paul humbuckers and Vox AC30 Top Boost.'
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
    Bass: 4.2
    Cut: true
    Tone Cut: 5.5
    Treble: 6.5
    Volume: 3.5
  la2a:
    gain: 40
    peak_reduction: 35
  logic_eq:
    band1:
      freq: 80
      on: true
      slope: 2
    band8:
      freq: 6500
      on: true
      slope: 2
---

# Ruby '63 — Les Paul Velvet Crunch & Chime

## Target Sound

While the Vox AC30 (emulated by the UADx Ruby '63) is legendary for single-coil "jangle" (think Rickenbackers and Strats in the British Invasion), pairing it with a dual-humbucker guitar like the **Gibson Les Paul Studio** unlocks a completely different, highly prestigious sonic profile: the **Class A Velvet Crunch**. 

Unlike high-headroom American Fender amps, the AC30 runs hot and compresses early. When fed the thick, high-output, mid-focused signal of Les Paul humbuckers, the amp does not clip harshly; instead, it yields a rich, singing, mid-forward crunch that is incredibly touch-sensitive. This is the sound of late-era Beatles grit (*"Revolution"*, *"Sgt. Pepper"*), the saturated orchestral voice of Queen (Brian May's custom humbucking setup), the chimey indie textures of Radiohead, and the warm, delay-driven arena anthems of U2.

The key to this tone is **balance**. The Les Paul's warm 490R neck pickup and warm-voiced 490T bridge pickup (both Alnico II — a matched pair) provide the woody weight and sustain, while the AC30's **BRILLIANT channel with Top Boost** provides the cutting high-mid chime and compression. This toneprint is dialed to prevent low-end mud while preserving the throatiness and vocal quality of your humbuckers.

> [!TIP]
> **The Midrange Decision — Plugging Straight In:**
> While the Tone King Imperial's Rhythm channel emulates a Fender Blackface (which features a classic, beautiful mid-scoop), running your Les Paul **directly into the Audient iD14's JFET DI input (bypassing the Tone King entirely)** is the preferred, purist approach here. 
> Bypassing the Tone King preserves the raw, rich, wood-flavored impedance and vocal midrange of the 490R/490T humbuckers, letting them interact dynamically and directly with the AC30's EL84 power tube model. If you want a glassier, single-coil-adjacent tone, you can always engage the Tone King's Blackface mid-scoop to pre-shape the signal; but for the ultimate "velvet crunch," plug straight into the interface and let those gorgeous humbucker mids sing!

> [!IMPORTANT]
> **Humbucker Gain Alert:** Humbuckers will push the Ruby '63 into overdrive *much* earlier than single-coils. The amp Volume must be carefully balanced (Vol 3.5 for clean-chime with natural compression; Vol 5.0 for velvety, singing overdrive).

---

## Signal Chain

```
[Les Paul Studio] → [Audient iD14 (JFET DI)] → [LA-2A Gray Comp] → [Ruby '63 Amp] → [AC30 Celestion Blue Cab] → [Post-EQ] → [Aux Spatial Buses]
```

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

To get the pure, dynamic midrange interaction of your Les Paul's humbuckers and the AC30, plug your guitar straight into the high-headroom **JFET Instrument Input (DI)** of the Audient iD14 mkII, bypassing the Tone King Imperial Preamp entirely.

| Component / Setting | Target Level / Option | Purpose |
|---------|---------|---------|
| **Guitar Input** | JFET Instrument Input (DI) | Discretely voiced JFET stage adds subtle harmonic warmth, acting like a classic tube DI front-end |
| **Preamp Gain** | Set to target peaks around −18 dBFS | Bypasses Tone King coloring. Provides the pure, uncolored, dynamic output of the humbuckers to the DAW |
| **Tone King Imperial** | **Bypassed** | Bypassed — preserves the natural humbucker midrange rather than pre-scooping it (which would happen on the Blackface-style Rhythm channel) |


### 2. UADx LA-2A Gray Compressor — dynamic smoothing

#### Amp Settings
Placed before the amp to tame humbucker transients and add singing sustain. The Gray variant has a slightly slower, smoother recovery response that is perfect for sustaining humbucker instruments.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Compress | Gentle 3:1 optical compression ratio |
| Peak Reduction | 35 | Target 2–3 dB of gain reduction on hard strums. Smooths out heavy humbucker attack peaks. |
| Gain | 40 | Makeup gain to restore unity level into the amp plugin |

---

#### Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 3. UADx Ruby '63 Top Boost Amp — chime & drive

The core character generator. We leverage the **BRILLIANT** channel to access the Top Boost EQ (Treble and Bass) and the amp's high-frequency cut controls.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **BRILLIANT** | Engages the Top Boost preamp circuit, providing the essential Vox chime |
| Volume | **3.5 to 5.0** | **Vol 3.5**: Clean-chime; warm, compressed, glassy. <br>**Vol 5.0**: Velvet crunch; rich, saturated overdrive that cleans up by rolling back the guitar volume. |
| Cut Switch | **ON** | Low-frequency cut. **CRITICAL for humbuckers** — filters out flubby bass before the preamp to prevent mud. |
| Top Boost Treble | 6.5 | Boosts high-mid definition, helping the Les Paul's thick voice cut through the mix |
| Top Boost Bass | 4.2 | Subtly rolled back to keep the low-end tight under high-output humbucker strumming |
| Tone Cut | **5.5** | **Counterintuitive control — higher = fewer highs.** Set to 5.5 to smooth out digital "fizz" while leaving the rich, chimey high-mids fully intact. |

**Cabinet & Speaker Selection:**
* **Cab**: AC30 2x12 Celestion Alnico Blue (the classic Vox combination; compresses beautifully in the mids).
* **Mics**: Blend of **Ribbon 121** (on-axis, provides warm, woody body) and **Condenser 414** (off-axis, captures airy top-end articulation).

---

### 4. Post-FX surgical EQ (Logic Channel EQ)

A safety net to clean up room frequencies and polish the high-end.

* **High-Pass Filter**: 80 Hz (12 dB/octave) to remove unnecessary low-end rumble.
* **Low-Pass Filter**: 6.5 kHz (smooth 12 dB/octave slope) to act as a gentle "electronic veil," smoothing out top-end transients and creating a cohesive, organic texture.

---

### 5. Spatial Effects — Bus-First Aux Routing

To maintain maximum clarity and prevent the Les Paul's thick midrange from getting "smeared" or muddy, all spatial effects are run on parallel buses.

#### Bus 3 (Reverb): Logic ChromaVerb (100% Wet)
* **Room Type**: Chamber or Retro Space (adds a lush, reflective, vintage room character).
* **Decay Time**: 1.4 seconds.
* **Logic Send Level**: `-14 dB` (adjust to taste for depth).

#### Bus 4 (Delay): UADx Galaxy Tape Echo (100% Wet)
* **Head Select**: 1 (focused single repeat).
* **Echo Rate**: 5 (~220ms; a subtle slap/room delay).
* **Feedback**: 2.5 (3 to 4 quiet, warm tape repeats).
* **Tape Age**: Used (adds gentle wow/flutter and high-end roll-off to the repeats).
* **Logic Send Level**: `-18 dB` (sits quietly in the background as an ambient pillow).

---

## Guitar Interaction & Playback Guide

* **The "7/7" Balance (Guitar Controls)**:
  * Set your Les Paul's physical **Guitar Volume to 7** and **Tone to 7**.
  * **Why**: This takes the high-output "edge" off the humbuckers, expanding the clean headroom of the Ruby and bringing out a glassy, woody quality. Turn the guitar volume up to 10 only when you want to push the amp into full, singing lead overdrive.
* **Pickup Sweet Spots**:
  * **Middle Position (Bridge + Neck)**: The ultimate clean tone. It naturally scoops the mids slightly and rolls off sub-bass, producing a pristine, glassy, acoustic-adjacent chime.
  * **Neck Position (490R)**: Thick, warm, vocal, and cello-like. Perfect for expressive blues lines and jazz-fusion phrasing.
  * **Bridge Position (490T)**: Warm and punchy with more mid-presence than the neck, but not aggressive — the Alnico II magnet keeps it smooth. Think late-Beatles chord crunch or Radiohead rhythm parts rather than biting hard-rock bridge tone.

---

## Feedback History

### 2026-05-20 — refined
Bypassed the Tone King Imperial Preamp to allow direct injection into the Audient iD14's JFET DI. Documented the rationale: while the Tone King's Blackface-style Rhythm channel provides a beautiful mid-scoop that can push the Les Paul closer to a single-coil glassiness, plugging straight in preserves the pure, dynamic, woody throatiness of the humbuckers interacting directly with the AC30's EL84 tube saturation, which is the soul of this velvet crunch sound.

### 2026-05-20 — initial
Created specifically to bridge the Gibson Les Paul Studio (dual humbuckers) into the UADx Ruby '63 (AC30 Top Boost) engine. Volume dialed back to 3.5 (clean) and 5.0 (crunch) to accommodate the high humbucker output. Cut switch engaged and Top Boost Bass set to 4.2 to prevent low-mid flubbiness. LA-2A Gray Compressor added to tame transients and increase sustain. Standardized on the 2x12 Celestion Blue cab blended with a Ribbon 121 and Condenser 414. Set up for parallel bus routing on Bus 3 (ChromaVerb) and Bus 4 (Galaxy Echo).
