# TONEX Model Library

## Library Shape (as of 2026-04-17)

| Capture Type | Count | What it is |
|---|---|---|
| Stomp | 1,769 | Overdrive / distortion / fuzz pedal captures |
| Amp+Cab | 835 | Full amp + cabinet in one capture |
| ComplexRig | 248 | Multi-component chain (amp + one or more stomps) |
| Amp (no cab) | 89 | Preamp stage only — needs a cabinet IR downstream |
| CustomIR | 64 | Cabinet IR files |
| Stomp+Amp | 13 | Stomp into amp, no cab |

**Total: 3,018 models**
- Factory/IK Multimedia: 1,265
- Community captures: 1,753

Represented hardware includes Fender Deluxe Reverb, Mesa Boogie Dual Rectifier, Vox AC30, Marshall JMP/JCM variants, Orange, Bogner, ENGL, Dumble, Benson Chimera, and many others. Stomp captures cover Boss, Fulltone OCD, Suhr Riot, Wampler, JHS, Darkglass, Beetronics, and more.

## Querying the Library

Use `query_tonex.py` to search at recommendation time. Never try to maintain a static copy of this data — query the live JSON instead.

```sh
# By amp name (substring, case-insensitive)
python3 query_tonex.py --amp "Deluxe Reverb"

# By pedal name
python3 query_tonex.py --stomp "OCD"

# By category
python3 query_tonex.py --category "CLEAN"
python3 query_tonex.py --category "HI-GAIN"

# Free-text search across name, amp, stomp, description, keywords
python3 query_tonex.py --search "benson"

# Filter by capture type
python3 query_tonex.py --target amp     # Amp+Cab and Amp types
python3 query_tonex.py --target stomp
python3 query_tonex.py --target rig

# Combine filters
python3 query_tonex.py --amp "Deluxe Reverb" --target amp --factory

# Stats overview
python3 query_tonex.py --stats
```

Output columns: Model Name, Type, Amp, Stomp, Source (factory/community), GUID.
Present the GUID alongside the model name so the user can locate it in TONEX.

## Flexibility Caveat

TONEX captures are fixed neural snapshots of hardware at one specific setting. Unlike traditional amp emulations (UA Dream '65, Logic Amp Designer, Neural DSP), there are **no adjustable amp parameters** — no gain, no EQ, no master volume on the captured hardware. The only controls TONEX exposes per model are input level and output level.

This makes TONEX useful for "does a capture of this specific amp or pedal exist in the library?" matching, not for dialing in tone from scratch. Treat it as a starting reference, not a flexible tool.

## Signal Chain Rules

### Amp+Cab and ComplexRig captures

These captures include cabinet simulation. Apply the same rule as Logic amp+cab simulations:

- **Tone King IR active** → do NOT use an Amp+Cab TONEX capture. Double-cabbing degrades the tone.
- **Tone King IR bypassed** → Amp+Cab or ComplexRig TONEX capture works as the amp+cab stage.

### Amp (no cab) captures

These capture only the preamp stage. A cabinet IR is still needed downstream — either activate the Tone King IR, or add a Logic/UAD cab sim after TONEX.

### Stomp captures

Stomp captures function as a drive/boost stage. The Tone King IR and downstream amp sim are still needed. Stomp captures slot into the chain the same position as any other overdrive pedal plugin.

### Post-TONEX processing

TONEX output benefits from the same post-amp processing as any other amp sim: compression, EQ, modulation, delay, reverb from Logic or UAD plugins. The capture handles the amp/pedal character; the rest of the chain is still yours to shape.

## Plugin Access

TONEX captures are available in both **TONEX** and **AmpliTube 5** (which can host TONEX captures natively). Either plugin sees the same model library.
