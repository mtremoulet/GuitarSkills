# Hitsville Reverb Chambers — UADx

Source: https://help.uaudio.com/hc/en-us/articles/10095944517396-Hitsville-Reverb-Chambers-Manual

---

## Overview

Emulation of the two attic reverb chambers above Hitsville U.S.A. (Motown Studios) in Detroit. Uses UA's Dynamic Room Modeling — hybrid of sampled impulse responses + algorithmic DSP. Full signal chain emulation of Hitsville's custom amplifiers, speakers, preamps, and mics.

Natural decay: approximately 3–4 seconds. Decay control can reduce to ~0.5 seconds minimum.

**Latency warning**: Higher latency than other UAD plug-ins. Use on an aux send/return bus rather than as a direct insert on tracks when tracking live.

---

## Chambers

| Chamber | Address | Character |
|---------|---------|-----------|
| **Chamber 1** | 2648 West Grand Blvd | Bright reverb with flutter/parallel wall echo artifacts. More presence. Use for vocals, solos, percussion. |
| **Chamber 2** | 2644 West Grand Blvd | Near-textbook perfect reverb. Smooth, full-range decay. Long pentagonal shape enhances stereo image. Use for strings, horns, piano, drums. |

---

## Speakers

| Chamber | Speaker Option | Notes |
|---------|---------------|-------|
| **1 (2648)** | Bozak 800 + EV T35B tweeters | 8" aluminum cone midrange drivers + tweeter array. Internal 500 Hz HPF. Longest-running 2648 setup. |
| **1 (2648)** | JBL 2482 + EV T35B tweeters | Replaced Bozak in 1968. Narrow-band "foghorn" driver — handles massive signal levels. Same Bozak crossover and tweeter array. |
| **2 (2644)** | Altec 605A Duplex + N-1500A crossover | Full-range 15" woofer + integrated HF horn driver. In ported Altec 612A cabinet. Original 2644 setup. |
| **2 (2644)** | Bose 901 with active equalizer | Full range, wide imaging. Drivers face backwards (as Bose intended). Replaced Altec 605As in late '60s. Lo control below -6 dB shifts cutoff frequency. |

---

## Microphones

| Mic | Type | Notes |
|-----|------|-------|
| **Shure Unidyne 545** | Cardioid dynamic | Predecessor to SM57. Most frequently used setup in Chamber 1 (with Bozak 800). |
| **RCA 44-BX** | Figure-8 ribbon | First mic used in Hitsville chambers. Low-mid complexity, subdued HF, strong proximity characteristics. |
| **Electro-Voice 631** | Omnidirectional dynamic | Band-limited frequency response, tight reach. Chrome cousin of EV 635. |
| **Neumann KM86** | Multi-pattern small diaphragm condenser | Crisp, versatile. Sole Motown mic for a period. Chamber 2 with Altec 605s: figure-8 Blumlein. Chamber 2 with Bose 901s: omni. Chamber 1: cardioid. |

---

## Controls

### Chamber Select
Click Chamber 1 / 2648 or Chamber 2 / 2644. Recalculation occurs on change.

### Speakers
Hover to show speaker icons, click to select. Two speaker options per chamber.

### Microphones
Hover to show microphone icons, click to select. Four mic pairs available for either chamber.

### Distance
Slider controlling distance between microphone pair and speakers. Drag slider or drag within chamber view.
- **Chamber 1**: MIN = original recorded position
- **Chamber 2**: 5.0 = original recorded position
- Closer = tighter room, more source presence; farther = more diffused
- Mic positions are saved per chamber independently

### Mono switch
When stereo-out: sums reverb to mono output, overriding Width. When mono-in/mono-out: locked in mono position (uses left speaker + left mic only).

### Width
Stereo imaging width. 0% = mono. 100% = natural stereo as captured. Not adjustable in mono configurations.

### Predelay
Time before reverb onset. Range: 0–250 ms (logarithmic scale, finer resolution at lower values). Click "0", "50 ms", or "250" labels for quick access.

### LO / HI Level
Gain for low and high frequency components of the speaker crossover (or EQ filter for Bose):
- **LO**: -36 dB to +6 dB continuously variable
- **HI**: ±6 dB continuously variable
- With Bose speakers: these become pre-emphasis EQ filter controls (continuous instead of stepped)

### Decay
Reverberation time. Counter-clockwise = shorter. MAX = natural room decay. Minimum ≈ 0.5 second. Click "MIN", "MID", or "MAX" labels for quick access.

### Mix
Blend of dry and wet signals. 0% = dry only. 100% = wet only.

**CRITICAL**: Mix uses a logarithmic scale. **At noon (12 o'clock), Mix = 15%, not 50%.** Click "0", "15%", or "100" labels for quick access.

### Solo
100% wet mode — mutes dry signal, Mix has no effect. Designed for aux return bus use. Global per-instance (does NOT change when a preset is loaded).

### Power
Enables/disables the plug-in.

---

## Automation Notes

| Parameter | Automation |
|-----------|-----------|
| Chamber Select, Microphones Select, Speakers Select, Lo (except Bose), Hi (except Bose), Decay | Not recommended (time lag / sonic artifacts with UAD-2) |
| Distance | Static snapshot automation between audio passages only |
| All other parameters | Continuous and static snapshot OK |

UADx handles recalculations faster than UAD-2 — automation artifacts are less severe on UADx.

---

## Notes for Guitar Use

- **Chamber 1** is the better choice for guitar — the brighter, more present character with the Bozak/EV speakers cuts through a mix. Chamber 2's smoother decay can wash over guitar.
- **Mix at noon ≠ 50%** — same logarithmic scale as Capitol Chambers. The "15%" text label at noon is the reference point. Start around 2–3 o'clock for a meaningful reverb presence.
- **Shure Unidyne 545** (predecessor to SM57) is the most familiar-sounding mic for guitar reverb — the SM57 character is well-suited to instrument sources.
- **Chamber 2 + long Distance + low Decay**: creates a wide, ambient guitar wash without excessive tail length — useful for clean guitar pads.
- Like Capitol Chambers: use on a send/return aux bus with Solo enabled, not as a direct insert.
