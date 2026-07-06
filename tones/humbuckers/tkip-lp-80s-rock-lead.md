---
id: tkip-lp-80s-rock-lead
preset_name: "TKIP LP 80s Rock Lead"
created: 2026-06-06
updated: 2026-06-06
guitar: "Gibson Les Paul Studio"
target: 'Pushed, singing 80s rock lead with classic Marshall 4x12 girth, rich midrange, and warm analog tape delay.'
tags: "classic-rock, lead, humbucker, marshall, crunch, gain"
tone-king-channel: lead
amp: "Tone King Imperial Preamp (Hardware)"
status: initial
pickup_type: humbucker
preset_data:
  amp_platform: hardware
  amp_settings:
    Channel: Lead
    Volume: 6.0
    Attenuation: 5.0
    Tone: 6.0
    Mid-Bite: 6.5
    Reverb: Off
    Tremolo: Off
    IR: Active (Marshall 4x12 Basketweave - OH 412 Basketweave M25)
  1176:
    input: 30.0
    output: 18.0
    ratio: 4.0
    attack: 3.0
    release: 5.0
  ua_610b:
    mode: Line
    input_gain: 0.0
    level: 5.0
    output: 0.0
    eq_high_freq: 4.5
    eq_high_gain: -1.5
    eq_low_freq: 200.0
    eq_low_gain: 1.5
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 12.0}
    band5: {on: true, freq: 2500.0, gain: 1.5, q: 1.0}
  galaxy:
    head_select: 3
    echo_rate: 5.5
    feedback: 3.0
    echo_volume: 4.0
    wet_solo: true
  capitol_chambers:
    chamber: 4
    decay: 2.2
    pre_delay: 20.0
    wet_solo: true
---

# TKIP LP 80s Rock Lead

## Target Sound
A high-sustain, mid-forward 80s classic rock lead tone inspired by Slash's signature Marshall JCM800 crunch. Built using the hardware Tone King Lead channel pushed hard (Volume 6.0, Mid-Bite 6.5, Tone 6.0) running into the built-in Marshall 4x12 cabinet IR (OH 412 Basketweave M25) for ultimate girth and authority. Post-amp plugins in Logic include the UADx 1176LN FET Compressor to squeeze out singing sustain, and the UADx 610-B Tube Preamp & EQ to add analog console saturation and warm up the highs. A lush tape delay and large room reverb are placed on send buses.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
Provides the primary high-gain preamp crunch and Marshall cabinet simulation.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Lead | Tweed character transformed into aggressive British crunch |
| Volume | 6.0 | Pushes the preamp stage into classic rock overdrive |
| Attenuation | 5.0 | Unity/moderate output |
| Tone | 6.0 | Slightly brightened for cutting high-frequency definition |
| Mid-Bite | 6.5 | Simultaneously boosts gain, tightens the bass, and pushes midrange presence |
| Reverb | Off | Handled in Logic sends |
| Tremolo | Off | Disabled |
| IR | Active (Marshall 4x12 Basketweave - OH 412 Basketweave M25) | Marshall 4x12 authority, mid-forward presence, and low-end girth |

### 2. UADx 1176LN Rev E Compressor — FET sustain engine
Placed inline to add singing sustain, glue notes together, and introduce classic FET hardware coloration.

| Control | Setting | Purpose |
|---------|---------|---------|
| Input | 30.0 | Drives the FET gain reduction circuit for healthy compression |
| Output | 18.0 | Balances output level |
| Attack | 3.0 | Medium-fast attack to let some transient pass while grabbing sustain |
| Release | 5.0 | Medium-fast release for dynamic breathing |
| Ratio | 4:1 | Standard compression ratio |
| Meter | GR (Gain Reduction) | Watch for 3–5 dB of reduction on hard-strummed lead lines |

### 3. UADx UA 610-B Tube Preamp & EQ — tube console saturation
Adds classic console analog saturation to warm up the sound and smooth out high-end fizz.

| Control | Setting | Purpose |
|---------|---------|---------|
| Input Select | Line | Cleaner input path for DI signal |
| Input Gain | 0 dB | Flat input |
| Level | 5.0 | Pushes the output tube stage to add subtle harmonic color |
| Output | 0 dB | Unity output trim |
| EQ LO Shelf | On — 200 Hz, +1.5 dB | Boosts lower-mid punch |
| EQ HI Shelf | On — 4.5 kHz, −1.5 dB | Smooths out high-end digital harshness and fizz |

### 4. Logic Channel EQ — presence sculpting
Placed last in the insert strip to clean up the low end and add solo articulation.

| Control | Setting | Purpose |
|---------|---------|---------|
| Band 1 (High Pass) | On — 80.0 Hz, 12 dB/oct | Cleans up cabinet sub-rumble |
| Band 5 (Peak) | On — 2.5 kHz, +1.5 dB, Q: 1.0 | Adds presence bite to help solos cut through the mix |

### 5. Galaxy Tape Echo (Bus 4 Send) — tape delay
Set on Bus 4 at **100% Wet** (Wet Solo ON) for classic 80s arena delay repeats.

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −14.0 dB | Prominent delay blend |
| Head Select | 3 | Dotted-eighth delay range (approx. 330ms) |
| Echo Rate | 5.5 | Setting for classic rock ballad tempos |
| Feedback | 3.0 | ~3 repeating echoes that fade naturally |
| Echo Volume | 4.0 | Present, sitting under the primary lead lines |
| Tape Age | New | Clear, legible repeats |

### 6. Capitol Chambers (Bus 3 Send) — large room reverb
Set on Bus 3 at **100% Wet** (Wet Solo ON) to put the guitar in a massive, open acoustic space.

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −12.0 dB | Wet, atmospheric reverb blend |
| Chamber | Chamber 4 (Altec A7) | Huge, open chamber space |
| Mix | 1.0 (100% Wet) | Aux bus blend |
| Decay | 2.2 seconds | Long, lush tail |
| Pre-Delay | 20 ms | Separates dry picking attack from the room response |

---

## Starting Point Guide
- **First adjustment:** Tone King Volume & Mid-Bite. If the tone is too dirty, roll the Tone King Volume down to **5.0** or Mid-Bite to **5.5**. If you need full Marshall saturation, push Volume to **7.0** and Mid-Bite to **7.0**.
- **Key interaction:** The 1176 Compressor and the 610-B Preamp interact heavily. If the sound starts to clip or compress too much, back off the 1176 Input (e.g., to **25**) before adjusting the 610-B Level.
- **Variations:** Engage the neck pickup (490R) and roll its tone to **7** to get Slash's iconic warm "woman tone" lead voicing (as in the solo for *Sweet Child O' Mine*).

---

## Feedback History

### 2026-06-06 — initial
Designed as a pushed 80s Marshall-style lead tone for the Gibson Les Paul Studio (490T bridge pickup). Uses the physical TKIP Lead channel (Volume 6.0, Attenuation 5.0, Tone 6.0, Mid-Bite 6.5) running into the built-in Marshall 4x12 cabinet IR (OH 412 Basketweave M25). Post-FX include UADx 1176LN for compression and sustain, UADx 610-B for analog console saturation, Galaxy Tape Echo on Bus 4, and Capitol Chambers on Bus 3.
