#!/usr/bin/env python3
"""
Generate 'Faust Fest' preset for Standalone Audio containing all 10 Faust virtual analog pedals.
Also updates scripts/preset_compiler/templates/standalone_templates.json with the native AU states.
"""

from __future__ import annotations

import os
import json
import uuid
import base64
import plistlib
import datetime
import ctypes
from ctypes import c_void_p, c_uint32, c_long, byref, Structure, POINTER
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_FILE = WORKSPACE_ROOT / "scripts" / "preset_compiler" / "templates" / "standalone_templates.json"
STANDALONE_PRESETS_DIR = Path.home() / "Library" / "Application Support" / "Standalone" / "Presets"

AudioToolbox = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox")
CoreFoundation = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation")

class AudioComponentDescription(Structure):
    _fields_ = [
        ("componentType", c_uint32),
        ("componentSubType", c_uint32),
        ("componentManufacturer", c_uint32),
        ("componentFlags", c_uint32),
        ("componentFlagsMask", c_uint32)
    ]

CoreFoundation.CFPropertyListCreateData.argtypes = [c_void_p, c_void_p, c_long, c_long, POINTER(c_void_p)]
CoreFoundation.CFPropertyListCreateData.restype = c_void_p
CoreFoundation.CFDataGetLength.argtypes = [c_void_p]
CoreFoundation.CFDataGetLength.restype = c_long
CoreFoundation.CFDataGetBytePtr.argtypes = [c_void_p]
CoreFoundation.CFDataGetBytePtr.restype = POINTER(ctypes.c_char)

def fourcc(s: str) -> int:
    return int.from_bytes(s.encode("latin1"), "big")

FAUST_PEDALS = [
    {
        "slot": 0,
        "name": "7 Samurai",
        "subtype": "GE7S",
        "desc_name": "7 Samurai (七人の侍)",
        "heritage": "Boss GE-7 7-band op-amp gyrator active equalizer",
        "bypass_on_load": False
    },
    {
        "slot": 1,
        "name": "Nobels ODR-1 Plus",
        "subtype": "ODR1",
        "desc_name": "Nobels ODR-1 Plus",
        "heritage": "Nobels ODR-1 natural overdrive with Spectrum & Bass Boost",
        "bypass_on_load": True
    },
    {
        "slot": 2,
        "name": "Arthur",
        "subtype": "ARTR",
        "desc_name": "Arthur",
        "heritage": "Analogman King of Tone / PedalPCB Paragon dual-channel overdrive",
        "bypass_on_load": True
    },
    {
        "slot": 3,
        "name": "BrokeBetterBlues",
        "template_key": "Broke Better Blues",
        "subtype": "BBBR",
        "desc_name": "Broke Better Blues",
        "heritage": "Marshall Bluesbreaker BB-1 with low-impedance high-clarity output stage",
        "bypass_on_load": True
    },
    {
        "slot": 4,
        "name": "Stumblelater",
        "subtype": "STMB",
        "desc_name": "Stumblelater",
        "heritage": "Dumble ABL passive send attenuator & Class-A recovery gain stage",
        "bypass_on_load": True
    },
    {
        "slot": 5,
        "name": "MattFoley",
        "template_key": "Matt Foley",
        "subtype": "MFLY",
        "desc_name": "Matt Foley",
        "heritage": "Wampler Talent Booster / Speaker Motivator dual-J201 parallel boost",
        "bypass_on_load": True
    },
    {
        "slot": 6,
        "name": "Fifty Shades of Blue V2",
        "subtype": "FSB2",
        "desc_name": "Fifty Shades of Blue V2",
        "heritage": "Multi-clipping Bluesbreaker overdrive with Ge/Schottky knees",
        "bypass_on_load": True
    },
    {
        "slot": 7,
        "name": "Fumble on the Grid V2",
        "subtype": "FMB2",
        "desc_name": "Fumble on the Grid V2",
        "heritage": "Dumble Overdrive Special JFET front-end preamp with variable drain bias",
        "bypass_on_load": True
    },
    {
        "slot": 8,
        "name": "Law of Averages V2",
        "subtype": "LOA2",
        "desc_name": "Law of Averages V2",
        "heritage": "Marshall Bluesbreaker buffer stage with selectable RF snubber capacitors",
        "bypass_on_load": True
    },
    {
        "slot": 9,
        "name": "Liberty Burnisher V2",
        "subtype": "LBB2",
        "desc_name": "Liberty Burnisher V2",
        "heritage": "Ge/Si harmonic polisher & treble/mid booster with Baxandall shelf",
        "bypass_on_load": True
    }
]

def extract_au_state(subtype: str) -> str:
    desc = AudioComponentDescription(fourcc("aufx"), fourcc(subtype), fourcc("SPIC"), 0, 0)
    comp = AudioToolbox.AudioComponentFindNext(None, byref(desc))
    if not comp:
        raise RuntimeError(f"Could not find AU component for subtype '{subtype}'")
    
    instance = c_void_p()
    status = AudioToolbox.AudioComponentInstanceNew(comp, byref(instance))
    if status != 0:
        raise RuntimeError(f"AudioComponentInstanceNew failed with status {status}")
    
    AudioToolbox.AudioUnitInitialize(instance)
    
    kAudioUnitProperty_ClassInfo = 0
    prop_size = c_uint32(ctypes.sizeof(c_void_p))
    plist_ref = c_void_p()
    status = AudioToolbox.AudioUnitGetProperty(instance, kAudioUnitProperty_ClassInfo, 0, 0, byref(plist_ref), byref(prop_size))
    if status != 0:
        AudioToolbox.AudioUnitUninitialize(instance)
        AudioToolbox.AudioComponentInstanceDispose(instance)
        raise RuntimeError(f"AudioUnitGetProperty ClassInfo failed with status {status}")
    
    err = c_void_p()
    data_ref = CoreFoundation.CFPropertyListCreateData(None, plist_ref, 200, 0, byref(err))
    length = CoreFoundation.CFDataGetLength(data_ref)
    ptr = CoreFoundation.CFDataGetBytePtr(data_ref)
    raw = ctypes.string_at(ptr, length)
    b64 = base64.b64encode(raw).decode("utf-8")
    
    AudioToolbox.AudioUnitUninitialize(instance)
    AudioToolbox.AudioComponentInstanceDispose(instance)
    return b64

def main():
    STANDALONE_PRESETS_DIR.mkdir(parents=True, exist_ok=True)
    
    templates = {}
    if TEMPLATES_FILE.exists():
        try:
            with open(TEMPLATES_FILE, "r", encoding="utf-8") as f:
                templates = json.load(f)
        except Exception as e:
            print(f"Warning loading templates: {e}")

    standalone_ns = uuid.UUID("3d3a34b7-43f9-4c61-be5b-580a4e6f880d")
    preset_uuid = str(uuid.uuid5(standalone_ns, "guitar-skills.preset.faust-fest")).upper()
    
    rack_items = []
    for pedal in FAUST_PEDALS:
        slot = pedal["slot"]
        name = pedal["name"]
        subtype = pedal["subtype"]
        desc_name = pedal["desc_name"]
        
        b64_state = extract_au_state(subtype)
        
        desc_obj = {
            "type": fourcc("aufx"),
            "manufacturer": fourcc("SPIC"),
            "subType": fourcc(subtype)
        }
        
        template_key = pedal.get("template_key", name)
        templates[template_key] = {
            "manufacturerName": "SPICEyNAM / Mike Tremoulet",
            "name": name,
            "desc": desc_obj,
            "statePlistBase64": b64_state
        }
        if template_key != desc_name:
            templates[desc_name] = templates[template_key]
        if template_key != name:
            templates[name] = templates[template_key]
            
        item_uuid = str(uuid.uuid5(standalone_ns, f"guitar-skills.preset.faust-fest.slot.{slot}")).upper()
        
        rack_items.append({
            "slotIndex": slot,
            "isBypassed": pedal["bypass_on_load"],
            "id": item_uuid,
            "manufacturerName": "SPICEyNAM / Mike Tremoulet",
            "name": name,
            "desc": desc_obj,
            "inputChannels": 1,
            "outputChannels": 1,
            "statePlistBase64": b64_state
        })

    TEMPLATES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TEMPLATES_FILE, "w", encoding="utf-8") as f:
        json.dump(templates, f, indent=2)

    pc_num = 58
    existing_presets = list(STANDALONE_PRESETS_DIR.glob("*.json"))
    used_pcs = set()
    for ep in existing_presets:
        try:
            with open(ep, "r", encoding="utf-8") as f:
                d = json.load(f)
                if "pcNumber" in d and d.get("id") != preset_uuid:
                    used_pcs.add(d["pcNumber"])
        except Exception:
            pass
    while pc_num in used_pcs:
        pc_num += 1

    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    preset_obj = {
        "id": preset_uuid,
        "parameterMappings": [],
        "name": "Faust Fest",
        "pcNumber": pc_num,
        "createdAt": now_iso,
        "items": rack_items,
        "inputMode": 0
    }

    preset_path = STANDALONE_PRESETS_DIR / f"{preset_uuid}.json"
    with open(preset_path, "w", encoding="utf-8") as f:
        json.dump(preset_obj, f, indent=2)

    print("==================================================")
    print(f"SUCCESS! Faust Fest preset compiled to:")
    print(f"{preset_path}")
    print(f"Name:        '{preset_obj['name']}'")
    print(f"PC Number:   {preset_obj['pcNumber']}")
    print(f"Preset ID:   {preset_obj['id']}")
    print(f"Modules:     {len(preset_obj['items'])} Faust pedals in rack")
    print("==================================================")

if __name__ == "__main__":
    main()
