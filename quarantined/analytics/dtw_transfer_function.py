#!/usr/bin/env python3
import soundfile as sf
import numpy as np
from scipy import signal
import librosa

base, sr = sf.read("quarantined/analytics/base.wav")
burn, sr = sf.read("quarantined/analytics/burnished.wav")
base_m = np.mean(base, axis=1)
burn_m = np.mean(burn, axis=1)

# Compute MFCCs for DTW
hop = 512
mfcc_base = librosa.feature.mfcc(y=base_m, sr=sr, n_mfcc=13, hop_length=hop)
mfcc_burn = librosa.feature.mfcc(y=burn_m, sr=sr, n_mfcc=13, hop_length=hop)

# DTW alignment
D, wp = librosa.sequence.dtw(X=mfcc_base, Y=mfcc_burn, metric='cosine')
# wp has shape (N, 2), index 0 is base frame, index 1 is burn frame. wp is in reverse order.
wp = wp[::-1]

print(f"DTW aligned path length: {len(wp)} frames")

# Let's compute average spectrum of aligned frames
n_fft = 4096
S_base = np.abs(librosa.stft(base_m, n_fft=n_fft, hop_length=hop))
S_burn = np.abs(librosa.stft(burn_m, n_fft=n_fft, hop_length=hop))

freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

# Map aligned spectra
aligned_base = S_base[:, wp[:, 0]]
aligned_burn = S_burn[:, wp[:, 1]]

# Filter out low-energy frames (silence/noise floor)
frame_energy = np.mean(aligned_base, axis=0)
active = frame_energy > np.percentile(frame_energy, 40)

aligned_base_act = aligned_base[:, active]
aligned_burn_act = aligned_burn[:, active]

# Empirical Gain curve (Burn / Base in dB)
mean_base_act = np.mean(aligned_base_act, axis=1)
mean_burn_act = np.mean(aligned_burn_act, axis=1)

gain_db = 20 * np.log10(np.maximum(mean_burn_act, 1e-8) / np.maximum(mean_base_act, 1e-8))

# Check key anchor frequencies
key_freqs = [30, 40, 60, 80, 100, 150, 250, 500, 1000, 2000, 3000, 4500, 6000, 8200, 10000, 12000]
print("\n--- EMPIRICAL GAIN CURVE ACROSS ALIGNED ACTIVE MUSICAL FRAMES ---")
for kf in key_freqs:
    idx = np.argmin(np.abs(freqs - kf))
    # Smooth across adjacent 3 bins
    val = np.mean(gain_db[max(0, idx-2):min(len(gain_db), idx+3)])
    print(f"Freq {kf:5d} Hz : {val:+6.2f} dB (Actual bin: {freqs[idx]:.1f} Hz)")

