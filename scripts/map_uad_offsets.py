#!/usr/bin/env python3
import sys
import os
import json
import base64
import struct

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/map_uad_offsets.py <base.json> <mod.json>")
        sys.exit(1)
        
    base_path = sys.argv[1]
    mod_path = sys.argv[2]
    
    if not os.path.exists(base_path) or not os.path.exists(mod_path):
        print("Error: One or both files do not exist.")
        sys.exit(1)
        
    with open(base_path, "r") as f:
        base_json = json.load(f)
    with open(mod_path, "r") as f:
        mod_json = json.load(f)
        
    base_bytes = base64.b64decode(base_json["chunk"])
    mod_bytes = base64.b64decode(mod_json["chunk"])
    
    base_size = len(base_bytes)
    mod_size = len(mod_bytes)
    
    print("==================================================")
    print("UNIVERSAL AUDIO UADX PRESET FLOAT MAPPER")
    print("==================================================")
    print(f"Comparing: {os.path.basename(base_path)}")
    print(f"     With: {os.path.basename(mod_path)}")
    print(f"Chunk size: {base_size} bytes ({base_size // 4} floats)")
    print("==================================================")
    
    if base_size != mod_size:
        print(f"Error: Chunk sizes do not match! ({base_size} vs {mod_size} bytes)")
        sys.exit(1)
        
    # Decoded Parameter Changes (4-byte aligned floats)
    print("| Float Index | Byte Offset | Base Float | Mod Float | Delta |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    
    found_floats = 0
    for offset in range(0, base_size - 3, 4):
        base_val = struct.unpack("f", base_bytes[offset:offset+4])[0]
        mod_val = struct.unpack("f", mod_bytes[offset:offset+4])[0]
        if abs(base_val - mod_val) > 1e-7:
            float_idx = offset // 4
            print(f"| {float_idx} | {offset} | {base_val:.6f} | {mod_val:.6f} | {mod_val - base_val:+.6f} |")
            found_floats += 1
            
    if found_floats == 0:
        print("\nNotice: No float differences were found at 4-byte boundaries.")
        print("Comparing raw bytes instead:")
        diffs = []
        for idx in range(base_size):
            if base_bytes[idx] != mod_bytes[idx]:
                diffs.append(idx)
        print(f"Changed byte offsets: {', '.join(map(str, diffs))}")
        
    print("==================================================")

if __name__ == "__main__":
    main()
