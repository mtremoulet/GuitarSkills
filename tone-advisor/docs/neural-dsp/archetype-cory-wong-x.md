# Archetype Cory Wong X — Documentation Cache

Source: `Archetype Cory Wong X v1.0.0.txt` (local manual)

---

## Plugin Structure / Signal Path

**Wah → Pre FX → Amp → Cab (+ Room Reverb) → EQ → Post FX**

### Global Audio Controls

| Control | Range / Notes |
|---------|--------------|
| INPUT | Level of signal fed into plugin |
| GATE Switch | Activate/deactivate noise gate |
| THRESHOLD | Dial up to increase noise gate threshold |
| TRANSPOSE | Pitch transpose ±12 semitones; bypassed at 0 |
| INPUT MODE | MONO / STEREO (stereo doubles CPU) |
| DOUBLER Switch | Duplicates signal for wider stereo image (disabled in STEREO INPUT MODE) |
| SPREAD | 3–20ms time offset between stereo sides of doubler |
| OUTPUT | Level fed out of plugin |

---

## Wah Section

| Control | Notes |
|---------|-------|
| WAH Switch | Activate/deactivate |
| POSITION | Peak response frequency (toe = high, heel = low) |
| AUTO-WAH Switch | Activate/deactivate auto-wah |
| ATTACK | 10ms–1000ms — time for auto-wah filter to fully open |
| RELEASE | 10ms–1000ms — time for auto-wah filter to close |
| SENSITIVITY | Input level needed to trigger auto-wah |

---

## Pre FX Section (four effects in series, each independently bypassable)

### "The Postal Service" — Envelope Filter Pedal

| Control | Range / Notes |
|---------|--------------|
| RANGE | Minimum cutoff frequency: 600Hz–1700Hz |
| SENSITIVITY | Input level needed to trigger filter |
| ATTACK | Time for envelope filter to open |
| DECAY | Time for envelope filter to close |
| BYPASS | Stomp switch |

### "The 4th Position Compressor" — Compressor Pedal

| Control | Range / Notes |
|---------|--------------|
| BLEND | Balance between direct and compressed signal |
| TONE | High-frequency control for compressed signal |
| COMPRESSION | Amount of compression; higher = more compressed |
| VOLUME | Output level |
| BYPASS | Stomp switch |

### "The Tuber" — Overdrive Pedal

| Control | Range / Notes |
|---------|--------------|
| TONE | High-frequency shaping |
| DRIVE | Gain amount |
| LEVEL | Output level |
| BYPASS | Stomp switch |

### "The Big Rig Overdrive" — Overdrive Pedal

| Control | Range / Notes |
|---------|--------------|
| TONE | High-frequency shaping |
| DRIVE | Gain amount |
| LEVEL | Output level |
| BYPASS | Stomp switch |

---

## Amp Section (three models; selecting amp also switches Graphic EQ)

### "D.I. Funk Console" — Analog Channel Strip

| Control | Range / Notes |
|---------|--------------|
| COMP | Compression amount |
| ATTACK Switch | Compression attack speed: SLOW / FAST |
| TUBE SAT | Distortion amount |
| HIGH PASS | Cutoff frequency: 20Hz–250Hz; increase to remove low frequencies |
| LOW PASS | Cutoff frequency: 2kHz–17kHz; decrease to remove high frequencies |
| LOWS, MIDS, HIGHS | 3-band tonestack EQ |
| FREQUENCY Switches | Toggle target frequency for LOWS, MIDS, HIGHS knobs |
| OUTPUT | Overall output volume |
| POWER BUTTON | Bypass/enable amp section |

### "The Clean Machine" — Clean Amplifier

**Note:** The PDF manual calls the first knob "GAIN" but the actual plugin interface labels it **"volume"**.

All knobs use **0–100% range** (confirmed via Logic Controls panel).

| Control | Range / Notes |
|---------|--------------|
| VOLUME | Input gain (labeled "volume" on the hardware, "GAIN" in the PDF manual) |
| BRIGHT Switch | High-frequency boost; UP = ON |
| BASS | Tonestack low; 0–100% |
| MIDDLE | Tonestack mid; 0–100% |
| TREBLE | Tonestack high; 0–100% |
| PRESENCE | High frequencies in power amp stage; 0–100% |
| OUTPUT | Overall output volume; 0–100% |
| POWER Button | Bypass/enable amp section |

### "The Amp Snob" — Clean/Crunch Amplifier

| Control | Range / Notes |
|---------|--------------|
| VOLUME | Input gain |
| BRIGHT Switch | High-frequency boost; UP = ON |
| BASS, MIDDLE, TREBLE | 3-band tonestack |
| MASTER | Power amp gain |
| PRESENCE | High frequencies in power amp stage |
| DRIVE Switch | Additional tube stage; UP = ON |
| OUTPUT | Overall output volume |
| POWER Button | Bypass/enable amp section |

**Note:** LEVEL knobs control overall amp volume without affecting tone.

**Amp/Cab Link:** By default, amps are linked to their respective cabinets. Click the link icon to unlink and mix/match.

---

## Cab Section

Comprehensive cabinet simulation with virtual mics positionable around speakers. Also accepts custom IR files.

### IR Loader Controls

| Control | Notes |
|---------|-------|
| IR Combo Box | Select factory mics/cabs or load custom IR |
| LEFT/RIGHT Nav Arrows | Cycle through factory mics and IRs |
| BYPASS Button | Bypass/enable selected mic or IR |
| POSITION | Mic position around speaker cone (disabled for custom IRs) |
| DISTANCE | Mic distance (disabled for custom IRs) |
| MIC LEVEL | Volume of selected IR |
| PAN | Output panning of selected IR |
| ROOM SEND Toggle | Activate/deactivate room reverb send for this mic slot |
| LEVEL (Send) | dB; how much signal is sent to the Room Reverb module |
| PHASE Button | Inverts phase of selected mic |

**Structure:** Two independent mic slots — **Cab L** (left) and **Cab R** (right). Each has its own type, position, distance, level, pan, phase, and Room Send. Cab R can be deactivated entirely (Cab R Active checkbox).

**Amp/Cab Link:** When enabled (default), each amp uses its matched cabinet. When unlinked, a "Cab Type" dropdown appears — options: **Clean, Snob** (and likely DI) — any cab can be paired with any amp.

**Factory mic types confirmed (from Logic Controls panel):** Ribbon 121, Dynamic 421. Additional types exist.

**Room Reverb module:** SEND levels adjustable independently per mic slot. Adds natural room bloom without a separate reverb pedal.

**POSITION and DISTANCE:** 0.000–1.000 range (normalized, not Hz/dB). Confirmed from Logic Controls panel: "Cab L Position: 0.503", "Cab L Distance: 0.221".

---

## EQ Section

**Three separate 9-band graphic EQs — one per amp model, each independently activatable.** Switching the active amp also switches which EQ is shown. Each EQ has its own Active checkbox.

From Logic Controls panel, the EQ band frequencies are: **65 Hz, 125 Hz, 250 Hz, 500 Hz, 1 kHz, 2 kHz, 4 kHz, 8 kHz, 16 kHz**. Each slider is ±12dB.

| Control | Notes |
|---------|-------|
| EQ Active (per amp) | Checkbox — each amp's EQ must be independently enabled |
| Band sliders (65Hz–16kHz) | ±12dB per band; click-drag up/down |
| HPF | High-pass filter; value in Hz (confirmed: default 20 Hz) |
| LPF | Low-pass filter; value in Hz (confirmed: default 20.0 kHz) |

---

## Post FX Section (three time-based effects in series)

### "The 80s" — Chorus Pedal

| Control | Range / Notes |
|---------|--------------|
| MIX | Wet/dry ratio |
| RATE | Speed: 0Hz–3Hz |
| WIDTH | Offset between L/R LFOs (stereo spread) |
| BYPASS | Stomp switch |

### "Delay-Y-Y" — Delay Pedal

**Note:** The PDF manual labels the high-pass control "LOW CUT" but the Logic Controls panel shows it as **"HPF"** with a value in Hz.

| Control | Range / Notes |
|---------|--------------|
| MIX | Wet/dry ratio; 0–100% |
| SYNC Switch | FREE (ms) / DAW (BPM sync) / TAP — Logic shows "DAW" not "DAW/APP" |
| MODE Switch | SINGLE / DUAL (TIME R disabled in SINGLE) |
| FEEDBACK | Repeat amount; 0–100% |
| HPF (Low Cut) | High-pass on delay repeats; Hz (confirmed range: ~50–800 Hz) |
| TIME L/R | Delay time; FREE: 100ms–1100ms; SYNC: 1/64T–1/1D |
| HIGH CUT | Low-pass on delay: 500Hz–5kHz |
| LCD Display | Shows current delay settings |
| ENGAGE | Stomp switch |
| TAP TEMPO | Set delay time by tapping |

### "The Wash" — Reverb Pedal

| Control | Range / Notes |
|---------|--------------|
| MIX | Wet/dry ratio |
| SHIMMER | Toggle shimmer effect (pitched-up reverb tail layered on direct) |
| DECAY | Length of reverb decay envelope |
| LOW CUT | High-pass on reverb |
| HIGH CUT | Low-pass on reverb |
| BYPASS | Stomp switch |
