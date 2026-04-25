# Amp Designer — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 774–1645

Add via: Amps and Pedals > Amp Designer in a channel strip Audio Effect plug-in menu.

---

## Overview

Amp Designer emulates more than 20 famous guitar amplifiers and their speaker cabinets. Each preconfigured model combines an amp, cabinet, and EQ recreating a well-known guitar amplifier sound. Also includes spring reverb, vibrato, and tremolo.

---

## Interface Sections

- **Model parameters**: Model pop-up menu selects a preconfigured combo (amp + cabinet + EQ + mic). Separate Amp, Cabinet, Mic, and EQ pop-up menus allow custom builds.
- **Amp parameters**: Gain (input preamplification), Presence, and Master (output volume to cabinet) — at each end of the knobs section
- **Effects parameters**: Reverb, Tremolo/Vibrato — center of the knobs section. **Note: Effects section is placed before Presence and Master in the signal flow, receiving the pre-amplified, pre-Master signal.**
- **Microphone parameters**: Mic type and position — right of the interface (full interface only)
- **Output slider**: Final output level fed to subsequent effect slots or channel strip output. **Different from Master — Master is both a sound-design control and level control for the Amp section.**

---

## Amplifier Controls

- **Gain knob**: Amount of preamplification. Behavior varies per model — e.g., British Amp at max produces powerful crunch; Vintage British Head at max produces heavy distortion suitable for lead solos.
- **Presence knob**: Adjusts ultra-high frequency range above Treble. Affects only the output (Master) stage.
- **Master knob**: Output volume of amplifier signal sent to cabinet. For tube amplifiers, higher Master = more compressed and saturated sound, more distortion. **WARNING: High Master settings can produce extremely loud output. Start low and raise slowly.**
- **Output slider/field**: Final level control for Amp Designer output.

---

## EQ Types

All EQ types have identical controls (Bass, Mids, Treble) but behave very differently. Choose EQ type from the EQ pop-up menu (click the word EQ or CUSTOM EQ above the tone knobs).

| EQ Type | Character |
|---------|-----------|
| **British Bright** | Inspired by 1960s British combos; loud and aggressive, stronger highs than Vintage EQ; more treble definition without overly clean sound |
| **Vintage** | American Tweed-style and vintage British stack response; loud, subject to distortion; rougher sound |
| **U.S. Classic** | American Black Panel circuit; higher fidelity than Vintage, tighter lows, crisper highs; good for brightening and reducing distortion |
| **Modern** | Based on 1980s–90s digital EQ unit; sculpts aggressive highs, deep lows, scooped mids (rock/metal) |
| **Boutique** | Modern retro boutique amp; precise EQ adjustments; may sound too clean with vintage amplifiers; good for cleaner, brighter sound |

**Note:** EQ types are calibrated for specific amplifier models. Mismatching can produce thin or unpleasantly distorted tone, but experimentation can yield good results.

---

## Amp Models

### Tweed Combos (1950s–early 1960s American)
Warm, complex, clean sounds → gentle distortion → raucous overdrive with gain. Responsive to playing dynamics.

| Model | Description |
|-------|-------------|
| Small Tweed Combo | 1×12", smooth clean-to-crunch transition; blues and rock. Set Treble and Presence ~7 for extra definition. |
| Large Tweed Combo | 4×10", originally for bass; more open/transparent than Small; can deliver crunch |
| Mini Tweed Combo | 1×10"; punchy; clean and crunch typical of Tweed combos |

**Tip:** Responsive to guitar volume knob — reduce guitar volume for cleaner tone, increase for soloing.

### Classic American Combos (mid-1960s: Black Panel, Brown Panel, Silver Panel)
Loud, clean, tight low-end, restrained distortion. Clean rock, vintage R&B, surf, twangy country, jazz.

| Model | Description |
|-------|-------------|
| Large Black Panel Combo | 4×10"; sweet, well-balanced; rock, surf, R&B; great for reverb-saturated chords or strident solos |
| Silver Panel Combo | 2×12"; loud, clean; percussive, articulate attack; funk, R&B, intricate chord work; can crunch when overdriven |
| Mini Black Panel Combo | 1×10"; bright and open, reasonable low end; clean tones with minimal overdrive |
| Small Brown Panel Combo | 1×12"; smooth and rich, retains detail |
| Blues Blaster Combo | 1×15"; clear top end, tight defined low end; blues and rock |

**Tip:** Use Pedalboard distortion stompbox for hard-edged crunch sounds with these clean amps.

### British Stacks (50W and 100W heads)
Medium gain = thick chords and riffs. High gain = lyrical solos and powerful rhythm. Complex tonal peaks/dips keep clarity even with heavy distortion.

| Model | Description |
|-------|-------------|
| Vintage British Stack | Late 1960s 50W; powerful, smooth distortion; notes retain clarity at maximum gain; definitive rock tone |
| Modern British Stack | 1980s–90s descendant; deeper and brighter low/high end; more scooped mids than Vintage British |
| Brown Stack | British head at lower voltages; "brown" sound — more distorted and loose; adds thickness |

**Tip:** Classic British head + 4×12" cabinet ideal for riffs at high gain. Also sounds good through small cabinets at clean, low-gain settings.

### British Combos (1960s British rock and pop)
Brash, treble-rich. High-end response, mellow distortion, smooth compression. Rarely harsh.

| Model | Description |
|-------|-------------|
| British Blues Combo | 2×12"; loud, aggressive; cleaner than British heads, but rich distorted tones at high gain |
| British Combo | 2×12"; early 1960s; chiming chords, crisp solos |
| Small British Combo | 1×12"; half the power of British Combo; darker, less open tone |
| Boutique British Combo | 2×12"; modern take on 1960s sound; thicker, stronger lows, milder highs |

**Tip:** Can use higher Treble and Presence settings than other amp types. Combine British Blues Combo with Hi Drive for aggressive blues tone, or Candy Fuzz for heavy rock.

### British Alternatives (late 1960s heads and combos)
Loud, aggressive, full mid frequencies. Sunshine: Brit-pop. Stadium: retains crisp treble and note definition at extreme levels.

| Model | Description |
|-------|-------------|
| Sunshine Stack | Robust; head + 4×12"; good for pop-rock chords; if too dark, use high Treble |
| Small Sunshine Combo | 1×12"; brighter than Sunshine Stack; similar tonal qualities to 1960s British Combo |
| Stadium Stack | Classic head + 4×12"; cleaner than other 4×12" stacks but retains body; power and clarity |
| Stadium Combo | 2×12"; smoother than Stadium Stack |

**Tip:** Stadium amps are slow to distort — famous users paired them with aggressive fuzz pedals (Candy Fuzz or Fuzz Machine stompboxes).

### Metal Stacks (modern high-gain heads with 4×12" cabinets)
Heavy distortion to extremely heavy distortion. Powerful lows, harsh highs, long sustain.

| Model | Description |
|-------|-------------|
| Modern American Stack | Powerful high-gain; heavy rock and metal; use Mids knob to set scoop or boost |
| High Octane Stack | Smooth gain transition, natural compression; fast soloing, 2–3 note chords |
| Turbo Stack | Aggressive; spiky highs, noisy harmonics especially at high gain; cuts through mixes |

**Tip:** Combining Turbo Stack with distortion/fuzz pedals diminishes its edgy tone — a dry sound is often the best choice.

### Additional Combos

| Model | Description |
|-------|-------------|
| Studio Combo | 1×12"; 1980s–90s boutique; multiple gain stages; smooth sustain-heavy distortion and bold bright clean; heavier sound with 4×12" cabinet |
| Boutique Retro Combo | 2×12"; inspired by expensive modern amps; clean and crunch; old-fashioned flavor with crisp highs and defined lows; very sensitive tone controls |
| Pawnshop Combo | 1×8"; inexpensive 1960s American department store amp; warm clean, thick distortion despite small speaker |
| Transparent Preamp | A preamp stage with no coloration. Selected from the Amp pop-up menu, not the Model menu. |

---

## Cabinets

| Cabinet | Description |
|---------|-------------|
| Tweed 1×12 | Open-back, 1950s; warm and smooth |
| Tweed 4×10 | Open-back, late 1950s; sparkling presence (originally for bass) |
| Tweed 1×10 | Open-back, 1950s; smooth |
| Black Panel 4×10 | Open-back; deeper and darker than Tweed 4×10 |
| Silver Panel 2×12 | Open-back, 1960s; low-end punch |
| Black Panel 1×10 | Open-back, 1960s; glassy highs, low/mid body |
| Brown Panel 1×12 | Open-back, 1960s; balanced, smooth, transparent, rich |
| Brown Panel 1×15 | Open-back, early 1960s; largest speaker in Amp Designer; clear glassy highs, tight focused lows |
| Vintage British 4×12 | Closed-back, late 1960s; big, thick, bright, lively — complex phase cancelations between four 30W speakers |
| Modern British 4×12 | Closed-back; brighter and better low end than Vintage British 4×12, less midrange emphasis |
| Brown 4×12 | Closed-back; good low end, complex midrange |
| British Blues 2×12 | Open-back; bright, solid lows, crisp highs even at high gain |
| Modern American 4×12 | Closed-back; full sound; denser lows/mids than British 4×12 cabinets |
| Studio 1×12 | Open-back; compact, full mids, glassy highs |
| British 2×12 | Open-back, mid-1960s; open, smooth tone |
| British 1×12 | Open-back; crisp highs, low/mid transparency |
| Boutique British 2×12 | Based on British 2×12; richer midrange, more powerful in treble range |
| Sunshine 4×12 | Closed-back; thick, rich midrange |
| Sunshine 1×12 | Open-back; lively; bright, sweet highs; transparent mids |
| Stadium 4×12 | Closed-back; tight, bright, bold upper/mid peaks |
| Stadium 2×12 | Open-back; balanced modern British; compromise between Black Panel 4×10 warmth and British 2×12 brilliance |
| Boutique Retro 2×12 | Based on British 2×12; rich, open midrange; more powerful in treble range |
| High Octane 4×12 | Closed-back, European; strong lows and highs, scooped mids; metal and heavy rock |
| Turbo 4×12 | Closed-back, European; strong lows, very strong highs, deeply scooped mids; metal and heavy rock |
| Pawnshop 1×8 | Strong low-end punch |
| Direct | Bypasses speaker emulation entirely |

**Cabinet selection notes:**
- Open-back = bright, airy highs, spacious sound
- Closed-back = tight, focused, more powerful-sounding, tighter low end
- Aged speakers = looser, duller but smoother and more musical
- Multiple speakers = phase cancelations add texture and interest

---

## Microphones

Choose via Mic pop-up menu. Position via XY pad (white dot). Only accessible in full interface (click disclosure arrow if in small interface).

| Mic Type | Character |
|----------|-----------|
| Condenser 87 | Fine, transparent, well-balanced — good for blues, jazz |
| Condenser 414 | Fine, transparent, well-balanced |
| Dynamic 20 | Brighter and more cutting than condensers; mid-range boosted, softer lower-mids; good for rock and cutting through a mix |
| Dynamic 57 | Same character as Dynamic 20 family |
| Dynamic 421 | Same character |
| Dynamic 609 | Same character |
| Ribbon 121 | Often described as bright or brittle yet still warm; useful for rock, crunch, and clean tones |

**Mic positioning:**
- Center of speaker cone (on-axis, default) = fuller, more powerful sound; blues or jazz
- Rim of speaker (off-axis) = brighter, thinner tone; cutting rock or R&B parts
- Closer to speaker = emphasizes bass response

---

## Built-in Effects

### Reverb
Always available, even for models based on amps without reverb.
- **On/Off switch**: Turn reverb on/off
- **Reverb pop-up menu** (click word REVERB): Vintage Spring, Simple Spring, Mellow Spring, Bright Spring, Dark Spring, Resonant Spring, Boutique Spring, Sweet Reverb, Rich Reverb, Warm Reverb
- **Level knob**: Amount of reverb applied to the preamplified signal

| Type | Character |
|------|-----------|
| Vintage Spring | Bright, splashy; classic combo amp reverb sound since early 1960s |
| Simple Spring | Darker, subtler spring sound |
| Mellow Spring | Even darker, low-fidelity spring sound |
| Bright Spring | Some Vintage Spring brilliance, less surf-style splash |
| Dark Spring | Moody, more restrained than Mellow Spring |
| Resonant Spring | 1960s style; strong, slightly distorted midrange emphasis |
| Boutique Spring | Modernized Vintage Spring; richer bass and mids |
| Sweet Reverb | Smooth modern reverb; rich lows, restrained highs |
| Rich Reverb | Rich and balanced modern reverb |
| Warm Reverb | Lush modern reverb; rich lows/mids, understated highs |

### Tremolo / Vibrato
- **On/Off switch**: Turn on/off
- **Trem/Vib switch**: Choose tremolo (amplitude modulation) or vibrato (pitch modulation)
- **Depth knob**: Intensity of modulation
- **Speed knob**: Speed in hertz. Lower = smooth floating sound. Higher = rotor-like effect.
- **Sync/Free switch**: Sync = synchronize with host tempo. Free = set with Speed knob (also allows 1/8, 1/16, and dotted/triplet note values)

---

## Key Notes for Guitar Use

- Logic's Amp Designer is sitting AFTER the Tone King in the signal chain. The signal already has Tone King's character before Amp Designer sees it.
- Use Tone King IR bypass when using Amp Designer's cabinet simulation — double-cabbing degrades tone.
- The Output slider controls the final level post-processing. The Master knob shapes the amp character/saturation.
- The Direct cabinet option bypasses speaker emulation — use with Space Designer + warped speaker IRs for creative processing.
