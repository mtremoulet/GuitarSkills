---
id: lion-68-jumped-plexi-crunch
created: 2026-05-08
updated: 2026-05-16
guitar: "Epiphone Les Paul Standard (humbuckers \u2014 bridge or neck-bridge blend)"
target: "The Plexi \"jumped channel\" sweet crunch \u2014 Zeppelin, Cream, and mid-period\
  \ Hendrix harmonic richness; warm compressed British rock, distinctly different\
  \ from the MRH810's 1980s precision gain"
tags: plexi, british, crunch, classic-rock, les-paul, humbucker, zeppelin, lion-68,
  marshall
tone-king-channel: lead
amp: Lion '68
status: tested
pickup_type: humbucker
---

# Lion '68 — Jumped Plexi Crunch

## Target Sound

The Lion '68 is a Marshall Super Lead Plexi 1959 100-watt amplifier — a 1968 non-master-volume design. This is a fundamentally different amp from the MRH810 (JCM800): where the JCM800 has a master volume and extra gain stages tuned for 1980s precision distortion, the Plexi has no master volume and gets all its character from cranking. At lower settings it's harmonically rich and surprisingly clean; at 6–7 it enters the compressed, singing crunch that defines Zeppelin, Cream, Hendrix's electric period, and early Stones.

The key technique is **channel jumping** — connecting both channel inputs together so both Volume controls are active simultaneously. This creates a richer, fuller tone than either channel alone: you get the bite and presence of one channel combined with the body and warmth of the other. Most classic Plexi recordings you know were made this way.

**Gain Staging & Room Note:** In testing, end-to-end levels were ~ `-23.3dB` input and ~ `-11.9dB` output. The plugin's built-in **Room** control should be set to `0%` to prevent "room stacking" with the external reverb. 

**This tone vs. MRH810 Classic Lead:** Use Lion '68 when you want warm, vintage-voiced crunch that responds to dynamics and cleans up with guitar volume roll-off. Use MRH810 when you need tighter, more aggressive 1980s gain — the MRH810 doesn't clean up as gracefully but has more gain and definition for modern rock lead work. They're complementary, not redundant.

---

## Signal Chain

### 1. Tone King Imperial Preamp — lead channel drive

Unlike the clean toneprints where the Tone King acts as a buffer, here the Lead channel provides useful front-end harmonic complexity before the Plexi. Vol 3 on the Lead channel adds subtle color that thickens the Plexi's response without pushing it into more gain.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Lead** | 50s Tweed + British rock character; adds body before the Plexi rather than acting as a neutral buffer |
| Volume | 3 | Gentle front-end push — not trying to distort the Tone King's preamp, just adding harmonic weight |
| Attenuation | 6 | Moderate-high output to drive the Plexi's input effectively |
| Bass | 5 | Flat |
| Treble | 5 | Flat |
| Reverb | Off | Space Designer handles reverb post-amp |
| IR | **Bypassed** | Lion '68 handles the full cab simulation |

---

### 2. UADx Lion '68 Super Lead Amp — Plexi crunch

The Lion '68 is a non-master-volume amp — the Volume knobs are where the character lives. Below 5, the amp is clean but rich. At 6–7, the crunch sweet spot appears.

**Channel jumping:** Set both Vol I and Vol II above 0 simultaneously. This activates the jumped configuration — the two channels interact to create a tone fuller than either alone. In the original hardware, you achieve this with a patch cable between the channels; the plugin implements it by running both volumes together.

| Control | Setting | Purpose |
|---------|---------|---------|
| Model | **Lead** | Classic Plexi voice |
| Volume I | 6.5 | The "bite" channel |
| Volume II | 6.5 | The "body" channel |
| Treble | 5 | Neutral |
| Middle | 5 | Neutral |
| Bass | 4 | Slightly pulled back |
| Presence | 5 | Neutral |
| Ghost Notes | **ON** | Even-order harmonics |
| Bright Cap | **OFF** | Tame glassy highs |
| Input Routing| **JUMP** | **CRITICAL:** Manually select JUMP in the plugin dropdown |
| Room | **0%** | Mute the built-in room sound |
| Noise Gate | **20.0** | Threshold to kill the idle Plexi hum |
| Input Trim | −8.0 dB | Plugin-level pad; calibrated 2026-05-16 for direct-to-iD14 path |
| Output Trim | +10.0 dB | Makeup gain to restore −12 dBFS after amp model |

---

### 3. UADx 1176 Rev A (Bluestripe) — FET character compression

The 1176 Rev A (Bluestripe) has a slower attack range and more harmonic color than the Rev E. 

*UI markings on this compressor are attenuation based: ∞ down to 0.*

| Control | Setting | Purpose |
|---------|---------|---------|
| Input | −48 dB | How hard the signal hits the compressor (scale: −∞ to 0 dB); pulled back from −38 dB to reduce compression drive |
| Output | −12.75 dB | Output level (scale: −∞ to 0 dB); raised from −16 dB as makeup gain |
| Attack | 4 | Medium-fast |
| Release | 7 | Fast release |
| Ratio | **4:1** | Moderate compression |

---

### 4. Logic Space Designer — room and reverb

| Control | Setting | Purpose |
|---------|---------|---------|
| IR | 1.3s_Soft_Plate | Bright, metallic decay that complements British crunch |
| Pre-Delay | 8 ms | Separation from attack |
| Size | 74% | Medium-large space |
| Length | 535ms | Shortened to provide depth without mud |
| Dry | 0.0 dB | Unity |
| Wet | −24 dB | Reduced during 2026-05-16 calibration — less wash needed without TKIP in chain |

---

## Optional TONEX Stomp (pre-Tone King)

Both options push the Plexi into more crunch or a different tonal character. Place *before* the Tone King — either TONEX ONE hardware, or TONEX plugin as the first insert on the Logic channel.

| Capture | Character | Why it works here |
|---------|-----------|-------------------|
| **Wampler Plexi Drive** (~42 captures) | Voiced specifically for Plexi amp response — adds crunch and harmonic bloom without changing the amp's fundamental character | Pushes the Lion '68 further into sweet crunch without the mid-hump of a tubescreamer; specifically designed for this interaction |
| **Hudson Broadcast** (~5 captures) | Rangemaster-style treble booster — adds presence and sustain with a bright, harmonic quality | The classic British combination: Rangemaster → Plexi is Brian May, Tony Iommi, Rory Gallagher. More focused than a tubescreamer. Pairs best with the Bright Cap ON if using this capture. |

*Default: stomp bypassed. The jumped Plexi with the 1176 already has significant character — engage the stomp when you want a more driven, less dynamic sound.*

---

## Starting Point Guide

- **Volume knob sweep:** Start both Vol I and Vol II at 5 (clean-but-rich territory), then sweep up to 7 to find where the crunch sweet spot sounds best for the guitar you're using. The 490R humbuckers will find sweet crunch earlier than single coils.
- **Ghost Notes test:** Play a sustained chord with Ghost Notes ON, then bypass it. The difference is subtle on dry notes but becomes the "alive" quality you associate with Plexi recordings. If it sounds too much, pull Volume back slightly — the effect becomes more pronounced at higher volumes.
- **vs. MRH810 Classic Lead:** Play the same phrase on both. The Lion will feel warmer, more "vintage," and will clean up more gracefully with guitar volume rolloff. The MRH810 will feel tighter, more aggressive, and more modern. Both are valid — they're different tools for different tracks.
- **Brown voice exploration:** If you want EVH character (Van Halen, "Eruption"-era), switch to Brown voice — this is the Variac-modified Plexi character. Very different territory; note in Feedback History.

---

## Feedback History

### 2026-05-16 — gain staging calibration (direct to iD14)
Signal path changed: guitar now routes direct into iD14 instrument input (Tone King Imperial Preamp bypassed pending its own calibration pass). iD14 gain set to **0**. Guitar bus changed to **Mono** (was Stereo). Lion '68 plugin I/O trims set: **Input −8.0 dB / Output +10.0 dB**. 1176 Rev A hardware knobs recalibrated: **Input −48 dB / Output −12.75 dB** (scale is −∞ to 0 dB; less negative Input = more compression drive; less negative Output = louder). Space Designer **Wet reduced to −24 dB** (from −18 dB).

### 2026-05-08 — tested
Verified in DAW session. Key findings: **JUMP** input routing is mandatory. **1176 at Input −38 dB / Output −16 dB** achieves the target 3dB reduction. **Room knob at 0%** prevents ambient clash. **Space Designer at 535ms Soft Plate** confirmed for vintage crunch. **Noise Gate at 20.0** necessary for Plexi hum. End-to-end: ~ -23.3dB in / -11.9dB out. Status updated to `tested`.

### 2026-05-08 — initial
Built to fill the Plexi gap in the toneprint library. Lion '68 chosen for its three Plexi variants (Lead/Bass/Brown), Ghost Notes switch, and authentic non-master-volume response. Jumped-channel configuration specified as the primary setup. 1176 Rev A (Bluestripe) chosen for its slower attack range and harmonic color, which complements rather than tames the Plexi character. Tone King Lead channel at Vol 3 specified for front-end harmonic complexity rather than the neutral buffer role it plays in jazz toneprints. TONEX Wampler Plexi Drive and Hudson Broadcast listed as optional boosts.
