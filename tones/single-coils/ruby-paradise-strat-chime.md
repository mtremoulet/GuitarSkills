---
id: "ruby-paradise-strat-chime"
preset_name: Ruby Strat Chime Paradise
created: "2026-05-20"
updated: "2026-05-20"
guitar: "Squier Stratocaster (bridge + middle pickup position — \\"quack\\")"
target: "Classic VOX AC30 Top Boost chime, shimmer, and modulated delay; optimized for the bright clarity of Squier Stratocaster single-coils, using Paradise Guitar Studio and bypassing the Tone King preamp."
tags: "vox, ac30, ruby-63, strat, single-coil, chime, echo, paradise-studio, jangle, rock, post-punk"
tone-king-channel: bypassed
amp: "Ruby '63"
status: initial
pickup_type: "single-coil"
preset_overrides: 
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 4.5
    Treble: 6.5
    Bass: 5
    Tone Cut: 5.5
    Cut: true
  logic_compressor:
    ratio: 4
    attack: 63
    release: 4
    makeup_gain: -18
---

# Ruby '63 — Stratocaster Chime & Echo (Paradise Guitar Studio)

## Target Sound

The pairing of a **Squier Stratocaster** (specifically in its bridge + middle position 4 "quack" setting) with a **Vox AC30 Top Boost** (emulated here by the Ruby '63 engine within UADx Paradise Guitar Studio) is one of the most celebrated sounds in rock history. It is the defining voice of the British Invasion (The Shadows' Hank Marvin), the rhythmic delay architectures of U2's The Edge, the indie-rock counterpoint of The Smiths' Johnny Marr, the bell-like arpeggios of Radiohead, and the raw, expressive neck-pickup grooves of John Frusciante.

This toneprint is anchored on Squier Stratocaster single-coils. These pickups capture extremely fast, sharp transient attacks with an abundance of top-end "glass." When plugged straight into your interface — bypassing the Tone King preamp entirely — the raw single-coil signal goes directly into the **Paradise Guitar Studio** plugin. Within Paradise, the Ruby '63 engine's Class A cathode-biased power section compresses these fast plucks musically, softening the harsh spikes and converting them into a round, percussive "pop" with a rich harmonic bloom.

By using the all-in-one environment of **Paradise Guitar Studio**, we build a highly cohesive signal chain. The onboard studio effects (like the 1176 compressor, vintage tape delay, and plate reverb) live inside the plugin, providing maximum convenience and a beautifully unified space.

---

## Signal Chain

```
[Squier Stratocaster] → [Audient iD14 (JFET DI)] → [Paradise Guitar Studio (1176 → Ruby '63 → Tape Delay → Plate Reverb)]
```

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

Plugging your Strat straight into the high-headroom JFET DI input preserves the fast, glassy transient response of your single-coils, allowing them to interact dynamically and directly with the AC30's EL84 virtual tube model.

| Component / Control | Setting | Purpose |
|---------------------|---------|---------|
| **Guitar Input** | JFET Instrument Input (DI) | Discretely voiced JFET stage adds subtle harmonic warmth, acting like a classic tube DI front-end |
| **Preamp Gain** | Set to target peaks around −18 dBFS | Bypasses Tone King coloring. Provides the pure, uncolored, dynamic output of the single-coils to the DAW |
| **Tone King Imperial** | **Bypassed** | Bypassed entirely — preserves the raw, crystalline Strat treble and midrange, letting the single-coils drive the AC30 model directly |

---

### 2. UADx Paradise Guitar Studio — All-In-One Signal Path

Within Paradise Guitar Studio, we activate four core components: the 1176 compressor, the Ruby '63 Brilliant channel amp, a tape delay, and a vintage plate reverb.

#### A. Pre-FX Pedal Menu (Optional Boosts)
*Both pedals are **OFF** by default. Engage them only when you want to add gain or mid-range thickness.*

*   **TS Overdrive (Onboard)**: OFF (Drive: 2.0, Level: 6.0, Tone: 5.0) — *Engage for classic mid-boost crunch.*
*   **Nashville OD (Onboard)**: OFF (Drive: 2.5, Level: 5.5, Tone: 5.5) — *Engage for a warmer, transparent tube-like boost.*

#### B. Amp: Ruby '63 (Brilliant Channel) — Chime & Compression
The heart of the toneprint, leveraging the Top Boost Brilliant channel.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **BRILLIANT** | Engages the Top Boost preamp circuit, providing the essential Vox chime |
| Volume | **4.5** | **Vol 4.5**: Clean-chime sweet spot. Retains single-coil clarity while providing natural, touch-sensitive compression. Digging in hard creates a satisfying, harmonically rich bloom. |
| Cut Switch | **ON** | Low-frequency cut. **CRITICAL for single-coils** — filters out sub-bass flub to keep arpeggios tight and articulate. |
| Top Boost Treble | **6.5** | Boosts high-mid definition, helping the Strat's glassy character cut through without becoming harsh. |
| Top Boost Bass | **5.0** | Neutral — provides the low-mid weight that balances the bright treble boost. |
| Tone Cut | **5.5** | **Counterintuitive control — higher = fewer highs.** Set to 5.5 to smooth out digital "fizz" while leaving the rich, chimey high-mids fully intact. |

#### C. Cabinet & Room
The classic Vox speaker combination.

| Component | Setting | Purpose |
|-----------|---------|---------|
| **Cabinet** | AC30 2x12 Celestion Alnico Blue | The classic Vox combination; captures maximum chime and midrange focus. |
| **Mics** | Ribbon 121 (On-Axis) + Condenser 414 (Off-Axis) | The Ribbon 121 adds woody body and rounds off high-end transients; the Condenser 414 captures the airy top-end shimmer. |
| **Room Mix** | 15% (Studio A) | Small, controlled space to give the amp a realistic, three-dimensional depth in your headphones. |

#### D. Post-FX Studio Menu (Onboard Paradise Studio Effects)
We use the onboard studio compressor, delay, and reverb inside the plugin for a self-contained, low-latency chain.

| Effect / Control | Setting | Purpose |
|------------------|---------|---------|
| **1176 Compressor** | **ON** (Ratio 4:1, Input: 30, Output: 18, Attack: 3, Release: 5) | Placed post-amp to act as vintage studio "glue." Attack is set medium-slow to let the Strat's transient "snap" through before compressing; release is fast for natural decay. |
| **Tape Delay** | **OFF** (Time: 350ms, Feedback: 3.5, Mix: 20%, Wow/Flutter: 4.0) | A classic Echoplex-style delay. Turn **ON** for U2-style dotted-eighth rhythmic textures or Hank Marvin instrumental echo. |
| **Plate Reverb** | **ON** (Decay: 2.0s, Pre-delay: 20ms, Mix: 15%) | Rich, vintage plate reverb that adds room depth and a lush harmonic wash behind the notes without smearing the dry signal. |

---

## Starting Point Guide

*   **The "7/7" Baseline (Guitar Controls)**:
    *   Set your Stratocaster's physical **Guitar Volume to 7** and **Tone to 7**.
    *   **Why**: This rolls off the raw, high-output single-coil edge, expanding the clean headroom of the Ruby engine and bringing out a sweet, woody quality. Roll the guitar volume up to 10 only when you want to push the amp into full, singing lead overdrive.
*   **Pickup Position Sweet Spots**:
    *   **Position 4 (Neck + Middle)**: The "Gold Standard" clean tone. It naturally scoops the mids and rolls off sub-bass, producing a pristine, glassy, acoustic-adjacent chime. Ideal for fingerstyle playing (think John Frusciante's *"Under the Bridge"* or Mark Knopfler's fingerstyle snaps).
    *   **Position 2 (Bridge + Middle)**: The ultimate jangle and "quack" setting. Combines the bright bite of the bridge with the hollow woodiness of the middle pickup. Perfect for Johnny Marr's syncopated Smiths lines or Tom Petty rhythm beds.
    *   **Position 5 (Neck)**: Warm, woody, and highly expressive. Ideal for singing blues lines (Rory Gallagher style) and atmospheric Radiohead arpeggios (*"Street Spirit"*).
*   **Tone Cut Tuning**:
    *   Remember that the **Tone Cut control is counterintuitive** (higher setting = fewer highs). If your Strat feels too bright or "spiky" in your Sennheiser HD660S2 headphones, turn the Tone Cut *clockwise* (up to 6.5 or 7.0) to tame the transients rather than adjusting the Treble knob.

---

## Feedback History

### 2026-05-20 — initial
Created specifically for the Squier Stratocaster (single-coils) paired with the Ruby '63 engine inside Paradise Guitar Studio. Bypassed the Tone King preamp entirely, plugging straight into the Audient iD14's JFET DI to allow the raw Strat single-coils to drive the EL84 virtual power section directly. Selected the AC30 2x12 Celestion Blue cabinet mic'd with a Ribbon 121 and Condenser 414. Configured the onboard Pre-FX and Post-FX menus within Paradise, utilizing the 1176 compressor for post-amp studio glue, a plate reverb for depth, and an optional vintage tape delay for iconic echo rhythms.
