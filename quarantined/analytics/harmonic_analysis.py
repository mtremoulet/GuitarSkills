#!/usr/bin/env python3
import soundfile as sf
import numpy as np
from scipy import signal
import librosa

base, sr = sf.read("quarantined/analytics/base.wav")
burn, sr = sf.read("quarantined/analytics/burnished.wav")
base_m = np.mean(base, axis=1)
burn_m = np.mean(burn, axis=1)

# Let's track pitch with pyin on steady segments
fmin = librosa.note_to_hz('E2')
fmax = librosa.note_to_hz('E5')

f0_base, voiced_flag_b, voiced_probs_b = librosa.pyin(base_m, fmin=fmin, fmax=fmax, sr=sr, hop_length=512)
f0_burn, voiced_flag_u, voiced_probs_u = librosa.pyin(burn_m, fmin=fmin, fmax=fmax, sr=sr, hop_length=512)

# Compute harmonic ratios on stable voiced frames
hop = 512
n_fft = 8192
freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

def extract_harmonics(audio, f0, voiced_probs, sr, hop=512, n_fft=8192):
    S = np.abs(librosa.stft(audio, n_fft=n_fft, hop_length=hop))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    
    h2_h1_list = []
    h3_h1_list = []
    h2_h3_list = []
    thd_list = []
    
    # only consider frames where f0 is stable and confidence > 0.85
    for t in range(1, len(f0)-1):
        if voiced_probs[t] > 0.85 and np.abs(f0[t] - f0[t-1]) < 2.0 and np.abs(f0[t] - f0[t+1]) < 2.0:
            fund = f0[t]
            if fund < 80 or fund > 600:
                continue
            
            frame_spec = S[:, t]
            
            harm_amps = []
            for h in range(1, 6):
                h_f = h * fund
                if h_f > sr / 2:
                    break
                idx = np.argmin(np.abs(freqs - h_f))
                # local peak within +/- 2 bins
                pk_val = np.max(frame_spec[max(0, idx-2):min(len(frame_spec), idx+3)])
                harm_amps.append(pk_val)
                
            if len(harm_amps) >= 3 and harm_amps[0] > 1e-4:
                h1, h2, h3 = harm_amps[0], harm_amps[1], harm_amps[2]
                h2_h1 = 20 * np.log10(h2 / h1)
                h3_h1 = 20 * np.log10(h3 / h1)
                h2_h3 = 20 * np.log10(h2 / max(h3, 1e-8))
                
                harm_sum_sq = sum(a**2 for a in harm_amps[1:])
                thd = np.sqrt(harm_sum_sq) / harm_amps[0]
                
                h2_h1_list.append(h2_h1)
                h3_h1_list.append(h3_h1)
                h2_h3_list.append(h2_h3)
                thd_list.append(thd)
                
    return {
        "h2_h1": np.array(h2_h1_list),
        "h3_h1": np.array(h3_h1_list),
        "h2_h3": np.array(h2_h3_list),
        "thd": np.array(thd_list)
    }

h_base = extract_harmonics(base_m, f0_base, voiced_probs_b, sr)
h_burn = extract_harmonics(burn_m, f0_burn, voiced_probs_u, sr)

print("\n--- HARMONIC ANALYSIS ON VOICED / SUSTAINED PITCHES ---")
print(f"Base frames evaluated: {len(h_base['h2_h1'])}, Burnished frames evaluated: {len(h_burn['h2_h1'])}")
print(f"H2 / H1 (Even 2nd Harmonic relative to Fundamental):")
print(f"  Base      : Mean = {np.mean(h_base['h2_h1']):.2f} dB | Median = {np.median(h_base['h2_h1']):.2f} dB")
print(f"  Burnished : Mean = {np.mean(h_burn['h2_h1']):.2f} dB | Median = {np.median(h_burn['h2_h1']):.2f} dB")
print(f"  Difference: Burnished has {np.mean(h_burn['h2_h1']) - np.mean(h_base['h2_h1']):+.2f} dB more H2 energy relative to H1!")

print(f"\nH3 / H1 (Odd 3rd Harmonic relative to Fundamental):")
print(f"  Base      : Mean = {np.mean(h_base['h3_h1']):.2f} dB | Median = {np.median(h_base['h3_h1']):.2f} dB")
print(f"  Burnished : Mean = {np.mean(h_burn['h3_h1']):.2f} dB | Median = {np.median(h_burn['h3_h1']):.2f} dB")

print(f"\nH2 / H3 Ratio (Even vs Odd Dominance):")
print(f"  Base      : Mean = {np.mean(h_base['h2_h3']):.2f} dB | Median = {np.median(h_base['h2_h3']):.2f} dB")
print(f"  Burnished : Mean = {np.mean(h_burn['h2_h3']):.2f} dB | Median = {np.median(h_burn['h2_h3']):.2f} dB")
print(f"  Difference: Burnished H2/H3 ratio is {np.mean(h_burn['h2_h3']) - np.mean(h_base['h2_h3']):+.2f} dB higher (stronger 2nd-order even warmth over 3rd-order odd buzz)!")

