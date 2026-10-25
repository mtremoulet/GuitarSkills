#!/usr/bin/env python3
"""
Digital Comparison Preset Compiler.

Generates native presets for both Universal Audio Paradise Guitar Studio (.json)
and Neural DSP Archetype Cory Wong X (.xml) for the Tone King Imperial toneprint suite,
enabling an all-digital workflow and direct cross-amp comparison across:
1. Tone King Imperial Preamp (Physical Tube Hardware)
2. UADx Paradise Guitar Studio (Component-Modeled DSP)
3. Neural DSP Archetype Cory Wong X (Algorithmic / Machine-Modeled DSP)
"""

from __future__ import annotations

import os
import sys
import json
import uuid
from pathlib import Path
from typing import Dict, Any

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from scripts.utils.config import (
    NEURAL_TEMPLATE,
    NEURAL_TEMPLATE_ALT,
    NEURAL_OUTPUT_DIR,
    PARADISE_DIR,
    PARADISE_TEMPLATE,
)
from scripts.preset_compiler.base import replace_binary_parameter

PERCENTAGE_KEYS = {
    "compressorBlend", "compressorCompression", "compressorVolume", "compressorTone",
    "bigRigDrive", "bigRigLevel", "bigRigTone",
    "tuberLevel", "tuberDrive", "tuberTone",
    "washMix", "washDecay", "washLowCut", "washHighCut",
    "snobVolume", "snobMaster", "snobBass", "snobMid", "snobTreble", "snobPresence", "snobOutputLevel",
    "cleanVolume", "cleanBass", "cleanMid", "cleanTreble", "cleanPresence", "cleanOutputLevel",
    "funkVolume", "funkTubeSat", "funkComp",
    "chorusMix", "chorusWidth", "chorusRate",
    "delayMix", "delayFeedback",
}

COMPARISON_PRESETS = [
    {
        "id": "midnight-velvet-archtop",
        "name": "Midnight Velvet Archtop",
        "paradise": {
            "folder": "Dream '65",
            "amp_index": 0,
            "cab_index": 29,
            "controls": {
                "dream_volume": 2.5,
                "dream_treble": 3.5,
                "dream_bass": 4.8,
                "dream_bright": False,
                "dream_reverb": 2.5,
                "dream_reverb_enable": True,
                "dream_amp_mod": 0,
                "dream_boost_enable": False,
                "output": 12.0,
            },
            "prefx": {},
            "postfx": {
                1: {"pedal": 8, "power": True},  # Brigade Chorus (subtle Mode 1 widening)
            },
        },
        "neural": {
            "selectedAmp": "1",  # The Clean Machine
            "selectedCab": "2",
            "ampCabLinkedState": "false",
            "leftCabActive": "true",
            "leftCab0MicType": "4",
            "leftCabPosition": "0.48",
            "leftCabDistance": "0.25",
            "leftRoomMicLevel": "-28.0",
            "rightCabActive": "false",
            "cleanVolume": "0.3000",
            "cleanBass": "0.4500",
            "cleanMid": "0.6500",
            "cleanTreble": "0.4000",
            "cleanPresence": "0.5000",
            "cleanBright": "false",
            "cleanOutputLevel": "0.7000",
            "cleanEQActive": "true",
            "cleanEQBand1": "0.0",
            "cleanEQBand2": "-0.5",
            "cleanEQBand3": "-2.0",
            "cleanEQBand4": "1.5",
            "cleanEQBand5": "1.0",
            "cleanEQBand6": "-1.0",
            "cleanEQBand7": "-1.5",
            "cleanEQBand8": "0.0",
            "cleanEQBand9": "0.0",
            "compressorActive": "true",
            "compressorBlend": "0.4500",
            "compressorCompression": "0.3000",
            "compressorTone": "0.4500",
            "compressorVolume": "0.5500",
            "washActive": "true",
            "washMix": "0.1500",
            "washDecay": "0.3500",
            "washShimmer": "false",
            "tuberActive": "false",
            "bigRigActive": "false",
            "postalActive": "false",
            "chorusActive": "false",
            "delayActive": "false",
        },
    },
    {
        "id": "tokyo-neon-1984",
        "name": "Tokyo Neon 1984",
        "paradise": {
            "folder": "Dream '65",
            "amp_index": 0,
            "cab_index": 29,
            "controls": {
                "dream_volume": 3.2,
                "dream_treble": 6.5,
                "dream_bass": 4.8,
                "dream_bright": True,
                "dream_reverb": 1.5,
                "dream_reverb_enable": True,
                "dream_amp_mod": 0,
                "dream_boost_enable": False,
                "output": 12.0,
            },
            "prefx": {
                1: {"pedal": 14, "power": True},  # 1176 Compressor (parallel funk squeeze)
            },
            "postfx": {
                1: {"pedal": 8, "power": True},   # Brigade Chorus
                2: {"pedal": 17, "power": True},  # Digital Delay (slapback)
            },
        },
        "neural": {
            "selectedAmp": "1",  # The Clean Machine
            "selectedCab": "2",
            "ampCabLinkedState": "false",
            "leftCabActive": "true",
            "leftCab0MicType": "4",
            "leftCabPosition": "0.50",
            "leftCabDistance": "0.22",
            "leftRoomMicLevel": "-24.0",
            "rightCabActive": "false",
            "cleanVolume": "0.2800",
            "cleanBass": "0.4800",
            "cleanMid": "0.3800",
            "cleanTreble": "0.6200",
            "cleanPresence": "0.5200",
            "cleanBright": "true",
            "cleanOutputLevel": "0.5000",
            "cleanEQActive": "false",
            "compressorActive": "true",
            "compressorBlend": "0.6000",
            "compressorCompression": "0.4500",
            "compressorTone": "0.5000",
            "compressorVolume": "0.5500",
            "chorusActive": "true",
            "chorusMix": "0.4000",
            "chorusRate": "0.2500",
            "chorusWidth": "0.3500",
            "delayActive": "true",
            "delayMix": "0.2000",
            "delayFeedback": "0.1000",
            "washActive": "false",
            "tuberActive": "false",
            "bigRigActive": "false",
            "postalActive": "false",
        },
    },
    {
        "id": "smoky-tweed-roots",
        "name": "Smoky Tweed Roots",
        "paradise": {
            "folder": "Woodrow '55",
            "amp_index": 5,
            "cab_index": 32,
            "controls": {
                "woodrow_inst_volume": 3.2,
                "woodrow_mic_volume": 2.5,
                "woodrow_tone": 5.0,
                "woodrow_boost_enable": False,
                "woodrow_boost_type": 0,
                "woodrow_boost_amount": 1.0,
                "output": 12.0,
            },
            "prefx": {},
            "postfx": {
                1: {"pedal": 12, "power": True},  # Trem '65 (bias-style pulse)
                2: {"pedal": 18, "power": True},  # EP-III Tape Delay
            },
        },
        "neural": {
            "selectedAmp": "2",  # The Amp Snob (Drive OFF = Tweed edge-of-breakup)
            "selectedCab": "2",
            "ampCabLinkedState": "false",
            "leftCabActive": "true",
            "leftCab0MicType": "4",
            "leftCabPosition": "0.45",
            "leftCabDistance": "0.28",
            "leftRoomMicLevel": "-22.0",
            "rightCabActive": "false",
            "snobDrive": "false",
            "snobBright": "false",
            "snobVolume": "0.5800",
            "snobMaster": "0.7000",
            "snobBass": "0.5800",
            "snobMid": "0.5500",
            "snobTreble": "0.4200",
            "snobPresence": "0.3800",
            "snobOutputLevel": "0.5500",
            "snobEQActive": "true",
            "snobEQBand1": "0.0",
            "snobEQBand2": "1.5",
            "snobEQBand3": "1.5",
            "snobEQBand4": "1.0",
            "snobEQBand5": "0.0",
            "snobEQBand6": "-0.5",
            "snobEQBand7": "-1.5",
            "snobEQBand8": "0.0",
            "snobEQBand9": "0.0",
            "delayActive": "true",
            "delayMix": "0.2200",
            "delayFeedback": "0.2000",
            "washActive": "true",
            "washMix": "0.1500",
            "washDecay": "0.2500",
            "washShimmer": "false",
            "compressorActive": "false",
            "tuberActive": "false",
            "bigRigActive": "false",
            "postalActive": "false",
            "chorusActive": "false",
        },
    },
    {
        "id": "mayer-trinity-vocal-lead",
        "name": "Mayer Trinity Vocal Lead",
        "paradise": {
            "folder": "Enigmatic '82",
            "amp_index": 1,
            "cab_index": 2,
            "controls": {
                "enigmatic_volume": 5.0,
                "enigmatic_master_gain": 7.8,
                "enigmatic_middle": 7.0,
                "enigmatic_treble": 5.0,
                "enigmatic_bass": 4.4,
                "enigmatic_presence": 4.2,
                "enigmatic_model": 2,  # Cream
                "enigmatic_channel": 1,
                "enigmatic_bright_enable": False,
                "enigmatic_boost_enable": False,
                "output": 12.0,
            },
            "prefx": {
                1: {"pedal": 5, "power": True},  # TS Overdrive
            },
            "postfx": {
                1: {"pedal": 21, "power": True},  # Plate 140 Reverb
            },
        },
        "neural": {
            "selectedAmp": "2",  # The Amp Snob (Drive ON = Dumble/Plexi Lead)
            "selectedCab": "2",
            "ampCabLinkedState": "false",
            "leftCabActive": "true",
            "leftCab0MicType": "4",
            "leftCabPosition": "0.50",
            "leftCabDistance": "0.20",
            "leftRoomMicLevel": "-20.0",
            "rightCabActive": "false",
            "snobDrive": "true",
            "snobBright": "false",
            "snobVolume": "0.6200",
            "snobMaster": "0.6500",
            "snobBass": "0.4200",
            "snobMid": "0.7500",
            "snobTreble": "0.4800",
            "snobPresence": "0.4500",
            "snobOutputLevel": "0.5000",
            "tuberActive": "true",
            "tuberDrive": "0.2500",
            "tuberLevel": "0.7000",
            "tuberTone": "0.4000",
            "snobEQActive": "true",
            "snobEQBand1": "0.0",
            "snobEQBand2": "-2.0",
            "snobEQBand3": "0.0",
            "snobEQBand4": "1.0",
            "snobEQBand5": "2.5",
            "snobEQBand6": "1.5",
            "snobEQBand7": "0.0",
            "snobEQBand8": "-0.5",
            "snobEQBand9": "0.0",
            "delayActive": "true",
            "delayMix": "0.2500",
            "delayFeedback": "0.2800",
            "chorusActive": "true",
            "chorusMix": "0.1500",
            "chorusRate": "0.1500",
            "chorusWidth": "0.4000",
            "washActive": "false",
            "compressorActive": "false",
            "bigRigActive": "false",
            "postalActive": "false",
        },
    },
    {
        "id": "nordic-cathedral",
        "name": "Nordic Cathedral",
        "paradise": {
            "folder": "Dream '65",
            "amp_index": 0,
            "cab_index": 29,
            "controls": {
                "dream_volume": 2.5,
                "dream_treble": 3.5,
                "dream_bass": 6.0,
                "dream_bright": False,
                "dream_reverb": 3.5,
                "dream_reverb_enable": True,
                "dream_vibrato_enable": True,
                "dream_speed": 2.5,
                "dream_intensity": 3.5,
                "dream_amp_mod": 0,
                "output": 12.0,
            },
            "prefx": {},
            "postfx": {
                1: {"pedal": 18, "power": True},  # EP-III Tape Delay
                2: {"pedal": 22, "power": True},  # Reverb 224 (Concert Hall wash)
            },
        },
        "neural": {
            "selectedAmp": "1",  # The Clean Machine
            "selectedCab": "1",
            "ampCabLinkedState": "false",
            "leftCabActive": "true",
            "leftCab0MicType": "4",
            "leftCabPosition": "0.52",
            "leftCabDistance": "0.30",
            "leftRoomMicLevel": "-18.0",
            "rightCabActive": "false",
            "cleanVolume": "0.2500",
            "cleanBass": "0.6800",
            "cleanMid": "0.4500",
            "cleanTreble": "0.3200",
            "cleanPresence": "0.2500",
            "cleanBright": "false",
            "cleanOutputLevel": "0.5500",
            "cleanEQActive": "false",
            "compressorActive": "true",
            "compressorBlend": "0.5000",
            "compressorCompression": "0.3500",
            "compressorTone": "0.4500",
            "compressorVolume": "0.5500",
            "delayActive": "true",
            "delayMix": "0.3000",
            "delayFeedback": "0.4500",
            "washActive": "true",
            "washMix": "0.4500",
            "washDecay": "0.7000",
            "washShimmer": "true",
            "washLowCut": "120.0",
            "washHighCut": "5000.0",
            "tuberActive": "false",
            "bigRigActive": "false",
            "postalActive": "false",
            "chorusActive": "false",
        },
    },
]


def compile_paradise_preset(p_info: Dict[str, Any], base_json: Dict[str, Any]) -> bytes:
    data = json.loads(json.dumps(base_json))
    name = f"Toneprint - {p_info['name']}"
    data["name"] = name
    data["uid"] = uuid.uuid4().hex

    controls = data["chunk"]["controls"]
    p_cfg = p_info["paradise"]
    controls["amp"] = {"real_value": p_cfg["amp_index"]}
    controls["cab_and_mic"] = {"real_value": p_cfg["cab_index"]}

    for k, v in p_cfg["controls"].items():
        controls[k] = {"real_value": v}

    # Clear prefx
    for i in range(1, 6):
        controls[f"prefx_{i}"] = {"real_value": 0}
        controls[f"prefx_{i}_power"] = {"real_value": False}

    for slot, cfg in p_cfg.get("prefx", {}).items():
        controls[f"prefx_{slot}"] = {"real_value": cfg["pedal"]}
        controls[f"prefx_{slot}_power"] = {"real_value": cfg["power"]}

    # Clear postfx
    for i in range(1, 6):
        controls[f"postfx_{i}"] = {"real_value": 0}
        controls[f"postfx_{i}_power"] = {"real_value": False}

    for slot, cfg in p_cfg.get("postfx", {}).items():
        controls[f"postfx_{slot}"] = {"real_value": cfg["pedal"]}
        controls[f"postfx_{slot}_power"] = {"real_value": cfg["power"]}

    return json.dumps(data, indent=4).encode("utf-8")


def compile_neural_preset(p_info: Dict[str, Any], base_bytes: bytes) -> bytes:
    name = f"Toneprint - {p_info['name']}"
    settings = {"name": name}
    for k, v in p_info["neural"].items():
        settings[k] = v

    data = base_bytes
    for k, v in settings.items():
        data = replace_binary_parameter(data, k, v)
    return data


def main():
    print("==================================================")
    print("COMPILING DIGITAL COMPARISON PRESETS")
    print("UAD Paradise (.json) & Archetype Cory Wong X (.xml)")
    print("==================================================")

    with open(PARADISE_TEMPLATE, "r") as f:
        paradise_base = json.load(f)

    neural_tpl = NEURAL_TEMPLATE if NEURAL_TEMPLATE.exists() else NEURAL_TEMPLATE_ALT
    with open(neural_tpl, "rb") as f:
        neural_base = f.read()

    repo_paradise_dir = WORKSPACE_ROOT / "tones" / "presets" / "paradise"
    repo_neural_dir = WORKSPACE_ROOT / "tones" / "presets" / "neural"
    repo_paradise_dir.mkdir(parents=True, exist_ok=True)
    repo_neural_dir.mkdir(parents=True, exist_ok=True)

    quarantined_paradise_base = (
        WORKSPACE_ROOT / "quarantined" / "Documents" / "Universal Audio" / "Presets" / "Plug-Ins" / "uaudio_paradise_guitar_studio"
    )
    quarantined_neural_dir = (
        WORKSPACE_ROOT / "quarantined" / "Library" / "Audio" / "Presets" / "Neural DSP" / "Archetype Cory Wong X" / "Toneprints"
    )
    quarantined_neural_dir.mkdir(parents=True, exist_ok=True)

    for item in COMPARISON_PRESETS:
        name = item["name"]
        folder = item["paradise"]["folder"]

        # 1. Paradise Compilation
        p_bytes = compile_paradise_preset(item, paradise_base)

        (repo_paradise_dir / f"Toneprint - {name}.json").write_bytes(p_bytes)

        q_dir = quarantined_paradise_base / folder
        q_dir.mkdir(parents=True, exist_ok=True)
        (q_dir / f"Toneprint - {name}.json").write_bytes(p_bytes)
        (quarantined_paradise_base / f"Toneprint - {name}.json").write_bytes(p_bytes)

        try:
            live_p_folder = PARADISE_DIR / folder
            live_p_folder.mkdir(parents=True, exist_ok=True)
            (live_p_folder / f"Toneprint - {name}.json").write_bytes(p_bytes)
            (PARADISE_DIR / f"Toneprint - {name}.json").write_bytes(p_bytes)
            print(f"✓ Paradise Live + Repo: 'Toneprint - {name}' -> [{folder}]")
        except (PermissionError, OSError) as e:
            print(f"✓ Paradise Repo Preserved: 'Toneprint - {name}' (Live skip: {e})")

        # 2. Neural Compilation
        n_bytes = compile_neural_preset(item, neural_base)

        (repo_neural_dir / f"Toneprint - {name}.xml").write_bytes(n_bytes)
        (repo_neural_dir / f"{name}.xml").write_bytes(n_bytes)

        (quarantined_neural_dir / f"Toneprint - {name}.xml").write_bytes(n_bytes)
        (quarantined_neural_dir / f"{name}.xml").write_bytes(n_bytes)

        try:
            NEURAL_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            (NEURAL_OUTPUT_DIR / f"Toneprint - {name}.xml").write_bytes(n_bytes)
            (NEURAL_OUTPUT_DIR / f"{name}.xml").write_bytes(n_bytes)
            print(f"✓ Neural Live + Repo: '{name}.xml'")
        except (PermissionError, OSError) as e:
            print(f"✓ Neural Repo Preserved: '{name}.xml' (Live skip: {e})")

    print("\nDigital preset compilation completed successfully!")


if __name__ == "__main__":
    main()
