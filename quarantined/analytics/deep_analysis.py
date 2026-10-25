#!/usr/bin/env python3
import soundfile as sf
import numpy as np
from scipy import signal
import librosa

base, sr = sf.read("quarantined/analytics/base.wav")
burn, sr = sf.read("quarantined/analytics/burnished.wav")

base_m = np.mean(base, axis=1)
burn_m = np.mean(burn, axis=1)

# 1. Chroma & Musical Structure
chroma_base = librosa.feature.chroma_cqt(y=base_m, sr=sr, hop_length=1024)
chroma_burn = librosa.feature.chroma_cqt(y=burn_m, sr=sr, hop_length=1024)

# Global chroma correlation
corr = np.corrcoef(np.mean(chroma_base, axis=1), np.mean(chroma_burn, axis=1))[0, 1]
print(f"Chroma correlation across pitches: {corr:.3f}")

pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
top_base_pitches = np.argsort(np.mean(chroma_base, axis=1))[::-1][:5]
top_burn_pitches = np.argsort(np.mean(chroma_burn, axis=1))[::-1][:5]
print("Top pitches in Base     :", [pitch_names[i] for i in top_base_pitches])
print("Top pitches in Burnished:", [pitch_names[i] for i in top_burn_pitches])

# 2. Dynamic Miller Effect Analysis: Attack vs Sustain Frequency Balance
onsets_base = librosa.onset.onset_detect(y=base_m, sr=sr, units='samples', backtrack=True)
onsets_burn = librosa.onset.onset_detect(y=burn_m, sr=sr, units='samples', backtrack=True)

def compute_attack_vs_sustain_spectra(audio, onsets, sr):
    att_len = int(0.025 * sr)   # 0-25 ms (transient pick attack)
    sus_start = int(0.080 * sr) # 80 ms
    sus_len = int(0.150 * sr)   # 80-230 ms (body sustain)
    
    att_specs = []
    sus_specs = []
    
    fft_n = 2048
    freqs = np.fft.rfftfreq(fft_n, 1/sr)
    
    for o in onsets:
        if o + sus_start + sus_len >= len(audio):
            continue
        att_seg = audio[o : o + att_len]
        sus_seg = audio[o + sus_start : o + sus_start + sus_len]
        
        if np.max(np.abs(att_seg)) < 0.01:
            continue
            
        # Window & FFT
        w_att = np.hanning(len(att_seg))
        w_sus = np.hanning(len(sus_seg))
        
        S_att = np.abs(np.fft.rfft(att_seg * w_att, n=fft_n))
        S_sus = np.abs(np.fft.rfft(sus_seg * w_sus, n=fft_n))
        
        att_specs.append(S_att)
        sus_specs.append(S_sus)
        
    avg_att = np.mean(att_specs, axis=0)
    avg_sus = np.mean(sus_specs, axis=0)
    return freqs, avg_att, avg_sus

freqs, base_att, base_sus = compute_attack_vs_sustain_spectra(base_m, onsets_base, sr)
_, burn_att, burn_sus = compute_attack_vs_sustain_spectra(burn_m, onsets_burn, sr)

# Calculate ratio of High (>3kHz) to Mid (500Hz-2kHz) in Attack vs Sustain
idx_mid = (freqs >= 500) & (freqs <= 2000)
idx_high = (freqs >= 3000) & (freqs <= 8000)

base_att_ratio = 20*np.log10(np.mean(base_att[idx_high]) / np.mean(base_att[idx_mid]))
base_sus_ratio = 20*np.log10(np.mean(base_sus[idx_high]) / np.mean(base_sus[idx_mid]))

burn_att_ratio = 20*np.log10(np.mean(burn_att[idx_high]) / np.mean(burn_att[idx_mid]))
burn_sus_ratio = 20*np.log10(np.mean(burn_sus[idx_high]) / np.mean(burn_sus[idx_mid]))

print(f"\n--- ATTACK vs SUSTAIN HIGH/MID RATIO (3-8kHz vs 500-2000Hz) ---")
print(f"Base      : Attack High/Mid = {base_att_ratio:.2f} dB | Sustain High/Mid = {base_sus_ratio:.2f} dB | Delta (Attack brightness excess) = {base_att_ratio - base_sus_ratio:+.2f} dB")
print(f"Burnished : Attack High/Mid = {burn_att_ratio:.2f} dB | Sustain High/Mid = {burn_sus_ratio:.2f} dB | Delta (Attack brightness excess) = {burn_att_ratio - burn_sus_ratio:+.2f} dB")

# 3. Dynamic Range & Compression Analysis
# Analyze sustain decay rates
def compute_decay_tails(audio, onsets, sr):
    decays = []
    w_size = int(0.010 * sr)
    for o in onsets:
        if o + int(0.5 * sr) >= len(audio):
            continue
        env = []
        for i in range(50):
            t0 = o + i * w_size
            env.append(np.sqrt(np.mean(audio[t0:t0+w_size]**2)))
        env = np.array(env)
        pk = np.max(env)
        if pk > 0.005:
            # measure time to drop -6 dB from peak
            pk_idx = np.argmax(env)
            half_pts = np.where(env[pk_idx:] <= 0.5 * pk)[0]
            if len(half_pts) > 0:
                decays.append(half_pts[0] * 10) # ms
    return np.array(decays)

dec_base = compute_decay_tails(base_m, onsets_base, sr)
dec_burn = compute_decay_tails(burn_m, onsets_burn, sr)
print(f"\n--- SUSTAIN DECAY DYNAMICS (T_6dB half-decay time) ---")
print(f"Base      : Mean T_6dB = {np.mean(dec_base):.1f} ms | Median = {np.median(dec_base):.1f} ms")
print(f"Burnished : Mean T_6dB = {np.mean(dec_burn):.1f} ms | Median = {np.median(dec_burn):.1f} ms")

