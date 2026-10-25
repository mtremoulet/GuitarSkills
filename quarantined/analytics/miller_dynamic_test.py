#!/usr/bin/env python3
import soundfile as sf
import numpy as np
import librosa

base, sr = sf.read("quarantined/analytics/base.wav")
burn, sr = sf.read("quarantined/analytics/burnished.wav")
base_m = np.mean(base, axis=1)
burn_m = np.mean(burn, axis=1)

def evaluate_miller_dynamics(audio, name, sr):
    onsets = librosa.onset.onset_detect(y=audio, sr=sr, units='samples', backtrack=True)
    att_len = int(0.020 * sr) # 20 ms
    
    fft_n = 2048
    freqs = np.fft.rfftfreq(fft_n, 1/sr)
    idx_mid = (freqs >= 400) & (freqs <= 1500)
    idx_high = (freqs >= 3000) & (freqs <= 8000)
    
    events = []
    for o in onsets:
        if o + att_len >= len(audio):
            continue
        seg = audio[o : o + att_len]
        pk = np.max(np.abs(seg))
        if pk < 0.005:
            continue
        slew = np.max(np.abs(np.diff(seg))) * sr
        
        # Spectral ratio in this attack window
        w = np.hanning(len(seg))
        S = np.abs(np.fft.rfft(seg * w, n=fft_n))
        mid_e = np.mean(S[idx_mid])
        high_e = np.mean(S[idx_high])
        
        if mid_e > 1e-6 and high_e > 1e-6:
            ratio_db = 20 * np.log10(high_e / mid_e)
            events.append((pk, slew, ratio_db))
            
    events = sorted(events, key=lambda x: x[0]) # sort by peak amplitude
    n = len(events)
    soft_events = events[: n // 3]      # quietest 1/3
    hard_events = events[2 * n // 3 :]  # loudest 1/3
    
    soft_ratio = np.mean([e[2] for e in soft_events])
    hard_ratio = np.mean([e[2] for e in hard_events])
    
    print(f"=== {name} ===")
    print(f"Total valid attacks analyzed: {n}")
    print(f"Soft attacks (lowest 33% velocity) High/Mid ratio : {soft_ratio:6.2f} dB")
    print(f"Hard attacks (highest 33% velocity) High/Mid ratio: {hard_ratio:6.2f} dB")
    print(f"Dynamic Brightness Delta (Hard vs Soft)           : {hard_ratio - soft_ratio:+6.2f} dB")
    return soft_ratio, hard_ratio

print("--- TESTING DYNAMIC MILLER CAPACITANCE HYPOTHESIS ---")
evaluate_miller_dynamics(base_m, "Base (No Pedal)", sr)
evaluate_miller_dynamics(burn_m, "Burnished (Liberty Burnisher + Stumblelater)", sr)

