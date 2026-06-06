---
amp: "Woodrow '55"
created: 2026-05-02
guitar: "Squier Stratocaster (single coils)"
id: woodrow-sweet-spot
pickup_type: single-coil
preset_name: "Woodrow Sweet Spot SC"
status: tested
tags: "tweed, woodrow, blues, classic-rock, strat, compressed, mid-forward"
target: "The \\\"Sweet Spot\\\" — vocal, mid-forward Tweed character; clean-ish with a light touch, compressing and \\\"hairing up\\\" beautifully when you dig in."
tone-king-channel: bypassed
updated: 2026-05-03
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Bass: 5
    Boost: false
    Treble: 5.5
    Volume: 3.5
    Volume (Mic): 3
  galaxy:
    echo_rate: 6.5
    echo_volume: 2.0
    feedback: 1.5
    head_select: 1
    tape_age: New
  la2a:
    gain: 35
    peak_reduction: 25
---

# Woodrow Sweet Spot

## Target Sound

The Tweed Deluxe (Woodrow '55) is the polar opposite of the "Blackface" amps (like the Dream '65) you're used to. While Blackface amps have a mid-scooped, "glassy" clean with lots of headroom, the Tweed is mid-forward, "woolly," and has very little headroom.

If you push it too hard, the low end "farts out" and becomes muddy. The trick to a great Tweed sound is finding the **Sweet Spot**: where it sounds clean and chimey when you play softly, but instantly compresses and adds harmonic "hair" when you dig in. 

We're pairing this with your **Squier Strat**. The lower output of the single coils gives the Woodrow more room to breathe before it collapses into total saturation. This is the sound of early ZZ Top, Larry Carlton, or the "Layla" era Strat-into-Tweed tone.

---

## Signal Chain

### Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### Guitar Track → Woodrow Chain

#### 1. Woodrow '55 — The Tweed Sweet Spot

The key here is "jumping" the channels (simulating a patch cable between the Mic and Inst inputs) to get the best of both worlds: the bite of the Instrument channel and the body of the Mic channel.

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume (Inst) | 3.5 | The primary "bite" and gain. Keep it low to preserve that clean-to-grit transition. |
| Volume (Mic) | 3.0 | Adds "thump" and midrange body. Adjust this to fill out the sound. |
| Tone | 5.5 | **CRITICAL:** On a Tweed, turning this up adds gain. 5-6 is the chimey sweet spot for a Strat. |
| Boost (Stock) | **TOGGLE OFF** | Keeps the signal path pure. (Switch stays on Stock, Knob can be at 1.0/default). |
| Input | **High (Input 1)** | Sets the gain stage. Note: **"Jumped"** is automatic when both Volume knobs are > 0. |
| Room | **30%** | Adds natural studio air/ambience. (Roughly 10 o'clock). |
| Cabinet | **GB25** | **Fixed Pairing:** Celestion Greenback + 57. Provides mid-forward chime and grit. |

---

#### 2. Galaxy Tape Echo — Subtle Hair & Space

Tweed amps and Tape Echoes are a match made in heaven. The tape saturation complements the amp's midrange.

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 1 | Single head for a focused slapback character. |
| Echo Rate | 6.5 | **Clockwise = Shorter.** ~100ms on Head 1 for classic depth. |
| Feedback | 1.5 | Set low for essentially a single, discrete repeat. |
| Echo Volume | 2.0 | Supportive — a subtle "shadow" behind the note. |
| Tape Age | New | Keeps the repeats clean and distinct. |

---

#### 3. LA-2A Gray Compressor — Post-Amp Glue

Since the Woodrow is already compressing naturally, we use the Gray LA-2A (which is a bit "faster" and "clearer" than the Silver) just to catch any stray peaks and glue the tape echo to the amp sound.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 25 | Very light; just 1-2dB of movement on the meter |
| Gain | 35 | Makeup gain |

---

## Starting Point Guide

- **The Dynamic Test**: Set your Strat to the Neck/Middle position (Pos 4). Play very lightly—it should sound clean and "woody." Now, hit a double-stop (two notes) hard. You should hear the amp "clamping down" (compression) and adding a bit of grit. That is the Tweed magic.
- **Taming the "Fart"**: If the low E string sounds mushy or distorted in an unpleasant way, roll the **Volume (Mic)** down to 2.0. The Mic channel is where the heavy low-end lives.
- **The Larry Carlton Trick**: Set the **Tone** to 7 and roll your **Strat's Tone knob** back to 6. This creates a vocal, "woman tone" midrange that sings for lead lines without being harsh.

---

## Feedback History

### 2026-05-02 — initial
Designed to introduce Mike to the "Sweet Spot" of the Woodrow '55. Focuses on low-gain, jumped-channel settings paired with a Squier Strat to maximize dynamic headroom and vocal midrange. Corrected for UADx plugin interface (fixed GB25 cabinet, 0.0-10.0 Galaxy scales).

### 2026-05-03 — tested
Tested with Telecaster (single coils). Sounds excellent — clean but with real character. Surprised by the amount of headroom; may need to raise Tele pickups to get the amp into the compressing/hairing-up zone more easily. The preset was designed for the lower-output Squier Strat, so the Tele's slightly different output profile could explain the extra headroom.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
