#!/usr/bin/env python3
import sys
import os
import struct

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/map_pst_offsets.py <base.pst> <mod.pst>")
        sys.exit(1)
        
    base_path = sys.argv[1]
    mod_path = sys.argv[2]
    
    if not os.path.exists(base_path) or not os.path.exists(mod_path):
        print("Error: One or both files do not exist.")
        sys.exit(1)
        
    base_size = os.path.getsize(base_path)
    mod_size = os.path.getsize(mod_path)
    
    if base_size != mod_size:
        print(f"Error: File sizes do not match! ({base_size} vs {mod_size} bytes)")
        sys.exit(1)
        
    with open(base_path, "rb") as f:
        base_data = f.read()
    with open(mod_path, "rb") as f:
        mod_data = f.read()
        
    print("==================================================")
    print("LOGIC NATIVE PRESET BYTE OFFSET DICTIONARY MAPPER")
    print("==================================================")
    print(f"Comparing: {os.path.basename(base_path)}")
    print(f"     With: {os.path.basename(mod_path)}")
    print(f"File Size: {base_size} bytes")
    print("==================================================")
    
    # 1. Byte-by-byte comparison
    diff_bytes = []
    for idx in range(base_size):
        if base_data[idx] != mod_data[idx]:
            diff_bytes.append(idx)
            
    if not diff_bytes:
        print("Success: Files are identical!")
        return
        
    print(f"Bytes that changed (Indices): {', '.join(map(str, diff_bytes))}")
    
    # 2. Float-level comparison (4-byte aligned, starting at byte 8)
    print("\nDecoded Parameter Changes (4-Byte aligned 32-bit float sweep):")
    print("| Float Index | Byte Offset | Base Float | Mod Float | Delta |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    
    found_floats = 0
    for offset in range(8, base_size - 3, 4):
        base_val = struct.unpack("f", base_data[offset:offset+4])[0]
        mod_val = struct.unpack("f", mod_data[offset:offset+4])[0]
        if abs(base_val - mod_val) > 1e-7:
            # Index starting from byte 8 (first parameter float)
            float_idx = (offset - 8) // 4
            print(f"| {float_idx} | {offset} | {base_val:.6f} | {mod_val:.6f} | {mod_val - base_val:+.6f} |")
            found_floats += 1
            
    if found_floats == 0:
        print("\nNotice: No float differences were found at 4-byte boundaries.")
        print("This could mean parameters are stored as integers, chars, or non-aligned types.")
        print("Raw Byte Diff:")
        for idx in diff_bytes:
            print(f"  Byte {idx}: {base_data[idx]:02x} -> {mod_data[idx]:02x}")
            
    print("==================================================")

if __name__ == "__main__":
    main()
