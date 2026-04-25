# Space Designer — Logic Pro Convolution Reverb

Convolution reverb using impulse response (IR) files or synthesized IRs. Can operate as mono, stereo, true stereo, or surround.

---

## Interface sections

- **Sampled IR / Synthesized IR** — mode selector (top bar)
- **IR Sample pop-up** — select impulse response file
- **Main display** — shows IR waveform and envelope editing (Volume Env, Filter Env, Output EQ)
- **Global parameters** — bottom panel; all primary controls for everyday use

---

## Global parameters (the controls you use for guitar)

| Control | Range / Notes |
|---------|--------------|
| Input slider | Stereo / Mono / XStereo — how stereo input is processed; Mono sums L+R before reverb |
| Predelay | 0–1000 ms — time between dry signal and first reverb reflections |
| Length | ms — length of impulse response used. Works with Size knob. Maximum value + Size 100% = full IR length. Determined by IR choice; leave at max unless truncating deliberately. |
| Size | 0–100% — perceived size of the space; multiplied with Length. 100% = full original IR. Lower values = smaller/tighter room feel. |
| X-Over | Hz — crossover between Lo Spread and Hi Spread |
| Lo Spread | 0–100% — stereo width of frequencies below X-Over |
| Hi Spread | 0–100% — stereo width of frequencies above X-Over |
| Dry | dB fader — level of the dry (unprocessed) signal in the output |
| Wet | dB fader — level of the wet (reverb) signal in the output |

**No "Mix %" knob** — wet/dry balance is controlled by the separate Dry and Wet faders in dB.

**No single "Stereo Width" control** — stereo width is set by Lo Spread and Hi Spread (split at X-Over frequency).

---

## Mix % to Wet dB conversion (Dry at 0.0 dB)

| Mix target | Wet fader |
|-----------|----------|
| 5% | −26 dB |
| 8% | −22 dB |
| 10% | −20 dB |
| 15% | −16.5 dB |
| 20% | −14 dB |
| 25% | −12 dB |
| 30% | −10.5 dB |

---

## Quality pop-up

- **Lo-Fi** — divides sample rate by 4, grainy
- **Low** — halves sample rate, doubles IR length (useful for very large spaces with less CPU)
- **Medium** — matches project sample rate (standard use)
- **High** — uses highest possible sample rate

---

## Guitar use

- **Intimate small room**: Room IRs, Predelay 5 ms, Size 70%, Lo/Hi Spread 60%, Dry 0.0 dB, Wet −22 dB (~8%)
- **Natural room presence**: Room IRs, Predelay 10 ms, Size 80–100%, Lo/Hi Spread 80%, Dry 0.0 dB, Wet −20 dB (~10%)
- **Plate**: Plates IRs, Predelay 15–20 ms, Size 100%, Wet −14 to −12 dB (~20–25%)

---

## Automation note

Space Designer cannot be fully automated. The following parameters are automatable: X-Over, Dry/Wet output levels, Output EQ.
