---
id: "lion-68-jumped-plexi-crunch-p90"
created: "2026-05-26"
updated: "2026-05-26"
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
target: "Plexi jumped-channel vintage crunch optimized for P-90 growl — Zeppelin, Who, and classic British rock bite; tighter and throatier than humbuckers."
tags: "plexi, british, crunch, classic-rock, framus, p-90, zeppelin, lion-68, marshall"
tone-king-channel: lead
amp: "Lion '68"
status: initial
pickup_type: "p-90"
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 2.5
    Treble: 5
    Middle: 5.5
    Bass: 4.5
    Presence: 4.5
  logic_compressor:
    threshold: 3
    ratio: 1
    attack: 4
    release: 7
    makeup_gain: 3
---

# Lion '68 — Jumped Plexi Crunch (P-90 Variant)

## Target Sound

The UADx Lion '68 is a meticulous model of the Marshall Super Lead Plexi 1959 100-watt head. With no master volume, a Plexi gets all its magic by being pushed. P-90s through a Plexi is one of the most iconic classic rock combinations in history—think Pete Townshend's live Who recordings or Leslie West's Mountain tones. P-90s provide a tighter, punchier, and far more vocal crunch than muddy humbuckers, and the swamp ash body adds a signature bite that slices through any mix.

We utilize **channel jumping** (patching the two channel inputs together) to blend the bite of the Instrument channel with the body of the Mic channel. 

To optimize this for the Framus Earl Slick Artist Series, we make three main adjustments:
1.  **Harmonic Pre-compression**: We run the physical Tone King Lead channel active at a low Volume (**2.5**) to add initial harmonic complexity and warm saturation before the signal hits the Plexi.
2.  **EQ Midrange Push**: We push the Plexi's midrange to **5.5** to capitalize on the DiMarzio P-90's focal "roar," while backing off Treble to **4.5** and Volume I to **6.0** to keep the roundwound strings from sounding fizzy.
3.  **Hum Suppression**: We raise the plugin's built-in noise gate threshold to **25.0** to tame single-coil P-90 hum under classic rock gain settings.

---

## Signal Chain

### 1. Tone King Imperial Preamp — Lead channel driver
*   **Status:** **ACTIVE**
*   **Purpose:** The Lead channel adds subtle analog preamp saturation that thickens the Plexi's response.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Lead** | 50s Tweed + British rock character; adds harmonic weight |
| Volume | 2.5 | Gentle preamp push; adds texture without overloading the Plexi input |
| Attenuation | 6.0 | Moderate-high output to drive the Plexi effectively |
| Bass | 4.5 | Slightly pulled back to keep the low end tight |
| Treble | 5.0 | Flat EQ baseline |
| Reverb / Tremolo | Off | Bypassed |
| IR | **Bypassed** | UAD Lion '68 handles the full cabinet simulation |

---

### 2. UADx Lion '68 Super Lead Amp — Plexi crunch

We manually select the **JUMP** input routing in the plugin. Volume I controls the "bite" and Volume II controls the "body."

| Control | Setting | Purpose |
|---------|---------|---------|
| Model | **Lead** | Classic Plexi voice |
| Volume I (Bite) | **6.0** | High-end drive; slightly rolled back to keep P-90 snap crisp and not fizzy |
| Volume II (Body)| **6.2** | Low-mid body and warmth; provides the classic Plexi punch |
| Treble | **4.5** | Slightly pulled back to smooth out the DiMarzio bridge P-90's high end |
| Middle | **5.5** | Pushed to capture the P-90's vocal throatiness and roaring mids |
| Bass | 4.0 | Rolled back to prevent low-end mud in the swamp ash body |
| Presence | 4.5 | Softens the extreme high-frequency cap |
| Ghost Notes | **ON** | Authentically models even-order power tube harmonic saturation |
| Bright Cap | **OFF** | Essential to prevent roundwound strings from sounding glassy |
| Input Routing| **JUMP** | **CRITICAL:** Activates jumped-channel interaction |
| Room | **0%** | Bypassed; prevents room stacking with post-FX reverb |
| Noise Gate | **25.0** | **CRITICAL:** High-quality gate engaged to block idle P-90 single-coil hum |
| Input Trim | −8.0 dB | Calibrated input pad for direct JFET/preamp gain staging |
| Output Trim | +10.0 dB | Makeup gain to restore −12 dBFS output targets |

---

### 3. UADx 1176 Rev A (Bluestripe) — classic FET compressor
Placed inline to catch transient peaks and glue the Plexi crunch. The Bluestripe adds a signature harmonic saturation and character.

| Control | Setting | Purpose |
|---------|---------|---------|
| Input | −45 dB | Signal level hitting the gain-reduction circuit |
| Output | −12.0 dB | Makeup gain |
| Attack | 4 | Medium-fast attack; lets the swamp ash pick attack pop before compressing |
| Release | 7 | Fast release; maintains maximum punch |
| Ratio | **4:1** | Moderate rock compression |

---

### 4. Logic Space Designer — plate reverb
Placed on the channel insert to blend into the crunch.

| Control | Setting | Purpose |
|---------|---------|---------|
| IR | 1.3s_Soft_Plate | Classic bright, metallic plate decay that complements Plexi grit |
| Pre-Delay | 8 ms | Natural separation |
| Length | 535 ms | Shortened decay to provide depth without muddying the rhythm |
| Dry / Wet | 0.0 dB / −24 dB | Subtle ambient blend |

---

## Optional TONEX Stomp (pre-Tone King)
Place as the first insert on the Logic channel.

| Capture | Character | Why it works here |
|---------|-----------|-------------------|
| **Wampler Plexi Drive** | Tweed-voiced crunch booster | Pushes the Lion '68 into heavier classic rock overdrive without changing the Plexi's fundamental voicing. |
| **Hudson Broadcast** | Treble booster / Germanium drive | Adds a biting, fuzz-like edge and endless sustain. The classic British combination (Rangemaster → Plexi). Turn the Lion's Bright Cap ON if using this. |

---

## Starting Point Guide

- **Pickup Selector Selection**: Set the Framus to the **Bridge P-90** for aggressive, biting rock rhythm (Who / Zeppelin style). For a rounder, singing woman-tone lead, switch to the **Neck P-90** and roll the guitar's physical tone knob back to **6**.
- **Adjusting the Gain**: Volume I is where the gain and high-end bite live. If you want a cleaner "Wind Cries Mary" tone, roll Volume I and Volume II down to **4.5**. If you want a saturated, heavy lead tone, push both Volumes up to **7.0**.
- **Bigsby Expressiveness**: The Bigsby B500 on your Framus is perfect for this tone! Play a sustained power chord, let the 1176 and Plexi compress and sustain the notes, and use the Bigsby for a slow, expressive vibrato.

---

## Feedback History

### 2026-05-26 — initial
Ported from humbucker Les Paul variant. Keeps Tone King active on the Lead channel at Vol 2.5 to provide initial harmonic richness. Adjusts Lion '68 settings: Volume I down to 6.0 and Treble down to 4.5 to smooth out roundwound brightness, pushes Middle to 5.5 to capture vocal P-90 mids, and raises the noise gate to 25.0 to suppress single-coil hum under gain.
