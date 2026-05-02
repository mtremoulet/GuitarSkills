---
id: mardal-dancing-moonlight-sheraton
created: 2026-04-16
updated: 2026-04-18
guitar: Sheraton II
target: Rebecca Mardal "Dancing in the Moonlight" — warm jazz clean with lush-not-ambient reverb
tags: jazz, clean, warm, lush, semi-hollow, neo-soul, Neural DSP
tone-king-channel: rhythm
status: tested
---

# Mardal "Dancing in the Moonlight" — Sheraton II

## Target Sound
Rebecca Mardal's approach is famously minimal: Sheraton II plugged into Neural DSP Archetype Cory Wong X, nearly straight in. The tone is warm, round, and clean — the semi-hollow's natural bloom doing most of the heavy lifting — with a musical reverb tail that fills the room without becoming atmospheric. Not dry, not washed out. Think: the reverb is audible when you lift your fingers, but it sits behind the note rather than in front of it.

The Tone King Rhythm channel enters as a warm buffer with low preamp gain — enough to impart a little character but not enough to impose its Fender mid-scoop. The Cory Wong X's Clean Machine then adds back mids to compensate and provides the cabinet and reverb.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Clean blackface platform; character stays subtle at low Volume |
| Volume | 2.5 | Below breakup and below the point where the TK's tonestack colors heavily |
| Attenuation | 5 | Nominal output; sets level going into interface |
| Bass | 5 | Neutral — don't thicken further; humbuckers already have body |
| Treble | 4 | Slightly rolled off — smooth, not bright |
| Reverb | Off | All reverb handled by Cory Wong X |
| Tremolo | Off | — |
| IR | Bypassed | Neural DSP provides cabinet simulation |

*With TK Volume this low, the Rhythm channel acts more as a clean coloring stage than an active amp character. The inherent Fender mid-scoop is present but subtle; the Cory Wong X amp compensates with a mid lift.*

### 2. Archetype Cory Wong X: Pre FX — 4th Position Compressor

| Control | Setting | Purpose |
|---------|---------|---------|
| Active | On | |
| Blend | 55% | Mostly compressed but some of the direct attack preserved |
| Tone | 50% | Neutral — don't darken the compressed signal |
| Compression | 40% | Light-to-moderate jazz comp — evens out pick attack, adds sustain |
| Volume | 50% | Unity level |

*Mardal plays with a soft touch; this compressor models what her technique naturally achieves on a plugged-in recording. If you play very lightly already, try Compression 30% or bypass entirely.*

### 3. Archetype Cory Wong X: Amp — The Clean Machine

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Type | Clean | Selects The Clean Machine |
| Volume | 30% | Barely cooking — clean headroom |
| Bright | Off | Warm jazz, not sparkly; off removes the top-end cap lift |
| Bass | 50% | Flat; Sheraton's semi-hollow resonance already provides low-end bloom |
| Middle | 70% | Compensates for TK Rhythm channel's inherent Fender mid-scoop |
| Treble | 40% | Smooth rolloff — match the rolled-off treble coming from the TK |
| Presence | 30% | Low presence keeps the power amp dark and warm |
| Output | 100% | Full signal to cab section |

*Middle at 70% is the key call here. Without this lift, the combined TK + amp stack is too scooped and thin for jazz.*

### 4. Archetype Cory Wong X: Cab — Ribbon 121, Room Send

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Linked | Off (unlinked) | Cab Type can be set independently |
| Cab Type | Snob | Currently using Amp Snob's cabinet — warm 2x12 character |
| Cab L Active | On | Left mic slot active |
| Mic L Type | Ribbon 121 | Warm, dark ribbon mic character — correct for jazz |
| Cab L Position | 0.50 | Center of cone — balanced response |
| Cab L Distance | 0.22 | Close-ish but not pinned to the cone; slight air |
| Mic L Level | +2.0 dB | Slight lift on this mic slot |
| Pan | C | Center |
| Room L Active | On | Enables the built-in room reverb send |
| Room L Send | −3.0 dB | Moderate room send — first layer of "lush" |
| Cab R Active | Off | Right slot inactive — single-mic setup |

*Ribbon 121 is the right call for this tone: darker, warmer, less presence-peak than a dynamic. The Room Send at −3 dB adds a subtle room bloom before the reverb pedal does its work — this is what gives the sound that "recorded in a room" quality.*

*Note: If you want to try the Clean Machine's own matched cabinet instead, enable Amp/Cab Linked and set Cab Type to Clean. The Snob cab is slightly warmer/rounder, which works well here.*

### 5. Archetype Cory Wong X: Post FX — The Wash (Reverb)

| Control | Setting | Purpose |
|---------|---------|---------|
| Active | On | |
| Mix | 10% | Subtle presence — audible when you lift fingers, well behind the dry signal. Tested: 35% was overpowering, 20% still too heavy. |
| Shimmer | Off | Shimmer tips reverb into ethereal/ambient; off keeps it grounded in jazz |
| Decay | 55% | Medium tail — fills the space when you lift; doesn't pile up on chord changes |
| Low Cut | 27% | Keeps reverb from muddying the warm humbucker low-end (~100–150 Hz) |
| High Cut | 60% | Warm reverb tails — no shimmer or air, just body |

*The 80s Chorus and Delay-y-y: both bypassed. Mardal's approach is plug-in-and-go; adding either would shift the character away from hers.*

---

## EQ Section Note

The Clean Machine's 9-band graphic EQ (EQ pane in the plugin) is currently **inactive** — this is correct for this starting point. The amp's tonestack (Volume, Bass, Middle, Treble, Presence) handles all frequency shaping. The EQ is a diagnostic tool for refinement after playing:

- If the tone feels boomy in the low-mids: pull 250 Hz down 2–3 dB
- If chord changes start to blur (too much resonance): pull 500 Hz down 1–2 dB
- If there's upper-mid harshness: pull 2 kHz down 1–2 dB
- Otherwise leave it inactive

---

## Starting Point Guide

- **First adjustment**: The Wash Mix. 10% is the tested starting point — this tone runs drier than the initial design expected. If it feels too dry, try 12–15%. Do not go above 20% (confirmed too heavy). This single knob controls most of the lush/dry spectrum.
  - **Alternative direction**: Bypass The Wash entirely, increase Cab Room L Send to 0 dB. Gives natural room bloom without a reverb-effect character — more subtle and transparent than The Wash at any setting.
- **Key interaction**: TK Rhythm Volume + Cory Wong X Middle. If TK Volume goes up for any reason, the Fender mid-scoop deepens — back off Middle on the Clean Machine to compensate.
- **Variations**:
  - *More natural room, less reverb pedal*: Bypass The Wash, increase Cab Room L Send to 0 dB. Confirmed alternative — tested direction.
  - *Subtle width*: Enable the Doubler (Global) with Spread at 8 ms. Gentle stereo image without chorus movement.

---

## Feedback History

### 2026-04-16 — initial
Built from research into Rebecca Mardal's documented rig (Neural DSP Archetype Cory Wong X, Epiphone Sheraton II) and her stated approach: minimal effects, warm clean jazz. "Dancing in the Moonlight" cover shows the same warm round humbucker character with a musical but restrained reverb. Middle boosted to 70% on Clean Machine to compensate for TK Rhythm channel's Fender tonestack mid-scoop at low gain. Settings verified against Logic Controls panel screenshots — all percentage values confirmed correct.

### 2026-04-18 — tested (further refinement)
The Wash Mix pulled back again — 20% was still overpowering. Settled at 10%. Mix progression: 35% (initial, too heavy) → 20% (first pass, still too heavy) → 10% (confirmed working). This tone runs significantly drier than the brief implied. Decay (55%) and Low/High Cut remain correct. Core signal chain confirmed working otherwise.

### 2026-04-18 — tested
The Wash reverb at 35% Mix was too heavy-handed — present in front of the notes rather than behind them. Reduced to 20%. The Decay (55%) and Low/High Cut settings remain correct; Mix was the only adjustment needed. Two valid paths for adjusting reverb weight: (1) lower The Wash Mix from 20% toward 15% for drier feel, or (2) bypass The Wash entirely and increase Cab Room L Send to 0 dB for a more natural, unprocessed room character. Core signal chain and all other settings confirmed working.
