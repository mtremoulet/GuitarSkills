#!/usr/bin/env python3
import os
import json
import base64
import struct

def compare_presets(file1_path, file2_path, label):
    if not os.path.exists(file1_path) or not os.path.exists(file2_path):
        print(f"Skipping {label} - file missing.")
        return
        
    with open(file1_path, "r") as f:
        data1 = json.load(f)
    with open(file2_path, "r") as f:
        data2 = json.load(f)
        
    bytes1 = base64.b64decode(data1["chunk"])
    bytes2 = base64.b64decode(data2["chunk"])
    
    print(f"\n--- Comparing {label} ({len(bytes1)} bytes) ---")
    diffs = 0
    for i in range((len(bytes1) + 3) // 4):
        offset = i * 4
        if offset + 4 <= len(bytes1):
            val1_f = struct.unpack("f", bytes1[offset:offset+4])[0]
            val2_f = struct.unpack("f", bytes2[offset:offset+4])[0]
            val1_i = struct.unpack("<i", bytes1[offset:offset+4])[0]
            val2_i = struct.unpack("<i", bytes2[offset:offset+4])[0]
            
            if abs(val1_f - val2_f) > 1e-7 or val1_i != val2_i:
                print(f"Index {i:2d} (Offset {offset:3d}):")
                print(f"  File 1: Float={val1_f:7.4f}, Int={val1_i:d}")
                print(f"  File 2: Float={val2_f:7.4f}, Int={val2_i:d}")
                diffs += 1
                
    if diffs == 0:
        print("No differences found.")

def main():
    presets_dir = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins/uaudio_studio_d_chorus"
    
    m1 = os.path.join(presets_dir, "StudioD_Mode1.json")
    m2 = os.path.join(presets_dir, "StudioD_Mode2.json")
    m3 = os.path.join(presets_dir, "StudioD_Mode3.json")
    m4 = os.path.join(presets_dir, "StudioD_Mode4.json")
    moff = os.path.join(presets_dir, "StudioD_ModeOff.json")
    poff = os.path.join(presets_dir, "StudioD_PowerOff.json")
    secret = os.path.join(presets_dir, "Mike's Secret Mode.json")
    
    compare_presets(m1, m2, "Mode 1 vs Mode 2")
    compare_presets(m1, m3, "Mode 1 vs Mode 3")
    compare_presets(m1, m4, "Mode 1 vs Mode 4")
    compare_presets(m1, moff, "Mode 1 vs Mode Off")
    compare_presets(m1, poff, "Mode 1 vs Power Off")
    compare_presets(m1, secret, "Mode 1 vs Mike's Secret Mode (All Buttons)")

if __name__ == "__main__":
    main()
