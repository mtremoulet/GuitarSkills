#!/usr/bin/env python3
import json
import base64
import struct

def main():
    json_path = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins/uaudio_galaxy_tape_echo/WhereAmI.json"
    with open(json_path, "r") as f:
        data = json.load(f)
        
    chunk_bytes = base64.b64decode(data["chunk"])
    print(f"Chunk size: {len(chunk_bytes)} bytes")
    
    print("\n--- FLOATS IN WhereAmI.json ---")
    print("| Index | Float Offset | Float Value | Int Value | Hex Bytes |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    for i in range(27):
        offset = i * 4
        if offset + 4 <= len(chunk_bytes):
            val_bytes = chunk_bytes[offset:offset+4]
            f_val = struct.unpack("f", val_bytes)[0]
            i_val = struct.unpack("<i", val_bytes)[0]
            hex_str = " ".join(f"{b:02x}" for b in val_bytes)
            print(f"| {i:2d} | {offset:4d} | {f_val:11.6f} | {i_val:11d} | {hex_str} |")

if __name__ == "__main__":
    main()
