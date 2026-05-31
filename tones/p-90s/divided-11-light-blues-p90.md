---
id: "divided-11-light-blues-p90"
created: "2026-05-26"
updated: "2026-05-26"
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
target: "Light, dynamic blues tone through the Divided 11 — optimized for hot P-90s: clean when backing off, Class A tweed growl when digging in."
tags: "blues, dynamic, clean, grit, slapback, class-a, divided-11, framus, p-90"
tone-king-channel: rhythm
amp: "Divided 11, Tone King Imperial Preamp"
status: initial
pickup_type: "p-90"
preset_data:
  la2a:
    peak_reduction: 18
    gain: 42
---

# Divided 11 Light Blues (P-90 Variant)

## Target Sound

The Divided 11 (Divided by 13 CJ11) is a boutique, tube-rectified Class A 11-watt amplifier with Tweed Fender DNA. Class A circuits are extremely touch-sensitive and dynamic; they reward picking hand dynamics with a smooth, gradual transition into compression and grit rather than a sudden clipping threshold.

Because the DiMarzio P-90s in your Framus are much hotter and thicker than traditional single-coils, they will push this amp into early overdrive. To preserve the "clean-to-grit" transition where light fingerstyle stays clear but digging in barks, we make three essential adjustments:
1.  **Hardware Pad**: We engage the **LOW input switch** on the Divided 11. This acts as a pad, keeping the virtual preamp from being overwhelmed by the hot P-90s.
2.  **Gain sweet spot**: We back the Volume knob down slightly to **4.5** (from 5.0) to give your picking hand more dynamic range.
3.  **Treble Calibration**: We lower the Treble control slightly to **5.5** (from 6.0) to balance the swamp ash body's snappy transients.

We pair this edge-of-breakup platform with a warm, subtle **Galaxy Tape Echo slapback** (~85ms) and a shared **Space Designer reverb** bus for a luxurious, breathing blues tone.

---

## Signal Chain

### 1. Tone King Imperial Preamp — transparent buffer front-end
*   **Status:** **ACTIVE**
*   **Purpose:** Acting as a high-quality hardware signal buffer driving the audio interface cleanly.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Cleanest available Tone King voicing |
| Volume | 2.0 | Kept very low to prevent any preamp coloration |
| Attenuation | 5.0 | Moderate output |
| Bass | 5.0 | Flat EQ |
| Treble | 5.0 | Flat EQ |
| Reverb / Tremolo | Off | Bypassed |
| IR | **Bypassed** | Divided 11 handles the full amp + cab simulation |

---

### 2. Guitar Track → Nembrini Divided 11 Amp & Cab

| Control | Setting | Purpose |
|---------|---------|---------|
| Power | On | — |
| Input | **LOW Switch** | **CRITICAL:** Pads the hot DiMarzio P-90s to preserve preamp headroom |
| Volume | **4.5** | Preamp gain sweet spot; clean on a light touch, growls when you dig in |
| Treble | **5.5** | Slightly above noon for note definition, but smoothed to prevent swamp ash harshness |
| Bass | **4.5** | Kept tight; prevents the swamp ash body from causing low-end boominess |
| Master | 5.0 | Moderate output |
| Boost | **OFF** | Keeps the gain structure organic and dynamic |
| Noise Gate | Active | Adjust threshold to kill idle single-coil hum without clipping note decay |

**Cabinet Section**

*   **Cabinet**: **THIRTEEN 1x12 GREEN** (Divided By 13 1x12 combo with Celestion G12M) — the reference cab, providing woodiness and classic midrange chime.
*   **Microphone 1 (Off-axis)**: **Ribbon 121** (warmth, smooth high-frequency roll-off), positioned at 50% (centered-ish on the speaker cone) with Distance at 40% (avoids low-end mud).
*   **Microphone 2 (On-axis)**: **Dynamic 57** at **−8 dB** (noon-panned; provides a touch of attack definition and swamp ash snap without dominating the ribbon mic's warmth).
*   **Filters**:
    *   Rumbling: **ON** (cuts sub-bass mud, keeping the Class A bloom tight and focused).
    *   Tight / Harsh: **OFF**.

---

### 3. UADx LA-2A Tube Compressor — light peak-leveling

**CRITICAL NOTE:** We keep the compressor's Peak Reduction extremely low. The Divided 11's dynamic response is the entire point of this toneprint — over-compressing will squash the clean-to-grit pick transition.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Compress | Gentle 3:1 optical ratio |
| Peak Reduction | **18** | Very light leveling (~1–2 dB of reduction on hard picks only) |
| Gain | 42 | Makeup gain |
| Meter | Gain Reduction | Watch for very subtle movement on hard strums |

---

### 4. UADx Galaxy Tape Echo — subtle slapback
Placed directly on the channel insert to glue the tape echo to the amp sound.

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 1 | Single head for classic slapback |
| Echo Rate | 6.5 | **Clockwise = Shorter.** ~85ms on Head 1 for slapback space |
| Feedback | 1.5 | Fades away after a single ghost repeat |
| Echo Volume | **3.0** | Kept subtle; acts as a room shadow behind the dry note |
| Treble | 4.0 | Rolled back to keep repeats warmer than the dry note |
| Bass | 5.0 | Flat EQ |
| Tape Age | Used | Light wow/flutter for organic feel |
| Wet Solo | OFF | Insert configuration |
| Reverb Volume | 0.0 | Bypassed; reverb is on the bus |

---

### 5. Send from Guitar Track → Bus 3 (Reverb): −18 dB

---

### 6. Reverb Aux — Space Designer (small studio room)
Add an Aux channel strip with Input = Bus 3. On this Aux, add Space Designer.

| Control | Setting | Purpose |
|---------|---------|---------|
| IR | Rooms folder — small-medium studio room | Provides a natural acoustic space around the slapback |
| Predelay | 8 ms | Natural separation |
| Size | 75% | Small room reflections |
| Lo/Hi Spread | 70% / 75% | Stereo width |
| Dry / Wet | −inf dB / 0 dB | Wet only on Aux |

**Aux Fader: −14 dB** (subtle room blend)

---

## Starting Point Guide

- **Finding your dynamic sweet spot**: Set the Framus to the **Neck P-90**. Play a single-note melody using a very light fingerstyle or light pick stroke—it should sound clear and chiming. Now, dig in hard on a double-stop (two notes together). The amp should compress slightly and "hair up" with a beautiful, vocal growl.
- **Taming the "Spank"**: If the swamp ash body and roundwound strings make the pick attack feel too sharp or "clicky," roll the **Treble** control on the Divided 11 down to **5.0** (noon) or roll your physical **Guitar Tone knob** back to **8**.
- **Input Gain Interaction**: If you switch the Divided 11 to the **HIGH input switch**, you will get a much throatier, saturated tone. If you do this, lower the **Volume** control on the amp to **3.5** to keep it in the edge-of-breakup zone.

---

## Feedback History

### 2026-05-26 — initial
Ported from single-coil Tele variant. Keeps Tone King active as a clean buffer. Utilizes the Divided 11 LOW input switch to pad the hot DiMarzio P-90s, backs Volume down to 4.5 to expand dynamic range, and smooths Treble to 5.5 to balance swamp ash snap. Sets LA-2A Peak Reduction to 18 to protect the Class A dynamics.
