---
amp: "Ruby '63 (UADx)"
created: 2026-05-08
guitar: "Squier Stratocaster (bridge + middle pickup position — \\\"quack\\\")"
id: ruby-63-vox-jangle
pickup_type: single-coil
preset_name: "Ruby 63 Vox Jangle SC"
status: initial
tags: "vox, jangle, british-invasion, folk-rock, strat, single-coil, ruby-63, ac30, chime"
target: "AC30 Top Boost chime and jangle — British Invasion, Byrds folk-rock, Tom Petty, and R.E.M. shimmer; the most tonally distinctive amp voicing in the UADx collection"
tone-king-channel: bypassed
updated: 2026-06-28
preset_data:
  amp_platform: uad_paradise
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  amp_settings:
    Bass: 5.0
    Tone Cut: 6
    Treble: 7.0
    Volume: 4.0
  galaxy:
    echo_rate: 6.0
    echo_volume: 2.5
    feedback: 2.0
    head_select: 1
    tape_age: New
---

# Ruby '63 — Vox Top Boost Jangle

## Target Sound

The Ruby '63 (Vox AC30 '63) doesn't sound like anything else in the UADx collection. Every other amp in the rig is either American Fender character or British Marshall character; the AC30 is its own thing entirely — Class A, EL84 tubes, Top Boost, and a natural compression that happens early and musically. It doesn't have the Fender mid-scoop or the Marshall midrange aggression; it has a chimey, almost "papery" top end and a warmth that sits in the midrange rather than the lows.

The **BRILLIANT channel with Top Boost** is the definitive AC30 sound: Treble and Bass controls that shape presence and cut, running into a naturally compressing amp that rewards a light touch but responds to hard picking with a satisfying bloom rather than harsh clipping. This is the British Invasion (Beatles, Hollies, Searchers), the jangle of the Byrds, Tom Petty's chiming Rickenbacker-adjacent clean, and R.E.M.'s 80s-college-radio shimmer.

The Strat in its bridge + middle "quack" position adds the upper-mid sparkle and the slight nasal quality that complements the AC30's natural chime. Together they produce a texture that's adjacent to a 12-string without actually being one.

**Critical control note — Tone Cut is counterintuitive:** *Higher* Tone Cut setting = *fewer* highs. This is the opposite of every other EQ control in this rig. Start at 6 (relatively fewer highs, preserving chime without harshness) and reduce toward 4 for more open jangle. Do not reflexively pull it back expecting more brightness.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

**Pre-FX / Pre-Amp Stompbox Option**

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 2. UADx Ruby '63 Top Boost Amp — chime source

The Ruby '63 has three independent channels: VIB-TREM (tremolo), NORMAL, and BRILLIANT. The **BRILLIANT** channel is the one with the Top Boost EQ (Treble + Bass controls) and the definitive AC30 voice. Low headroom — this amp compresses and blooms at moderate volume levels.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **BRILLIANT** | The only channel with Top Boost EQ controls; the AC30 jangle character |
| Volume | 4–5 | Vol 4: clean with natural compression. Vol 5: just entering the bloom zone — light strumming stays clean, picked accents develop slight harmonic color. Don't push above 6; this amp has minimal headroom. |
| Top Boost Treble | 7 | The Top Boost gives presence and cut — this is what puts the "chime" in AC30 chime. At 5 it sounds flat; at 7–8 it sings. |
| Top Boost Bass | 5 | Neutral — provides the low-mid weight that balances the bright treble boost |
| Tone Cut | **6** | **Counterintuitive control — higher = fewer highs.** Start at 6 (preserves chime without harshness); reduce toward 4 for a more open, "glassy" quality; raise toward 8 for darker character. Do not confuse with a standard Treble control. |

**Cab note:** The Ruby '63 cab options range from the original AC30 Celestion Blue 2x12 (full, warm chime) to brighter, more modern-voiced options. Start with the Celestion Blue configuration — that's the British Invasion reference. If the chime is too pronounced, try a more neutral option.

---

### 3. UADx Galaxy Tape Echo — space and texture

At these settings the Galaxy Tape Echo is not a rhythmic delay effect — it's ambient texture that replicates the natural "room" quality of British Invasion studio recordings. Just enough repeat to fill the space between notes without drawing attention to itself.

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 1 | Single playback head — focused, not multi-tap |
| Echo Rate | 6 | ~200–250ms on Head 1 — a barely-there pre-reverb delay |
| Feedback | 2 | Very low — effectively a single, quiet repeat; not a distinct slapback effect |
| Echo Volume | 2.5 | Quiet; this is texture, not effect |
| Wet Solo | **OFF** | Must be off — this routes dry signal through as well |
| Tape Age | New | Keeps the repeat clean rather than adding degradation |

---

### 4. Logic ChromaVerb — subtle room wash

| Control | Setting | Purpose |
|---------|---------|---------|
| Room Type | Chamber or Small Room | A chamber gives the slightly reflective, old-studio quality of British Invasion recordings |
| Decay | 1.2s | Short enough to stay out of the way; long enough to add bloom between notes |
| Mix | −20 dB (~10% wet) | Subtle — adds space rather than reverb character |
| High EQ | Slightly rolled off | The AC30 is already bright; the reverb tail doesn't need to add more top end |

---

## Optional TONEX Stomp (pre-Tone King)

| Capture | Character | Why it works here |
|---------|-----------|-------------------|
| **Klon Centaur** (~28 captures) | Transparent boost with added harmonic shimmer — does not impose its own tonal color | Pushes the AC30 slightly further into its natural compression without changing the amp's chime character; good when you want Vol 5's bloom with a slightly cleaner attack |

*Default: stomp bypassed. The AC30 jangle tone is complete without a pedal. Engage the Klon only when you want to push the amp slightly harder for a more compressed, "all the time bloom" texture.*

---

## Optional Variation: VIB-TREM Channel

The Ruby '63's VIB-TREM channel has built-in tremolo — a different approach from the BRILLIANT channel that's well suited to surf or 60s R&B. To explore it: switch the active channel to VIB-TREM, keep the Tone Cut counterintuitive behavior in mind, and reduce the Galaxy Tape Echo Feedback to 1. The combined effect of the tremolo and the tape echo creates a hypnotic, vintage-surf-radio quality.

---

## Starting Point Guide

- **The Tone Cut calibration:** When you first open the Ruby '63, the Tone Cut will probably feel backwards. Play with it before deciding it's wrong. At 6 it's the AC30 jangle reference; at 4 it opens up; at 8 it darkens noticeably. Get oriented before making changes.
- **Strat pickup position:** Bridge + Middle ("quack") is the reference for this toneprint. The bridge alone will be very bright through the AC30 — use it sparingly or reduce Top Boost Treble to 5–6 if it's too cutting. Neck + Middle will be warmer and smoother — a different but valid jangle character.
- **Volume sweet spot:** Vol 4 and Vol 5 on the Ruby '63 are genuinely different characters. At 4 it's cleaner and more chimey; at 5 it's slightly compressed and more "alive." Play lightly at Vol 5 for the Beatle-ish clean feel; strum harder for the natural bloom. This amp rewards playing with the right hand.
- **What it's for:** If a track calls for anything in the British Invasion, Byrds, Petty, R.E.M., or jangly indie family, this is the toneprint to reach for. If it feels too bright or "jangly" for a given context, that's the correct assessment — those adjectives are features here, not bugs.

---

## Feedback History

### 2026-05-08 — initial
Built to fill the only distinctly "Vox" tone gap in the library — nothing else sounds like the AC30. BRILLIANT channel with Top Boost specified as the definitive AC30 voice. Tone Cut counterintuitive behavior called out prominently in both the toneprint and starting point guide (easy to misuse on first load). Strat bridge + middle specified for the "quack" position that adds upper-mid sparkle complementing the AC30 chime. Galaxy Tape Echo at very low levels for British Invasion "room" texture rather than echo effect. VIB-TREM channel noted as an optional variation for surf/tremolo exploration.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
