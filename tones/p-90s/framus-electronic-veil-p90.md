---
id: framus-electronic-veil-p90
created: 2026-05-26
updated: 2026-05-26
guitar: Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)
target: "Ed Bickert \"Electronic Veil\" — Adapted for hot P-90s and roundwound strings: extremely dark, warm, and syrupy, emulating a traditional hollowbody jazz box."
tags: jazz, framus, p-90, dark, warm, bickert, veil
tone-king-channel: rhythm
amp: Showtime '64
status: initial
pickup_type: p-90
---

# The Electronic Veil (P-90/Framus Variant)

## Target Sound

The goal of this toneprint is the quintessential "dark jazz" sound pioneered by Ed Bickert, adapted specifically to the **Framus Earl Slick Artist Series**. Translating a dark jazz tone designed for a flatwound-strung Telecaster to a swamp ash solid-body with **D'Addario XS roundwounds** and hot **DiMarzio P-90s** requires a multi-stage damping strategy. 

We combat the brightness and snappy transients of the swamp ash and roundwound strings using a four-fold approach:
1.  **Guitar Controls**: The physical guitar volume and tone knobs are treated as active components of the signal chain, rolled back to **6** and **2–3** respectively to dark the signal at the source.
2.  **Tone King Preamp (Hardware Buffer)**: We engage the physical Tone King Rhythm channel, using its volume and EQ to act as a warm analog tube buffer that rolls off high frequencies before the DAW.
3.  **Low-Pass Filtering**: We use a steep Logic High-Cut filter set to **3.8 kHz** to strip away the roundwounds' metallic "fizz."
4.  **Saturated Compression**: We push the LA-2A Gray compressor to **Peak Reduction 36** to create a highly compressed, "syrupy" optical sustain that rounds off pick transients.

The result is an incredibly intimate, thick, and woody jazz-box tone with the singing, vocal mid-range sustain of a P-90.

---

## Signal Chain

**Routing**: Logic Pro mono input only.

```
[Guitar (Vol 6/Tone 2)] → [Tone King Preamp (Treble 2)] → [iD14 Input 1] → [Showtime '64] → [Logic EQ (3.8kHz High-Cut)] → [LA-2A Gray (PR 36)] → [Hitsville Reverb (Bus 2)]
```

---

### 1. Tone King Imperial Preamp — physical front-end & tube buffer
*   **Status:** **ACTIVE**
*   **Purpose:** Acts as a warm analog tube driver and high-frequency filter before the audio interface.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Rhythm** | Clean Blackface foundation; provides a warm tube buffer |
| Volume | 2.5 | Transparency zone; keeps the hot P-90 neck pickup clean |
| Attenuation | 5.0 | Unity/moderate output |
| Bass | 5.0 | Flat EQ baseline |
| Treble | **2.0** | **CRITICAL:** Strong physical treble rolloff; darkens the signal before the DAW |
| Reverb | Off | Space handled by Hitsville Reverb |
| Tremolo | Off | Bypassed |
| IR | **Bypassed** | UAD Showtime '64 handles the cabinet simulation |

---

### 2. UADx Showtime '64 Tube Amp — clean platform
Chosen for its high headroom and neutral, non-scooped midrange character, which allows the woody P-90 neck pickup resonance to stand out.

| Control | Setting | Purpose |
|---------|---------|---------|
| In | HI-Z | |
| Bright / Normal | **Normal** | Removes the bright cap; essential to strip away roundwound brightness |
| Volume | 3.0 | Pristine clean headroom |
| Treble | **2.5** | Rolled back further to soften the top-end snap of the maple neck |
| Middle | **5.5** | Pushed slightly to highlight the woody, vocal midrange of the P-90 |
| Bass | 4.0 | Controlled; avoids low-mid boominess in the swamp ash body |
| Vibrato | Off | Bypassed |
| Room | Off | Reverb handled by Hitsville chambers |
| Mic | **Ribbon 160** | Warm, dark ribbon mic with natural high-frequency roll-off |
| Input Trim | 0 dB | Neutral |
| Output Trim | +12 dB | Compensates for the padded input path |

---

### 3. Logic Channel EQ — surgical shaping & "The Veil"

| Band | Frequency | Gain | Slope / Q | Purpose |
|------|-----------|------|-----------|---------|
| **High-cut** | **3.8 kHz** | **24 dB/oct** | — | **The "Veil"** — steep filter that strips away all roundwound string "fizz" and digital air |
| **Peak** | **250 Hz** | **+2.5 dB** | **Q: 0.8** | **Woody Resonance** — broad boost to simulate a hollowbody's acoustic chest resonance |

---

### 4. UADx LA-2A Gray Compressor — syrupy optical glue
We use the LA-2A Gray (which has a slightly faster recovery curve) but push the peak reduction to clamp down on transients and elongate the note decay.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | **36** | Pushed to achieve ~4-5 dB of reduction on firm picks; rounds off pick attack |
| Gain | 26 | Makeup gain |
| Mode | **Compress** | Gentle 3:1 optical ratio; creates a "syrupy," flowing sustain |

---

### 5. UADx Hitsville Reverb Chambers — intimate space
Placed on **Bus 2** (Reverb bus). Channel send: **−20 dB**, Aux Bus Fader: **−8 dB**.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | 2644 | Warm, intimate, and smooth chamber reflections |
| Mix | **Wet Solo (ON)** | Correct for a send/bus setup (outputs wet signal only) |
| Decay | **9:00** | Short decay; provides a sense of room air without wash |
| All other controls | Default | Bypassed/neutral |

---

## Starting Point Guide

- **The Physical Knobs (Crucial)**: This tone print is entirely dependent on your guitar's controls. Set the Framus pickup selector to the **Neck P-90**. Start with your **Guitar Volume at 6** and **Guitar Tone at 2**. If the tone feels too dark or "muffled," raise the Tone knob to **3**. If it feels too bright or single-coil-like, roll the Tone knob back to **1.5**.
- **Adjusting the "Syrup"**: The **Peak Reduction** on the LA-2A Gray controls the envelope of your pick attack. If you want a more traditional, dynamic jazz response, lower it to **30**. If you want a thick, vocal, horn-like legato sustain, raise it to **40**.
- **Managing Mids**: If the neck P-90 midrange feels too congested in the low-mids, lower the **250 Hz** peak in the Logic Channel EQ to **+1.5 dB** or roll the Tone King's **Bass** control down to **4.5**.

---

## Feedback History

### 2026-05-26 — initial
Adapted for the Framus P-90 platform with roundwounds. Activates Tone King Rhythm channel as a warm analog hardware buffer (Volume 2.5, Treble 2.0). Lowers Showtime '64 Treble to 2.5, pushes Middle to 5.5. Pulls Logic High-Cut filter down to 3.8 kHz to veil roundwound string sizzle, and pushes LA-2A Gray Peak Reduction to 36 for a thicker, syrupy sustain. Recommends starting with physical guitar controls at Volume 6 / Tone 2.
