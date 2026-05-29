#!/usr/bin/env python3
import os

# Paths
TEMPLATE_PATH = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/User/Telecaster Tones.xml"
OUTPUT_DIR = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/User"
OUTPUT_FILENAME = "Amp Snob Boutique Warm Clean.xml"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)

# Custom Binary Parameter Replacer
def replace_binary_parameter(data, param_name, new_val_str):
    search_bytes = param_name.encode("utf-8") + b"\x00\x01"
    idx = data.find(search_bytes)
    if idx == -1:
        # Some parameters might be in a different submodel or not present
        return data
    
    length_byte_idx = idx + len(search_bytes)
    old_length = data[length_byte_idx]
    
    replace_start = length_byte_idx
    replace_end = length_byte_idx + 1 + old_length
    
    new_val_bytes = new_val_str.encode("utf-8")
    new_length = len(new_val_bytes) + 2
    new_block = bytes([new_length, 0x05]) + new_val_bytes + b"\x00"
    
    return data[:replace_start] + new_block + data[replace_end:]

def main():
    print(f"Loading base preset DNA template from: {TEMPLATE_PATH}...")
    if not os.path.exists(TEMPLATE_PATH):
        # Fallback to default if Telecaster Tones is missing
        TEMPLATE_PATH_ALT = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Default.xml"
        if os.path.exists(TEMPLATE_PATH_ALT):
            template_file = TEMPLATE_PATH_ALT
        else:
            print("Error: No base Archetype Cory Wong X template preset found!")
            return
    else:
        template_file = TEMPLATE_PATH

    with open(template_file, "rb") as f:
        data = f.read()

    # Define all values for "Amp Snob — Boutique Warm Clean"
    preset_settings = {
        # Metadata
        "name": "Amp Snob Boutique Warm Clean",
        "selectedAmp": "2",            # The Amp Snob is Amp 3 (index 2)
        "selectedCab": "2",            # Snob 2x12 Cab (index 2)
        "ampCabLinkedState": "false",  # Unlinked Cabinets

        # Compressor (The 4th Position Compressor)
        "compressorActive": "true",
        "compressorBlend": "0.40",     # 40%
        "compressorCompression": "0.35", # 35%
        "compressorTone": "0.50",      # 50%
        "compressorVolume": "0.55",    # 55%

        # Bypassed Pre-FX
        "tuberActive": "false",
        "bigRigActive": "false",
        "postalActive": "false",

        # Amp Settings (The Amp Snob)
        "snobVolume": "0.42",          # 42%
        "snobMaster": "0.75",          # 75%
        "snobDrive": "false",
        "snobBright": "false",
        "snobBass": "0.46",            # 46%
        "snobMid": "0.58",             # 58%
        "snobTreble": "0.48",          # 48%
        "snobPresence": "0.50",        # 50%
        "snobOutputLevel": "0.70",     # 70%

        # Cabinet Left (Active close-mic Ribbon 121)
        "leftCabActive": "true",
        "leftCab0MicType": "4",        # Ribbon 121
        "leftCabPosition": "0.48",     # 0.48
        "leftCabDistance": "0.25",     # 0.25
        "leftRoomMicLevel": "-28.0",   # -28.0 dB room send

        # Cabinet Right (Bypassed for phase coherence)
        "rightCabActive": "false",

        # 9-Band Graphic EQ Settings
        "snobEQActive": "true",
        "snobEQBand1": "0.0",          # 65 Hz
        "snobEQBand2": "-0.5",         # 125 Hz
        "snobEQBand3": "-1.5",         # 250 Hz (Humbucker neck mud cut)
        "snobEQBand4": "1.0",          # 500 Hz (Vocal warmth boost)
        "snobEQBand5": "1.5",          # 1 kHz (Dumble mid singing boost)
        "snobEQBand6": "-1.0",         # 2 kHz (Pick hash cut)
        "snobEQBand7": "0.0",          # 4 kHz
        "snobEQBand8": "0.0",          # 8 kHz
        "snobEQBand9": "0.0",          # 16 kHz
        "snobEQHpf": "20.0",
        "snobEQLpf": "20000.0",

        # Bypassed Post-FX
        "delayActive": "false",
        "washActive": "false",
        "chorusActive": "false"
    }

    print("Injecting Boutique Warm Clean parameters...")
    for key, val in preset_settings.items():
        data = replace_binary_parameter(data, key, val)

    print(f"Saving compiled preset to: {OUTPUT_PATH}...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    print("\nSUCCESS! The preset was successfully injected and saved.")
    print("You can now open Logic Pro, open Archetype Cory Wong X, and select")
    print('\"Amp Snob Boutique Warm Clean\" from your User presets menu!')

if __name__ == "__main__":
    main()
