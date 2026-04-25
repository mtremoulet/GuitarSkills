# UADx Lion '68 Super Lead Amp — Documentation Cache

Source: https://help.uaudio.com/hc/en-us/articles/30847259997972-Lion-68-Super-Lead-Amp-Manual
Fetched: 2026-04-14 (rev 2 — corrected from live page via playwright-cli)

---

## Overview

Based on three distinct 100-watt Plexi amplifiers. Classic boost effects, room sound, and a collection of perfectly miked speaker cabs. Covers clean to aggressive breakup to hot-rodded roar.

Calibrated to provide the exact same tone and response as the original amp when used with Apollo and Volt interfaces. For other interfaces: connect to Hi-Z input, set preamp gain to minimum, leave plug-in IN at default Hi-Z position.

---

## Controls

### In
Adjusts the input level to the plug-in. Hover to see HI-Z and LINE labels and input gain in dB.

### Gate (Noise Gate)
Silences extraneous noise by detecting signal at input, acting at end of signal chain. Toggle with button to right of Gate. Drag triangle left up/down to adjust threshold. Click ••• for additional gate controls.

### Room
Adjusts amount of room tone mixed into signal.

- Range: 0–10 knob
- **Noon = good starting point**
- Room only active when using a speaker cabinet; no fully wet Room sound
- Setting fully off = recording in isolation booth; turning up adds ambience from room microphones

### Out
Output level. At noon = roughly same level as bypassed signal.

### On / Off
Bypasses the plug-in and reduces plug-in processing.

### Presence
Adjusts the amp's brightness and gain. Controls overall brilliance and gain of the power amp section. Increase for more available gain and edge.

### Bass
Low frequency component of amp's tone stack.

### Middle
Overall midrange. Reduce for Fender-style scooped tones. Increase for more lead impact and warmth. Can have a lot of impact — don't set below 5 for classic tone.

### Treble
High frequency component of amp's tone stack.

### Volume 1 / Volume 2
Channel I and II gain.
- Channel I: brighter, more aggressive as you turn up
- Channel II: darker, more bottom end
- Both channels connected with virtual Y cable; to use one independently, turn other completely down
- Character changes substantially as you increase either volume — much more saturated and distorted at higher settings
- For clean post-amp volume adjustments, use the Output control (not Volume)

### Lion Inputs (Input Routing)

| Routing | Description |
|---------|-------------|
| LOW | Y cable into Low inputs. Cleaner, slightly darker sound. |
| HIGH | Y cable into High inputs. Brighter sound, more gain and edge. **Default setting.** |
| JUMP | Plugging into High input I, patch cable from Low input I to High input II. Less treble and slightly less gain from Volume II. |

Input Routing is not global — saved per preset.

---

## Lion Models

Click model name to select. Use Boost knob to push amp input for more gain.

| Model | Description | Notes |
|-------|-------------|-------|
| BASS | Classic 100W Super Bass, running at 117 volts. No bright cap — prevents overly bright/brittle tone. | Smooth, rich, excellent pedal platform. "All of your Hendrix dream tones are in here." Dark crunch when driven. |
| LEAD | Classic 100W Super Lead, running at 110 volts. Bright cap modified to 100 pF (JTM 45 value) for jangly highs without harshness. | More gain, more saturation, brighter than Super Bass. Use Vol I for brightness/edge/tight gain; Vol II for bottom end girth. |
| BROWN | Super Lead Variac'd down to 90 volts for sag/thickness, biased high for aggressive attack, bounce, sustain, and compression. Bright cap removed by default. | Darker, thicker, more gain. Very heavy at high volumes. Great for leads and loose fat cleans at low volumes. |

---

## Lion Boost

Has both an **enable button** (click to toggle on/off; lit = enabled) and a **knob** (amount).

- **Disabled** (button unlit): No effect on amp color or gain whatsoever.
- **Enabled** (button lit): EP-III preamp is engaged, adding color and warmth.
  - Up to ~10 o'clock position: adds clean gain, pushes amp's front end
  - Past 10 o'clock: midrange boost curve from a graphic EQ pedal adds thick character
- "Boost adds color and gain from multiple elements with a single control. The Boost elements work together to create harmonic density."

---

## Lion Mods

Two custom modifications. Not global — saved per preset.

| Mod | Description |
|-----|-------------|
| Ghost Notes | When ON: stock amp behavior — original transformer/power supply produces extra hum and "ghost notes" (harmonics from intermodulation distortion); adds life and "scream" to notes higher on the neck. When OFF: cleaner power supply, eliminates ghost notes. **Default: ON.** |
| Bright Cap | Toggles bright cap on Channel I. Adds brightness at lower gains; effect reduced and removed at full gain. ON by default on Lead amp, OFF on Brown. **Not available on Bass model.** |

**NOTE: There is NO Power (Full/Half) control on the Lion '68.** This does not exist in the manual or the plugin UI.

---

## Speaker Cabinets

| Speaker | Speaker/Cab/Mic | Notes |
|---------|-----------------|-------|
| Stripped On-Axis | 1968 basketweave 4x12, Celestion Greenbacks, Ribbon 160 + Dynamic 57 | Classic Celestion bark with smooth open midrange of '60s ribbon and edge of 57 |
| Stripped Off-Axis | Same cab, off-axis, Ribbon 160 + Dynamic 57 | Less edge and brightness vs. on-axis |
| GB30 | Vintage Celestion Greenback 30W in 4x12 closed-back, 57 + Ribbon 121 | Tight bass response, good treble definition; great for distorted classic rock |
| Brown JB | 1968 basketweave 4x12, 2x Celestion Greenback + 2x JBL 120F, dual 57s pre-mixed | Girth and midrange of Celestion + high end sizzle of JBL |
| EV12 | 200W Electro-Voice EVM12L 1x12, 414 condenser | Focused single speaker, thick tight bottom end with airy top end; versatile |
| D65 | Custom ported 2x12, British 65W speakers, 421 dynamic + Ribbon 121 | Tight bottom end clarity. **Favored by many blues and rock players.** |
| V30 | 4x12 V30s, 414 condenser | Standard for modern rock/metal; tight bottom end, high end punch; scooped |
| Direct | No cab/mic/room | Use with external cabinet emulation |

---

## Tone-Targeted Starting Points

*Blues/Hendrix edge-of-breakup (Tone King Lead driving):* BASS model, LOW input, Vol 1: 4, Vol 2: 3, Middle 7, Treble 6, Bass 5, Presence 5, Ghost Notes ON, Bright Cap N/A, Boost OFF, Cab: D65, Room: 3.

*Classic rock crunch (Clapton/Page-style):* LEAD model, HIGH input, Vol 1: 8, Vol 2: 6, Treble 6, Middle 7, Bass 5, Presence 6, Cab: Stripped On-Axis.

*Brown sound (early VH):* BROWN model, HIGH input, Vol 1: 9, Vol 2: 7, Treble 5, Middle 6, Bass 4, Presence 7, Cab: GB30.
