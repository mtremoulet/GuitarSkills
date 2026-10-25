# Tone King Imperial Preamp — Hardware & Circuit Validation

## 1. Overview & Circuit Heritage

The **Tone King Imperial All-Tube Preamp** pedal is a high-voltage, analog tube preamp pedal modeled directly on Mark Bartel's flagship **Tone King Imperial MKII** combo amplifier.

Unlike typical starved-plate tube overdrive stompboxes running at 9V or 12V DC, the Imperial Preamp accepts a 9–12V DC input (minimum 9W) and uses an internal DC-to-DC charge-pump circuit to run its three **12AX7 vacuum tubes at authentic high plate voltage (~250V–300V DC)**.

Crucially, the analog audio circuit includes:
1. **Rhythm Preamp Section**: Pure 1960s American Blackface (Fender AB763 Deluxe Reverb / Twin Reverb).
2. **Lead Preamp Section**: 1950s American Tweed (Fender 5E3) through vintage British rock (Marshall Plexi) via Mark Bartel's proprietary **Mid-Bite** network.
3. **Phase Inverter (PI) Circuit**: Complete analog 12AX7 phase inverter stage, capturing the power-amp drive dynamics, asymmetrical clipping, and dynamic tube sag of the Imperial MKII before the attenuation network.
4. **Ironman II Attenuation Network**: Post-PI reactive attenuation simulation providing transparent master volume control.
5. **Shared Effects**: Analog-modeled convolution spring reverb (Level, Dwell) and digital bias-style tremolo (Depth, Speed), independently assignable per channel.
6. **Impulse Response Engine**: Studio-grade DSP cabinet simulation loaded with three Kevin Rowe (OwnHammer) multi-mic IRs.

---

## 2. The Rhythm Channel: Blackface Heritage & Gain Staging

### Voicing & Tone Stack Topology
- **Heritage**: 1960s Fender Blackface AB763 combo (Deluxe Reverb / Twin Reverb).
- **Controls**: **Volume, Attenuation, Bass, Treble**. (No Middle or Presence knobs).
- **Tone Stack Behavior**: The passive FMV circuit uses a fixed internal resistor (~6.8 kΩ) to ground, creating an inherent **midrange notch centered around ~500 Hz** (400 Hz–600 Hz).
  - *Scooped Glass & Sparkle*: Setting Bass and Treble higher (5.0–7.0 pips) deepens the relative 500 Hz scoop, emphasizing crystalline bell-tones, pick snap, and airy shimmer (ideal for funk rhythm, country, and yacht rock).
  - *Flattening the Curve for Warm Jazz / Neo-Soul*: Dialing Bass and Treble back (e.g., Treble at 2.0–3.0, Bass at 4.5–5.5) flattens the frequency curve, lifting the relative midrange and delivering a round, warm, woody jazz tone on neck humbuckers and P-90s.

### Volume (Gain) vs. Attenuation (Master)
- **Volume**: Preamp gain stage driving the 12AX7 input triodes.
- **Attenuation**: Post-phase-inverter attenuation (Ironman II technology).
- **Gain-Staging Modes**:
  - *High-Headroom Clean (Volume 1.0–3.0 | Attenuation 4.5–5.5)*: Keeps tubes in their linear operating zone for maximum headroom and instantaneous transient recovery.
  - *Edge-of-Breakup Bloom (Volume 3.5–5.0 | Attenuation 4.5–5.0)*: Soft-knee tube compression; soft picking stays clean, digging in produces rich second-order harmonic overtones.
  - *Pushed Blackface Growl (Volume 5.5–7.0+ | Attenuation 4.0–5.0)*: Saturates the preamp and phase inverter into raw, Texas-style blues grit while controlling track volume via attenuation.

---

## 3. The Lead Channel & The Mid-Bite Transformation

The Lead channel is controlled by **Volume, Attenuation, Tone (high-frequency contour), and Mid-Bite**.

### Sonic Spectrum Across Mid-Bite (1 to 9 Scale)

```
[Pip 1.0 – 3.0] ───────────────> [Pip 4.0 – 5.5] ───────────────> [Pip 6.0 – 9.0]
50s American Tweed (5E3)          Hot-Rod Tweed / Vocal Blues      Vintage British Rock / Marshall Plexi
Spongy, fat bass, soft highs     Firming low end, singing mids     Tight bass, rolled highs, 1.5–2.5 kHz peak
```

#### 1. Low Mid-Bite (1.0 to 3.0 Pips) — 1950s Tweed Deluxe (5E3)
- Warm, spongy, touch-sensitive feel with blooming low-end resonance and soft top-end roll-off.
- Authentic 5E3 dynamic sag; ideal for loose vintage blues, fingerstyle folk, and warm jazz comping on neck pickups.

#### 2. Medium Mid-Bite (4.0 to 5.5 Pips) — Vocal Blues & Singing Sustain
- The loose low-end begins firming up.
- Midrange shifts forward, producing a vocal, expressive singing quality with touch-sensitive compression.

#### 3. High Mid-Bite (6.0 to 9.0 Pips) — British Rock / Marshall Plexi Crunch
- **The Exact Circuit Mechanism**: As Mid-Bite is raised, it simultaneously:
  1. **Tightens the bass**: Introduces pre-gain high-pass filtering that cuts loose sub-bass rumble, preventing "blocking distortion" and muddy low-end "farting out."
  2. **Increases gain**: Drives the 12AX7 grids harder into symmetrical and asymmetrical clipping.
  3. **Rolls off extreme high frequencies**: Filters out buzzy, brittle treble (>5–6 kHz) for a smooth, musical drive.
  4. **Creates a pronounced upper-midrange peak (1.5 kHz to 2.5 kHz)**: Replicates the iconic resonant punch of British EL34 power stages and Celestion speakers cutting through a dense mix.
- Transforms the amp from an American Tweed combo into a roaring Marshall Plexi / 1987 Super Lead crunch machine.

---

## 4. Shared Onboard Effects: Spring Reverb & Bias Tremolo

### Spring Convolution Reverb
- Sampled directly from Tone King's physical tube-driven spring tank.
- **LEVEL**: Wet/dry blend.
- **DWELL**: Controls virtual spring tank drive and decay envelope.
  - *Low Dwell (1.0–3.0)*: Gentle drive; short, intimate, room-like decay without splashy flutter.
  - *High Dwell (4.0–9.0)*: Pushes the virtual spring into non-linear mechanical resonance with authentic metallic drip and lingering decay.
- **Reverb Tails**: Retained across channel/preset switches via Tone King Editor software.

### Digital Bias-Style Tremolo
- Authentically reproduces tube-bias modulation (modulating the tube grid bias rather than using an optical photocell or harmonic frequency crossover).
- **DEPTH**: Modulation depth / amplitude dip intensity.
- **SPEED**: LFO rate.
  - *Low Speed (1.0–3.5)*: Floating, oceanic "swamp" pulse that breathes musically with chord decays.
  - *High Speed (6.0–9.0)*: Rapid, percussive, rotor-like Leslie chop.

### Channel Independence
- Reverb and Tremolo can be independently toggled ON or OFF per channel (e.g., Rhythm with subtle reverb; Lead with dry punch or tremolo pulse).

---

## 5. Stock IR Options & Tone King Editor

### Pre-Loaded Kevin Rowe (OwnHammer) Multi-Mic Impulse Responses

| Slot | IR Model Name | Cabinet & Speaker Heritage | Mics & Preamp | Sonic Profile & Primary Musical Styles |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **OH 112 Imperial TK1660** | Tone King Imperial 1x12 open-back combo with custom TK1660 speaker | SM57, U87, R121 via API 312 | Warmest, balanced mids, 3D open-back bloom. **Ideal for:** Jazz, Neo-Soul, Fingerstyle. |
| **2** | **OH 212 Class A Blue** | 1963 Vox AC30 2x12 open-back combo with Celestion Alnico Blues | SM57, U87, R121 via API 312 | Glassy top-end chime, upper-mid bell resonance. **Ideal for:** Jangle, Funk Quack, Yacht Rock. |
| **3** | **OH 412 Basketweave M25** | 1971 Marshall 1960B 4x12 straight cab with Celestion G12M-25 Greenbacks | SM57, MD421, R121 via API 312 | Heavy low-end thump, focused midrange push, rolled highs. **Ideal for:** Classic Rock Crunch, British Lead. |

### Tone King Editor Capabilities
- Internal library of **15 custom OwnHammer IRs**; supports loading external 44.1 kHz–96 kHz WAV files.
- **3 Lowpass Filter Options**: Tames ultra-high digital sizzle.
- **HF Comp (High Frequency Compensation)**: Restores top-end brilliance when extreme attenuation is engaged.
- **128 MIDI Presets**: Recalls channel, IR slot, effects states, and bypass over standard 5-pin MIDI IN.

---

## 6. Physical Dial Calibration: The 9-Pip Standard

Every knob on the Tone King Imperial Preamp features **9 visible pips (ticks)**:
- **Pip 1 (1.0)**: Minimum / fully counter-clockwise (CCW).
- **Pip 5 (5.0)**: Exactly at **12:00 noon** — nominal baseline / unity.
- **Pip 9 (9.0)**: Maximum / fully clockwise (CW).

---

## 7. Pedal-Less Dynamic Control: 4-Dimensional Articulation

With no external pedals in front of the Imperial Preamp, tone shaping relies on:
1. **Guitar Volume Pot as Gain Governor**:
   - Setting the Lead Channel to Volume 5.0 and Mid-Bite 5.5–6.5:
     - Volume on 10: Full British Plexi crunch with singing sustain.
     - Volume on 7–8: Vocal, touch-sensitive edge-of-breakup.
     - Volume on 4–6: Woody, pristine clean with zero distortion.
2. **Pick Attack as Timbral Switch**: Soft thumb/fingerstyle attack stays beneath the tube clipping threshold; aggressive pick downstrokes drive the 12AX7 stages into harmonic compression.
3. **Guitar Tone Pot as Missing Cut/Mid Contour**: Rolling tone back to 6–7 tames single-coil/P-90 bite; rolling to 1–3 produces the creamy Clapton "Woman Tone" on humbuckers.
4. **Volume vs. Attenuation Staging**:
   - Volume 2.5–3.5 / Attenuation 5.5–6.5: Fast, tight, dynamic transient tracking.
   - Volume 5.0–6.5 / Attenuation 4.0–4.5: Spongy, blooming tube sag that cushions note attack and extends sustain.
