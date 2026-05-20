# Gain Staging Calibration Day

**Goal:** Establish a stable, consistent, and repeatable signal chain from guitar to track output.
Calibrate on the **Gibson Les Paul Studio (490R neck pickup)** as the reference instrument.
Do a final Telecaster pass at the end to establish the single-coil correction value.

---

## Core Principles

**The target:** −12 dBFS peak throughout the chain. Use this number as your ruler at every stage.

**Perceived loudness ≠ dBFS level.** Amp plugins drop the measured signal even as they make things sound fuller and denser. Trust the meter, not your ear, for calibration.

**0 dB I/O trim everywhere is not parity.** Each plugin has its own internal gain structure built into the model. The I/O trims sit *outside* the model — they compensate for what the model does, they don't neutralize it. Setting both to 0.0 dB means "no correction applied," not "unity gain."

**Use the right lever for each job:**

| Lever | Purpose | Do NOT use it for |
|---|---|---|
| iD14 interface gain | Sets the A/D conversion ceiling | Per-guitar or per-toneprint adjustment |
| TKIP Volume | Tone/color — drives the preamp circuit | Level control |
| TKIP Attenuation | Level output — post-preamp trim | Tone shaping |
| Plugin input trim | Sets how hard you hit the virtual circuit (tone decision) | Makeup gain |
| Plugin output trim | Normalizes the plugin's output level | Tone shaping |
| Logic gain plugin | Per-guitar correction (Tele vs LP) | Anything else |
| LA-2A Peak Reduction | Compression character | Level management |
| LA-2A Gain | Makeup gain — restores level after compression | Compression |

---

## Order of Operations

### Step 1 — Set the iD14 Interface Gain

**Signal path:** Guitar → iD14 instrument input (direct, no pedals, no Logic plugins)

1. Open Logic. Insert the Multimeter on the input channel. Set it to **Peak** mode.
2. Play the LP Studio, neck pickup, full volume and tone, hard strums.
3. Adjust the iD14 gain knob until hard strums peak at **−12 dBFS**.
4. Mark or note the knob position. **This is now set and forget.**

> The iD14 gain is calibrated for the LP — the hottest guitar in the stable. Setting it for the hottest signal ensures you never clip at the converter on any guitar. The Telecaster shortfall will be handled in software (Step 7).

---

### Step 2 — Calibrate the Tonex One Pedal

**Signal path:** Guitar → Tonex One → iD14 instrument input (no Logic plugins)

The Tonex One has no "null" or bypass model. Use **hardware bypass** as your reference.

1. Engage hardware bypass on the Tonex One. Note the input level in Logic — this is your reference.
2. Engage a stomp model (e.g., BD-2 T1G1).
3. **Output trim:** Adjust until the engaged stomp model level matches the hardware bypass level.
4. **Input trim:** This controls how hard you hit the model's virtual circuit — it's a tone decision, not a level decision. Set it so the model sounds right (not fizzy/broken-up when it shouldn't be, not thin/quiet). Accept whatever output level results, then correct with output trim.
5. Test with both LP and Tele. Note the level difference between guitars at this stage.

> The goal is: Tonex One engaged = same output level as Tonex One bypassed. Input trim shapes character; output trim normalizes level.

---

### Step 3 — Document the TKIP's Effect on Input Level

**Signal path:** Guitar → Tonex One (bypass) → TKIP → iD14 → Logic

This step is for awareness, not calibration. The TKIP settings will vary per toneprint, so you're building a feel for how much the pedal is doing.

1. Set TKIP to noon on all knobs (Volume 5, Attenuation 5, Bass 5, Treble 5). Note the Logic input level.
2. Try the Rhythm channel and Lead channel separately. Note any level difference.
3. Dial Attenuation down toward the typical toneprint values (5–6) and note how the level changes.
4. Try Volume at 3 (the Jazz Clean / Blackface Jazz toneprint value) and note the difference from noon.

> **Key distinction:** Volume drives the preamp circuit — it's a tone tool, and changing it changes harmonic character. Attenuation is post-preamp — it's a pure level trim. When targeting −12 dBFS at the iD14 input for a given toneprint, **Attenuation is the right lever**, not Volume.

> The TKIP naturally narrows the LP/Tele level gap (from ~8 dB direct to ~3 dB through the pedal). Even so, don't use Attenuation to compensate for guitar-to-guitar differences — that belongs in software.

---

### Step 4 — Calibrate Each Toneprint (Plugin by Plugin)

**Signal path:** Full chain — guitar → Tonex One → TKIP → iD14 → Logic plugins

Do this for each toneprint template. Insert the Logic Multimeter (or a trim/gain plugin with a meter) **between every plugin** in the chain. Work left to right, one plugin at a time.

**Target at every meter insertion point: −12 dBFS peak.**

#### 4a. Amp Sim (PGS, Showtime '64, Dream '65, etc.)

- **Input trim:** Sets how hard the signal hits the virtual amp circuit. This is a tone decision — dial it until the amp responds the way you want it (clean and full, slightly pushed, etc.). Lock it.
- **Output trim:** After the input trim is set, adjust output trim until the plugin output reads **−12 dBFS**. This is a pure level decision with no effect on the model's character.

> Note: Amp sims typically *drop* the measured signal significantly even though they sound louder. PGS drops ~9 dB; the Showtime '64 barely moves the level. Neither is wrong — they're accurate models of hardware with different gain profiles. The output trim exists precisely to compensate for this.

#### 4b. LA-2A Silver Compressor

With a consistent −12 dBFS signal arriving from the amp sim:

- **Peak Reduction:** Adjust until the gain reduction meter shows approximately **−3 dB** of reduction on hard playing. This is the starting target — adjust by ear once it's in the ballpark.
- **Gain (makeup):** Adjust until the compressor output reads **−12 dBFS**.
- Mode: **Compress** (3:1) for clean jazz tones. Limit for more aggressive compression if needed.

> The LA-2A is optical and slow — the gain reduction meter doesn't behave like a VCA. Trust your ears on whether the compression feels right once the levels are set.

> **Known issue:** The Jazz Clean — Intimate toneprint has LA-2A at PR 30 / Gain 50. Measurements confirmed this produces positive dBFS output (clipping). Gain 50 needs to be pulled back substantially. Set peak reduction first, then set makeup gain to restore −12 dBFS — don't use the existing Gain 50 as a starting point.

#### 4c. Reverb / Room (Space Designer, Hitsville, etc.)

Reverb is last in the chain and is a taste decision, not a level calibration. However:

- Check that the final output of the chain (after reverb) still reads **−12 dBFS** or lower.
- If the reverb wet signal is pushing the output above −12 dBFS, reduce the wet level until it doesn't.
- Space Designer's dry signal at 0.0 dB + wet signal adds gain — keep an eye on the final output meter.

---

### Step 5 — Save Everything

For each toneprint, before moving to the next:

- [ ] **Plugin presets:** Save a named preset in each UADx plugin (amp sim, LA-2A, Hitsville, etc.) matching the toneprint name.
- [ ] **Channel strip preset:** Save the full Logic channel strip as a named preset.
- [ ] **Logic project template:** Re-save the project template with the updated settings.
- [ ] **Toneprint .md file:** Update the toneprint file in `tones/humbuckers/` or `tones/single-coils/` with confirmed settings and a Feedback History entry noting the calibration date and any changes made.

---

### Step 6 — Telecaster Correction Pass (do this once, at the end)

**Signal path:** Tele Player II (neck pickup, full volume/tone) → full chain → Logic

1. Remove all Logic plugins. Measure the Tele input level at the iD14 gain setting established in Step 1.
2. Note the gap between Tele and LP input levels (expect ~8 dB direct, ~3 dB through TKIP).
3. Insert a **Gain plugin at the top of the Logic chain** (before the amp sim). Dial in the gain correction to bring the Tele input up to −12 dBFS.
4. Note this gain correction value. It becomes the standard baked into all single-coil toneprint templates.
5. Verify that the rest of the chain (amp sim, LA-2A, reverb) tracks correctly from there — levels should behave consistently from the amp sim onward without further adjustment.

> The iD14 knob stays at the LP setting. The gain plugin in Logic is the Tele's correction — it lives inside the template, not on the hardware. Single-coil channel strip presets include this gain plugin as part of the preset.

---

## Toneprint Calibration Checklist

Use one row per toneprint. Check off as you go.

| Toneprint | Guitar | Amp Sim Output −12? | LA-2A PR ~−3dB? | LA-2A Output −12? | Reverb Output ≤−12? | Plugin Preset | Strip Preset | Template | .md Updated |
|---|---|---|---|---|---|---|---|---|---|
| Jazz Clean — Intimate | LP | | | | | | | | |
| Blackface Jazz | LP | | | | | | | | |
| JC120 Pristine Jazz Clean | LP | | | | | | | | |
| Mardal Dancing Moonlight | LP | | | | | | | | |
| MRH810 Classic Lead | LP | | | | | | | | |
| Lion 68 Jumped Plexi Crunch | LP | | | | | | | | |
| Two Rock Bloomfield Warm Clean | LP | | | | | | | | |
| Paradise Pedal Platform (HB) | LP | | | | | | | | |
| Sheraton Jazz Acoustic | LP/Sheraton | | | | | | | | |
| Divided 11 Light Blues | Tele | | | | | | | | |
| Dream '65 Blackface Sparkle | Tele | | | | | | | | |
| Ruby '63 Vox Jangle | Tele | | | | | | | | |
| Strat Ambient Bath | Strat | | | | | | | | |
| Tele Electronic Veil Bickert | Tele | | | | | | | | |
| Tele Singing Blues Carlton | Tele | | | | | | | | |
| Woodrow Sweet Spot | Tele | | | | | | | | |
| Paradise Pedal Platform (SC) | Tele | | | | | | | | |

---

## Quick Reference: Known Issues Going In

- **Jazz Clean — Intimate:** LA-2A Gain 50 confirmed clipping (positive dBFS measured). Gain needs significant reduction. Recalibrate from scratch.
- **Blackface Jazz:** LA-2A PR 40 / Gain 30 produced −12 dBFS output. This is the best-performing toneprint going in — use it as a sanity check early to confirm your calibration process is working.
- **Showtime '64 output:** Barely drops the signal (~1 dB). Expect to pull the output trim down significantly to hit −12 dBFS before the LA-2A.
- **PGS output:** Drops ~9 dB. Expect less output trim correction needed after PGS.
- **Space Designer:** At the Jazz Clean settings (Dry 0.0 dB, Wet −22 dB), measured output was higher than input. Check the final output meter after the reverb — it may need a small trim.
