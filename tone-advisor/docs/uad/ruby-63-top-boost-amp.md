# Ruby '63 Top Boost Amp — UADx

Source: https://help.uaudio.com/hc/en-us/articles/30847299809556-Ruby-63-Top-Boost-Amp-Manual

---

## Overview

Emulation of a Vox AC30 Top Boost amplifier. Three channels (Brilliant, Normal, Vib-Trem), each with unique boost circuitry. Tone controls are **inverse** of most amps — clockwise cuts frequencies.

---

## Input Level Setup

- Connect guitar to audio interface Hi-Z input
- Set hardware preamp gain to minimum
- Set IN to center (Hi-Z) position
- For hot signals (humbuckers, active pickups, pre-amplified tracks): reduce IN toward LINE

---

## Controls

### IN
Input level to plug-in. Center = Hi-Z (default). Minimum = LINE. Does not change when loading presets — set once, browse freely.

### OUT
Output level from plug-in. At noon ≈ bypassed level. Use for clean level adjustments (not Volume, which changes amp character).

### Room
Amount of room tone mixed in. Only active when a speaker cabinet is selected (no room sound when Direct/bypassed). Noon is a good starting point.

### Volume
Amp gain. Increasing Volume changes character — more overdrive and compression. Minimum position still produces audible signal (adjusted from hardware behavior). For post-amp level control, use OUT.

### Boost button + knob
Enable the boost circuit for the selected channel. Rotate clockwise to increase gain/effect. Boost type varies by channel — see Channels section.

### Speaker Cabinet
Select from drop-down or < > arrows. See Cabinets table below.

### On / Off
Bypasses plug-in and reduces processing load.

---

## Tone Controls (IMPORTANT — Inverse Operation)

**All tone controls rotate counterclockwise to boost, clockwise to cut.** This matches the original Vox hardware and is the reverse of most amplifiers.

### Cut
Reduces high frequencies from the power amp. Rotate clockwise = darker sound. Expanded range from hardware for easier use (total Cut amount matches original).

### Treble (Brilliant channel only)
**Cuts** treble clockwise. Has no effect on Normal or Vib-Trem channels.

### Bass (Brilliant channel only)
**Cuts** bass clockwise. Has no effect on Normal or Vib-Trem channels.

**Key interactions:**
- Bass and Treble controls are **extremely interactive** with each other
- Both fully clockwise (all the way "up"): extreme smiley-face EQ — bass and treble increased, midrange reduced
- Both at noon: more natural, flatter, fuller tone with stronger midrange
- Similar positions on both knobs often yields the best sounds

---

## Vibrato Controls (Vib-Trem channel only)

- **Vibrato LED button**: Enable/disable. Controls unavailable on Brilliant and Normal channels.
- **Speed knob**: Vibrato rate (extended range beyond original hardware — can go slower)
- **Vib-Trem knob**: Vibrato intensity. Low settings → harmonic tremolo-type tones; high settings → more aggressive volume tremolo
- Note: Adjusting vibrato controls when Vib-Trem is disabled will change the amp's volume slightly (same behavior as original hardware)

---

## Channels

### Brilliant
Based on '63 "top-boost" amp. Extra tube stage = more gain, more treble, less headroom before breakup.
- Cut, Bass, and Treble knobs active
- Vibrato disabled
- Boost: EP-III tape echo preamp — smooth, adds gain. Low boost setting smooths the channel's character.

### Normal
Based on '61 "non-top-boost" amp. More headroom, lower overall gain than Brilliant.
- Only Cut knob active (Bass and Treble have no effect)
- Vibrato disabled
- Boost: Germanium treble booster — midrange-boosted gain. Signature sound on countless records.
- Takes pedals especially well. Try a bright overdrive or distortion in front.

### Vib-Trem
Based on '63 "top-boost" amp, uniquely voiced with its own input circuit. Vibrato circuit active.
- Only Cut knob active for EQ
- Vibrato Speed and Vib-Trem controls available
- Boost: Clean boost without added distortion. As boost increases, midrange and treble increase slightly, bass decreases slightly (prevents flubby distortion).

---

## Tone Shortcuts

- **Blue + Brilliant**: Pairing used by the Beatles and U2
- **Silver + Normal**: The classic Queen sound

---

## Speaker Cabinets

| Cabinet | Speaker/Cab/Mic | Notes |
|---------|-----------------|-------|
| **Silver** | Rare 15W Celestion Silver Bulldog speakers in 2x12 combo, mic'd with 57 | High end warmth and sheen, open midrange |
| **Blue** | Original Celestion Blue Bulldog speakers in 2x12 combo, mic'd with 57 | Classic speaker, more high end and chime |
| **Green** | Modern Celestion G12Hs speakers in 2x12 combo, mic'd with M160 ribbon | More midrange honk, tamer highs, thicker with distortion |
| **Blue Mod** | 2x12 cabinet with modern Blue Bulldog speakers, mic'd with 57 | Brighter, more chime, clarity, and jangle than vintage Blue |
| **Match** | Matchless 2x12 with Celestion G12Hs, mic'd with 57 | More muscular, modern take on the Ruby sound. Great with overdrive/distortion in front. |
| **Gold** | 1x12 Two-Rock cab with Celestion Gold, mic'd with 421 dynamic | Narrower sound, midrange forward, thicker with less high end |
| **Direct** | No cabinet | Use with external cabinet emulation |

---

## Notes for Guitar Use

- **The Tone King front end + Ruby '63**: Rhythm channel (blackface American) in front of a British top-boost creates two fundamentally different voicings stacked. Keep Tone King Volume low to pass a cleaner signal into the Ruby's gain stage.
- **Inverse EQ logic**: After years of turning treble knobs clockwise to add brightness, the Ruby requires the opposite mental model. Noon on Bass/Treble does NOT mean flat — it means a significant cut relative to fully counterclockwise.
- **Normal channel + Germanium Boost**: This combination is particularly well-matched to a Tone King → Ruby chain for British crunch. The germanium boost adds characteristic midrange bite.
- **Green cabinet** is the best pairing when using the Ruby for distorted or crunch tones — the ribbon mic on G12Hs tames the Vox high-end harshness.
- **Tone King IR active**: Set Ruby cabinet to Direct and use the Tone King IR as the cab.
