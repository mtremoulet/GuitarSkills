# The Parallel John Mayer Trinity Rig Guide

A comprehensive architectural manual, gain-staging reference, and preset guide for the **3-Amp Parallel Matrix** and **4-Stage Overdrive Pedalboard**, modeling the signature tone architecture of John Mayer across the *Continuum*, *Trio*, *Battle Studies*, and *Dead & Company* eras.

---

## 1. Architectural Philosophy: The "Three-in-One" Rig

Rather than switching between clean and dirty channels on a single amplifier, John Mayer’s signature studio and touring sound relies on **three distinct tube amplifiers running simultaneously in parallel**:

```
                                          ┌─────────────────────────────────────────────────────────────┐
                                          │               3-Way Parallel Amp Matrix                     │
                                          │                                                             │
                            ┌─────────────┼──► [Paradise 1: Showtime '64 (SSS Anchor)] ──► [Airwindows] ┼──► Ch 1 ┐
                            │             │                                                             │          │
[Guitar In] ──► [Pad -3.4] ─┼──► [Pedals] ┼──► [Paradise 2: Dream '65 (Vibroverb Bloom)] ─► [Airwindows] ┼──► Ch 2 ┼──► [Amp Bus Mixer]
                            │ (Clon/808/  │                                                             │          │        │
                            │  Barker/BD2)└──► [Paradise 3: Enigmatic '82 (ODS Vocal)] ──► [Airwindows] ┼──► Ch 3 ┘        ▼
                            └───────────────────────────────────────────────────────────────────────────┘             [LA-2A Glue]
                                                                                                                            │
                                                                        ┌───────────────────────────────────────────────────┴───────────────────────┐
                                                                        ▼                                                                           ▼
                                                             [Master Mixer (Ch 1: Dry Sum)]                                             [Hitsville Reverb (Parallel Room)]
                                                                        │                                                                           │
                                                                        └──────────────────────────────────────┬────────────────────────────────────┘
                                                                                                               ▼
                                                                                                     [Master Mixer (Ch 2: Wet)]
                                                                                                               │
                                                                                                               ▼
                                                                                                      [Stereo Audio Out]
```

### The Roles of the Three Amps:
1. **Showtime '64 (Dumble Steel String Singer #002 Foundation — "Headroom Hero")**:
   * **Role**: The high-headroom, glassy, ultra-fast transient anchor. It remains pristine, deep, and percussive even when hit with heavy boost pedals.
   * **Stereo Placement**: Panned slightly Left (**L12 / ~12% Left**) via Airwindows Consolidated.
2. **Dream '65 (1964 Blackface Deluxe / Vibroverb Bloom — "Smooth Operator")**:
   * **Role**: The harmonic "sponge" and internal spring depth. Provides organic mid-scoop, tube compression, and subtle internal spring reverb.
   * **Stereo Placement**: Panned dead **Center (0%)** via Airwindows Consolidated.
3. **Enigmatic '82 (Dumble Overdrive Special #83 / Two-Rock Vocal Lead — "Signature 83")**:
   * **Role**: Thick, singing mid-range and vocal sustain. When hit with overdrive pedals, this amp compresses musically and provides horn-like lead sustain without harsh top end.
   * **Stereo Placement**: Panned slightly Right (**R12 / ~12% Right**) via Airwindows Consolidated.

---

## 2. The 4-Stage Overdrive Pedalboard

The front-end drive section sits in-line post-input-pad, feeding all three amplifiers in parallel.

```
[Guitar In Pad -3.4dB] ──► [NA Clon Minotaur] ──► [Efektor Blues Barker] ──► [Efektor Blues River] ──► [NA 808] ──► [Parallel Amp Split]
```

| Stompbox | Emulation & Model | Staging Role & Sonic Character |
| :--- | :--- | :--- |
| **Nembrini NA Clon Minotaur** | *Klon Centaur (Gold/Silver Horsey)* | **Always-On Transparent Lift / Punch**: `Gain 2.2`, `Output 6.1`, `Treble 4.6`. Adds subtle harmonic weight and opens up top-end clarity. |
| **Kuassa Efektor Blues Barker** | *Marshall Bluesbreaker v1* | **Low-Gain Edge of Breakup**: `Gain 2.9` (0.286), `Tone 5.5` (0.554), `Level 3.3` (0.333), `Type A`. The quintessential *Continuum* rhythm crunch. |
| **Kuassa Efektor Blues River** | *Boss BD-2 (Keeley KLY Mod)* | **Trio Era Gritty Snarl**: `Gain 3.0` (0.300), `Tone 5.0` (0.500), `Level 2.2` (0.220), `Type 3` (KLY MOD). The aggressive, fat lead bite from the *Try!* live album. |
| **Nembrini NA 808** | *Ibanez TS-10 / TS-808* | **Vocal Mid-Hump Solo Boost**: `Drive 2.0`, `Level 4.1`, `Tone 3.9`. Tightens low end, lifts 720 Hz mids, and pushes the Enigmatic ODS into fluid sustain. |

---

## 3. Amplifier & Speaker Voicings (Paradise Guitar Studio)

Each instance of **UADx Paradise Guitar Studio** is dialed to occupy a discrete, non-overlapping frequency domain while sharing calibrated output loudness parity:

### Amp 1: Showtime '64 (SSS Clean Glass Anchor)
* **Preset File**: `Toneprint - Mayer Trinity - Amp 1 (Showtime SSS Clean).json`
* **Folder**: `uaudio_paradise_guitar_studio/Showtime '64/`
* **Controls**:
  * Volume: `3.6` (Massive clean headroom, instantaneous dynamic transient speed)
  * Treble: `6.2` (Crystal top-end glass without ice-pick harshness)
  * Middle: `4.2` (Sculpted dip to prevent mid-hump congestion and leave room for the Dumble vocal core)
  * Bass: `4.6` (Tight, unyielding, piano-like low-string snap)
  * Bright: `On` (Restores the quintessential SSS percussive sparkle)
  * Output: `12.0 dB` (Calibrated factory unity parity)
* **Cabinet & Mic Pairing**: **2x12 Showman** (`cab_and_mic: 29`). High fidelity, fast transient attack, and open treble projection.

### Amp 2: Dream '65 (1964 Blackface Reverb Bloom)
* **Preset File**: `Toneprint - Mayer Trinity - Amp 2 (Dream 65 Bloom).json`
* **Folder**: `uaudio_paradise_guitar_studio/Dream '65/`
* **Controls**:
  * Volume: `4.0` (Just touching the threshold of warm 6V6 tube sag and compression)
  * Treble: `5.6` (Sweet, airy top end)
  * Bass: `4.8` (Vintage blackface low-end roundness)
  * Reverb: `2.4` (Organic spring tank bloom before hitting the room reverb)
  * Bright: `Off`
  * Output: `12.0 dB` (Calibrated factory unity parity)
* **Cabinet & Mic Pairing**: **1x12 EV12** (`cab_and_mic: 29`). Warm, punchy, vintage blackface response with smooth speaker excursion.

### Amp 3: Enigmatic '82 (Dumble ODS Vocal Lead Engine)
* **Preset File**: `Toneprint - Mayer Trinity - Amp 3 (Enigmatic 82 Lead).json`
* **Folder**: `uaudio_paradise_guitar_studio/Enigmatic '82/`
* **Controls**:
  * Volume: `5.0` (Touch-sensitive preamp push)
  * Treble: `5.0` (Smooth, rounded top end—zero sizzle)
  * Middle: `7.0` (Rich vocal midrange engine—800 Hz to 2.5 kHz)
  * Bass: `4.4` (Tightened low end to eliminate flub under overdrive)
  * Presence: `4.2` (Smooth upper harmonic sheen)
  * Master: `7.8` (Compensates for Dumble master volume circuit attenuation to achieve parity with Fenders)
  * Channel: `Clean / Normal` (`enigmatic_channel: 1`, `overdrive_enable: False`)
  * Bright: `Off`
  * Output: `12.0 dB` (Calibrated factory unity parity)
* **Cabinet & Mic Pairing**: **2x12 Boutique D65** (`cab_and_mic: 2`). Celestion G12-65 response: rich vocal mids, smooth rolled highs, creamy sustain.

---

## 4. Studio Submix & Spatial Chain

### 1. 3-Channel Amp Bus Mixer (`element.audioMixer`)
* Sums the 3 stereo Airwindows-panned amp signals into a single stereo submix.
* Applied with an internal **-8 dB pad** to maintain +18 dBu headroom into the master compressor.

### 2. UADx LA-2A Silver Compressor (Submix Glue)
* **Preset File**: `Toneprint - Mayer Trinity - Bus LA-2A.json`
* **Folder**: `uaudio_teletronix_la-2a_silver/`
* **Settings**: Mode `Compress`, Peak Reduction `29.0%`, Gain `24.0%`.
* **Behavior**: Gently catches 1.5–2.5 dB of peak transients on full strummed chords while letting single-note lines pass untouched (0.0–0.5 dB GR), preserving 100% pick touch-sensitivity and dynamic freedom.

### 3. UADx Hitsville Reverb Chambers (Parallel Acoustic Room)
* **Preset File**: `Toneprint - Mayer Trinity - Bus Hitsville.json`
* **Folder**: `uaudio_hitsville_chambers/`
* **Settings**: 
  * Chamber: `2648`
  * Distance: `Min` (direct cabinet proximity)
  * Microphones: `KM86` (Neumann condensers)
  * Decay: `2.0` (tight ~1.0s natural studio acoustic decay)
  * Filters: Low `-36.0 dB`, High `-6.0 dB`
  * Mix: `100%` (Wet Solo for parallel aux return)
* **Behavior**: Provides realistic early acoustic room reflections without artificial metallic decay tails, creating a 3D "standing in front of three cranked cabs" feel on Sennheiser HD660S2 headphones.

---

## 5. Curated Amp Mixing Recipes (The Multi-Amp Fader Matrix)

Because all three amplifiers are now matched to **equal loudness parity at `0.0 dB`**, adjusting the **Amp Bus Mixer (Node 6)** faders with bold offsets (-6 dB to -9 dB) dramatically shifts the foundational personality of the entire rig:

### Recipe 1: The Continuum / Studio Hi-Fi Clean *(SSS Dominant Glass)*
* **Ch 1 (Showtime '64 / SSS)**: **`0.0 dB`** (Primary Anchor — 60% presence)
* **Ch 2 (Dream '65 / Blackface)**: **`-6.0 dB`** (Subtle spring warmth underneath)
* **Ch 3 (Enigmatic '82 / ODS)**: **`-9.0 dB`** (Gentle lower-mid body support)
* **Sonic Profile**: Massive clean headroom, crystalline pick attack on high strings, and deep percussive snap on low notes. Perfect for "Neon", "Stop This Train", "Slow Dancing in a Burning Room" intro, and "Gravity".

### Recipe 2: The Trio / Texas Blues Roar *(ODS Vocal Lead Dominant)*
* **Ch 3 (Enigmatic '82 / ODS)**: **`0.0 dB`** (Pushed directly to the front)
* **Ch 1 (Showtime '64 / SSS)**: **`-6.0 dB`** (Pick attack clarity underneath)
* **Ch 2 (Dream '65 / Blackface)**: **`-6.0 dB`** (Vintage air & sag)
* **Sonic Profile**: Fat, woody, mid-forward roar with creamy sustain. When hit with the Klon, Bluesbreaker, or TS-10, this blooms into thick, horn-like lead sustain without harsh top-end sizzle. Perfect for "Who Did You Think I Was", "Wait Until Tomorrow", and SRV-style Texas blues.

### Recipe 3: The 1964 Blackface Reverb Bloom *(Dream '65 Dominant)*
* **Ch 2 (Dream '65 / Blackface)**: **`0.0 dB`** (Center Bloom — Primary Anchor)
* **Ch 1 (Showtime '64 / SSS)**: **`-6.0 dB`** (Sub-bass transient punch)
* **Ch 3 (Enigmatic '82 / ODS)**: **`-8.0 dB`** (Body warmth)
* **Sonic Profile**: Vintage Fender blackface bell-tone, spring tank resonance, and bouncy tube compression. Ideal for ballad chord-melody, fingerstyle jazz, and warm soulful cleans.

### Recipe 4: The 3D Trinity Master Blend *(The Mayer Stadium Tone)*
* **Ch 1 (Showtime '64 / SSS)**: **`0.0 dB`** (Glass & transient anchor)
* **Ch 2 (Dream '65 / Blackface)**: **`-3.0 dB`** (Reverb bloom & tube sag)
* **Ch 3 (Enigmatic '82 / ODS)**: **`-3.0 dB`** (Vocal core & singing mids)
* **Sonic Profile**: The ultimate hybrid wall-of-sound: you get the crystalline transient snap of the SSS, the singing vocal body of the Dumble, and the 3D spring air of the Fender all at once with zero phase clash or frequency masking.

---

## 6. The 5 Signature Pedal Stacking Recipes

Mayer never relies on high-gain distortion pedals; he stacks multiple low-to-medium gain overdrives into a high-headroom multi-amp canvas. Use these 5 proven stacking combinations:

### Stack 1: "The Core Clean Boost / Always-On Lift"
* **Pedal Engaged**: **NA Clon Minotaur alone** (Key `1`)
* **Settings**: Gain `2.2`, Output `6.1`, Treble `4.6`.
* **Sound & Use**: Adds subtle harmonic density, restores top-end chime, and tightens pick response. Great as a baseline tone for fingerpicking and clean rhythm.

### Stack 2: "The Continuum Rhythm Crunch / Edge-of-Breakup"
* **Pedal Engaged**: **Efektor Blues Barker alone** (Key `2`)
* **Settings**: Gain `2.9` (0.286), Tone `5.5` (0.554), Level `3.3` (0.333), Type `A`.
* **Sound & Use**: Amp-like British low-gain breakup. When you play soft, it is pristine clean; when you dig in with the pick, it clips into rich vintage crunch.

### Stack 3: "The Continuum Singing Solo" *(Klon + TS-10)*
* **Pedals Engaged**: **NA Clon Minotaur (Key `1`) $\rightarrow$ NA 808 (Key `3`)**
* **Settings**:
  * Clon: Gain `2.2`, Output `6.1`, Treble `4.6`
  * NA 808: Drive `2.0`, Level `4.1`, Tone `3.9`
* **How It Works**: The Klon provides the broad, fat foundation; the TS-10 cuts sub-bass mud and injects a focused 720 Hz vocal mid-hump. Stacked together into the Enigmatic ODS amp, this delivers Mayer’s signature soaring, horn-like lead sustain ("Gravity" live solos, "Slow Dancing" outro).

### Stack 4: "The 2005 Trio Live Gritty Snarl" *(Bluesbreaker + BD-2 Keeley Mod)*
* **Pedals Engaged**: **Efektor Blues Barker (Key `2`) $\rightarrow$ Efektor Blues River (Key `4`)**
* **Settings**:
  * Blues Barker: Gain `2.9`, Tone `5.5`, Level `3.3`
  * Blues River: Gain `3.0`, Tone `5.0`, Level `2.2`, Type `3` (KLY MOD)
* **Sound & Use**: Aggressive, punchy, asymmetrical clipping with full low-end body. Captures the raw, biting power-trio sound from the *Try!* live album ("Who Did You Think I Was").

### Stack 5: "The Ultimate Wall-of-Sound Lead" *(Klon + BD-2 + TS-10)*
* **Pedals Engaged**: **Clon (Key `1`) $\rightarrow$ Blues River (Key `4`) $\rightarrow$ NA 808 (Key `3`)**
* **Sound & Use**: Maximum singing saturation for heavy climactic soloing. The TS-10 sits at the end of the dirt chain, acting as a laser-focus EQ filter that tightens the broad saturation of the BD-2 and Klon into a screaming, focused lead line ("Vultures" solo, "Covered in Rain").

---

## 7. Humbucker Calibration & Gain Staging Guide (Les Paul Tuning)

Because John Mayer primarily plays vintage-style low-output single-coil Stratocasters (~100–150 mV output, ~5.8k–6.2k DCR), using **Humbuckers (Les Paul Studio / Epiphone LP, ~250–400+ mV output)** will hit the overdrive pedals with nearly double the voltage. 

If unmanaged, stacking two pedals with humbuckers can quickly avalanche into fuzzy "Hendrix / Fuzz Face" distortion rather than creamy Mayer sustain. Follow these three calibration rules:

### 1. The Guitar Volume Sweet Spot (`6–7`)
* **Set your Les Paul volume knob to `6–7`** for your core playing.
* At `6–7`, the pickup output matches a vintage single-coil, restoring full dynamic headroom and glassy top end to the SSS and Dream '65 amps.
* Roll up to **`10`** only when you want to push the pedals into full saturated lead territory.

### 2. Calibrating the Input Pad (Node 7)
* In Kushview Element, **Node 7 (`Guitar In Pad`)** is set to **`-3.4 dB`**.
* If you are playing hot bridge humbuckers and the pedals feel like they clip too abruptly, adjust Node 7 to **`-5.0 dB` or `-6.0 dB`**. This gives the overdrive clipping diodes room to breathe.

### 3. Maximum Gain Ceiling Guidelines
When dialing in the drive pedals for humbuckers, keep gain knobs in the lower third:
* **NA Clon Minotaur**: Gain $\le$ `2.5`, Output `6.0`
* **Efektor Blues Barker**: Gain $\le$ `3.0` (0.300), Level `3.3`
* **Efektor Blues River**: Gain $\le$ `3.0` (0.300), Level `2.2`
* **NA 808**: Drive $\le$ `2.0`, Level `4.0`

---

## 8. Static Amp Canvas Philosophy

In professional multi-amp rigs, **the amplifier settings remain completely static throughout a performance**:
* Neither Mayer nor his guitar tech Rene Martinez adjusts amp EQ knobs mid-set.
* Instead, the three amplifiers are set to **discrete, non-overlapping frequency bands**:
  * **Showtime '64**: Anchors the ultra-lows (<120 Hz) and ultra-highs (>4.5 kHz).
  * **Dream '65**: Anchors the vintage mid-dip (500 Hz–1.2 kHz) and spring tank depth.
  * **Enigmatic '82**: Anchors the vocal midrange core (800 Hz–3 kHz).
* **All dynamic variation is controlled via**:
  1. Right-hand pick dynamics (flesh vs. pick attack).
  2. Guitar volume and tone pot adjustments.
  3. Stompbox switching combinations (Hammerspoon keys `1`–`5`).
  4. Submix fader recipe adjustments in the Amp Bus Mixer (Node 6).

---

## 9. Kushview Element Session Recall & Hotkeys

### Session Location:
`/Users/miketremoulet/Music/Element/Sessions/Toneprints/Parallel_Mayer_Trinity_3Amp.els`

### Hammerspoon Hotkey Reference (Active when Element is in focus):
* **Key `1`**: Toggle **NA Clon Minotaur** (MIDI Channel 1)
* **Key `2`**: Toggle **Kuassa Efektor Blues Barker** (MIDI Channel 2)
* **Key `3`**: Toggle **NA 808** (MIDI Channel 3)
* **Key `4`**: Toggle **Kuassa Efektor Blues River KLY Mod** (MIDI Channel 4)
* **Key `5`**: Master Toggle **All 4 Pedals** (All ON / All OFF)

### Recompiling Presets:
To rebuild or reset all 9 plugin preset files to their canonical factory defaults, run:
```bash
python3 scripts/compile_mayer_trinity_presets.py
```
