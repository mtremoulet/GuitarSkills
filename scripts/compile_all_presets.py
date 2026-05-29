#!/usr/bin/env python3
import os
import json
import re
import uuid
import xml.etree.ElementTree as ET
import base64
import struct

# Directories & Path Configurations
TONES_DIR = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"

# Neural DSP Paths
NEURAL_TEMPLATE = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/User/Telecaster Tones.xml"
NEURAL_TEMPLATE_ALT = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Default.xml"
NEURAL_OUTPUT_DIR = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints"

# Universal Audio Paths
BASE_UAD_PRESETS_DIR = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins"
PARADISE_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_paradise_guitar_studio")
PARADISE_TEMPLATE = os.path.join(PARADISE_DIR, "Boutique Warm Clean - Enigmatic.json")

LA2A_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_teletronix_la-2a_silver/Mike - Alternative.json")
HITSVILLE_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_hitsville_chambers/Mike Live Strings.json")
GALAXY_BASE = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins/uaudio_galaxy_tape_echo/Galaxy_BaseEchoRate0.json"
STUDIO_D_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_studio_d_chorus/whereami.json")
VALHALLA_BASE = "/Library/Application Support/Valhalla DSP, LLC/ValhallaSupermassive/Presets/User/whereami.vpreset"

# Logic Pro Native Paths
LOGIC_EQ_BASE = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Channel EQ/FlatEQ.pst"
LOGIC_COMP_BASE_ALT = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Compressor/CompThreshNeg35.pst"
LOGIC_COMP_BASE_DEFAULT = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Compressor/DefaultComp.pst"
LOGIC_COMP_BASE = LOGIC_COMP_BASE_ALT if os.path.exists(LOGIC_COMP_BASE_ALT) else LOGIC_COMP_BASE_DEFAULT

# MixWave Paths
MIXWAVE_TEMPLATE = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/User/ToneprintTemplate.xml"
MIXWAVE_TEMPLATE_ALT = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/User/Mike's Two Rocks.xml"
MIXWAVE_TEMPLATE_FACTORY = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/Factory/LUSH CLEAN.xml"
MIXWAVE_OUTPUT_DIR = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/User"

# Yamaha THR-II Paths
YAMAHA_THR_OUTPUT_DIR = "/Users/miketremoulet/claude-projects/GuitarSkills/tones/presets/yamaha"

# Nembrini Audio XML Presets Paths
NEMBRINI_DOCS_DIR = "/Users/miketremoulet/Documents/Nembrini Audio"
NEMBRINI_TEMPLATES = {
    "mrh810": os.path.join(NEMBRINI_DOCS_DIR, "NA Mrh810 V2/MRH810-All5.xml"),
    "jc120": os.path.join(NEMBRINI_DOCS_DIR, "NA Jazz Chorus/JC_Base.xml"),
    "div11": os.path.join(NEMBRINI_DOCS_DIR, "NA Divided 11/Div11-All5.xml"),
    "acoustic_voice": os.path.join(NEMBRINI_DOCS_DIR, "NA Acoustic Voice Pro/AVP_Base.xml"),
    "puretone": os.path.join(NEMBRINI_DOCS_DIR, "HK Puretone/HK_Base.xml")
}

DEFAULT_THR_PRESET = {
    "schema": "L6Preset",
    "version": 5,
    "data": {
        "device": 48,
        "device_version": 65536,
        "meta": {
            "name": "Default Name",
            "tnid": 0
        },
        "tone": {
            "THRGroupAmp": {
                "@asset": "thr_clean",
                "Bass": 0.5,
                "Drive": 0.3,
                "Master": 0.5,
                "Mid": 0.5,
                "Treble": 0.5
            },
            "THRGroupCab": {
                "@asset": "thr_cab_2x12",
                "SpkSimType": "Default"
            },
            "THRGroupFX1Compressor": {
                "@asset": "thr_compressor",
                "@enabled": False,
                "Level": 0.5,
                "Sustain": 0.5
            },
            "THRGroupFX2Effect": {
                "@asset": "thr_chorus",
                "@enabled": False,
                "@wetDry": 0.5,
                "Depth": 0.5,
                "Feedback": 0.0,
                "Freq": 0.3,
                "Pre": 0.0
            },
            "THRGroupFX3EffectEcho": {
                "@asset": "thr_tape_echo",
                "@enabled": False,
                "@wetDry": 0.3,
                "Bass": 0.5,
                "Feedback": 0.3,
                "Time": 0.4,
                "Treble": 0.5
            },
            "THRGroupFX4EffectReverb": {
                "@asset": "thr_hall_reverb",
                "@enabled": False,
                "@wetDry": 0.3,
                "Decay": 0.5,
                "PreDelay": 0.1,
                "Tone": 0.5
            },
            "THRGroupGate": {
                "@asset": "thr_noise_gate",
                "@enabled": False,
                "Decay": 0.5,
                "Thresh": 0.1
            },
            "global": {
                "THRPresetParamTempo": 120.0
            }
        }
    }
}

# Custom Binary Parameter Replacer for Neural DSP (TLV format)
def replace_binary_parameter(data, param_name, new_val_str):
    search_bytes = param_name.encode("utf-8") + b"\x00\x01"
    idx = data.find(search_bytes)
    if idx == -1:
        return data
    
    length_byte_idx = idx + len(search_bytes)
    old_length = data[length_byte_idx]
    
    replace_start = length_byte_idx
    replace_end = length_byte_idx + 1 + old_length
    
    new_val_bytes = new_val_str.encode("utf-8")
    new_length = len(new_val_bytes) + 2
    new_block = bytes([new_length, 0x05]) + new_val_bytes + b"\x00"
    
    return data[:replace_start] + new_block + data[replace_end:]

# Robust Standard Library YAML Frontmatter Parser (Recursive)
def parse_yaml_frontmatter(content):
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    body = content[match.end():]
    
    # Simple line parser
    lines = yaml_text.splitlines()
    parsed_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            
            # Type casting
            if val == "":
                val = None
            elif val.lower() == "true":
                val = True
            elif val.lower() == "false":
                val = False
            else:
                try:
                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
            parsed_lines.append((indent, key, val))
            
    # Build tree from parsed_lines
    def build_tree(start_idx, parent_indent):
        result = {}
        idx = start_idx
        while idx < len(parsed_lines):
            indent, key, val = parsed_lines[idx]
            if indent <= parent_indent:
                break
            
            next_idx = idx + 1
            has_children = False
            if next_idx < len(parsed_lines):
                next_indent, _, _ = parsed_lines[next_idx]
                if next_indent > indent:
                    has_children = True
            
            if has_children:
                child_dict, next_idx = build_tree(next_idx, indent)
                result[key] = child_dict
                idx = next_idx
            else:
                result[key] = val
                idx += 1
        return result, idx

    tree, _ = build_tree(0, -1)
    return tree, body

# Robust Markdown Parameter Extractor
def find_numeric_parameter(content, param_names):
    for name in param_names:
        # Match standard decimals like 5.5, 3.0, -1.5, −1.5 (with Unicode minus)
        # Put the hyphen at the end of the character class to prevent range interpretation
        pattern = r"\|\s*" + re.escape(name) + r"\s*\|\s*(?:\*\*)?([~0-9.+−-]+)(?:\*\*)?(?:\s*%)?\s*\|"
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            val_str = match.group(1).replace("−", "-").replace("~", "").strip()
            try:
                val = float(val_str)
                # Check if this line contains a % symbol (percentages are scaled to 0.0 - 1.0)
                full_line = content[max(0, match.start()-10) : min(len(content), match.end()+25)]
                if "%" in full_line:
                    return val / 100.0
                return val
            except ValueError:
                pass
    return None

def find_boolean_parameter(content, param_names):
    for name in param_names:
        pattern = r"\|\s*" + re.escape(name) + r"\s*\|\s*(?:\*\*)?([A-Za-z/ ]+)(?:\*\*)?\s*\|"
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            val = match.group(1).strip().upper()
            if val in ["ON", "ACTIVE", "BRIGHT", "YES", "TRUE"]:
                return True
            if val in ["OFF", "NORMAL", "BYPASSED", "NO", "FALSE"]:
                return False
    return None

# Dynamic Neural DSP Parser & Compiler
def compile_neural_toneprint(filepath, base_data, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    amp_settings = preset_data.get("amp_settings") if isinstance(preset_data, dict) else None

    settings = {}
    settings["name"] = output_name

    if amp_settings and isinstance(amp_settings, dict):
        for k, v in amp_settings.items():
            if isinstance(v, bool):
                settings[k] = "true" if v else "false"
            else:
                settings[k] = str(v)
    else:
        with open(filepath, "r") as f:
            content = f.read()

        # 1. Parse Compressor (The 4th Position Compressor)
        comp_active = find_boolean_parameter(content, ["The 4th Position Compressor", "Compressor Active", "Compressor"])
        if comp_active is not None:
            settings["compressorActive"] = "true" if comp_active else "false"
            
        for key in ["Blend", "Tone", "Compression", "Volume"]:
            val = find_numeric_parameter(content, [key])
            if val is not None:
                settings["compressor" + key] = f"{val:.2f}"

        # 2. Parse Amp Knobs (The Amp Snob / Amp 3)
        settings["selectedAmp"] = "2"  # Amp 3 (index 2)
        settings["selectedCab"] = "2"  # Snob 2x12 Cab (index 2)
        settings["ampCabLinkedState"] = "false"
        
        knobs = {
            "snobBass": ["Bass"],
            "snobMid": ["Middle", "Mids"],
            "snobTreble": ["Treble"],
            "snobPresence": ["Presence"],
            "snobMaster": ["Master"],
            "snobVolume": ["Volume (Gain)", "Volume"],
            "snobOutputLevel": ["Output"]
        }
        
        for param, names in knobs.items():
            val = find_numeric_parameter(content, names)
            if val is not None:
                settings[param] = f"{val:.2f}"
                
        drive = find_boolean_parameter(content, ["Drive Switch", "Drive"])
        if drive is not None:
            settings["snobDrive"] = "true" if drive else "false"
            
        bright = find_boolean_parameter(content, ["Bright Switch", "Bright"])
        if bright is not None:
            settings["snobBright"] = "true" if bright else "false"

        # 3. Parse Cabinet settings
        pos = find_numeric_parameter(content, ["Position L", "Position"])
        if pos is not None: settings["leftCabPosition"] = f"{pos:.2f}"
        
        dist = find_numeric_parameter(content, ["Distance L", "Distance"])
        if dist is not None: settings["leftCabDistance"] = f"{dist:.2f}"
        
        room = find_numeric_parameter(content, ["Room Send L", "Room Send"])
        if room is not None: settings["leftRoomMicLevel"] = f"{room:.1f}"

        settings["leftCabActive"] = "true"
        settings["leftCab0MicType"] = "4"   # Ribbon 121
        settings["rightCabActive"] = "false" # Bypassed

        # 4. Parse EQ Bands (1 to 9)
        eq_active = find_boolean_parameter(content, ["EQ Status", "EQ Active", "snobEQActive"])
        if eq_active is not None:
            settings["snobEQActive"] = "true" if eq_active else "false"
            
        bands = ["65 Hz", "125 Hz", "250 Hz", "500 Hz", "1 kHz", "2 kHz", "4 kHz", "8 kHz", "16 kHz"]
        for i, band in enumerate(bands, 1):
            val = find_numeric_parameter(content, [band])
            if val is not None:
                settings[f"snobEQBand{i}"] = f"{val:.1f}"

        settings["snobEQHpf"] = "20.0"
        settings["snobEQLpf"] = "20000.0"

        # 5. Default bypassed pedals
        for pedal in ["tuberActive", "bigRigActive", "postalActive", "delayActive", "washActive", "chorusActive"]:
            settings[pedal] = "false"

    # Inject overrides from frontmatter (supporting custom studio FX/cabs/etc.)
    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            if isinstance(v, bool):
                settings[k] = "true" if v else "false"
            else:
                settings[k] = str(v)

    # Inject into binary preset
    preset_data_bytes = base_data
    for key, val in settings.items():
        preset_data_bytes = replace_binary_parameter(preset_data_bytes, key, val)
        
    # Save preset
    os.makedirs(NEURAL_OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(NEURAL_OUTPUT_DIR, f"{output_name}.xml")
    with open(out_path, "wb") as f:
        f.write(preset_data_bytes)
    print(f"-> Compiled Neural Preset: '{output_name}'")
    return True

# Dynamic UADx Parser & Compiler
def compile_uad_toneprint(filepath, base_preset, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    amp_settings = preset_data.get("amp_settings") if isinstance(preset_data, dict) else None
        
    amp_str = frontmatter.get("amp", "")
    
    # Identify target amp type and indexes
    amp_type = None
    amp_index = None
    cab_index = 2 # default open back Boutique D65
    
    if "Dream" in amp_str:
        amp_type = "dream"
        amp_index = 0
        cab_index = 29
    elif "Enigmatic" in amp_str:
        amp_type = "enigmatic"
        amp_index = 1
        cab_index = 2
    elif "Woodrow" in amp_str:
        amp_type = "woodrow"
        amp_index = 5
        cab_index = 2
    elif "Ruby" in amp_str:
        amp_type = "ruby"
        amp_index = 3
        cab_index = 1
    elif "Showtime" in amp_str:
        amp_type = "showtime"
        amp_index = 4
        cab_index = 29
    elif "Lion" in amp_str:
        amp_type = "lion"
        amp_index = 2
        cab_index = 2
        
    if amp_type is None: return

    if amp_settings and isinstance(amp_settings, dict):
        vol = amp_settings.get("Volume")
        vol_mic = amp_settings.get("Volume (Mic)")
        treble = amp_settings.get("Treble")
        mid = amp_settings.get("Middle")
        bass = amp_settings.get("Bass")
        presence = amp_settings.get("Presence")
        master = amp_settings.get("Master")
        tone_cut = amp_settings.get("Tone Cut")
        bright = amp_settings.get("Bright")
        boost = amp_settings.get("Boost")
        cut_sw = amp_settings.get("Cut")
        
        # normalize types
        if vol is not None: vol = float(vol)
        if vol_mic is not None: vol_mic = float(vol_mic)
        if treble is not None: treble = float(treble)
        if mid is not None: mid = float(mid)
        if bass is not None: bass = float(bass)
        if presence is not None: presence = float(presence)
        if master is not None: master = float(master)
        if tone_cut is not None: tone_cut = float(tone_cut)
        if bright is not None: bright = bool(bright)
        if boost is not None: boost = bool(boost)
        if cut_sw is not None: cut_sw = bool(cut_sw)
    else:
        with open(filepath, "r") as f:
            content = f.read()
        vol = find_numeric_parameter(content, ["Volume (Gain)", "Volume", "Volume (Inst)", "inst_volume"])
        vol_mic = find_numeric_parameter(content, ["Volume (Mic)", "mic_volume"])
        treble = find_numeric_parameter(content, ["Treble", "Top Boost Treble", "Tone"])
        mid = find_numeric_parameter(content, ["Middle", "Mids", "Top Boost Mids"])
        bass = find_numeric_parameter(content, ["Bass", "Top Boost Bass"])
        presence = find_numeric_parameter(content, ["Presence"])
        master = find_numeric_parameter(content, ["Master (labeled 6.5)", "Master", "Master volume"])
        tone_cut = find_numeric_parameter(content, ["Tone Cut"])
        bright = find_boolean_parameter(content, ["Bright Switch", "Bright / Normal", "Bright"])
        boost = find_boolean_parameter(content, ["Boost Button", "Boost Switch", "Boost (Stock)", "Boost"])
        cut_sw = find_boolean_parameter(content, ["Cut Switch", "Cut"])

    # Map settings into Paradise Guitar Studio JSON
    preset_data_json = json.loads(json.dumps(base_preset)) # deep copy
    preset_data_json["name"] = f"Toneprint - {output_name}"
    preset_data_json["uid"] = uuid.uuid4().hex
    
    controls = preset_data_json["chunk"]["controls"]
    
    # Inject amp and cabinet selection
    controls["amp"] = {"real_value": amp_index}
    controls["cab_and_mic"] = {"real_value": cab_index}
    
    # Inject mapped parameters
    if amp_type == "dream":
        if vol is not None: controls["dream_volume"] = {"real_value": vol}
        if treble is not None: controls["dream_treble"] = {"real_value": treble}
        if bass is not None: controls["dream_bass"] = {"real_value": bass}
        if bright is not None: controls["dream_bright"] = {"real_value": bright}
        if boost is not None: controls["dream_boost_enable"] = {"real_value": boost}
        controls["dream_reverb_enable"] = {"real_value": True}
        controls["dream_reverb"] = {"real_value": 2.5}
    elif amp_type == "enigmatic":
        if vol is not None: controls["enigmatic_volume"] = {"real_value": vol}
        if treble is not None: controls["enigmatic_treble"] = {"real_value": treble}
        if mid is not None: controls["enigmatic_middle"] = {"real_value": mid}
        if bass is not None: controls["enigmatic_bass"] = {"real_value": bass}
        if presence is not None: controls["enigmatic_presence"] = {"real_value": presence}
        if master is not None: controls["enigmatic_master_gain"] = {"real_value": master}
        if bright is not None: controls["enigmatic_bright_enable"] = {"real_value": bright}
        if boost is not None: controls["enigmatic_boost_enable"] = {"real_value": boost}
        controls["enigmatic_model"] = {"real_value": 0}            # Suede
        controls["enigmatic_channel"] = {"real_value": 1}          # NOR
        controls["enigmatic_tone_stack_type"] = {"real_value": 0}  # Skyline
        controls["enigmatic_tone_stack_eq"] = {"real_value": 0}    # Jazz
        controls["enigmatic_overdrive_enable"] = {"real_value": False}
    elif amp_type == "ruby":
        if vol is not None: controls["ruby_volume"] = {"real_value": vol}
        if treble is not None: controls["ruby_treble"] = {"real_value": treble}
        if bass is not None: controls["ruby_bass"] = {"real_value": bass}
        if tone_cut is not None: controls["ruby_tone_cut"] = {"real_value": tone_cut}
        if boost is not None: controls["ruby_boost_enable"] = {"real_value": boost}
        controls["ruby_channel"] = {"real_value": 2} # Brilliant
        controls["ruby_cut"] = {"real_value": 5.0 if cut_sw else 0.0}
    elif amp_type == "woodrow":
        if vol is not None: controls["woodrow_inst_volume"] = {"real_value": vol}
        if vol_mic is not None: controls["woodrow_mic_volume"] = {"real_value": vol_mic}
        if treble is not None: controls["woodrow_tone"] = {"real_value": treble}
        if boost is not None: controls["woodrow_boost_enable"] = {"real_value": boost}
    elif amp_type == "showtime":
        if vol is not None: controls["showtime_volume"] = {"real_value": vol}
        if treble is not None: controls["showtime_treble"] = {"real_value": treble}
        if mid is not None: controls["showtime_middle"] = {"real_value": mid}
        if bass is not None: controls["showtime_bass"] = {"real_value": bass}
        if bright is not None: controls["showtime_bright"] = {"real_value": bright}

    # Bypassed post-amp effects for clean platform comparison (defaults)
    controls["prefx_power"] = {"real_value": False}
    controls["postfx_power"] = {"real_value": False}

    # Inject overrides from frontmatter (supporting 1176, delays, plate reverbs, etc.)
    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            controls[k] = {"real_value": v}

    # Write output JSON preset file
    os.makedirs(PARADISE_DIR, exist_ok=True)
    out_path = os.path.join(PARADISE_DIR, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data_json, f, indent=4)
        
    print(f"-> Compiled UAD Paradise Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic MixWave Two-Rock Bloomfield Drive XML Parser & Compiler
def compile_mixwave_toneprint(filepath, base_xml_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    amp_settings = preset_data.get("amp_settings") if isinstance(preset_data, dict) else None

    # Parse XML Template using Standard ElementTree
    tree = ET.parse(base_xml_path)
    root = tree.getroot()

    # Find the variables blocks
    global_vars = root.find("Variables")
    amp_module = root.find(".//Module[@moduleName='Amp']")
    amp_vars = amp_module.find("Variables") if amp_module is not None else None
    cab_module = root.find(".//Module[@moduleName='Cab']")
    cab_vars = cab_module.find("Variables") if cab_module is not None else None
    od_module = root.find(".//Module[@moduleName='Overdrive']")
    od_vars = od_module.find("Variables") if od_module is not None else None

    if amp_settings and isinstance(amp_settings, dict):
        gain = amp_settings.get("Gain")
        treble = amp_settings.get("Treble")
        mid = amp_settings.get("Middle")
        bass = amp_settings.get("Bass")
        presence = amp_settings.get("Presence")
        master = amp_settings.get("Master")
        reverb = amp_settings.get("Reverb")
        vibe = amp_settings.get("Vibe")
        bright = amp_settings.get("Bright")
        mid_sw = amp_settings.get("Mid")
        deep = amp_settings.get("Deep")
        bypass_sw = amp_settings.get("Tone Stack Bypass")
        lead_sw = amp_settings.get("Lead")
        gate_val = amp_settings.get("Noise Gate")
        input_trim = amp_settings.get("Input Trim")
        output_trim = amp_settings.get("Output Trim")
        
        # normalize types
        if gain is not None: gain = float(gain)
        if treble is not None: treble = float(treble)
        if mid is not None: mid = float(mid)
        if bass is not None: bass = float(bass)
        if presence is not None: presence = float(presence)
        if master is not None: master = float(master)
        if reverb is not None: reverb = float(reverb)
        if vibe is not None: vibe = float(vibe)
        if bright is not None: bright = bool(bright)
        if mid_sw is not None: mid_sw = bool(mid_sw)
        if deep is not None: deep = bool(deep)
        if bypass_sw is not None: bypass_sw = bool(bypass_sw)
        if lead_sw is not None: lead_sw = bool(lead_sw)
        if gate_val is not None: gate_val = float(gate_val)
        if input_trim is not None: input_trim = float(input_trim)
        if output_trim is not None: output_trim = float(output_trim)
    else:
        with open(filepath, "r") as f:
            content = f.read()
        gain = find_numeric_parameter(content, ["Gain"])
        treble = find_numeric_parameter(content, ["Treble"])
        mid = find_numeric_parameter(content, ["Middle", "Mids"])
        bass = find_numeric_parameter(content, ["Bass"])
        presence = find_numeric_parameter(content, ["Presence"])
        master = find_numeric_parameter(content, ["Master"])
        reverb = find_numeric_parameter(content, ["Reverb"])
        vibe = find_numeric_parameter(content, ["Vibe"])
        bright = find_boolean_parameter(content, ["Bright Switch", "Bright"])
        mid_sw = find_boolean_parameter(content, ["Mid Switch", "Mid"])
        deep = find_boolean_parameter(content, ["Deep Switch", "Deep"])
        bypass_sw = find_boolean_parameter(content, ["Tone Stack Bypass"])
        lead_sw = find_boolean_parameter(content, ["Lead Switch", "Lead"])
        gate_val = find_numeric_parameter(content, ["Noise Gate", "Gate Threshold"])
        input_trim = find_numeric_parameter(content, ["Input Trim"])
        output_trim = find_numeric_parameter(content, ["Output Trim"])

    # Map settings to Amp Variables XML attributes
    if amp_vars is not None:
        if gain is not None: amp_vars.set("AmpGain", f"{gain:.3f}")
        if treble is not None: amp_vars.set("AmpTreble", f"{treble:.3f}")
        if mid is not None: amp_vars.set("AmpMiddle", f"{mid:.3f}")
        if bass is not None: amp_vars.set("AmpBass", f"{bass:.3f}")
        if presence is not None: amp_vars.set("AmpPresence", f"{presence:.3f}")
        if master is not None: amp_vars.set("AmpMaster", f"{master:.3f}")
        if reverb is not None: amp_vars.set("AmpReverb", f"{reverb:.3f}")
        
        # Switches: MixWave uses "1" for On, "0" for Off
        if bright is not None: amp_vars.set("AmpBrightOnOff", "1" if bright else "0")
        if mid_sw is not None: amp_vars.set("AmpMidOnOff", "1" if mid_sw else "0")
        if deep is not None: amp_vars.set("AmpDeepOnOff", "1" if deep else "0")
        if bypass_sw is not None: amp_vars.set("AmpToneBypassOnOff", "1" if bypass_sw else "0")
        if lead_sw is not None: amp_vars.set("AmpType", "2" if lead_sw else "1")

    # Map Vibe to Cab 1 Vibe in the cabinet section
    if cab_vars is not None and vibe is not None:
        cab_vars.set("Cab1Vibe", f"{vibe:.3f}")

    # Global Variables
    if global_vars is not None:
        if gate_val is not None:
            global_vars.set("GateOnOff", "1")
            global_vars.set("GateThreshold", f"{gate_val:.3f}")
        if input_trim is not None:
            global_vars.set("InputLevel", f"{input_trim:.3f}")
        if output_trim is not None:
            global_vars.set("OutputLevel", f"{output_trim:.3f}")

    # Inject overrides from frontmatter (pedals, custom mic placements, etc.)
    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            val_str = "1" if isinstance(v, bool) and v else ("0" if isinstance(v, bool) else str(v))
            if k.startswith("Overdrive") and od_vars is not None:
                od_vars.set(k, val_str)
            elif k.startswith("Amp") and amp_vars is not None:
                amp_vars.set(k, val_str)
            elif k.startswith("Cab") and cab_vars is not None:
                cab_vars.set(k, val_str)
            elif global_vars is not None:
                global_vars.set(k, val_str)

    # Save XML preset directly in the user-level folder
    os.makedirs(MIXWAVE_OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(MIXWAVE_OUTPUT_DIR, f"{output_name}.xml")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"-> Compiled MixWave Preset: '{output_name}'")
    return True

# Robust parameter extractor for Compressor that falls back to cell regex if find_numeric_parameter fails
def extract_comp_param(content, keywords):
    val = find_numeric_parameter(content, keywords)
    if val is not None:
        return val
        
    for line in content.split("\n"):
        line_lower = line.lower()
        if any(kw.lower() in line_lower for kw in keywords):
            parts = [p.strip() for p in line.split("|")]
            text_to_search = parts[2] if len(parts) >= 3 else line
            match = re.search(r"([+-]?\d+(?:\.\d+)?)\s*(?:db|ms|:1)?\b", text_to_search.replace("−", "-"), re.IGNORECASE)
            if match:
                return float(match.group(1))
    return None

def extract_freq(text):
    freq_match = re.search(r"(\d+(?:\.\d+)?)\s*(k?Hz)\b", text, re.IGNORECASE)
    if freq_match:
        val = float(freq_match.group(1))
        unit = freq_match.group(2).lower()
        if unit == "khz" or (val < 22.0 and unit == "hz"):
            val *= 1000.0
        return val
    return None

def extract_slope(text):
    slope_match = re.search(r"(\d+)\s*db", text, re.IGNORECASE)
    if slope_match:
        db_val = int(slope_match.group(1))
        mapping = {6: 1.0, 12: 2.0, 18: 3.0, 24: 4.0, 30: 5.0, 36: 6.0, 48: 7.0}
        if db_val in mapping:
            return mapping[db_val]
        return float(db_val // 6)
    return None

def parse_eq_bands(content):
    bands = {i: {"on": None, "freq": None, "gain_or_slope": None, "q": None} for i in range(1, 9)}
    in_eq_section = False
    
    for line in content.split("\n"):
        line_lower = line.lower()
        
        if line.strip().startswith("#"):
            if "channel eq" in line_lower or "surgical shaping" in line_lower:
                in_eq_section = True
                continue
            else:
                in_eq_section = False
                continue
            
        if not in_eq_section:
            continue
            
        if "|" not in line:
            if "high-pass" in line_lower or "hpf" in line_lower or "low cut" in line_lower:
                freq = extract_freq(line)
                slope = extract_slope(line)
                if freq is not None:
                    bands[1]["on"] = 1.0
                    bands[1]["freq"] = freq
                if slope is not None:
                    bands[1]["gain_or_slope"] = slope
            elif "low-pass" in line_lower or "lpf" in line_lower or "high cut" in line_lower or "high-cut" in line_lower:
                freq = extract_freq(line)
                slope = extract_slope(line)
                if freq is not None:
                    bands[8]["on"] = 1.0
                    bands[8]["freq"] = freq
                if slope is not None:
                    bands[8]["gain_or_slope"] = slope
            continue
            
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            continue
            
        first_col = parts[1].lower()
        band_num = None
        if "band 1" in first_col or "low cut" in first_col or "hpf" in first_col or "high-pass" in first_col:
            band_num = 1
        elif "band 2" in first_col or "low shelf" in first_col:
            band_num = 2
        elif "band 3" in first_col or "peak 1" in first_col:
            band_num = 3
        elif "band 4" in first_col or "peak 2" in first_col or ("peak" in first_col and "250 hz" in line_lower):
            band_num = 4
        elif "band 5" in first_col or "peak 3" in first_col:
            band_num = 5
        elif "band 6" in first_col or "peak 4" in first_col:
            band_num = 6
        elif "band 7" in first_col or "high shelf" in first_col:
            band_num = 7
        elif "band 8" in first_col or "high cut" in first_col or "lpf" in first_col or "low-pass" in first_col or "high-cut" in first_col:
            band_num = 8
        elif "peak" in first_col:
            band_num = 3
            
        if band_num is None:
            continue
            
        col_text = " ".join(parts[2:])
        freq = extract_freq(col_text)
        gain_or_slope = None
        q = None
        
        if band_num in [1, 8]:
            gain_or_slope = extract_slope(col_text)
        else:
            gain_match = re.search(r"([+-]?\d+(?:\.\d+)?)\s*db\b", col_text.replace("−", "-"), re.IGNORECASE)
            if gain_match:
                gain_or_slope = float(gain_match.group(1))
                
        q_match = re.search(r"\bq(?:-factor)?(?:\s*:\s*|\s+)(\d+(?:\.\d+)?)\b", col_text, re.IGNORECASE)
        if q_match:
            q = float(q_match.group(1))
            
        bands[band_num]["on"] = 1.0
        if freq is not None:
            bands[band_num]["freq"] = freq
        if gain_or_slope is not None:
            bands[band_num]["gain_or_slope"] = gain_or_slope
        if q is not None:
            bands[band_num]["q"] = q
            
    return bands

# Dynamic UADx Teletronix LA-2A JSON Compiler (Silver / Gray)
def compile_la2a_toneprint(filepath, base_preset_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    la2a_data = preset_data.get("la2a") if isinstance(preset_data, dict) else None

    if la2a_data and isinstance(la2a_data, dict):
        peak_reduction = la2a_data.get("peak_reduction")
        gain = la2a_data.get("gain")
        mode_compress = la2a_data.get("compress")
        
        # normalize types
        if peak_reduction is not None: peak_reduction = float(peak_reduction)
        if gain is not None: gain = float(gain)
        if mode_compress is not None: mode_compress = bool(mode_compress)
    else:
        with open(filepath, "r") as f:
            content = f.read()
        # Extract Peak Reduction and Gain
        peak_reduction = find_numeric_parameter(content, ["Peak Reduction"])
        gain = find_numeric_parameter(content, ["Gain", "Makeup Gain"])
        mode_compress = find_boolean_parameter(content, ["Compress Mode", "Compress"]) # True = Compress, False = Limit
    
    # If not found in tables, check overrides or skip
    if peak_reduction is None and gain is None:
        return False

    # Load base template JSON
    with open(base_preset_path, "r") as f:
        preset_data = json.load(f)

    # Decode chunk
    chunk_bytes = bytearray(base64.b64decode(preset_data["chunk"]))
    
    # Surgically patch floats
    # Float 10: Gain (0.0 to 1.0)
    if gain is not None:
        val_scaled = gain / 100.0 if gain > 1.0 else gain
        struct.pack_into("f", chunk_bytes, 10 * 4, val_scaled)
    # Float 11: Peak Reduction (0.0 to 1.0)
    if peak_reduction is not None:
        val_scaled = peak_reduction / 100.0 if peak_reduction > 1.0 else peak_reduction
        struct.pack_into("f", chunk_bytes, 11 * 4, val_scaled)
    # Float 13: Mode (1.0 = Compress, 0.0 = Limit)
    if mode_compress is not None:
        struct.pack_into("f", chunk_bytes, 13 * 4, 1.0 if mode_compress else 0.0)

    # Re-encode chunk
    preset_data["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data["name"] = f"Toneprint - {output_name}"
    preset_data["uid"] = uuid.uuid4().hex

    # Write output
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data, f, indent=4)
        
    print(f"-> Compiled UADx LA-2A Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic UADx Hitsville Reverb Chambers JSON Compiler
def compile_hitsville_toneprint(filepath, base_preset_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    hitsville_data = preset_data.get("hitsville") if isinstance(preset_data, dict) else None

    if hitsville_data and isinstance(hitsville_data, dict):
        mix = hitsville_data.get("mix")
        pre_delay = hitsville_data.get("pre_delay")
        decay = hitsville_data.get("decay")
        
        # normalize
        if mix is not None: mix = float(mix)
        if pre_delay is not None: pre_delay = float(pre_delay)
        if decay is not None: decay = float(decay)
    else:
        with open(filepath, "r") as f:
            content = f.read()
        mix = find_numeric_parameter(content, ["Mix", "Room Mix"])
        pre_delay = find_numeric_parameter(content, ["Pre-Delay"])
        decay = find_numeric_parameter(content, ["Decay"])

    if mix is None and pre_delay is None and decay is None:
        return False

    # Load base template JSON
    with open(base_preset_path, "r") as f:
        preset_data = json.load(f)

    # Decode chunk
    chunk_bytes = bytearray(base64.b64decode(preset_data["chunk"]))

    # Float 21: Mix (0.0 to 1.0)
    if mix is not None:
        val_scaled = mix / 100.0 if mix > 1.0 else mix
        struct.pack_into("f", chunk_bytes, 21 * 4, val_scaled)
    # Float 12: Pre-Delay (ms scaled to 0.0-1.0, e.g. 8ms -> 0.08)
    if pre_delay is not None:
        val_scaled = pre_delay / 100.0
        struct.pack_into("f", chunk_bytes, 12 * 4, val_scaled)

    preset_data["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data["name"] = f"Toneprint - {output_name}"
    preset_data["uid"] = uuid.uuid4().hex

    # Write output
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data, f, indent=4)

    print(f"-> Compiled UADx Hitsville Reverb Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic UADx Galaxy Tape Echo JSON Preset Compiler
def compile_galaxy_toneprint(filepath, base_preset_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    galaxy_data = preset_data.get("galaxy") if isinstance(preset_data, dict) else None

    if galaxy_data and isinstance(galaxy_data, dict):
        echo_rate = galaxy_data.get("echo_rate")
        feedback = galaxy_data.get("feedback")
        echo_volume = galaxy_data.get("echo_volume")
        reverb_volume = galaxy_data.get("reverb_volume")
        head_select = galaxy_data.get("head_select")
        tape_age = galaxy_data.get("tape_age")
        
        # normalize types
        if echo_rate is not None: echo_rate = float(echo_rate)
        if feedback is not None: feedback = float(feedback)
        if echo_volume is not None: echo_volume = float(echo_volume)
        if reverb_volume is not None: reverb_volume = float(reverb_volume)
        if head_select is not None: head_select = str(head_select)
        if tape_age is not None: tape_age = str(tape_age)
    else:
        with open(filepath, "r") as f:
            full_content = f.read()
            
        # Isolate to Galaxy section to prevent parameter collision
        content = extract_markdown_section(full_content, ["Galaxy Tape Echo", "Galaxy Echo", "Galaxy"])
        
        echo_rate = find_numeric_parameter(content, ["Echo Rate", "Rate"])
        feedback = find_numeric_parameter(content, ["Feedback"])
        echo_volume = find_numeric_parameter(content, ["Echo Volume", "Volume (Echo)", "Echo Vol"])
        reverb_volume = find_numeric_parameter(content, ["Reverb Volume", "Reverb Vol"])
        
        # Head Select can be integer or string; prioritize string cell first
        hs_match = re.search(r"\|\s*Head Select\s*\|\s*(?:\*\*)?([^|]+?)(?:\*\*)?\s*\|", content, re.IGNORECASE)
        if hs_match:
            head_select = hs_match.group(1).strip()
        else:
            head_select_raw = find_numeric_parameter(content, ["Head Select", "Head"])
            head_select = str(int(head_select_raw)) if head_select_raw is not None else None
            
        ta_match = re.search(r"\|\s*Tape Age\s*\|\s*(?:\*\%)?([A-Za-z]+)(?:\*\%)?\s*\|", content, re.IGNORECASE)
        tape_age = ta_match.group(1).strip() if ta_match else None

    # If all critical controls are None, skip
    if echo_rate is None and feedback is None and echo_volume is None:
        return False

    # Load base template JSON preset
    try:
        with open(base_preset_path, "r") as f:
            preset_data_json = json.load(f)
    except Exception as e:
        print(f"Error: Failed to parse Galaxy base preset JSON template: {e}")
        return False

    # Decode chunk
    chunk_bytes = bytearray(base64.b64decode(preset_data_json["chunk"]))
    
    # 1. Echo Rate: Float Index 19 (Offset 76)
    if echo_rate is not None:
        val_scaled = echo_rate / 10.0 if echo_rate > 1.0 else echo_rate
        struct.pack_into("f", chunk_bytes, 19 * 4, val_scaled)
        
    # 2. Reverb Volume: Float Index 20 (Offset 80)
    if reverb_volume is not None:
        val_scaled = reverb_volume / 10.0 if reverb_volume > 1.0 else reverb_volume
        struct.pack_into("f", chunk_bytes, 20 * 4, val_scaled)
        
    # 3. Feedback: Float Index 21 (Offset 84)
    if feedback is not None:
        val_scaled = feedback / 10.0 if feedback > 1.0 else feedback
        struct.pack_into("f", chunk_bytes, 21 * 4, val_scaled)
        
    # 4. Echo Volume: Float Index 22 (Offset 88)
    if echo_volume is not None:
        val_scaled = echo_volume / 10.0 if echo_volume > 1.0 else echo_volume
        struct.pack_into("f", chunk_bytes, 22 * 4, val_scaled)
        
    # 5. Tape Age: Float Index 23 (Offset 92) (New=0.0, Used=0.5, Old=1.0)
    if tape_age is not None:
        ta_lower = tape_age.lower()
        if "new" in ta_lower:
            val = 0.0
        elif "used" in ta_lower:
            val = 0.5
        elif "old" in ta_lower:
            val = 1.0
        else:
            try:
                val = float(tape_age)
            except ValueError:
                val = 0.0
        struct.pack_into("f", chunk_bytes, 23 * 4, val)
        
    # 6. Head Select: Float Index 14 (Offset 56)
    if head_select is not None:
        hs_val = 0.0 # Default to Repeat 1
        try:
            hs_str = str(head_select).lower()
            if "1+2+3" in hs_str or "1,2,3" in hs_str or "all" in hs_str:
                hs_val = 10.0 / 11.0 # Reverb+Repeat 7 (Heads 1+2+3)
            elif "1+3" in hs_str or "1,3" in hs_str:
                hs_val = 9.0 / 11.0 # Reverb+Repeat 6 (Heads 1+3)
            elif "reverb only" in hs_str or "only reverb" in hs_str:
                hs_val = 1.0 # Reverb Only
            else:
                clean_hs = "".join(c for c in hs_str if c.isdigit() or c == ".")
                if clean_hs:
                    hs_num = int(float(clean_hs))
                    if 1 <= hs_num <= 12:
                        hs_val = (hs_num - 1) / 11.0
        except ValueError:
            pass
        struct.pack_into("f", chunk_bytes, 14 * 4, hs_val)

    # Re-encode chunk
    preset_data_json["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data_json["name"] = f"Toneprint - {output_name}"
    preset_data_json["uid"] = uuid.uuid4().hex

    # Output directory: standard documents plugin presets folder for UADx
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    
    try:
        with open(out_path, "w") as f:
            json.dump(preset_data_json, f, indent=4)
        print(f"-> Compiled UADx Galaxy Tape Echo Preset: 'Toneprint - {output_name}'")
        return True
    except Exception as e:
        print(f"Error: Failed to write Galaxy preset: {e}")
        return False


# Dynamic Universal Audio UADx Studio D Chorus JSON Compiler
def compile_studio_d_toneprint(filepath, base_preset_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    studio_d_data = preset_data.get("studio_d") if isinstance(preset_data, dict) else None

    mode = None
    power = None

    if studio_d_data and isinstance(studio_d_data, dict):
        mode = studio_d_data.get("mode")
        power = studio_d_data.get("power")
        
        # normalize types
        if mode is not None:
            mode = str(mode)
        if power is not None:
            if isinstance(power, bool):
                pass
            else:
                power = str(power).lower() in ("true", "on", "1")
    else:
        with open(filepath, "r") as f:
            full_content = f.read()
            
        # Isolate to Studio D section to prevent parameter collision
        content = extract_markdown_section(full_content, ["Studio D Chorus", "Studio D", "Dimension D", "Dimension Chorus"])
        
        # Look for Mode. It could be string or numeric (e.g. "4", "1+4", "all")
        # Let's search for the Mode setting inside the table
        mode_match = re.search(r"\|\s*Mode\s*\|\s*(?:\*\?)?([^|]+?)(?:\*\%)?\s*\|", content, re.IGNORECASE)
        if mode_match:
            mode = mode_match.group(1).strip()
        else:
            # Let's try finding the numeric parameter for Mode
            mode_num = find_numeric_parameter(content, ["Mode"])
            if mode_num is not None:
                mode = str(int(mode_num))

        # Look for Power (ON / OFF)
        power = find_boolean_parameter(content, ["Power"])
        bypass = find_boolean_parameter(content, ["Bypass"])
        if bypass is not None:
            power = not bypass

    # If both are None, skip
    if mode is None and power is None:
        return False

    # Load base template JSON preset
    try:
        with open(base_preset_path, "r") as f:
            preset_data_json = json.load(f)
    except Exception as e:
        print(f"Error: Failed to parse Studio D base preset JSON template: {e}")
        return False

    # Decode chunk
    chunk_bytes = bytearray(base64.b64decode(preset_data_json["chunk"]))

    # Dimension Mode button mapping
    if mode is not None:
        mode_str = str(mode).lower().strip()
        # Parse modes:
        # Off: 0.0
        # 1: 1/15.0
        # 2: 2/15.0
        # 3: 4/15.0
        # 4: 8/15.0
        # "all" or "secret" or "1+2+3+4": 15/15.0 = 1.0
        # Custom combinations, e.g. "1+4": sum weights 1 + 8 = 9 -> 9/15.0
        mode_val = 0.0
        if mode_str in ("off", "0", "none", "bypassed"):
            mode_val = 0.0
        elif mode_str in ("all", "secret", "1+2+3+4", "1,2,3,4"):
            mode_val = 1.0
        else:
            # Parse custom combination or single mode
            parts = re.findall(r"\d", mode_str)
            if parts:
                weight_sum = 0
                for part in parts:
                    n = int(part)
                    if n == 1:
                        weight_sum += 1
                    elif n == 2:
                        weight_sum += 2
                    elif n == 3:
                        weight_sum += 4
                    elif n == 4:
                        weight_sum += 8
                # scale by 15.0
                mode_val = min(1.0, max(0.0, weight_sum / 15.0))
            else:
                try:
                    # Fallback to direct float conversion if they passed an exact float
                    mode_val = float(mode_str)
                except ValueError:
                    mode_val = 0.0
        
        struct.pack_into("f", chunk_bytes, 10 * 4, mode_val)

    # Power Switch mapping
    if power is not None:
        power_val = 1.0 if power else 0.0
        struct.pack_into("f", chunk_bytes, 12 * 4, power_val)

    # Re-encode chunk
    preset_data_json["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data_json["name"] = f"Toneprint - {output_name}"
    preset_data_json["uid"] = uuid.uuid4().hex

    # Output directory: standard documents plugin presets folder for UADx Studio D
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")

    try:
        with open(out_path, "w") as f:
            json.dump(preset_data_json, f, indent=4)
        print(f"-> Compiled UADx Studio D Chorus Preset: 'Toneprint - {output_name}'")
        return True
    except Exception as e:
        print(f"Error: Failed to write Studio D preset: {e}")
        return False


# Dynamic Valhalla Supermassive XML VPRESET Compiler
def compile_supermassive_toneprint(filepath, base_preset_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    supermassive_data = preset_data.get("supermassive") if isinstance(preset_data, dict) else None

    mix = None
    delay_ms = None
    warp = None
    feedback = None
    density = None
    mode = None

    if supermassive_data and isinstance(supermassive_data, dict):
        mix = supermassive_data.get("mix")
        delay_ms = supermassive_data.get("delay")
        warp = supermassive_data.get("warp")
        feedback = supermassive_data.get("feedback")
        density = supermassive_data.get("density")
        mode = supermassive_data.get("mode")
    else:
        with open(filepath, "r") as f:
            full_content = f.read()
            
        content = extract_markdown_section(full_content, ["ValhallaSuperMassive", "SuperMassive", "Valhalla Super Massive"])
        
        mix = find_numeric_parameter(content, ["Mix"])
        
        # Look for Delay specifically with custom regex to handle "ms" or "s"
        delay_match = re.search(r"\|\s*(?:Delay|Delay time)\s*\|\s*(?:\*\?)?([~0-9.+−-]+)(?:ms|s)?(?:\*\%)?\s*\|", content, re.IGNORECASE)
        if delay_match:
            val_str = delay_match.group(1).replace("−", "-").replace("~", "").strip()
            try:
                delay_ms = float(val_str)
            except ValueError:
                delay_ms = None
        else:
            delay_ms = find_numeric_parameter(content, ["Delay", "Delay time"])
            
        warp = find_numeric_parameter(content, ["Warp"])
        feedback = find_numeric_parameter(content, ["Feedback"])
        density = find_numeric_parameter(content, ["Density"])
        
        mode_match = re.search(r"\|\s*Mode\s*\|\s*(?:\*\?)?([^|]+?)(?:\*\%)?\s*\|", content, re.IGNORECASE)
        if mode_match:
            mode = mode_match.group(1).strip()

    # Skip if we don't have enough parameters
    if mix is None and delay_ms is None and feedback is None:
        return False

    # Load base template vpreset file
    try:
        with open(base_preset_path, "r") as f:
            preset_text = f.read()
    except Exception as e:
        print(f"Error: Failed to read Valhalla Supermassive base template: {e}")
        return False

    try:
        root_node = ET.fromstring(preset_text.encode("utf-8"))
        if root_node.tag != "ValhallaSupermassive":
            return False
            
        # Update name
        root_node.set("presetName", f"Toneprint - {output_name}")
        
        # 1. Mix (0.0 to 1.0)
        if mix is not None:
            val = mix / 100.0 if mix > 1.0 else mix
            root_node.set("Mix", f"{val:.15f}".rstrip("0").rstrip("."))
            
        # 2. Delay (ms to scaled float: ms / 1000.0)
        if delay_ms is not None:
            val = delay_ms / 1000.0 if delay_ms > 2.0 else delay_ms
            root_node.set("Delay_Ms", f"{val:.15f}".rstrip("0").rstrip("."))
            
        # 3. Warp (0.0 to 1.0)
        if warp is not None:
            val = warp / 100.0 if warp > 1.0 else warp
            root_node.set("DelayWarp", f"{val:.15f}".rstrip("0").rstrip("."))
            
        # 4. Feedback (0.0 to 1.0)
        if feedback is not None:
            val = feedback / 100.0 if feedback > 1.0 else feedback
            root_node.set("Feedback", f"{val:.15f}".rstrip("0").rstrip("."))
            
        # 5. Density (0.0 to 1.0)
        if density is not None:
            val = density / 100.0 if density > 1.0 else density
            root_node.set("Density", f"{val:.15f}".rstrip("0").rstrip("."))
            
        # 6. Mode (Index / 24.0)
        if mode is not None:
            mode_str = str(mode).lower().strip()
            VALHALLA_MODES = [
                "gemini", "hydra", "centaurus", "sagittarius", "great orion",
                "great annihilator", "andromeda", "lyra", "capricorn",
                "large magellanic cloud", "small magellanic cloud", "triangulum",
                "cirrus major", "cirrus minor", "cassiopeia", "ursa major",
                "ursa minor", "scorpio", "leo", "virgo"
            ]
            mode_idx = -1
            for idx, m in enumerate(VALHALLA_MODES):
                if m in mode_str or mode_str in m:
                    mode_idx = idx
                    break
            if mode_idx != -1:
                val = mode_idx / 24.0
                root_node.set("Mode", f"{val:.15f}".rstrip("0").rstrip("."))
            else:
                try:
                    root_node.set("Mode", f"{float(mode):.15f}".rstrip("0").rstrip("."))
                except ValueError:
                    pass
                    
        # 7. Default ModRate and ModDepth to 0.0 to keep it clean and detune-free
        root_node.set("ModRate", "0.0")
        root_node.set("ModDepth", "0.0")

        # Write back out
        out_xml = ET.tostring(root_node, encoding="utf-8").decode("utf-8")
        
        # Prepend XML declaration
        out_content = '<?xml version="1.0" encoding="UTF-8"?>\n\n' + out_xml + '\n'
        
        # Write out
        output_dir = os.path.dirname(base_preset_path)
        out_path = os.path.join(output_dir, f"Toneprint - {output_name}.vpreset")
        
        with open(out_path, "w") as f:
            f.write(out_content)
        print(f"-> Compiled ValhallaSupermassive Preset: 'Toneprint - {output_name}'")
        return True
    except Exception as e:
        print(f"Error: Failed to compile Supermassive preset: {e}")
        return False


# Dynamic Logic Pro Native Channel EQ PST Compiler
def compile_logic_eq_toneprint(filepath, base_preset_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    eq_data = preset_data.get("logic_eq") if isinstance(preset_data, dict) else None

    if eq_data and isinstance(eq_data, dict):
        bands = {i: {"on": None, "freq": None, "gain_or_slope": None, "q": None} for i in range(1, 9)}
        for band_str, params in eq_data.items():
            if not band_str.startswith("band") or not band_str[4:].isdigit():
                continue
            band_num = int(band_str[4:])
            if band_num < 1 or band_num > 8:
                continue
            
            if "on" in params:
                bands[band_num]["on"] = 1.0 if params["on"] else 0.0
            if "freq" in params:
                bands[band_num]["freq"] = float(params["freq"])
            if band_num in [1, 8]:
                if "slope" in params:
                    bands[band_num]["gain_or_slope"] = float(params["slope"])
            else:
                if "gain" in params:
                    bands[band_num]["gain_or_slope"] = float(params["gain"])
                if "q" in params:
                    bands[band_num]["q"] = float(params["q"])
    else:
        with open(filepath, "r") as f:
            content = f.read()
        # Parse all bands from toneprint markdown
        bands = parse_eq_bands(content)

    # Check if any band is active/configured
    any_configured = any(p["on"] is not None for p in bands.values())
    if not any_configured:
        return False

    # Load base .pst template
    with open(base_preset_path, "rb") as f:
        preset_bytes = bytearray(f.read())

    # surgically patch the float values
    for band_num, params in bands.items():
        if params["on"] is None and params["freq"] is None:
            continue
            
        if band_num == 1:
            # Low Cut: On/Off = Float 5, Freq = Float 6, Slope = Float 7
            if params["on"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 5 * 4, params["on"])
            if params["freq"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 6 * 4, params["freq"])
            if params["gain_or_slope"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 7 * 4, params["gain_or_slope"])
        elif band_num == 8:
            # High Cut: On/Off = Float 33, Freq = Float 34, Slope = Float 35
            if params["on"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 33 * 4, params["on"])
            if params["freq"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 34 * 4, params["freq"])
            if params["gain_or_slope"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 35 * 4, params["gain_or_slope"])
        else:
            # Bands 2 to 7
            base_idx = 9 + (band_num - 2) * 4
            
            if params["on"] is not None:
                struct.pack_into("f", preset_bytes, 8 + base_idx * 4, params["on"])
            if params["freq"] is not None:
                struct.pack_into("f", preset_bytes, 8 + (base_idx + 1) * 4, params["freq"])
            if params["gain_or_slope"] is not None:
                struct.pack_into("f", preset_bytes, 8 + (base_idx + 2) * 4, params["gain_or_slope"])
            if params["q"] is not None:
                struct.pack_into("f", preset_bytes, 8 + (base_idx + 3) * 4, params["q"])

    # Save preset
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(preset_bytes)

    print(f"-> Compiled Logic Channel EQ Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic Logic Pro Native Compressor PST Compiler
def compile_logic_compressor_toneprint(filepath, base_preset_path, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    comp_data = preset_data.get("logic_compressor") if isinstance(preset_data, dict) else None

    if comp_data and isinstance(comp_data, dict):
        threshold = comp_data.get("threshold")
        ratio = comp_data.get("ratio")
        attack = comp_data.get("attack")
        release = comp_data.get("release")
        gain = comp_data.get("makeup_gain")
        knee = comp_data.get("knee")
        
        # normalize types
        if threshold is not None: threshold = float(threshold)
        if ratio is not None: ratio = float(ratio)
        if attack is not None: attack = float(attack)
        if release is not None: release = float(release)
        if gain is not None: gain = float(gain)
        if knee is not None: knee = float(knee)
    else:
        with open(filepath, "r") as f:
            content = f.read()
        # Search for Compressor settings using robust helper
        threshold = extract_comp_param(content, ["Threshold"])
        ratio = extract_comp_param(content, ["Ratio"])
        attack = extract_comp_param(content, ["Attack"])
        release = extract_comp_param(content, ["Release"])
        gain = extract_comp_param(content, ["Gain", "Makeup Gain"])
        knee = extract_comp_param(content, ["Knee"])

    # If all are None, skip compressor generation
    if threshold is None and ratio is None and attack is None and release is None:
        return False

    # Load base .pst template
    with open(base_preset_path, "rb") as f:
        preset_bytes = bytearray(f.read())

    # Float 5: Threshold
    if threshold is not None:
        struct.pack_into("f", preset_bytes, 8 + 5 * 4, threshold)
    # Float 6: Ratio
    if ratio is not None:
        struct.pack_into("f", preset_bytes, 8 + 6 * 4, ratio)
    # Float 7: Attack
    if attack is not None:
        struct.pack_into("f", preset_bytes, 8 + 7 * 4, attack)
    # Float 8: Release
    if release is not None:
        struct.pack_into("f", preset_bytes, 8 + 8 * 4, release)
    # Float 9: Makeup Gain
    if gain is not None:
        struct.pack_into("f", preset_bytes, 8 + 9 * 4, gain)
    # Float 10: Knee
    if knee is not None:
        struct.pack_into("f", preset_bytes, 8 + 10 * 4, knee)

    # Save preset
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(preset_bytes)

    print(f"-> Compiled Logic Compressor Preset: 'Toneprint - {output_name}'")
    return True


# Dynamic Yamaha THR-II JSON Compiler (.thrl6p)
def compile_yamaha_thr_toneprint(filepath, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    thr_data = preset_data.get("yamaha_thr") if isinstance(preset_data, dict) else None
    
    # Load base template structure
    preset_json = json.loads(json.dumps(DEFAULT_THR_PRESET))
    preset_json["data"]["meta"]["name"] = output_name
    
    if thr_data and isinstance(thr_data, dict):
        tone = preset_json["data"]["tone"]
        
        # 1. Amp Settings
        amp_data = thr_data.get("amp", {})
        if isinstance(amp_data, dict):
            if "model" in amp_data: tone["THRGroupAmp"]["@asset"] = str(amp_data["model"])
            if "drive" in amp_data: tone["THRGroupAmp"]["Drive"] = float(amp_data["drive"])
            if "bass" in amp_data: tone["THRGroupAmp"]["Bass"] = float(amp_data["bass"])
            if "mid" in amp_data: tone["THRGroupAmp"]["Mid"] = float(amp_data["mid"])
            if "treble" in amp_data: tone["THRGroupAmp"]["Treble"] = float(amp_data["treble"])
            if "master" in amp_data: tone["THRGroupAmp"]["Master"] = float(amp_data["master"])
            
        # 2. Cabinet Settings
        cab_data = thr_data.get("cab", {})
        if isinstance(cab_data, dict):
            if "model" in cab_data: tone["THRGroupCab"]["@asset"] = str(cab_data["model"])
            if "sim_type" in cab_data: tone["THRGroupCab"]["SpkSimType"] = str(cab_data["sim_type"])
            
        # 3. Compressor
        comp_data = thr_data.get("compressor", {})
        if isinstance(comp_data, dict):
            if "enabled" in comp_data: tone["THRGroupFX1Compressor"]["@enabled"] = bool(comp_data["enabled"])
            if "model" in comp_data: tone["THRGroupFX1Compressor"]["@asset"] = str(comp_data["model"])
            if "level" in comp_data: tone["THRGroupFX1Compressor"]["Level"] = float(comp_data["level"])
            if "sustain" in comp_data: tone["THRGroupFX1Compressor"]["Sustain"] = float(comp_data["sustain"])
            
        # 4. Effect (Modulation)
        fx_data = thr_data.get("effect", {})
        if isinstance(fx_data, dict):
            if "enabled" in fx_data: tone["THRGroupFX2Effect"]["@enabled"] = bool(fx_data["enabled"])
            if "model" in fx_data: tone["THRGroupFX2Effect"]["@asset"] = str(fx_data["model"])
            if "wet_dry" in fx_data: tone["THRGroupFX2Effect"]["@wetDry"] = float(fx_data["wet_dry"])
            if "depth" in fx_data: tone["THRGroupFX2Effect"]["Depth"] = float(fx_data["depth"])
            if "feedback" in fx_data: tone["THRGroupFX2Effect"]["Feedback"] = float(fx_data["feedback"])
            if "freq" in fx_data: tone["THRGroupFX2Effect"]["Freq"] = float(fx_data["freq"])
            if "pre" in fx_data: tone["THRGroupFX2Effect"]["Pre"] = float(fx_data["pre"])
            
        # 5. Echo (Delay)
        echo_data = thr_data.get("echo", {})
        if isinstance(echo_data, dict):
            if "enabled" in echo_data: tone["THRGroupFX3EffectEcho"]["@enabled"] = bool(echo_data["enabled"])
            if "model" in echo_data: tone["THRGroupFX3EffectEcho"]["@asset"] = str(echo_data["model"])
            if "wet_dry" in echo_data: tone["THRGroupFX3EffectEcho"]["@wetDry"] = float(echo_data["wet_dry"])
            if "bass" in echo_data: tone["THRGroupFX3EffectEcho"]["Bass"] = float(echo_data["bass"])
            if "feedback" in echo_data: tone["THRGroupFX3EffectEcho"]["Feedback"] = float(echo_data["feedback"])
            if "time" in echo_data: tone["THRGroupFX3EffectEcho"]["Time"] = float(echo_data["time"])
            if "treble" in echo_data: tone["THRGroupFX3EffectEcho"]["Treble"] = float(echo_data["treble"])
            
        # 6. Reverb
        rev_data = thr_data.get("reverb", {})
        if isinstance(rev_data, dict):
            if "enabled" in rev_data: tone["THRGroupFX4EffectReverb"]["@enabled"] = bool(rev_data["enabled"])
            if "model" in rev_data: tone["THRGroupFX4EffectReverb"]["@asset"] = str(rev_data["model"])
            if "wet_dry" in rev_data: tone["THRGroupFX4EffectReverb"]["@wetDry"] = float(rev_data["wet_dry"])
            if "decay" in rev_data: tone["THRGroupFX4EffectReverb"]["Decay"] = float(rev_data["decay"])
            if "pre_delay" in rev_data: tone["THRGroupFX4EffectReverb"]["PreDelay"] = float(rev_data["pre_delay"])
            if "tone" in rev_data: tone["THRGroupFX4EffectReverb"]["Tone"] = float(rev_data["tone"])
            
        # 7. Gate
        gate_data = thr_data.get("gate", {})
        if isinstance(gate_data, dict):
            if "enabled" in gate_data: tone["THRGroupGate"]["@enabled"] = bool(gate_data["enabled"])
            if "model" in gate_data: tone["THRGroupGate"]["@asset"] = str(gate_data["model"])
            if "decay" in gate_data: tone["THRGroupGate"]["Decay"] = float(gate_data["decay"])
            if "thresh" in gate_data: tone["THRGroupGate"]["Thresh"] = float(gate_data["thresh"])
            
        # 8. Global Tempo
        global_data = thr_data.get("global", {})
        if isinstance(global_data, dict):
            if "tempo" in global_data: tone["global"]["THRPresetParamTempo"] = float(global_data["tempo"])

    # Output directory
    os.makedirs(YAMAHA_THR_OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(YAMAHA_THR_OUTPUT_DIR, f"{output_name}.thrl6p")
    
    with open(out_path, "w") as f:
        json.dump(preset_json, f, indent=4)
        
    print(f"-> Compiled Yamaha THR Preset: '{output_name}'")
    return True


# Helper to extract a specific device's section from Markdown body
def extract_markdown_section(content, keywords):
    lines = content.splitlines()
    section_lines = []
    in_section = False
    in_section_level = 0
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            header_level = len(stripped) - len(stripped.lstrip("#"))
            header_text = stripped.lstrip("#").strip().lower()
            
            # Skip page title headers (H1) to avoid matching top-level tone names
            if header_level == 1:
                continue
                
            if in_section:
                # Exit section if we hit another header of same or higher level
                if header_level <= in_section_level:
                    break
            
            # Check if this header matches our device keywords
            if any(kw.lower() in header_text for kw in keywords):
                in_section = True
                in_section_level = header_level
                continue
                
        if in_section:
            section_lines.append(line)
            
    if in_section and section_lines:
        return "\n".join(section_lines)
    return content  # Fallback to full content if not found


# Dynamic Nembrini XML Presets Compiler
def compile_nembrini_xml_preset(filepath, base_preset_path, output_name, frontmatter, plugin_type):
    # Load base XML preset template
    if not os.path.exists(base_preset_path):
        print(f"Warning: Nembrini base template missing for {plugin_type}: {base_preset_path}")
        return False

    preset_data = frontmatter.get("preset_data", {})
    
    # Identify target amp/plugin key in frontmatter
    yaml_keys = {
        "mrh810": "nembrini_mrh810",
        "jc120": "nembrini_jc120",
        "div11": "nembrini_div11",
        "acoustic_voice": "nembrini_acoustic_voice",
        "puretone": "nembrini_puretone"
    }
    
    yaml_key = yaml_keys.get(plugin_type)
    plugin_settings = preset_data.get(yaml_key) if isinstance(preset_data, dict) else None
    
    # If not present in frontmatter, dynamically parse from Markdown body
    if not plugin_settings or not isinstance(plugin_settings, dict):
        plugin_settings = {}
        with open(filepath, "r") as f:
            full_content = f.read()
            
        # Isolate the search space to the specific plugin's section to avoid Tone King conflicts
        keywords_map = {
            "mrh810": ["mrh810", "jcm800"],
            "jc120": ["jazz chorus", "jc120", "jc-120"],
            "div11": ["divided 11", "div11", "divided"],
            "acoustic_voice": ["acoustic voice"],
            "puretone": ["puretone", "pure tone"]
        }
        
        keywords = keywords_map.get(plugin_type, [plugin_type])
        content = extract_markdown_section(full_content, keywords)
            
        if plugin_type == "mrh810":
            # Determine channel first
            is_clean = "clean channel" in content.lower() and "lead channel" not in content.lower()
            plugin_settings["ChSel"] = 0.0 if is_clean else 1.0
            
            # Common controls
            master = find_numeric_parameter(content, ["Master", "Volume (master)"])
            presence = find_numeric_parameter(content, ["Presence"])
            out_level = find_numeric_parameter(content, ["Output (plugin Output slider)", "Output Level", "Output"])
            harsh = find_boolean_parameter(content, ["Harsh"])
            rumbling = find_boolean_parameter(content, ["Rumbling"])
            
            # Noise Gate
            gate_power = find_boolean_parameter(content, ["Noise Gate Power", "Noise Gate", "Gate Power"])
            gate_threshold = find_numeric_parameter(content, ["Noise Gate Threshold", "Threshold"])
            gate_range = find_numeric_parameter(content, ["Noise Gate Range", "Range"])
            
            if master is not None: plugin_settings["Master"] = master
            if presence is not None: plugin_settings["Presence"] = presence
            if out_level is not None: plugin_settings["OutLevel"] = out_level
            if harsh is not None: plugin_settings["Harsh"] = 1.0 if harsh else 0.0
            if rumbling is not None: plugin_settings["Rumbling"] = 1.0 if rumbling else 0.0
            if gate_power is not None: plugin_settings["NgPower"] = 1.0 if gate_power else 0.0
            if gate_threshold is not None: plugin_settings["NgThreshold"] = gate_threshold
            if gate_range is not None: plugin_settings["NgRange"] = gate_range
            
            # Channel specific controls
            gain = find_numeric_parameter(content, ["Gain"])
            volume = find_numeric_parameter(content, ["Volume (channel)", "Volume"])
            bass = find_numeric_parameter(content, ["Bass"])
            middle = find_numeric_parameter(content, ["Middle", "Mids"])
            treble = find_numeric_parameter(content, ["Treble"])
            
            if is_clean:
                if volume is not None: plugin_settings["CleanVolume"] = volume
                if bass is not None: plugin_settings["CleanBass"] = bass
                if treble is not None: plugin_settings["CleanTreble"] = treble
            else:
                if gain is not None: plugin_settings["LeadGain"] = gain
                if volume is not None: plugin_settings["LeadVolume"] = volume
                if bass is not None: plugin_settings["LeadBass"] = bass
                if middle is not None: plugin_settings["LeadMid"] = middle
                if treble is not None: plugin_settings["LeadTreble"] = treble
                
        elif plugin_type == "jc120":
            bass = find_numeric_parameter(content, ["Bass"])
            middle = find_numeric_parameter(content, ["Middle", "Mids"])
            treble = find_numeric_parameter(content, ["Treble"])
            volume = find_numeric_parameter(content, ["Volume"])
            bright = find_boolean_parameter(content, ["Bright Switch", "Bright"])
            distortion = find_numeric_parameter(content, ["Distortion"])
            reverb = find_numeric_parameter(content, ["Reverb"])
            out_level = find_numeric_parameter(content, ["Output (plugin Output slider)", "Output Level", "Output", "OutLevel"])
            
            if bass is not None: plugin_settings["Bass"] = bass
            if middle is not None: plugin_settings["Middle"] = middle
            if treble is not None: plugin_settings["Treble"] = treble
            if volume is not None: plugin_settings["Volume"] = volume
            if bright is not None: plugin_settings["Brigth"] = 1.0 if bright else 0.0
            if distortion is not None: plugin_settings["Distortion"] = distortion
            if reverb is not None: plugin_settings["Reverb"] = reverb
            if out_level is not None: plugin_settings["OutLevel"] = out_level
            
            # Modulation type and params
            mod_depth = find_numeric_parameter(content, ["Modulation Depth", "Mod Depth"])
            mod_speed = find_numeric_parameter(content, ["Modulation Speed", "Mod Speed"])
            if "chorus" in content.lower():
                plugin_settings["ModType"] = 2.0  # Chorus (value 2.0)
            elif "vibrato" in content.lower():
                plugin_settings["ModType"] = 1.0  # Vibrato (value 1.0)
                
            if mod_depth is not None: plugin_settings["ModDepth"] = mod_depth
            if mod_speed is not None: plugin_settings["ModSpeed"] = mod_speed
            
        elif plugin_type == "div11":
            bass = find_numeric_parameter(content, ["Bass"])
            master = find_numeric_parameter(content, ["Master"])
            volume = find_numeric_parameter(content, ["Volume"])
            treble = find_numeric_parameter(content, ["Treble"])
            tight = find_numeric_parameter(content, ["Tight"])
            harsh = find_numeric_parameter(content, ["Harsh"])
            boost = find_boolean_parameter(content, ["Boost Switch", "Boost"])
            out_level = find_numeric_parameter(content, ["Output (plugin Output slider)", "Output Level", "Output", "OutLevel"])
            
            if bass is not None: plugin_settings["Bass"] = bass
            if master is not None: plugin_settings["Master"] = master
            if volume is not None: plugin_settings["Volume"] = volume
            if treble is not None: plugin_settings["Treble"] = treble
            if tight is not None: plugin_settings["Tight"] = tight
            if harsh is not None: plugin_settings["Harsh"] = harsh
            if boost is not None: plugin_settings["Boost"] = 1.0 if boost else 0.0
            if out_level is not None: plugin_settings["OutLevel"] = out_level
            
        elif plugin_type == "acoustic_voice":
            gain = find_numeric_parameter(content, ["DI Preamp Gain", "Preamp Gain", "Gain"])
            notch = find_numeric_parameter(content, ["DI Preamp Notch", "Preamp Notch", "Notch"])
            
            comp_power = find_boolean_parameter(content, ["Compressor Power", "Compressor Active", "Compressor"])
            comp_attack = find_numeric_parameter(content, ["Compressor Attack"])
            comp_release = find_numeric_parameter(content, ["Compressor Release"])
            comp_ratio = find_numeric_parameter(content, ["Compressor Ratio"])
            comp_thresh = find_numeric_parameter(content, ["Compressor Threshold"])
            comp_out = find_numeric_parameter(content, ["Compressor Output", "Compressor Gain"])
            
            reverb_mix = find_numeric_parameter(content, ["Reverb Mix"])
            reverb_size = find_numeric_parameter(content, ["Reverb Size"])
            reverb_tone = find_numeric_parameter(content, ["Reverb Tone"])
            
            if gain is not None: plugin_settings["DiPreampGain"] = gain
            if notch is not None: plugin_settings["DiPreampNotch"] = notch
            if comp_power is not None: plugin_settings["CompressorPower"] = 1.0 if comp_power else 0.0
            if comp_attack is not None: plugin_settings["CompressorAttack"] = comp_attack
            if comp_release is not None: plugin_settings["CompressorRelease"] = comp_release
            if comp_ratio is not None: plugin_settings["CompressorRatio"] = comp_ratio
            if comp_thresh is not None: plugin_settings["CompressorThreshold"] = comp_thresh
            if comp_out is not None: plugin_settings["CompressorOut"] = comp_out
            if reverb_mix is not None: plugin_settings["ReverbMix"] = reverb_mix
            if reverb_size is not None: plugin_settings["ReverbSize"] = reverb_size
            if reverb_tone is not None: plugin_settings["ReverbTone"] = reverb_tone
            
        elif plugin_type == "puretone":
            volume = find_numeric_parameter(content, ["Volume"])
            growl = find_numeric_parameter(content, ["Growl"])
            bass = find_numeric_parameter(content, ["Bass"])
            mid = find_numeric_parameter(content, ["Middle", "Mids", "Mid"])
            treble = find_numeric_parameter(content, ["Treble"])
            tone = find_numeric_parameter(content, ["Tone"])
            out_level = find_numeric_parameter(content, ["Output (plugin Output slider)", "Output Level", "Output", "OutLevel"])
            
            if volume is not None: plugin_settings["Volume"] = volume
            if growl is not None: plugin_settings["Growl"] = growl
            if bass is not None: plugin_settings["Bass"] = bass
            if mid is not None: plugin_settings["Mid"] = mid
            if treble is not None: plugin_settings["Treble"] = treble
            if tone is not None: plugin_settings["Tone"] = tone
            if out_level is not None: plugin_settings["OutLevel"] = out_level

    # Skip if no settings were identified
    if not plugin_settings:
        return False

    # Standardize values to float types and strings
    mapped_settings = {}
    for k, v in plugin_settings.items():
        if isinstance(v, bool):
            mapped_settings[k] = 1.0 if v else 0.0
        elif isinstance(v, (int, float)):
            mapped_settings[k] = float(v)
        else:
            try:
                mapped_settings[k] = float(v)
            except ValueError:
                mapped_settings[k] = v

    # Parse and patch XML
    tree = ET.parse(base_preset_path)
    root = tree.getroot()
    
    # Surgically patch PARAM elements
    for param in root.findall("PARAM"):
        param_id = param.get("id")
        if param_id in mapped_settings:
            param.set("value", str(mapped_settings[param_id]))
            
    # Write back XML
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.xml")
    
    tree.write(out_path, encoding="UTF-8", xml_declaration=True)
    print(f"-> Compiled Nembrini {plugin_type.upper()} XML Preset: 'Toneprint - {output_name}'")
    return True


def main():
    print("==================================================")
    print("RIG-WIDE TONEPRINT COMPILER & PRESET GENERATOR (V2)")
    print("==================================================")
    
    # 1. Load Neural DSP Base DNA Data
    neural_template_file = NEURAL_TEMPLATE if os.path.exists(NEURAL_TEMPLATE) else NEURAL_TEMPLATE_ALT
    if os.path.exists(neural_template_file):
        with open(neural_template_file, "rb") as f:
            neural_base_data = f.read()
    else:
        print("Warning: Neural DSP base template missing. Skipping Neural compile.")
        neural_base_data = None
        
    # 2. Load UAD Paradise Base DNA JSON
    if os.path.exists(PARADISE_TEMPLATE):
        with open(PARADISE_TEMPLATE, "r") as f:
            uad_base_json = json.load(f)
    else:
        print("Warning: UAD Paradise template missing. Skipping UAD compile.")
        uad_base_json = None

    # 3. Load MixWave Two-Rock Bloomfield Drive Base DNA XML
    mixwave_base_xml = None
    for t_path in [MIXWAVE_TEMPLATE, MIXWAVE_TEMPLATE_ALT, MIXWAVE_TEMPLATE_FACTORY]:
        if os.path.exists(t_path):
            mixwave_base_xml = t_path
            break
    if not mixwave_base_xml:
        print("Warning: MixWave Bloomfield base template missing. Skipping MixWave compile.")

    # 4. Recursively Scan Tones Directory
    compiled_neural = 0
    compiled_uad = 0
    compiled_mixwave = 0
    compiled_la2a = 0
    compiled_hitsville = 0
    compiled_logiceq = 0
    compiled_logiccomp = 0
    compiled_thr = 0
    compiled_mrh810 = 0
    compiled_jc120 = 0
    compiled_div11 = 0
    compiled_acoustic = 0
    compiled_puretone = 0
    compiled_galaxy = 0
    compiled_studiod = 0
    compiled_supermassive = 0
    
    for root, dirs, files in os.walk(TONES_DIR):
        for f in files:
            if not f.endswith(".md") or f == "INDEX.md":
                continue
            
            filepath = os.path.join(root, f)
            with open(filepath, "r") as file:
                content = file.read()
                
            frontmatter, _ = parse_yaml_frontmatter(content)
            
            amp_str = frontmatter.get("amp", "")
            if not amp_str:
                continue
            
            # Determine beautiful preset name
            if "preset_name" in frontmatter:
                clean_name = frontmatter["preset_name"]
            else:
                # Fallback to standard word capitalization from filename
                name_parts = f.replace(".md", "").split("-")
                clean_name = " ".join([p.capitalize() for p in name_parts])
                
            # Compile based on target amp platform
            if "Cory Wong" in amp_str or "Amp Snob" in amp_str:
                if neural_base_data:
                    if compile_neural_toneprint(filepath, neural_base_data, clean_name, frontmatter):
                        compiled_neural += 1
            elif "Two Rock" in amp_str or "Bloomfield" in amp_str:
                if mixwave_base_xml:
                    if compile_mixwave_toneprint(filepath, mixwave_base_xml, clean_name, frontmatter):
                        compiled_mixwave += 1
            elif any(x in amp_str for x in ["THR10", "THR30", "Yamaha THR", "THR-II", "THR II"]):
                if compile_yamaha_thr_toneprint(filepath, clean_name, frontmatter):
                    compiled_thr += 1
            elif "MRH810" in amp_str or "JCM800" in amp_str:
                base_path = NEMBRINI_TEMPLATES["mrh810"]
                if compile_nembrini_xml_preset(filepath, base_path, clean_name, frontmatter, "mrh810"):
                    compiled_mrh810 += 1
            elif "Jazz Chorus" in amp_str or "JC120" in amp_str or "JC-120" in amp_str:
                base_path = NEMBRINI_TEMPLATES["jc120"]
                if compile_nembrini_xml_preset(filepath, base_path, clean_name, frontmatter, "jc120"):
                    compiled_jc120 += 1
            elif "Divided 11" in amp_str or "Div11" in amp_str or "Divided" in amp_str:
                base_path = NEMBRINI_TEMPLATES["div11"]
                if compile_nembrini_xml_preset(filepath, base_path, clean_name, frontmatter, "div11"):
                    compiled_div11 += 1
            elif "Acoustic Voice" in amp_str:
                base_path = NEMBRINI_TEMPLATES["acoustic_voice"]
                if compile_nembrini_xml_preset(filepath, base_path, clean_name, frontmatter, "acoustic_voice"):
                    compiled_acoustic += 1
            elif "Puretone" in amp_str or "HK Puretone" in amp_str:
                base_path = NEMBRINI_TEMPLATES["puretone"]
                if compile_nembrini_xml_preset(filepath, base_path, clean_name, frontmatter, "puretone"):
                    compiled_puretone += 1
            else:
                # Check if it is a UADx model
                is_uad = any(x in amp_str for x in ["Dream", "Enigmatic", "Woodrow", "Ruby", "Showtime", "Lion"])
                if is_uad and uad_base_json:
                    if compile_uad_toneprint(filepath, uad_base_json, clean_name, frontmatter):
                        compiled_uad += 1

            # Compile LA-2A Presets if UADx templates exist
            if os.path.exists(LA2A_BASE):
                # Only compile if LA-2A is in the toneprint content
                if "la-2a" in content.lower():
                    if compile_la2a_toneprint(filepath, LA2A_BASE, clean_name, frontmatter):
                        compiled_la2a += 1

            # Compile Hitsville Reverb Presets if UADx templates exist
            if os.path.exists(HITSVILLE_BASE):
                # Only compile if Hitsville is in the toneprint content
                if "hitsville" in content.lower():
                    if compile_hitsville_toneprint(filepath, HITSVILLE_BASE, clean_name, frontmatter):
                        compiled_hitsville += 1

            # Compile Galaxy Tape Echo Presets if templates exist
            if os.path.exists(GALAXY_BASE):
                # Only compile if Galaxy is in the toneprint content
                if "galaxy" in content.lower():
                    if compile_galaxy_toneprint(filepath, GALAXY_BASE, clean_name, frontmatter):
                        compiled_galaxy += 1

            # Compile Studio D Chorus Presets if templates exist
            if os.path.exists(STUDIO_D_BASE):
                # Only compile if Studio D or Dimension D is in the toneprint content
                if any(x in content.lower() for x in ["studio d", "dimension d", "dimension chorus"]):
                    if compile_studio_d_toneprint(filepath, STUDIO_D_BASE, clean_name, frontmatter):
                        compiled_studiod += 1

            # Compile Valhalla Supermassive Presets if templates exist
            if os.path.exists(VALHALLA_BASE):
                # Only compile if Supermassive is in the toneprint content
                if any(x in content.lower() for x in ["supermassive", "valhallasupermassive"]):
                    if compile_supermassive_toneprint(filepath, VALHALLA_BASE, clean_name, frontmatter):
                        compiled_supermassive += 1

            # Compile Logic Channel EQ Presets if native templates exist
            if os.path.exists(LOGIC_EQ_BASE):
                # Check if Logic Channel EQ is in toneprint
                if "channel eq" in content.lower() or "high-cut" in content.lower() or "low-cut" in content.lower():
                    if compile_logic_eq_toneprint(filepath, LOGIC_EQ_BASE, clean_name, frontmatter):
                        compiled_logiceq += 1

            # Compile Logic Compressor Presets if native templates exist
            if os.path.exists(LOGIC_COMP_BASE):
                # Only compile if Logic Compressor is in toneprint
                if "logic compressor" in content.lower() or "compressor" in content.lower() and "la-2a" not in content.lower():
                    if compile_logic_compressor_toneprint(filepath, LOGIC_COMP_BASE, clean_name, frontmatter):
                        compiled_logiccomp += 1

            # Compile Nembrini Acoustic Voice Pro Presets if templates exist
            base_avp_path = NEMBRINI_TEMPLATES["acoustic_voice"]
            if os.path.exists(base_avp_path):
                # Only compile if Acoustic Voice is in the toneprint content
                if "acoustic voice" in content.lower():
                    if compile_nembrini_xml_preset(filepath, base_avp_path, clean_name, frontmatter, "acoustic_voice"):
                        compiled_acoustic += 1

    print("\n==================================================")
    print(f"Rig Compilation Complete! Injected:")
    print(f"  -> {compiled_neural} Neural DSP presets in {NEURAL_OUTPUT_DIR}")
    print(f"  -> {compiled_uad} UAD Paradise presets in {PARADISE_DIR}")
    print(f"  -> {compiled_mixwave} MixWave Two-Rock presets in {MIXWAVE_OUTPUT_DIR}")
    print(f"  -> {compiled_la2a} UADx LA-2A presets in {os.path.dirname(LA2A_BASE)}")
    print(f"  -> {compiled_hitsville} UADx Hitsville presets in {os.path.dirname(HITSVILLE_BASE)}")
    print(f"  -> {compiled_logiceq} Logic Channel EQ presets in {os.path.dirname(LOGIC_EQ_BASE)}")
    print(f"  -> {compiled_logiccomp} Logic Compressor presets in {os.path.dirname(LOGIC_COMP_BASE)}")
    print(f"  -> {compiled_thr} Yamaha THR presets in {YAMAHA_THR_OUTPUT_DIR}")
    print(f"  -> {compiled_mrh810} Nembrini MRH810 XML presets in {os.path.dirname(NEMBRINI_TEMPLATES['mrh810'])}")
    print(f"  -> {compiled_jc120} Nembrini Jazz Chorus XML presets in {os.path.dirname(NEMBRINI_TEMPLATES['jc120'])}")
    print(f"  -> {compiled_div11} Nembrini Divided 11 XML presets in {os.path.dirname(NEMBRINI_TEMPLATES['div11'])}")
    print(f"  -> {compiled_acoustic} Nembrini Acoustic Voice XML presets in {os.path.dirname(NEMBRINI_TEMPLATES['acoustic_voice'])}")
    print(f"  -> {compiled_puretone} Nembrini Puretone XML presets in {os.path.dirname(NEMBRINI_TEMPLATES['puretone'])}")
    print(f"  -> {compiled_galaxy} UADx Galaxy Tape Echo presets in {os.path.dirname(GALAXY_BASE)}")
    print(f"  -> {compiled_studiod} UADx Studio D Chorus presets in {os.path.dirname(STUDIO_D_BASE)}")
    print(f"  -> {compiled_supermassive} Valhalla Supermassive presets in {os.path.dirname(VALHALLA_BASE)}")
    print("==================================================")

if __name__ == "__main__":
    main()
