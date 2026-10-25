#!/usr/bin/env python3
"""
Generate the 'Scarlett Solo Correction' preset for Standalone Audio (by Oort Media).

Signal Chain:
  Guitar (Scarlett Solo DI)
    -> 7 Samurai (Gyrator EQ damping simulation: -2.0 dB @ 3.2 kHz, -0.8 dB @ 6.4 kHz)
    -> Liberty Burnisher (Discrete JFET & dynamic Miller softening: 18V pump ON, Drive 0.20, Burnish 40%, Ge Warmth 40%, Air 0.0 dB)
    -> Ready for downstream Amp Sim

Outputs:
  - Live Host: ~/Library/Application Support/Standalone/Presets/2D0CC363-14F9-5C1D-8FFB-E406C6A4E4A3.json
  - Repo Mirror: tones/presets/standalone/2D0CC363-14F9-5C1D-8FFB-E406C6A4E4A3.json
"""

from __future__ import annotations

import os
import sys
import json
import uuid
import base64
import plistlib
import datetime
import struct
import ctypes
from ctypes import c_void_p, c_uint32, c_float, c_long, byref, Structure, POINTER
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
STANDALONE_LIVE_DIR = Path.home() / "Library" / "Application Support" / "Standalone" / "Presets"
REPO_MIRROR_DIR = WORKSPACE_ROOT / "tones" / "presets" / "standalone"
TEMPLATES_FILE = WORKSPACE_ROOT / "scripts" / "preset_compiler" / "templates" / "standalone_templates.json"

STANDALONE_NAMESPACE = uuid.UUID("3d3a34b7-43f9-4c61-be5b-580a4e6f880d")

# -----------------------------------------------------------------------------
# CoreAudio / AudioToolbox Helper for Native AU State Extraction
# -----------------------------------------------------------------------------
AudioToolbox = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox")
CoreFoundation = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation")


class AudioComponentDescription(Structure):
    _fields_ = [
        ("componentType", c_uint32),
        ("componentSubType", c_uint32),
        ("componentManufacturer", c_uint32),
        ("componentFlags", c_uint32),
        ("componentFlagsMask", c_uint32),
    ]


CoreFoundation.CFPropertyListCreateData.argtypes = [c_void_p, c_void_p, c_long, c_long, POINTER(c_void_p)]
CoreFoundation.CFPropertyListCreateData.restype = c_void_p
CoreFoundation.CFDataGetLength.argtypes = [c_void_p]
CoreFoundation.CFDataGetLength.restype = c_long
CoreFoundation.CFDataGetBytePtr.argtypes = [c_void_p]
CoreFoundation.CFDataGetBytePtr.restype = POINTER(ctypes.c_char)

AudioToolbox.AudioUnitSetParameter.argtypes = [c_void_p, c_uint32, c_uint32, c_uint32, c_float, c_uint32]
AudioToolbox.AudioUnitSetParameter.restype = ctypes.c_int


def fourcc(s: str) -> int:
    return int.from_bytes(s.encode("latin1"), "big")


def get_live_au_state(mfr_str: str, subtype_str: str, params: dict[int, float]) -> str:
    """Instantiate AudioUnit, set specified parameter values, and return base64 ClassInfo plist."""
    desc = AudioComponentDescription(fourcc("aufx"), fourcc(subtype_str), fourcc(mfr_str), 0, 0)
    comp = AudioToolbox.AudioComponentFindNext(None, byref(desc))
    if not comp:
        raise RuntimeError(f"Could not find AU component {mfr_str} {subtype_str}")

    inst = c_void_p()
    status = AudioToolbox.AudioComponentInstanceNew(comp, byref(inst))
    if status != 0:
        raise RuntimeError(f"AudioComponentInstanceNew failed with status {status}")

    AudioToolbox.AudioUnitInitialize(inst)

    # Set parameters: scope 0 (Global), element 0
    for pid, val in params.items():
        res = AudioToolbox.AudioUnitSetParameter(inst, c_uint32(pid), 0, 0, c_float(val), 0)
        if res != 0:
            print(f"Warning: AudioUnitSetParameter failed for param {pid}={val} (err={res})")

    # Read ClassInfo property (ID 0)
    prop_size = c_uint32(ctypes.sizeof(c_void_p))
    plist_ref = c_void_p()
    status = AudioToolbox.AudioUnitGetProperty(inst, 0, 0, 0, byref(plist_ref), byref(prop_size))
    if status != 0:
        AudioToolbox.AudioUnitUninitialize(inst)
        AudioToolbox.AudioComponentInstanceDispose(inst)
        raise RuntimeError(f"AudioUnitGetProperty ClassInfo failed with status {status}")

    err = c_void_p()
    data_ref = CoreFoundation.CFPropertyListCreateData(None, plist_ref, 200, 0, byref(err))
    length = CoreFoundation.CFDataGetLength(data_ref)
    ptr = CoreFoundation.CFDataGetBytePtr(data_ref)
    raw = ctypes.string_at(ptr, length)

    AudioToolbox.AudioUnitUninitialize(inst)
    AudioToolbox.AudioComponentInstanceDispose(inst)

    return base64.b64encode(raw).decode("utf-8")


def find_next_available_pc() -> int:
    """Find the next unassigned MIDI Program Change number in existing presets."""
    used_pcs = set()
    for directory in (STANDALONE_LIVE_DIR, REPO_MIRROR_DIR):
        if directory.exists():
            for f in directory.glob("*.json"):
                try:
                    with open(f, "r", encoding="utf-8") as fp:
                        data = json.load(fp)
                    pc = data.get("pcNumber")
                    if pc is not None and isinstance(pc, int):
                        used_pcs.add(pc)
                except Exception:
                    pass
    cand = 1
    while cand in used_pcs:
        cand += 1
    return cand


def build_scarlett_solo_correction_preset() -> dict:
    preset_name = "Scarlett Solo Correction"
    preset_uuid = str(uuid.uuid5(STANDALONE_NAMESPACE, "guitar-skills.preset.scarlett-solo-correction")).upper()
    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # 1. Parameter definitions for 7 Samurai
    # Katsushiro Okamoto (3.2 kHz): -2.0 dB
    # Kikuchiyo (6.4 kHz): -0.8 dB
    # 100 Hz - 1.6 kHz: 0.0 dB (flat)
    # Level: 0.0 dB, Bypass: 0 (Active EQ)
    samurai_params = {
        0: 0.0,   # 100 Hz
        1: 0.0,   # 200 Hz
        2: 0.0,   # 400 Hz
        3: 0.0,   # 800 Hz
        4: 0.0,   # 1.6 kHz
        5: -2.0,  # 3.2 kHz
        6: -0.8,  # 6.4 kHz
        7: 0.0,   # Level
        8: 0.0,   # Bypass
    }
    samurai_b64 = get_live_au_state("FWAG", "7SAM", samurai_params)

    # 2. Parameter definitions for Liberty Burnisher
    # Drive: 0.20 (low clean unity chime)
    # Burnish: 40.0% (pick transient softener)
    # Air: 0.0 dB (flat)
    # Ge Warmth: 40.0% (restores H2 note weight)
    # Master Volume: 0.0 dB
    # Bypass: 0 (Active)
    # 18V Charge Pump: 1.0 (ON - high headroom)
    burnisher_params = {
        0: 0.20,  # Drive
        1: 40.0,  # Burnish (%)
        2: 0.0,   # Air (dB)
        3: 40.0,  # Ge Warmth (%)
        4: 0.0,   # Master Volume (dB)
        5: 0.0,   # Bypass
        6: 1.0,   # 18V Charge Pump (ON)
    }
    burnisher_b64 = get_live_au_state("FWAG", "LBBR", burnisher_params)

    slot0_uuid = str(uuid.uuid5(STANDALONE_NAMESPACE, "guitar-skills.preset.scarlett-solo-correction.slot.0")).upper()
    slot1_uuid = str(uuid.uuid5(STANDALONE_NAMESPACE, "guitar-skills.preset.scarlett-solo-correction.slot.1")).upper()

    pc_num = find_next_available_pc()

    preset_obj = {
        "id": preset_uuid,
        "name": preset_name,
        "pcNumber": pc_num,
        "createdAt": now_iso,
        "inputMode": 0,
        "parameterMappings": [],
        "items": [
            {
                "slotIndex": 0,
                "isBypassed": False,
                "id": slot0_uuid,
                "manufacturerName": "Faust & Wagner",
                "name": "7 Samurai",
                "desc": {
                    "type": 1635083896,
                    "subType": 928203085,
                    "manufacturer": 1180123463,
                },
                "inputChannels": 1,
                "outputChannels": 1,
                "statePlistBase64": samurai_b64,
            },
            {
                "slotIndex": 1,
                "isBypassed": False,
                "id": slot1_uuid,
                "manufacturerName": "Faust & Wagner",
                "name": "Liberty Burnisher",
                "desc": {
                    "type": 1635083896,
                    "subType": 1279410770,
                    "manufacturer": 1180123463,
                },
                "inputChannels": 1,
                "outputChannels": 1,
                "statePlistBase64": burnisher_b64,
            },
        ],
    }

    return preset_obj


def main():
    print("==================================================")
    print("COMPILING 'SCARLETT SOLO CORRECTION' STANDALONE PRESET")
    print("==================================================")

    preset = build_scarlett_solo_correction_preset()
    preset_id = preset["id"]
    filename = f"{preset_id}.json"

    # 1. Write to repo mirror
    REPO_MIRROR_DIR.mkdir(parents=True, exist_ok=True)
    repo_file = REPO_MIRROR_DIR / filename
    with open(repo_file, "w", encoding="utf-8") as f:
        json.dump(preset, f, indent=2)
    print(f"-> Saved repo mirror: {repo_file}")

    # 2. Write to live Standalone Presets directory
    STANDALONE_LIVE_DIR.mkdir(parents=True, exist_ok=True)
    live_file = STANDALONE_LIVE_DIR / filename
    try:
        with open(live_file, "w", encoding="utf-8") as f:
            json.dump(preset, f, indent=2)
        print(f"-> Saved live Standalone preset: {live_file}")
    except (PermissionError, OSError) as e:
        print(f"-> Live directory write failed ({e}); repo mirror preserved.")

    # 3. Update standalone_templates.json with authoritative 7 Samurai template
    if TEMPLATES_FILE.exists():
        try:
            with open(TEMPLATES_FILE, "r", encoding="utf-8") as f:
                templates = json.load(f)
            templates["7 Samurai"] = {
                "manufacturerName": "Faust & Wagner",
                "name": "7 Samurai",
                "desc": {
                    "type": 1635083896,
                    "subType": 928203085,
                    "manufacturer": 1180123463,
                },
                "statePlistBase64": preset["items"][0]["statePlistBase64"],
            }
            with open(TEMPLATES_FILE, "w", encoding="utf-8") as f:
                json.dump(templates, f, indent=2)
            print(f"-> Updated 7 Samurai template in {TEMPLATES_FILE}")
        except Exception as e:
            print(f"-> Notice: Could not update {TEMPLATES_FILE}: {e}")

    print("==================================================")
    print(f"SUCCESS: '{preset['name']}' compiled (PC #{preset['pcNumber']})")
    print(f"UUID: {preset_id}")
    print("==================================================")


if __name__ == "__main__":
    main()
