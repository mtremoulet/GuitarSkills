#!/usr/bin/env python3
import os
import json
import base64
import struct

def compare_files(file1_path, file2_path, label):
    if not os.path.exists(file1_path) or not os.path.exists(file2_path):
        print(f"Skipping {label} - one or both files missing.")
        return
        
    with open(file1_path, "r") as f:
        data1 = json.load(f)
    with open(file2_path, "r") as f:
        data2 = json.load(f)
        
    bytes1 = base64.b64decode(data1["chunk"])
    bytes2 = base64.b64decode(data2["chunk"])
    
    print(f"\n--- Comparing {label} ---")
    diffs = 0
    for i in range(27):
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
    presets_dir = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins/uaudio_galaxy_tape_echo"
    
    h1 = os.path.join(presets_dir, "Galaxy_Head1.json")
    h10 = os.path.join(presets_dir, "Galaxy_Head10_StratBath.json")
    h11 = os.path.join(presets_dir, "Galaxy_Head11_Head1+2+3_StratBath.json")
    h12 = os.path.join(presets_dir, "Galaxy_Head12_ReverbOnly.json")
    
    print("==================================================")
    print("MAPPING EXTENDED HEAD SELECT JSON OFFSETS")
    print("==================================================")
    
    compare_files(h1, h10, "Head 1 vs Head 10 (Heads 1+3)")
    compare_files(h1, h11, "Head 1 vs Head 11 (Heads 1+2+3)")
    compare_files(h1, h12, "Head 1 vs Head 12 (Reverb Only)")

if __name__ == "__main__":
    main()
