#!/usr/bin/env python3
import os
import re

# Base DNA Template Preset
TEMPLATE_PATH = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/User/Telecaster Tones.xml"
TEMPLATE_PATH_ALT = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Default.xml"

# Target dedicated preset folder Mike created
OUTPUT_DIR = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints"

# Map of markdown source files to output preset names
TONEPRINT_SOURCES = [
    {
        "source_path": "tones/humbuckers/cory-wong-amp-snob-boutique-clean.md",
        "preset_name": "Amp Snob Boutique Clean HB"
    },
    {
        "source_path": "tones/p-90s/cory-wong-amp-snob-p90.md",
        "preset_name": "Amp Snob Boutique Clean P90"
    }
]

# Custom Binary Parameter Replacer
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

# Markdown Parser
def parse_markdown_toneprint(filepath):
    if not os.path.exists(filepath):
        print(f"Warning: Toneprint file not found at {filepath}")
        return None
        
    with open(filepath, "r") as f:
        content = f.read()
    
    settings = {}
    
    # 1. Parse Compressor (The 4th Position Compressor)
    comp_active = re.search(r"Compressor\*\*\s*\|\s*\*\*Active\*\*\s*\|\s*\*\*([A-Z]+)\*\*", content)
    if comp_active:
        settings["compressorActive"] = "true" if comp_active.group(1) == "ON" else "false"
    
    for key in ["Blend", "Tone", "Compression", "Volume"]:
        match = re.search(r"\|\s*\|\s*\*\*" + key + r"\*\*\s*\|\s*\*\*([0-9]+)%\*\*", content)
        if match:
            settings["compressor" + key] = f"{float(match.group(1)) / 100.0:.2f}"

    # 2. Parse Amp Knobs (The Amp Snob / Amp 3)
    settings["selectedAmp"] = "2"  # Amp 3 (index 2)
    settings["selectedCab"] = "2"  # Snob 2x12 Cab (index 2)
    
    knob_mappings = {
        "snobBass": r"\|\s*Bass\s*\|\s*\*\*([0-9]+)%\*\*",
        "snobMid": r"\|\s*Middle\s*\|\s*\*\*([0-9]+)%\*\*",
        "snobTreble": r"\|\s*Treble\s*\|\s*\*\*([0-9]+)%\*\*",
        "snobPresence": r"\|\s*Presence\s*\|\s*\*\*([0-9]+)%\*\*",
        "snobMaster": r"\|\s*Master\s*\|\s*\*\*([0-9]+)%\*\*",
        "snobVolume": r"\|\s*Volume\s*\(Gain\)\s*\|\s*\*\*([0-9]+)%\*\*",
        "snobOutputLevel": r"\|\s*Output\s*\|\s*\*\*([0-9]+)%\*\*"
    }
    
    for param, regex in knob_mappings.items():
        match = re.search(regex, content)
        if match:
            settings[param] = f"{float(match.group(1)) / 100.0:.2f}"
            
    drive_match = re.search(r"\|\s*Drive\s*Switch\s*\|\s*\*\*([A-Z]+)\*\*", content)
    if drive_match:
        settings["snobDrive"] = "true" if drive_match.group(1) == "ON" else "false"
        
    bright_match = re.search(r"\|\s*Bright\s*Switch\s*\|\s*\*\*([A-Z]+)\*\*", content)
    if bright_match:
        settings["snobBright"] = "true" if bright_match.group(1) == "ON" else "false"

    # 3. Parse Cabinet Settings
    link_match = re.search(r"\|\s*Amp/Cab\s*Link\s*\|\s*\*\*([a-zA-Z\s/-]+)\*\*", content)
    if link_match:
        settings["ampCabLinkedState"] = "false" if "Off" in link_match.group(1) else "true"
        
    pos_match = re.search(r"\|\s*Position\s*L\s*\|\s*\*\*([0-9.]+)\*\*", content)
    if pos_match:
        settings["leftCabPosition"] = pos_match.group(1)
        
    dist_match = re.search(r"\|\s*Distance\s*L\s*\|\s*\*\*([0-9.]+)\*\*", content)
    if dist_match:
        settings["leftCabDistance"] = dist_match.group(1)
        
    room_match = re.search(r"\|\s*Room\s*Send\s*L\s*\|\s*\*\*([0-9.+-]+)\s*dB\*\*", content)
    if room_match:
        settings["leftRoomMicLevel"] = f"{float(room_match.group(1)):.1f}"

    settings["leftCabActive"] = "true"
    settings["leftCab0MicType"] = "4"  # Ribbon 121
    settings["rightCabActive"] = "false" # Bypassed

    # 4. Parse EQ Bands (1 to 9)
    eq_match = re.search(r"\|\s*EQ\s*Status\s*\|\s*\*\*([a-zA-Z]+)\*\*", content)
    if eq_match:
        settings["snobEQActive"] = "true" if eq_match.group(1) == "Active" else "false"
        
    bands = ["65 Hz", "125 Hz", "250 Hz", "500 Hz", "1 kHz", "2 kHz", "4 kHz", "8 kHz", "16 kHz"]
    for i, band in enumerate(bands, 1):
        match = re.search(r"\|\s*" + band + r"\s*\|\s*([0-9.+-−]+)\s*dB", content)
        if match:
            val_str = match.group(1).replace("−", "-")
            settings[f"snobEQBand{i}"] = f"{float(val_str):.1f}"

    settings["snobEQHpf"] = "20.0"
    settings["snobEQLpf"] = "20000.0"

    # 5. Default Bypassed Pedals
    settings["tuberActive"] = "false"
    settings["bigRigActive"] = "false"
    settings["postalActive"] = "false"
    settings["delayActive"] = "false"
    settings["washActive"] = "false"
    settings["chorusActive"] = "false"

    return settings

def main():
    print("--------------------------------------------------")
    print("NEURAL DSP TONEPRINT COMPILER (ARCHETYPE CORY WONG X)")
    print("--------------------------------------------------")
    
    # 1. Load the DNA Template
    if os.path.exists(TEMPLATE_PATH):
        template_file = TEMPLATE_PATH
    elif os.path.exists(TEMPLATE_PATH_ALT):
        template_file = TEMPLATE_PATH_ALT
    else:
        print("Error: No base Archetype Cory Wong X template preset found!")
        return

    print(f"Using template DNA: {template_file}")
    with open(template_file, "rb") as f:
        base_data = f.read()

    # 2. Compile each Toneprint
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    compiled_count = 0
    for tone in TONEPRINT_SOURCES:
        source = tone["source_path"]
        name = tone["preset_name"]
        print(f"\nProcessing toneprint: {source}...")
        
        # Parse Markdown
        parsed_settings = parse_markdown_toneprint(source)
        if not parsed_settings:
            continue
            
        # Add metadata name
        parsed_settings["name"] = name
        
        # Clone template and inject parameters
        preset_data = base_data
        for key, val in parsed_settings.items():
            preset_data = replace_binary_parameter(preset_data, key, val)
            
        # Write to dedicated Toneprints folder
        out_path = os.path.join(OUTPUT_DIR, f"{name}.xml")
        with open(out_path, "wb") as f:
            f.write(preset_data)
            
        print(f"-> SUCCESS: Saved native preset: '{name}' to {out_path}")
        compiled_count += 1

    print("\n--------------------------------------------------")
    print(f"Compilation Complete! Successfully injected {compiled_count} presets.")
    print(f"Preset Directory: {OUTPUT_DIR}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
