#!/usr/bin/env python3
import os
import json
import re
import uuid
import xml.etree.ElementTree as ET
import base64
import struct
import plistlib
import argparse
import math

try:
    from Foundation import NSURL, NSURLBookmarkCreationSuitableForBookmarkFile
    FOUNDATION_AVAILABLE = True
except ImportError:
    FOUNDATION_AVAILABLE = False

# Directories & Path Configurations
TONES_DIR = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"

# Neural DSP Paths
NEURAL_TEMPLATE = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/User/Telecaster Tones.xml"
NEURAL_TEMPLATE_ALT = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Default.xml"
NEURAL_OUTPUT_DIR = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints"

# Universal Audio Paths
BASE_UAD_PRESETS_DIR = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins"
PARADISE_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_paradise_guitar_studio")
PARADISE_TEMPLATE = os.path.join(PARADISE_DIR, "Non-Toneprints", "Boutique Warm Clean - Enigmatic.json")

LA2A_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_teletronix_la-2a_silver/Mike - Alternative.json")
LA2A_GRAY_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_teletronix_la-2a_gray/Mike - Adjusting Gain Staging.json")
HITSVILLE_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_hitsville_chambers/Mike Live Strings.json")
GALAXY_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_galaxy_tape_echo/WhereAmI.json")
STUDIO_D_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_studio_d_chorus/whereami.json")
VALHALLA_BASE = "/Library/Application Support/Valhalla DSP, LLC/ValhallaSupermassive/Presets/User/whereami.vpreset"

# Logic Pro Native Paths
LOGIC_EQ_BASE = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Channel EQ/FlatEQ.pst"
LOGIC_COMP_BASE_ALT = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Compressor/CompThreshNeg35.pst"
LOGIC_COMP_BASE_DEFAULT = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Compressor/DefaultComp.pst"
LOGIC_COMP_BASE = LOGIC_COMP_BASE_ALT if os.path.exists(LOGIC_COMP_BASE_ALT) else LOGIC_COMP_BASE_DEFAULT
LOGIC_SPACEDESIGNER_BASE = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Space Designer/TP-Wooden Studio Default.pst"

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

THR_MODELS = {
    "envelope": {
        "device": 2359296,
        "device_version": 22020194,
        "schema": "L6Preset",
        "version": 5,
        "outer_meta": { "original": 0, "pbn": 0, "premium": 0 },
        "default_tempo": 110,
        "gate_threshold_db": {
            "slope": 0.96,
            "ui_offset": 100,
            "min_db": -96.0,
            "max_db": 0.0,
            "default_ui": 65
        }
    },
    "amps": {
        "guitar": {
            "Classic":  { "Clean": "THR10C_Deluxe",  "Crunch": "THR10C_DC30", "Lead": "THR10_Lead",    "Hi Gain": "THR10_Modern", "Special": "THR10X_Brown1" },
            "Boutique": { "Clean": "THR10C_BJunior2", "Crunch": "THR30_SR101", "Lead": "THR30_Blondie", "Hi Gain": "THR30_FLead",  "Special": "THR10X_South" },
            "Modern":   { "Clean": "THR30_Carmen",    "Crunch": "THR10C_Mini", "Lead": "THR10_Brit",    "Hi Gain": "THR10X_Brown2","Special": "THR30_Stealth" }
        },
        "bass": { "Classic": "THR10_Bass_Eden_Marcus", "Boutique": "THR10_Bass_Mesa", "Modern": "THR30_JKBass2" },
        "acoustic": {
            "Condenser": "THR10_Aco_Condenser1",
            "Dynamic": "THR10_Aco_Dynamic1",
            "Tube": "THR10_Aco_Tube1",
            "Nylon": "THR10_Aco_Nylon1"
        },
        "flat": { "default": "THR10_Flat", "Classic": "THR10_Flat", "Boutique": "THR10_Flat_B", "Modern": "THR10_Flat_V", "V": "THR10_Flat_V", "A": "THR10_Flat_A", "B": "THR10_Flat_B", "plain": "THR10_Flat" }
    },
    "cabinets": {
        "British 4x12": 0,
        "American 4x12": 1,
        "Brown 4x12": 2,
        "Vintage 4x12": 3,
        "Fuel 4x12": 4,
        "Juicy 4x12": 5,
        "Mods 4x12": 6,
        "American 2x12": 7,
        "British 2x12": 8,
        "British Blues 2x12": 9,
        "Boutique 2x12": 10,
        "Yamaha 2x12": 11,
        "California 1x12": 12,
        "American 1x12": 13,
        "American 4x10": 14,
        "Boutique 1x12": 15,
        "None": 16,
        "Flat": 16,
        "BYPASS": 16
    },
    "fx": {
        "gate": {
            "group": "THRGroupGate",
            "asset": "noiseGate",
            "params": ["Thresh", "Decay"]
        },
        "compressor": {
            "group": "THRGroupFX1Compressor",
            "asset": "RedComp",
            "params": ["Sustain", "Level"]
        },
        "modulation": {
            "group": "THRGroupFX2Effect",
            "has_wetDry": True,
            "types": {
                "Chorus":   { "asset": "StereoSquareChorus", "params": ["Depth", "Feedback", "Freq", "Pre"] },
                "Tremolo":  { "asset": "BiasTremolo",        "params": ["Depth", "Speed"] },
                "Flanger":  { "asset": "L6Flanger",          "params": ["Depth", "Freq"] },
                "Phaser":   { "asset": "Phaser",             "params": ["Feedback", "Speed"] }
            }
        },
        "echo": {
            "group": "THRGroupFX3EffectEcho",
            "has_wetDry": True,
            "types": {
                "Tape":          { "asset": "TapeEcho",       "params": ["Time", "Bass", "Treble", "Feedback"] },
                "Digital Delay": { "asset": "L6DigitalDelay", "params": ["Time", "Bass", "Treble", "Feedback"] }
            }
        },
        "reverb": {
            "group": "THRGroupFX4EffectReverb",
            "has_wetDry": True,
            "types": {
                "Hall":   { "asset": "ReallyLargeHall", "params": ["Decay", "PreDelay", "Tone"] },
                "Plate":  { "asset": "LargePlate1",     "params": ["Decay", "PreDelay", "Tone"] },
                "Room":   { "asset": "SmallRoom1",      "params": ["Decay", "PreDelay", "Tone"] },
                "Spring": { "asset": "StandardSpring",  "params": ["Time", "Tone"] }
            }
        },
        "cab": {
            "group": "THRGroupCab",
            "asset": "speakerSimulator",
            "params": ["SpkSimType"]
        },
        "amp": {
            "group": "THRGroupAmp",
            "params": ["Drive", "Bass", "Mid", "Treble", "Master"]
        }
    },
    "all_known_assets": {
        "amps": [
            "THR10C_Deluxe", "THR10C_DC30", "THR10C_Mini", "THR10C_BJunior2",
            "THR10X_Brown1", "THR10X_Brown2", "THR10X_South",
            "THR10_Lead", "THR10_Modern", "THR10_Brit", "THR10_Flat", "THR10_Flat_A", "THR10_Flat_B", "THR10_Flat_V",
            "THR10_Bass_Eden_Marcus", "THR10_Bass_Mesa",
            "THR10_Aco_Condenser1", "THR10_Aco_Dynamic1", "THR10_Aco_Tube1", "THR10_Aco_Nylon1",
            "THR30_Carmen", "THR30_SR101", "THR30_Blondie", "THR30_FLead", "THR30_Stealth", "THR30_JKBass2"
        ],
        "fx_assets": [
            "noiseGate", "RedComp", "speakerSimulator",
            "StereoSquareChorus", "L6SineChorus", "BiasTremolo", "L6Flanger", "Phaser",
            "TapeEcho", "L6DigitalDelay",
            "ReallyLargeHall", "LargePlate1", "SmallRoom1", "StandardSpring"
        ]
    }
}

def detect_thr_device_id():
    """Best-effort detection of the connected THR-II device id."""
    rel = ["Yamaha", "THR Remote", "deviceConnection.json"]
    paths = []
    # Windows
    for env in ("APPDATA", "LOCALAPPDATA", "USERPROFILE"):
        base = os.environ.get(env)
        if base:
            paths.append(os.path.join(base, *rel))
            paths.append(os.path.join(base, "AppData", "Roaming", *rel))
    # macOS
    home = os.path.expanduser("~")
    paths.append(os.path.join(home, "Library", "Application Support", *rel))
    # Linux
    paths.append(os.path.join(home, ".config", *rel))

    for p in paths:
        try:
            if os.path.isfile(p):
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                dev = data.get("lastDeviceID")
                if isinstance(dev, int):
                    return dev
        except Exception:
            continue
    return 2359296  # Default fallback


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
            if val.startswith('{') and val.endswith('}'):
                # Parse inline dictionary
                inner_dict = {}
                pairs = val[1:-1].split(",")
                for pair in pairs:
                    if ":" in pair:
                        pk, _, pv = pair.partition(":")
                        pk = pk.strip()
                        pv = pv.strip()
                        if pv.startswith('"') and pv.endswith('"'):
                            pv = pv[1:-1]
                        elif pv.startswith("'") and pv.endswith("'"):
                            pv = pv[1:-1]
                        if pv == "":
                            pv = None
                        elif pv.lower() == "true":
                            pv = True
                        elif pv.lower() == "false":
                            pv = False
                        else:
                            try:
                                if "." in pv:
                                    pv = float(pv)
                                else:
                                    pv = int(pv)
                            except ValueError:
                                pass
                        inner_dict[pk] = pv
                val = inner_dict
            else:
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                elif val.startswith("'") and val.endswith("'"):
                    val = val[1:-1]
                
                # Type casting
                if val == "":
                    val = None
                elif isinstance(val, str) and val.lower() == "true":
                    val = True
                elif isinstance(val, str) and val.lower() == "false":
                    val = False
                elif isinstance(val, str):
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
    content = content.replace("**", "")
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
    content = content.replace("**", "")
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
        PERCENTAGE_KEYS = {
            "compressorBlend", "compressorCompression", "compressorVolume", "compressorTone",
            "bigRigDrive", "bigRigLevel", "bigRigTone",
            "tuberLevel", "tuberDrive", "tuberTone",
            "washMix", "washDecay", "washLowCut", "washHighCut",
            "snobVolume", "snobMaster", "snobBass", "snobMid", "snobTreble", "snobPresence", "snobOutputLevel",
            "cleanVolume", "cleanBass", "cleanMid", "cleanTreble", "cleanPresence", "cleanOutputLevel",
            "funkVolume", "funkTubeSat", "funkComp",
            "chorusMix", "chorusWidth", "chorusRate",
            "delayMix", "delayFeedback"
        }
        for k, v in amp_settings.items():
            if isinstance(v, bool):
                settings[k] = "true" if v else "false"
            elif isinstance(v, (int, float)) and k in PERCENTAGE_KEYS:
                # If value is greater than 1.0, scale it down to 0.0 - 1.0 (assuming it is on a 0-100 scale)
                if v > 1.0:
                    settings[k] = f"{float(v) / 100.0:.4f}"
                else:
                    settings[k] = f"{float(v):.4f}"
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

    # Enforce outer plugin input and output gain to 0.0 dB for gain staging
    settings["inputGain"] = "0.0"
    settings["outputGain"] = "0.0"

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

    boost_enable = None
    boost_amount = None
    reverb_val = None
    mod_val = None

    def to_bool(x):
        if isinstance(x, bool):
            return x
        return str(x).upper() in ("ON", "TRUE", "1", "ACTIVE", "BRIGHT", "YES")

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
        cut_sw = amp_settings.get("Cut")
        reverb_val = amp_settings.get("Reverb")
        mod_val = amp_settings.get("Mod")

        boost_raw = amp_settings.get("Boost")
        boost_sw_raw = amp_settings.get("Boost Switch")

        if boost_raw is not None:
            try:
                boost_amount = float(boost_raw)
            except ValueError:
                boost_enable = to_bool(boost_raw)

        if boost_sw_raw is not None:
            boost_enable = to_bool(boost_sw_raw)
        elif boost_amount is not None:
            boost_enable = boost_amount > 0.0
        
        # normalize types
        if vol is not None: vol = float(vol)
        if vol_mic is not None: vol_mic = float(vol_mic)
        if treble is not None: treble = float(treble)
        if mid is not None: mid = float(mid)
        if bass is not None: bass = float(bass)
        if presence is not None: presence = float(presence)
        if master is not None: master = float(master)
        if tone_cut is not None: tone_cut = float(tone_cut)
        if bright is not None: bright = to_bool(bright)
        if cut_sw is not None: cut_sw = to_bool(cut_sw)
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
        cut_sw = find_boolean_parameter(content, ["Cut Switch", "Cut"])
        reverb_val = find_numeric_parameter(content, ["Reverb"])

        boost_amount = find_numeric_parameter(content, ["Boost Control", "Boost (Stock)", "Boost"])
        boost_enable = find_boolean_parameter(content, ["Boost Switch", "Boost Button"])
        if boost_enable is None and boost_amount is not None:
            boost_enable = boost_amount > 0.0

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
        if boost_enable is not None: controls["dream_boost_enable"] = {"real_value": boost_enable}
        if boost_amount is not None: controls["dream_boost_amount"] = {"real_value": boost_amount}
        controls["dream_reverb_enable"] = {"real_value": True}
        controls["dream_reverb"] = {"real_value": float(reverb_val) if reverb_val is not None else 2.5}
        if mod_val is not None:
            mod_str = str(mod_val).upper()
            if "LEAD" in mod_str:
                controls["dream_amp_mod"] = {"real_value": 1}
            elif "TEX" in mod_str:
                controls["dream_amp_mod"] = {"real_value": 2}
            else:
                controls["dream_amp_mod"] = {"real_value": 0}
    elif amp_type == "enigmatic":
        if vol is not None: controls["enigmatic_volume"] = {"real_value": vol}
        if treble is not None: controls["enigmatic_treble"] = {"real_value": treble}
        if mid is not None: controls["enigmatic_middle"] = {"real_value": mid}
        if bass is not None: controls["enigmatic_bass"] = {"real_value": bass}
        if presence is not None: controls["enigmatic_presence"] = {"real_value": presence}
        if master is not None: controls["enigmatic_master_gain"] = {"real_value": master}
        if bright is not None: controls["enigmatic_bright_enable"] = {"real_value": bright}
        if boost_enable is not None: controls["enigmatic_boost_enable"] = {"real_value": boost_enable}
        voice_val = (amp_settings.get("Voice") or amp_settings.get("Model") or frontmatter.get("voice") if amp_settings else None)
        if voice_val:
            v_str = str(voice_val).upper()
            if "CREAM" in v_str:
                v_idx = 2
            elif "SANTA" in v_str:
                v_idx = 1
            elif "HRM" in v_str:
                v_idx = 3
            else:
                v_idx = 0 # Suede
        else:
            v_idx = 0
        controls["enigmatic_model"] = {"real_value": v_idx}
        controls["enigmatic_channel"] = {"real_value": 1}          # NOR
        controls["enigmatic_tone_stack_type"] = {"real_value": 0}  # Skyline
        controls["enigmatic_tone_stack_eq"] = {"real_value": 0}    # Jazz
        controls["enigmatic_overdrive_enable"] = {"real_value": False}
    elif amp_type == "ruby":
        if vol is not None: controls["ruby_volume"] = {"real_value": vol}
        if treble is not None: controls["ruby_treble"] = {"real_value": treble}
        if bass is not None: controls["ruby_bass"] = {"real_value": bass}
        if tone_cut is not None: controls["ruby_tone_cut"] = {"real_value": tone_cut}
        if boost_enable is not None: controls["ruby_boost_enable"] = {"real_value": boost_enable}
        if boost_amount is not None: controls["ruby_boost_amount"] = {"real_value": boost_amount}
        controls["ruby_channel"] = {"real_value": 2} # Brilliant
        controls["ruby_cut"] = {"real_value": 5.0 if cut_sw else 0.0}
    elif amp_type == "woodrow":
        if vol is not None: controls["woodrow_inst_volume"] = {"real_value": vol}
        if vol_mic is not None: controls["woodrow_mic_volume"] = {"real_value": vol_mic}
        if treble is not None: controls["woodrow_tone"] = {"real_value": treble}
        if boost_enable is not None: controls["woodrow_boost_enable"] = {"real_value": boost_enable}
        if boost_amount is not None: controls["woodrow_boost_amount"] = {"real_value": boost_amount}
    elif amp_type == "showtime":
        if vol is not None: controls["showtime_volume"] = {"real_value": vol}
        if treble is not None: controls["showtime_treble"] = {"real_value": treble}
        if mid is not None: controls["showtime_middle"] = {"real_value": mid}
        if bass is not None: controls["showtime_bass"] = {"real_value": bass}
        if bright is not None: controls["showtime_bright"] = {"real_value": bright}
    elif amp_type == "lion":
        # Lion '68 Super Lead / Super Bass mapping
        model = amp_settings.get("Model") if amp_settings else None
        vol1 = amp_settings.get("Volume I (Bite)") or amp_settings.get("Volume 1") or amp_settings.get("Volume_1") or amp_settings.get("Volume I") if amp_settings else None
        vol2 = amp_settings.get("Volume II (Body)") or amp_settings.get("Volume 2") or amp_settings.get("Volume_2") or amp_settings.get("Volume II") if amp_settings else None
        treble_val = amp_settings.get("Treble") if amp_settings else None
        mid_val = amp_settings.get("Middle") if amp_settings else None
        bass_val = amp_settings.get("Bass") if amp_settings else None
        presence_val = amp_settings.get("Presence") if amp_settings else None
        input_routing = amp_settings.get("Input Routing") or amp_settings.get("input_routing") or amp_settings.get("Input_Routing") or amp_settings.get("Input") if amp_settings else None
        ghost_notes = amp_settings.get("Ghost Notes") if amp_settings else None
        bright_cap = amp_settings.get("Bright Cap") if amp_settings else None
        boost_sw = amp_settings.get("Boost") if amp_settings else None
        room_val = amp_settings.get("Room") if amp_settings else None
        gate_val = amp_settings.get("Noise Gate") if amp_settings else None

        # 1. Amp Model (0 = LEAD, 1 = BASS, 2 = BROWN)
        if model is not None:
            model_str = str(model).upper()
            if "BASS" in model_str:
                model_idx = 1
            elif "BROWN" in model_str:
                model_idx = 2
            else:
                model_idx = 0 # default LEAD
            controls["lion_model"] = {"real_value": model_idx}
        else:
            controls["lion_model"] = {"real_value": 0} # default LEAD

        # 2. Volume Controls
        if vol1 is not None: controls["lion_volume_1"] = {"real_value": float(vol1)}
        if vol2 is not None: controls["lion_volume_2"] = {"real_value": float(vol2)}

        # 3. EQ Controls
        if treble_val is not None: controls["lion_treble"] = {"real_value": float(treble_val)}
        if mid_val is not None: controls["lion_middle"] = {"real_value": float(mid_val)}
        if bass_val is not None: controls["lion_bass"] = {"real_value": float(bass_val)}
        if presence_val is not None: controls["lion_presence"] = {"real_value": float(presence_val)}

        # 4. Input Routing
        ir_val = input_routing or (amp_settings.get("Input Routing") if amp_settings else None) or frontmatter.get("input_routing")
        if ir_val is not None:
            ir_str = str(ir_val).upper()
            if "LOW" in ir_str:
                ir_idx = 0
            elif "JUMP" in ir_str:
                ir_idx = 2
            else:
                ir_idx = 1 # HIGH
            controls["lion_input_routing"] = {"real_value": ir_idx}
        else:
            controls["lion_input_routing"] = {"real_value": 0} # default to Low for clean headroom

        # 5. Ghost Notes
        if ghost_notes is not None:
            gn_bool = True if str(ghost_notes).upper() in ("ON", "TRUE", "1") else False
            controls["lion_ghost_notes_mod"] = {"real_value": gn_bool}

        # 6. Bright Cap
        if bright_cap is not None:
            bc_val = 1 if str(bright_cap).upper() in ("ON", "TRUE", "1") else 0
            controls["lion_lead_amp_bright_cap"] = {"real_value": bc_val}
            controls["lion_brown_amp_bright_cap"] = {"real_value": bc_val}

        # 7. Boost Enable
        if boost_sw is not None:
            b_bool = True if str(boost_sw).upper() in ("ON", "TRUE", "1") else False
            controls["lion_boost_enable"] = {"real_value": b_bool}

        # 8. Room
        if room_val is not None:
            room_float = float(room_val)
            if room_float <= 10.0:
                room_float = room_float * 10.0 # scale 0-10 to 0-100%
            controls["room"] = {"real_value": room_float}

        # 9. Gate Controls
        if gate_val is not None:
            controls["gate_enable"] = {"real_value": True}
            controls["gate_threshold"] = {"real_value": float(gate_val)}

    # Enable prefx and postfx power racks and reset slots
    controls["prefx_power"] = {"real_value": True}
    controls["postfx_power"] = {"real_value": True}

    for s in range(1, 6):
        controls[f"prefx_{s}"] = {"real_value": 0}
        controls[f"prefx_{s}_power"] = {"real_value": False}
        controls[f"postfx_{s}"] = {"real_value": 0}
        controls[f"postfx_{s}_power"] = {"real_value": False}

    # Dynamic Pre-FX & Post-FX slot mapping from preset_data
    if isinstance(preset_data, dict):
        if "gold_overdrive" in preset_data:
            controls["prefx_1"] = {"real_value": 2} # Gold Overdrive ID = 2
            gold_info = preset_data["gold_overdrive"]
            if isinstance(gold_info, dict):
                controls["prefx_1_power"] = {"real_value": gold_info.get("enabled", False)}
                if "gain" in gold_info: controls["prefx_gold_overdrive_gain"] = {"real_value": float(gold_info["gain"])}
                if "output" in gold_info: controls["prefx_gold_overdrive_output"] = {"real_value": float(gold_info["output"])}
                if "treble" in gold_info: controls["prefx_gold_overdrive_treble"] = {"real_value": float(gold_info["treble"])}
        if "ep3_boost" in preset_data or "ep_iii" in preset_data:
            controls["prefx_2"] = {"real_value": 18} # EP-III Tape Echo ID = 18
            ep3_info = preset_data.get("ep3_boost") or preset_data.get("ep_iii")
            if isinstance(ep3_info, dict):
                controls["prefx_2_power"] = {"real_value": ep3_info.get("enabled", True)}
                controls["prefx_ep_iii_tape_echo_preamp_color"] = {"real_value": True}
        if "pgs_1176" in preset_data or "1176" in preset_data:
            controls["postfx_1"] = {"real_value": 14} # 1176 Compressor ID = 14
            c1176_info = preset_data.get("pgs_1176") or preset_data.get("1176")
            if isinstance(c1176_info, dict):
                controls["postfx_1_power"] = {"real_value": c1176_info.get("enabled", True)}
                controls["postfx_1176_compressor_input"] = {"real_value": float(c1176_info.get("input", -30.0))}
                controls["postfx_1176_compressor_output"] = {"real_value": float(c1176_info.get("output", -15.0))}

    # Inject overrides from frontmatter (supporting 1176, delays, plate reverbs, etc.)
    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            controls[k] = {"real_value": v}

    # Write output JSON preset file into model sub-directory
    model_subdirs = {
        0: "Dream '65",
        1: "Enigmatic '82",
        2: "Lion '68",
        3: "Ruby '63",
        4: "Showtime '64",
        5: "Woodrow '55"
    }
    model_subdir = model_subdirs.get(amp_index, "")
    out_dir = os.path.join(PARADISE_DIR, model_subdir) if model_subdir else PARADISE_DIR
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"Toneprint - {output_name}.json")
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
        if lead_sw is not None: amp_vars.set("AmpType", "1" if lead_sw else "0")

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
    # Float 10: Peak Reduction (scaled 0.0 to 1.0)
    if peak_reduction is not None:
        val_scaled = peak_reduction / 100.0
        struct.pack_into("f", chunk_bytes, 10 * 4, val_scaled)
    # Float 11: Gain (scaled 0.0 to 1.0)
    if gain is not None:
        val_scaled = gain / 100.0
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

    # Default values from text parsing or frontmatter
    if hitsville_data and isinstance(hitsville_data, dict):
        mix = hitsville_data.get("mix")
        pre_delay = hitsville_data.get("pre_delay")
        decay = hitsville_data.get("decay")
        chamber = hitsville_data.get("chamber")
        speaker = hitsville_data.get("speaker")
        mic = hitsville_data.get("mic")
        
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
        
        # Parse Chamber, Speaker, Mic from text
        chamber = None
        chamber_match = re.search(r"\|\s*Chamber\s*\|\s*\*\*([A-Za-z0-9/ ]+)\*\*", content, re.IGNORECASE)
        if chamber_match:
            chamber = chamber_match.group(1).strip()
            
        speaker = None
        speaker_match = re.search(r"\|\s*Speaker\s*\|\s*\*\*([A-Za-z0-9/ ]+)\*\*", content, re.IGNORECASE)
        if speaker_match:
            speaker = speaker_match.group(1).strip()
            
        mic = None
        mic_match = re.search(r"\|\s*Mic\s*\|\s*\*\*([A-Za-z0-9/ ]+)\*\*", content, re.IGNORECASE)
        if mic_match:
            mic = mic_match.group(1).strip()

    if mix is None and pre_delay is None and decay is None and chamber is None and speaker is None and mic is None:
        return False

    # Load base template JSON
    with open(base_preset_path, "r") as f:
        preset_data = json.load(f)

    # Decode chunk
    chunk_bytes = bytearray(base64.b64decode(preset_data["chunk"]))

    # 1. Chamber Select (Float 10: 0.0 = Chamber 1 / 2648, 1.0 = Chamber 2 / 2644)
    if chamber is not None:
        chamber_str = str(chamber).lower()
        if "2648" in chamber_str or "1" in chamber_str:
            val = 0.0
        elif "2644" in chamber_str or "2" in chamber_str:
            val = 1.0
        else:
            val = 0.0 # default Chamber 1
        struct.pack_into("f", chunk_bytes, 10 * 4, val)

    # 2. Speaker Select (Float 13: 0.0 = Set 1, 1.0 = Set 2)
    if speaker is not None:
        speaker_str = str(speaker).lower()
        if "bozak" in speaker_str or "altec" in speaker_str or "1" in speaker_str or "set 1" in speaker_str:
            val = 0.0
        elif "jbl" in speaker_str or "bose" in speaker_str or "2" in speaker_str or "set 2" in speaker_str:
            val = 1.0
        else:
            val = 0.0 # default Set 1
        struct.pack_into("f", chunk_bytes, 13 * 4, val)

    # 3. Microphone Select (Float 14: 0.0 = Unidyne 545, 1/3 = RCA 44-BX, 2/3 = EV 631, 1.0 = KM86)
    if mic is not None:
        mic_str = str(mic).lower()
        if "545" in mic_str or "unidyne" in mic_str or mic_str == "1":
            val = 0.0
        elif "rca" in mic_str or "44" in mic_str or mic_str == "2":
            val = 1.0 / 3.0
        elif "ev" in mic_str or "631" in mic_str or mic_str == "3":
            val = 2.0 / 3.0
        elif "km86" in mic_str or "km 86" in mic_str or mic_str == "4":
            val = 1.0
        else:
            val = 0.0 # default Unidyne 545
        struct.pack_into("f", chunk_bytes, 14 * 4, val)

    # 4. Pre-Delay (Float 17: logarithmic scaling)
    if pre_delay is not None:
        # Range: 0 to 250 ms. Using verified logarithmic scaling:
        # val_scaled = log(pre_delay / 22.9 + 1.0) / log(250.0 / 22.9 + 1.0)
        val_scaled = math.log(pre_delay / 22.9 + 1.0) / math.log(250.0 / 22.9 + 1.0)
        struct.pack_into("f", chunk_bytes, 17 * 4, val_scaled)

    # 5. Decay (Float 20: 0.0 to 1.0, e.g. 3.5s -> 0.35)
    if decay is not None:
        val_scaled = decay / 10.0
        struct.pack_into("f", chunk_bytes, 20 * 4, val_scaled)

    # 6. Mix (Float 21: 0.0 to 1.0)
    if mix is not None:
        val_scaled = mix / 100.0 if mix > 1.0 else mix
        struct.pack_into("f", chunk_bytes, 21 * 4, val_scaled)

    # 7. Internal Power Switch (Float 22: always force to 1.0 / On)
    struct.pack_into("f", chunk_bytes, 22 * 4, 1.0)

    # 8. EQ Low & High (Float 18 & 19: force to 0.5 / 0 dB midpoint)
    struct.pack_into("f", chunk_bytes, 18 * 4, 0.5)
    struct.pack_into("f", chunk_bytes, 19 * 4, 0.5)

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


# Helper parsing and scanning functions for Logic Space Designer Compiler
def parse_db_value(val_str):
    if not val_str:
        return None
    val_str_clean = val_str.lower().replace("−", "-")
    if "inf" in val_str_clean or "off" in val_str_clean or "∞" in val_str_clean:
        return -80.0
    match = re.search(r"([+-]?\d+(?:\.\d+)?)", val_str_clean)
    if match:
        return float(match.group(1))
    return None

def parse_space_designer_params(content):
    params = {
        "ir": None,
        "predelay": None,
        "size": None,
        "dry": None,
        "wet": None
    }
    in_section = False
    for line in content.split("\n"):
        line_lower = line.lower()
        # Look for Space Designer sections
        if "###" in line_lower and ("space designer" in line_lower or "reverb aux" in line_lower):
            in_section = True
            continue
        elif in_section and "###" in line:
            in_section = False
            
        if in_section and "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                key = parts[1].lower()
                val_str = parts[2]
                if "ir" in key:
                    params["ir"] = val_str
                elif "predelay" in key or "pre-delay" in key:
                    params["predelay"] = val_str
                elif "size" in key:
                    params["size"] = val_str
                elif "dry" in key:
                    params["dry"] = val_str
                elif "wet" in key:
                    params["wet"] = val_str
    return params

def get_sdir_list():
    base_dir = "/Users/miketremoulet/Music/Logic Pro Library.bundle/Impulse Responses"
    if not os.path.exists(base_dir):
        return []
    sdir_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(".sdir"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                sdir_files.append((rel_path, full_path))
    return sdir_files

def find_matching_sdir(text, sdir_list):
    if not text:
        return None
    text_lower = text.lower()
    best_match = None
    best_score = 0
    for rel_path, full_path in sdir_list:
        filename = os.path.basename(full_path).lower().replace(".sdir", "")
        clean_filename = re.sub(r'^[0-9.]+\s*[a-z_-]*', '', filename).strip()
        filename_words = set(re.findall(r'[a-z0-9]+', clean_filename))
        text_words = set(re.findall(r'[a-z0-9]+', text_lower))
        overlap = filename_words.intersection(text_words)
        if len(overlap) > best_score:
            best_score = len(overlap)
            best_match = (rel_path, full_path)
    return best_match

# Dynamic Logic Pro Native Space Designer PST Compiler
def compile_logic_space_designer_toneprint(filepath, base_preset_path, output_name, frontmatter):
    if not FOUNDATION_AVAILABLE:
        print("-> Warning: Foundation framework not available. Skipping Space Designer preset compilation.")
        return False

    with open(filepath, "r") as f:
        content = f.read()

    # Parse parameters from markdown table under Space Designer section
    params = parse_space_designer_params(content)

    # If no IR is specified, skip Space Designer generation
    if not params["ir"]:
        return False

    # Get SDIR list and find matching file
    sdirs = get_sdir_list()
    matched = find_matching_sdir(params["ir"], sdirs)
    if not matched:
        print(f"-> Warning: Could not find matching SDIR file for description '{params['ir']}'")
        return False

    rel_path, full_path = matched
    short_name = os.path.basename(full_path)
    print(f"-> Space Designer SDIR matched: '{short_name}' at path '{full_path}'")

    # Load base template preset
    if not os.path.exists(base_preset_path):
        print(f"-> Warning: Space Designer base template not found at {base_preset_path}")
        return False
        
    with open(base_preset_path, "rb") as f:
        template = bytearray(f.read())

    # Surgically patch the header fields:
    # 1. Filename length at offset 30
    template[30] = len(short_name)

    # 2. Short filename starting at 31
    # Clear out the short filename space (from 31 to 100)
    for i in range(31, 100):
        template[i] = 0
    template[31:31+len(short_name)] = short_name.encode('utf-8')

    # 3. Category/Folder index at byte 26
    byte26_val = 5
    if "Indoor Spaces" in full_path:
        byte26_val = 7
    elif "Plate Reverbs" in full_path:
        byte26_val = 3
    elif "Halls" in full_path:
        byte26_val = 2
    template[26] = byte26_val

    # 4. Surgically patch floats in header if specified in table
    # Dry parameter (offset 104)
    if params["dry"]:
        dry_val = parse_db_value(params["dry"])
        if dry_val is not None:
            struct.pack_into("f", template, 104, dry_val)

    # Wet parameter (offset 108)
    if params["wet"]:
        wet_val = parse_db_value(params["wet"])
        if wet_val is not None:
            struct.pack_into("f", template, 108, wet_val)

    # Predelay parameter (offset 112)
    if params["predelay"]:
        pre_match = re.search(r"(\d+(?:\.\d+)?)", params["predelay"])
        if pre_match:
            pre_val = float(pre_match.group(1)) # in ms
            struct.pack_into("f", template, 112, pre_val)

    # 5. Generate URL Bookmark
    try:
        url = NSURL.fileURLWithPath_(full_path)
        opt = NSURLBookmarkCreationSuitableForBookmarkFile
        bookmark_data, error = url.bookmarkDataWithOptions_includingResourceValuesForKeys_relativeToURL_error_(opt, None, None, None)
        if not bookmark_data:
            print(f"-> Error: Failed to generate bookmark data: {error}")
            return False
        bookmark_bytes = bytes(bookmark_data)
    except Exception as e:
        print(f"-> Error generating bookmark: {e}")
        return False

    # 6. Create binary plist payload
    plist_dict = {'CFileRef_Bookmark': bookmark_bytes}
    plist_payload = plistlib.dumps(plist_dict, fmt=plistlib.FMT_BINARY)
    plist_len = len(plist_payload)

    # Write plist size at 1572 (4 bytes little-endian)
    template[1572:1576] = struct.pack('<I', plist_len)

    # Write path starting at 1576
    # Clear out path space up to 3024
    for i in range(1576, 3024):
        template[i] = 0
    template[1576:1576+len(full_path)] = full_path.encode('utf-8')

    # 7. Assemble final bytes
    out_data = bytearray(template[:3024])
    out_data.extend(plist_payload)

    # Padding to offset 4189 with zeros if plist is shorter than 1165
    padding_len = 1165 - plist_len
    if padding_len > 0:
        out_data.extend(b'\x00' * padding_len)
    elif padding_len < 0:
        print(f"-> Warning: Plist length exceeds 1165 ({plist_len} bytes)")

    # Append static footer from template (offset 4189 to end, length 6179)
    footer = template[4189:]
    out_data.extend(footer)

    # 8. Patch Size float at offset 10196 in final file buffer (fixed size)
    if params["size"]:
        size_match = re.search(r"(\d+(?:\.\d+)?)", params["size"])
        if size_match:
            size_val = float(size_match.group(1)) # in percentage
            struct.pack_into("f", out_data, 10196, size_val)

    # Save to user presets folder
    output_dir = os.path.dirname(base_preset_path)
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(out_data)

    print(f"-> Compiled Logic Space Designer Preset: 'Toneprint - {output_name}'")
    return True


# Dynamic Yamaha THR-II JSON Compiler (.thrl6p)
def compile_yamaha_thr_toneprint(filepath, output_name, frontmatter):
    preset_data = frontmatter.get("preset_data", {})
    thr_data = preset_data.get("yamaha_thr") if isinstance(preset_data, dict) else None
    
    if not thr_data or not isinstance(thr_data, dict):
        return False

    # --------------------------------------------------------------------------- #
    # Nested Helpers
    # --------------------------------------------------------------------------- #
    _DEFAULT = 50
    
    def _norm(value) -> float:
        """Map a 0-100 knob value to a clamped 0.0-1.0 float."""
        try:
            v = float(value)
        except (TypeError, ValueError):
            v = float(_DEFAULT)
        return max(0.0, min(1.0, v / 100.0))

    def _gate_thresh_db(ui_value) -> float:
        """Map a 0-100 gate-threshold UI value to the dB value the device stores."""
        cfg = THR_MODELS["envelope"]["gate_threshold_db"]
        try:
            ui = float(ui_value)
        except (TypeError, ValueError):
            ui = float(cfg["default_ui"])
        db = (ui - cfg["ui_offset"]) * cfg["slope"]
        return round(max(cfg["min_db"], min(cfg["max_db"], db)), 2)

    def _canon_category(category: str) -> str:
        table = {
            "classic": "Classic", "boutique": "Boutique", "modern": "Modern",
            "bass": "Bass", "acoustic": "Acoustic", "aco": "Acoustic", "flat": "Flat",
        }
        key = table.get(str(category).strip().lower())
        if not key:
            raise ValueError(f"Unknown amp category {category!r}")
        return key

    def _canon_model(model: str | None, models: dict) -> str:
        if model is None:
            raise ValueError(f"amp spec needs a 'model'")
        aliases = {
            "clean": "Clean", "crunch": "Crunch", "lead": "Lead",
            "hi gain": "Hi Gain", "higain": "Hi Gain", "hi-gain": "Hi Gain",
            "high gain": "Hi Gain", "special": "Special",
        }
        key = aliases.get(str(model).strip().lower())
        if key is None or key not in models:
            raise ValueError(f"Unknown amp model {model!r}")
        return key

    def resolve_amp(category: str | None = None, model: str | None = None, *,
                    asset: str | None = None) -> str:
        if asset:
            if asset not in THR_MODELS["all_known_assets"]["amps"]:
                raise ValueError(f"Unknown amp asset {asset!r}")
            return asset

        if not category:
            raise ValueError("amp spec needs either 'asset' or 'category'")

        cat = _canon_category(category)
        amps = THR_MODELS["amps"]

        if cat in amps["guitar"]:
            models = amps["guitar"][cat]
            key = _canon_model(model, models)
            return models[key]
        if cat == "Bass":
            if model and model in amps["bass"]:
                return amps["bass"][model]
            return amps["bass"].get(_canon_category(model or "Classic"), amps["bass"]["Classic"])
        if cat == "Acoustic":
            return amps["acoustic"].get(model or "Condenser", amps["acoustic"]["Condenser"])
        if cat == "Flat":
            return amps["flat"].get(model or "default", amps["flat"]["default"])
        raise ValueError(f"Unknown amp category {category!r}")

    def resolve_cab(cab) -> int:
        cabs = THR_MODELS["cabinets"]
        if cab is None:
            return cabs["None"]
        if isinstance(cab, bool):
            raise ValueError(f"Invalid cab value {cab!r}")
        if isinstance(cab, int):
            return cab
        name = str(cab).strip()
        for key, val in cabs.items():
            if key.startswith("_"):
                continue
            if key.lower() == name.lower():
                return val
        raise ValueError(f"Unknown cabinet {cab!r}")

    def _block_params(spec_block: dict, device_params: list[str]) -> dict:
        out = {}
        for dev_key in device_params:
            out[dev_key] = _norm(spec_block.get(dev_key.lower(), _DEFAULT))
        return out

    def _match_type(name, types: dict) -> str:
        for key in types:
            if key.lower() == str(name).strip().lower():
                return key
        raise ValueError(f"Unknown FX type {name!r}")

    def _build_typed_fx(spec_block: dict, fx_def: dict, default_type: str) -> dict:
        types = fx_def["types"]
        type_name = spec_block.get("type", default_type)
        chosen = _match_type(type_name, types)
        asset = types[chosen]["asset"]
        block = {"@asset": asset, "@enabled": bool(spec_block.get("enabled", False))}
        block.update(_block_params(spec_block, types[chosen]["params"]))
        if fx_def.get("has_wetDry"):
            block["@wetDry"] = _norm(spec_block.get("mix", _DEFAULT))
        return block

    # --------------------------------------------------------------------------- #
    # Processing Spec
    # --------------------------------------------------------------------------- #
    try:
        env = THR_MODELS["envelope"]
        fx = THR_MODELS["fx"]

        # Resolve Amp
        amp_spec = thr_data.get("amp", {})
        amp_asset = resolve_amp(
            amp_spec.get("category"), amp_spec.get("model"), asset=amp_spec.get("asset")
        )

        # Resolve Cab
        cab_type = resolve_cab(thr_data.get("cab"))

        # Resolve EQ -> Amp Block
        eq = thr_data.get("eq", {})
        amp_block = {
            "@asset": amp_asset,
            "Drive": _norm(eq.get("gain", _DEFAULT)),
            "Bass": _norm(eq.get("bass", _DEFAULT)),
            "Mid": _norm(eq.get("mid", _DEFAULT)),
            "Treble": _norm(eq.get("treble", _DEFAULT)),
            "Master": _norm(eq.get("master", 70)),
        }

        # Compressor
        comp_spec = thr_data.get("compressor", {})
        comp_block = {
            "@asset": fx["compressor"]["asset"],
            "@enabled": bool(comp_spec.get("enabled", False)),
            "Sustain": _norm(comp_spec.get("sustain", 30)),
            "Level": _norm(comp_spec.get("level", 80)),
        }

        # Gate
        gate_spec = thr_data.get("gate", {})
        gate_block = {
            "@asset": fx["gate"]["asset"],
            "@enabled": bool(gate_spec.get("enabled", False)),
            "Thresh": _gate_thresh_db(gate_spec.get("thresh", env["gate_threshold_db"]["default_ui"])),
            "Decay": _norm(gate_spec.get("decay", 20)),
        }

        # Build complete JSON preset
        device_id = detect_thr_device_id()
        
        preset_json = {
            "schema": env["schema"],
            "version": env["version"],
            "data": {
                "device": device_id,
                "device_version": env["device_version"],
                "meta": {
                    "name": output_name,
                    "tnid": 0
                },
                "tone": {
                    "THRGroupGate": gate_block,
                    "THRGroupFX1Compressor": comp_block,
                    "THRGroupFX2Effect": _build_typed_fx(
                        thr_data.get("modulation", {}), fx["modulation"], "Chorus"),
                    "THRGroupFX3EffectEcho": _build_typed_fx(
                        thr_data.get("echo", {}), fx["echo"], "Tape"),
                    "THRGroupFX4EffectReverb": _build_typed_fx(
                        thr_data.get("reverb", {}), fx["reverb"], "Hall"),
                    "THRGroupCab": {"@asset": fx["cab"]["asset"], "SpkSimType": cab_type},
                    "THRGroupAmp": amp_block,
                    "global": {"THRPresetParamTempo": int(thr_data.get("tempo", env["default_tempo"]))},
                }
            },
            "meta": env["outer_meta"]
        }

        # Output directory
        os.makedirs(YAMAHA_THR_OUTPUT_DIR, exist_ok=True)
        out_path = os.path.join(YAMAHA_THR_OUTPUT_DIR, f"{output_name}.thrl6p")
        
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(preset_json, f, indent=4)
            f.write("\n")
            
        print(f"-> Compiled Yamaha THR Preset: '{output_name}'")
        return True

    except Exception as e:
        print(f"Error compiling Yamaha THR preset: {e}")
        return False


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

    # Normalize alias keys and special value types for Nembrini Audio plugins
    alias_map = {
        "puretone": {
            "DelayMix": "Mix",
            "DelayTime": "Time",
            "DelayFeedback": "Feedback",
            "DelaySpread": "Spread",
            "DelayNote": "Note",
            "DelayHostSync": "Sync",
            "EqHighPass": "EqHp",
            "EqLowPass": "EqLp",
            "NoiseGateRelease": "NoiseGateGate",
            "InputLevel": "InLevel",
            "Mic1Distance": "Mic1Dist",
            "Mic1Position": "Mic1Pos",
            "Mic2Distance": "Mic2Dist",
            "Mic2Position": "Mic2Pos",
            "CabinetMode": "CabMode",
            "CabinetType": "CabType"
        }
    }
    
    plugin_aliases = alias_map.get(plugin_type, {})
    normalized_settings = {}
    for k, v in plugin_settings.items():
        target_k = plugin_aliases.get(k, k)
        
        if target_k == "Feedback" and isinstance(v, str):
            if v.lower() in ["off", "none", "0", "0.0"]:
                v = 0.0
        elif target_k in ["CabMode", "CabinetMode"] and isinstance(v, str):
            v = 0.0 if v.lower() == "cabinet" else 1.0
        elif target_k in ["Mic1Type", "Mic2Type"] and isinstance(v, str):
            if "57" in v: v = 0.0
            elif "121" in v: v = 1.0
        elif target_k in ["CabType", "CabinetType"] and isinstance(v, str):
            if "tc 412" in v.lower() or "real" in v.lower() or "hughes" in v.lower():
                v = 1.0
        
        normalized_settings[target_k] = v
    plugin_settings = normalized_settings

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
    parser = argparse.ArgumentParser(description="Compile guitar toneprints into DAW plugin presets.")
    parser.add_argument("-f", "--filter", help="Filter target toneprints by filename, path, ID, or preset name substring (case-insensitive).")
    parser.add_argument("--file", help="Compile only a single specific toneprint file path (e.g. tones/humbuckers/my-tone.md).")
    args = parser.parse_args()
    filter_arg = args.filter.lower() if args.filter else None
    file_arg = args.file if args.file else None

    print("==================================================")
    print("RIG-WIDE TONEPRINT COMPILER & PRESET GENERATOR (V2)")
    if filter_arg:
        print(f"Filter active: compiling matching '{filter_arg}'")
    if file_arg:
        print(f"File active: compiling only '{file_arg}'")
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
    compiled_spacedesigner = 0
    
    for root, dirs, files in os.walk(TONES_DIR):
        for f in files:
            if not f.endswith(".md") or f == "INDEX.md":
                continue
            
            filepath = os.path.join(root, f)
            if file_arg:
                if os.path.abspath(filepath) != os.path.abspath(file_arg):
                    continue

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
                
            if filter_arg:
                t_id = frontmatter.get("id", "").lower()
                if filter_arg not in f.lower() and filter_arg not in filepath.lower() and filter_arg not in clean_name.lower() and filter_arg not in t_id:
                    continue
                
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
            elif any(x in amp_str.lower() for x in ["mrh810", "jcm800", "mrh"]):
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
            if "la-2a" in content.lower():
                compiled_any_la2a = False
                # Compile Gray if specified in the content
                if ("gray" in content.lower() or "grey" in content.lower()) and os.path.exists(LA2A_GRAY_BASE):
                    if compile_la2a_toneprint(filepath, LA2A_GRAY_BASE, clean_name, frontmatter):
                        compiled_la2a += 1
                        compiled_any_la2a = True
                # Compile Silver if specified, or as a default fallback
                if "silver" in content.lower() or not compiled_any_la2a:
                    if os.path.exists(LA2A_BASE):
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

            # Compile Logic Space Designer Presets if native templates exist
            if os.path.exists(LOGIC_SPACEDESIGNER_BASE):
                # Only compile if Space Designer is in toneprint
                if "space designer" in content.lower() or "reverb aux" in content.lower():
                    if compile_logic_space_designer_toneprint(filepath, LOGIC_SPACEDESIGNER_BASE, clean_name, frontmatter):
                        compiled_spacedesigner += 1

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
    print(f"  -> {compiled_la2a} UADx LA-2A presets in Silver/Gray folders")
    print(f"  -> {compiled_hitsville} UADx Hitsville presets in {os.path.dirname(HITSVILLE_BASE)}")
    print(f"  -> {compiled_logiceq} Logic Channel EQ presets in {os.path.dirname(LOGIC_EQ_BASE)}")
    print(f"  -> {compiled_logiccomp} Logic Compressor presets in {os.path.dirname(LOGIC_COMP_BASE)}")
    print(f"  -> {compiled_spacedesigner} Logic Space Designer presets in {os.path.dirname(LOGIC_SPACEDESIGNER_BASE)}")
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
