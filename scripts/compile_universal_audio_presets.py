#!/usr/bin/env python3
import os
import json
import re
import uuid

# Base paths for Universal Audio presets on macOS
BASE_UAD_PRESETS_DIR = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins"
PARADISE_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_paradise_guitar_studio")
PARADISE_TEMPLATE = os.path.join(PARADISE_DIR, "Boutique Warm Clean - Enigmatic.json")

# List of all toneprints mapped exclusively to Paradise Guitar Studio
PARADISE_TONEPRINTS = [
    {
        "source": "tones/humbuckers/paradise-enigmatic-boutique-clean.md",
        "preset_name": "Toneprint - Enigmatic Boutique Clean HB.json",
        "amp_index": 1,        # Enigmatic '82
        "cab_index": 2,        # 2x12 Boutique D65
        "controls": {
            "amp": 1,
            "enigmatic_volume": 5.5,
            "enigmatic_treble": 3.5,
            "enigmatic_middle": 7.5,
            "enigmatic_bass": 7.0,
            "enigmatic_presence": 0.5,
            "enigmatic_master_gain": 7.0,
            "enigmatic_model": 0,            # Suede
            "enigmatic_channel": 1,          # NOR input
            "enigmatic_bright_enable": False,
            "enigmatic_deep_mid": False,
            "enigmatic_tone_stack_type": 0,  # Skyline mods
            "enigmatic_tone_stack_eq": 0,    # Jazz
            "enigmatic_boost_enable": False,
            "enigmatic_overdrive_enable": False,
            "cab_and_mic": 2,
            "prefx_power": False,            # Bypass pedal slots
            "postfx_power": False
        }
    },
    {
        "source": "tones/single-coils/ruby-paradise-strat-chime.md",
        "preset_name": "Toneprint - Ruby Strat Chime Paradise.json",
        "amp_index": 3,        # Ruby '63
        "cab_index": 1,        # AC30 2x12 Alnico Blue
        "controls": {
            "amp": 3,
            "ruby_channel": 2,               # Brilliant channel
            "ruby_volume": 4.5,
            "ruby_cut": 5.0,                 # Cut Switch ON
            "ruby_treble": 6.5,              # Top Boost Treble
            "ruby_bass": 5.0,                # Top Boost Bass
            "ruby_tone_cut": 5.5,
            "ruby_boost_enable": False,
            "cab_and_mic": 1,
            "prefx_power": False,
            "postfx_power": True,            # Enable post FX for 1176 & Reverb
            "postfx_1_power": True,          # Enable 1176
            "postfx_2_power": False,         # Disable Delay
            "postfx_3_power": True,          # Enable Plate Reverb
            "postfx_plate_reverb_decay": 2.0,
            "postfx_plate_reverb_predelay": 20.0,
            "postfx_plate_reverb_mix": 15.0
        }
    },
    {
        # Ported from standalone Dream '65 Jazz HB
        "source": "tones/humbuckers/dream-65-blackface-jazz.md",
        "preset_name": "Toneprint - Dream 65 Blackface Jazz HB.json",
        "amp_index": 0,        # Dream '65
        "cab_index": 29,       # Dream 1x12 Deluxe Reverb
        "controls": {
            "amp": 0,
            "dream_volume": 3.5,
            "dream_treble": 4.5,
            "dream_bass": 4.0,
            "dream_reverb_enable": True,
            "dream_reverb": 2.5,
            "dream_bright": False,
            "dream_boost_enable": False,
            "cab_and_mic": 29,
            "prefx_power": False,
            "postfx_power": False
        }
    },
    {
        # Ported from standalone Dream '65 Sparkle SC
        "source": "tones/single-coils/dream-65-blackface-sparkle.md",
        "preset_name": "Toneprint - Dream 65 Blackface Sparkle SC.json",
        "amp_index": 0,        # Dream '65
        "cab_index": 29,       # Dream 1x12 Deluxe Reverb
        "controls": {
            "amp": 0,
            "dream_volume": 4.5,
            "dream_treble": 6.5,
            "dream_bass": 5.0,
            "dream_reverb_enable": True,
            "dream_reverb": 3.0,
            "dream_bright": True,
            "dream_boost_enable": False,
            "cab_and_mic": 29,
            "prefx_power": False,
            "postfx_power": False
        }
    },
    {
        # Ported from standalone Ruby '63 Vox Jangle SC
        "source": "tones/single-coils/ruby-63-vox-jangle.md",
        "preset_name": "Toneprint - Ruby 63 Vox Jangle SC.json",
        "amp_index": 3,        # Ruby '63
        "cab_index": 1,        # AC30 2x12 Alnico Blue
        "controls": {
            "amp": 3,
            "ruby_channel": 2,               # Brilliant
            "ruby_volume": 4.5,
            "ruby_treble": 6.0,
            "ruby_bass": 5.0,
            "ruby_tone_cut": 5.0,
            "ruby_boost_enable": False,
            "cab_and_mic": 1,
            "prefx_power": False,
            "postfx_power": False
        }
    },
    {
        # Ported from standalone Ruby '63 LP Velvet Crunch HB
        "source": "tones/humbuckers/ruby-les-paul-velvet-crunch.md",
        "preset_name": "Toneprint - Ruby LP Velvet Crunch HB.json",
        "amp_index": 3,        # Ruby '63
        "cab_index": 1,
        "controls": {
            "amp": 3,
            "ruby_channel": 2,               # Brilliant
            "ruby_volume": 5.5,
            "ruby_treble": 5.0,
            "ruby_bass": 5.5,
            "ruby_tone_cut": 4.5,
            "ruby_boost_enable": True,
            "ruby_boost_amount": 3.0,
            "cab_and_mic": 1,
            "prefx_power": False,
            "postfx_power": False
        }
    },
    {
        # Ported from standalone Woodrow '55 Sweet Spot SC
        "source": "tones/single-coils/woodrow-sweet-spot.md",
        "preset_name": "Toneprint - Woodrow Sweet Spot SC.json",
        "amp_index": 5,        # Woodrow '55 is index 5
        "cab_index": 2,        # 1x12 Tweed
        "controls": {
            "amp": 5,
            "woodrow_inst_volume": 6.5,
            "woodrow_mic_volume": 2.0,
            "woodrow_tone": 6.0,
            "woodrow_boost_enable": False,
            "cab_and_mic": 2,
            "prefx_power": False,
            "postfx_power": False
        }
    },
    {
        # Ported from Woodrow '55 Sweet Spot P-90 Variant
        "source": "tones/p-90s/woodrow-sweet-spot-p90.md",
        "preset_name": "Toneprint - Woodrow Sweet Spot P90.json",
        "amp_index": 5,        # Woodrow '55 is index 5
        "cab_index": 2,        # 1x12 Tweed
        "controls": {
            "amp": 5,
            "woodrow_inst_volume": 3.0,
            "woodrow_mic_volume": 2.5,
            "woodrow_tone": 5.0,
            "woodrow_boost_enable": False,
            "cab_and_mic": 2,
            "prefx_power": False,
            "postfx_power": False
        }
    },
    {
        # Ported from standalone Showtime '64 Jazz Clean Intimate HB
        "source": "tones/humbuckers/jazz-clean-intimate-les-paul.md",
        "preset_name": "Toneprint - Showtime Jazz Clean Intimate HB.json",
        "amp_index": 4,        # Showtime '64
        "cab_index": 29,       # Showtime 2x12
        "controls": {
            "amp": 4,
            "showtime_volume": 3.0,          # Labeled Vol 3 in print
            "showtime_treble": 4.0,
            "showtime_middle": 5.0,
            "showtime_bass": 5.0,
            "showtime_bright": False,
            "cab_and_mic": 29,
            "prefx_power": False,
            "postfx_power": False
        }
    }
]

# Old temporary standalone files to clean up
CLEANUP_FILES = [
    "uaudio_dream_amp/Dream 65 Blackface Jazz HB.json",
    "uaudio_dream_amp/Dream 65 Blackface Sparkle SC.json",
    "uaudio_ruby_amp/Ruby 63 Vox Jangle SC.json",
    "uaudio_ruby_amp/Ruby LP Velvet Crunch HB.json",
    "uaudio_woodrow_amp/Woodrow Sweet Spot SC.json"
]

def main():
    print("--------------------------------------------------")
    print("UNIVERSAL AUDIO (UADx) PARADISE PRESET COMPILER")
    print("--------------------------------------------------")
    
    # 1. Load the Paradise Template
    if not os.path.exists(PARADISE_TEMPLATE):
        print(f"Error: Paradise Guitar Studio DNA template not found at {PARADISE_TEMPLATE}!")
        return
        
    print(f"Using template DNA: {PARADISE_TEMPLATE}")
    with open(PARADISE_TEMPLATE, "r") as f:
        base_preset = json.load(f)
        
    compiled_count = 0
    
    # 2. Compile each preset into Paradise Studio
    for tp in PARADISE_TONEPRINTS:
        source_path = tp["source"]
        preset_name = tp["preset_name"]
        preset_controls = tp["controls"]
        
        # Clean name without .json extension for internal JSON metadata
        clean_preset_name = preset_name.replace(".json", "")
        
        print(f"\nProcessing toneprint: {source_path}...")
        
        if not os.path.exists(source_path):
            print(f"Warning: Toneprint source not found at {source_path}. Skipping.")
            continue
            
        # Clone template JSON
        preset_data = json.loads(json.dumps(base_preset)) # deep copy
        
        # Update metadata to fix preset name and sequential next/prev indexing
        preset_data["name"] = clean_preset_name
        preset_data["uid"] = uuid.uuid4().hex  # Fresh unique ID to fix Logic navigation
        
        # Access controls block
        controls = preset_data["chunk"]["controls"]
        
        # Inject Paradise routing
        controls["amp"] = {"real_value": tp["amp_index"]}
        controls["cab_and_mic"] = {"real_value": tp["cab_index"]}
        
        # Inject specific knob settings
        for key, val in preset_controls.items():
            controls[key] = {"real_value": val}
            
        # Write directly to Paradise presets directory
        os.makedirs(PARADISE_DIR, exist_ok=True)
        output_path = os.path.join(PARADISE_DIR, preset_name)
        
        with open(output_path, "w") as f:
            json.dump(preset_data, f, indent=4)
            
        print(f"-> SUCCESS: Compiled in-container preset '{clean_preset_name}'")
        compiled_count += 1
        
    # 3. Clean up old standalone files
    print("\nCleaning up deprecated standalone presets...")
    cleaned_count = 0
    for path_rel in CLEANUP_FILES:
        full_path = os.path.join(BASE_UAD_PRESETS_DIR, path_rel)
        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"-> Removed: {path_rel}")
            cleaned_count += 1
            
    print("\n--------------------------------------------------")
    print(f"Compilation Complete! Successfully compiled {compiled_count} unified presets.")
    if cleaned_count > 0:
        print(f"Cleaned up {cleaned_count} deprecated standalone files.")
    print(f"Paradise Presets Directory: {PARADISE_DIR}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
