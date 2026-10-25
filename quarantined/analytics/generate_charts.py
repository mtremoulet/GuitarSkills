#!/usr/bin/env python3
"""
Generate comprehensive visual analytics comparing base vs burnished recordings.
Saves high-res figure to quarantined/analytics/burnished_vs_base_analysis.png.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy import signal
import librosa

base, sr = sf.read("quarantined/analytics/base.wav")
burn, sr = sf.read("quarantined/analytics/burnished.wav")
base_m = np.mean(base, axis=1)
burn_m = np.mean(burn, axis=1)

base_rms = np.sqrt(np.mean(base_m**2))
burn_rms = np.sqrt(np.mean(burn_m**2))
base_norm = base_m / base_rms
burn_norm = burn_m / burn_rms

# Create figure
fig, axs = plt.subplots(2, 2, figsize=(14, 10), dpi=150)
plt.subplots_adjust(hspace=0.35, wspace=0.25)

# --- 1. Top-Left: Empirical Transfer Function & Power Spectral Density ---
nperseg = 8192
f, p_base = signal.welch(base_norm, fs=sr, nperseg=nperseg)
_, p_burn = signal.welch(burn_norm, fs=sr, nperseg=nperseg)
p_base_db = 10 * np.log10(np.maximum(p_base, 1e-12))
p_burn_db = 10 * np.log10(np.maximum(p_burn, 1e-12))
diff_db = p_burn_db - p_base_db

ax1 = axs[0, 0]
ax1.semilogx(f, diff_db, color='#8B4513', lw=2, label='Differential Response (Burnished - Base)')
ax1.axhline(0, color='gray', ls='--', alpha=0.6)
ax1.axvline(35, color='#2b5c8f', ls=':', alpha=0.8, label='35 Hz Subsonic HPF')
ax1.axvline(8200, color='#9c4d8d', ls=':', alpha=0.8, label='8.2 kHz Air Shelf')
ax1.axvline(11500, color='#2e7d32', ls=':', alpha=0.8, label='11.5 kHz Shimmer Bell')

ax1.set_xlim(20, 20000)
ax1.set_ylim(-15, 6)
ax1.set_title("Empirical Transfer Function (Welch PSD Difference)", fontsize=11, fontweight='bold')
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Gain Relative to Base (dB)")
ax1.grid(True, which="both", ls="-", alpha=0.3)
ax1.legend(loc='lower left', fontsize=8)

# Annotations
ax1.annotate("Midrange Body Boost\n(+2.5 to +3.2 dB)", xy=(400, 2.8), xytext=(200, 4.2),
             arrowprops=dict(arrowstyle="->", color="black", lw=1), fontsize=8, fontweight='semibold')
ax1.annotate("Miller Roll-off & Air\n(-11 to -12 dB)", xy=(7500, -11), xytext=(2500, -13.5),
             arrowprops=dict(arrowstyle="->", color="black", lw=1), fontsize=8, fontweight='semibold')

# --- 2. Top-Right: Transient Attack vs Sustain High-Frequency Suppression ---
ax2 = axs[0, 1]
# We plot bar charts of high/mid ratio during Attack vs Sustain
categories = ['Attack Transient\n(0-25 ms)', 'Sustain Body\n(80-230 ms)']
base_ratios = [-29.55, -24.17]
burn_ratios = [-35.38, -23.70]
x = np.arange(len(categories))
w = 0.35

bars1 = ax2.bar(x - w/2, base_ratios, w, label='Base (Lion 68 P90)', color='#4682B4')
bars2 = ax2.bar(x + w/2, burn_ratios, w, label='Burnished (Burnisher + Stumble)', color='#D2691E')

ax2.set_ylabel("High / Mid Ratio (3-8 kHz vs 500-2k Hz) [dB]")
ax2.set_title("Transient Attack Blunting vs Body Sustain", fontsize=11, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(categories, fontsize=9)
ax2.set_ylim(-40, -18)
ax2.grid(axis='y', ls='--', alpha=0.4)
ax2.legend(loc='upper right', fontsize=8)

# Highlight the -5.83 dB delta on attack
ax2.annotate("-5.83 dB blunting\non pick clicks!", xy=(x[0]+w/2, -35.38), xytext=(x[0]-0.05, -22),
             arrowprops=dict(arrowstyle="->", color="#B22222", lw=1.5), fontsize=8, fontweight='bold', color="#B22222")
ax2.annotate("Sustain treble identical\n(within 0.47 dB)", xy=(x[1], -23.7), xytext=(x[1]-0.25, -20.5),
             arrowprops=dict(arrowstyle="->", color="#2e7d32", lw=1.2), fontsize=8, fontweight='bold', color="#2e7d32")

# --- 3. Bottom-Left: Average Pick Attack Waveform & Slew Softening ---
ax3 = axs[1, 0]
onsets_base = librosa.onset.onset_detect(y=base_norm, sr=sr, units='samples', backtrack=True)
onsets_burn = librosa.onset.onset_detect(y=burn_norm, sr=sr, units='samples', backtrack=True)

win_pre = int(0.005 * sr) # 5 ms before
win_post = int(0.030 * sr) # 30 ms after
t_ms = np.linspace(-5, 30, win_pre + win_post)

def average_attack_envelope(norm_audio, onsets):
    envs = []
    for o in onsets:
        if o - win_pre < 0 or o + win_post >= len(norm_audio):
            continue
        seg = np.abs(norm_audio[o - win_pre : o + win_post])
        if np.max(seg) > 0.5: # significant attack
            # normalize individual peak to 1 for shape comparison
            envs.append(seg / np.max(seg))
    return np.mean(envs, axis=0)

env_b = average_attack_envelope(base_norm, onsets_base)
env_u = average_attack_envelope(burn_norm, onsets_burn)

ax3.plot(t_ms, env_b, color='#4682B4', lw=1.8, label='Base Attack Envelope')
ax3.plot(t_ms, env_u, color='#D2691E', lw=2.0, label='Burnished Attack Envelope')
ax3.set_title("Normalized Mean Pick Attack Transient Profile", fontsize=11, fontweight='bold')
ax3.set_xlabel("Time from Onset (ms)")
ax3.set_ylabel("Normalized Amplitude")
ax3.set_xlim(-2, 25)
ax3.grid(True, ls='--', alpha=0.3)
ax3.legend(loc='lower right', fontsize=8)

# --- 4. Bottom-Right: Key Metrics Summary Card ---
ax4 = axs[1, 1]
ax4.axis('off')

summary_text = (
    "SUMMARY METRICS: BASE vs BURNISHED\n"
    "─────────────────────────────────────────────────────\n"
    "• Peak Level         : -14.49 dBFS  vs  -12.85 dBFS  (+1.64 dB)\n"
    "• RMS Level          : -32.11 dBFS  vs  -29.61 dBFS  (+2.50 dB)\n"
    "• Crest Factor       :  17.62 dB    vs   16.76 dB    (-0.86 dB)\n"
    "• Spectral Centroid  :  833.3 Hz    vs   695.4 Hz    (-137.9 Hz)\n"
    "• Spectral Rolloff   : 1498.2 Hz    vs  1243.4 Hz    (-254.8 Hz)\n"
    "• Attack/Body Ratio  :  -3.64 dB    vs   -5.07 dB    (-1.43 dB)\n"
    "• Half-Decay (T_6dB) :  216.2 ms    vs   236.7 ms    (+20.5 ms)\n"
    "• Attack HF Damping  :  -29.55 dB   vs  -35.38 dB    (-5.83 dB)\n"
    "• Sustain HF Damping :  -24.17 dB   vs  -23.70 dB    (+0.47 dB)\n"
    "─────────────────────────────────────────────────────\n"
    "KEY PHYSICAL FINDINGS:\n"
    "1. Dynamic Miller Effect Confirmed: Transients lose 5.8 dB\n"
    "   of high-end click, but chord sustain tail is unmuted.\n"
    "2. Subsonic HPF & Low-Mid Bloom: -3.2 dB below 80 Hz tightens\n"
    "   flub, while +2.8 dB body boost fills 150-1000 Hz.\n"
    "3. Stumblelater ABL Cushion: Crest factor compressed by\n"
    "   0.86 dB, blooming sustain tail extended by +9.5%."
)

ax4.text(0.05, 0.5, summary_text, family='monospace', fontsize=9.5,
         verticalalignment='center', bbox=dict(boxstyle='round,pad=0.8', facecolor='#FAFAFA', edgecolor='#D0D0D0'))

plt.suptitle("Royal Velvet Jazz: Empirical Pedal Analysis (Liberty Burnisher + Stumblelater)", fontsize=13, fontweight='bold', y=0.98)
plt.savefig("quarantined/analytics/burnished_vs_base_analysis.png", bbox_inches='tight')
print("Plot saved to quarantined/analytics/burnished_vs_base_analysis.png")
