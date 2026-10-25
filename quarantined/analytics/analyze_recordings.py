#!/usr/bin/env python3
"""
Comparative analysis script for base vs burnished guitar recordings in quarantined/analytics.
"""

import os
import sys
import numpy as np
import soundfile as sf
from scipy import signal, stats
import librosa

def analyze():
    base_path = "quarantined/analytics/base.wav"
    burn_path = "quarantined/analytics/burnished.wav"
    
    base_audio, sr = sf.read(base_path)
    burn_audio, sr = sf.read(burn_path)
    
    # Mono conversion
    base_m = np.mean(base_audio, axis=1)
    burn_m = np.mean(burn_audio, axis=1)
    
    print(f"Sampling rate: {sr} Hz")
    print(f"Base length: {len(base_m)} samples ({len(base_m)/sr:.2f} s)")
    print(f"Burnished length: {len(burn_m)} samples ({len(burn_m)/sr:.2f} s)")
    
    # Basic energy stats
    base_rms = np.sqrt(np.mean(base_m**2))
    burn_rms = np.sqrt(np.mean(burn_m**2))
    base_peak = np.max(np.abs(base_m))
    burn_peak = np.max(np.abs(burn_m))
    
    print(f"\n--- OVERALL LEVELS ---")
    print(f"Base Peak: {20*np.log10(base_peak):.2f} dBFS | RMS: {20*np.log10(base_rms):.2f} dBFS | Crest Factor: {20*np.log10(base_peak/base_rms):.2f} dB")
    print(f"Burnished Peak: {20*np.log10(burn_peak):.2f} dBFS | RMS: {20*np.log10(burn_rms):.2f} dBFS | Crest Factor: {20*np.log10(burn_peak/burn_rms):.2f} dB")
    print(f"Gain difference: Peak +{20*np.log10(burn_peak/base_peak):.2f} dB | RMS +{20*np.log10(burn_rms/base_rms):.2f} dB")
    
    # Normalize for spectral & transient shape comparisons
    base_norm = base_m / base_rms
    burn_norm = burn_m / burn_rms
    
    # 1. Long Term Average Spectrum (PSD via Welch)
    nperseg = 8192
    f, p_base = signal.welch(base_norm, fs=sr, nperseg=nperseg)
    _, p_burn = signal.welch(burn_norm, fs=sr, nperseg=nperseg)
    
    p_base_db = 10 * np.log10(np.maximum(p_base, 1e-12))
    p_burn_db = 10 * np.log10(np.maximum(p_burn, 1e-12))
    
    # Band energy analysis
    bands = [
        ("Subsonic (<35 Hz)", 0, 35),
        ("Sub-bass (35-80 Hz)", 35, 80),
        ("Bass (80-250 Hz)", 80, 250),
        ("Low-Mids (250-800 Hz)", 250, 800),
        ("Mids (800-2000 Hz)", 800, 2000),
        ("Presence / Attack (2-5 kHz)", 2000, 5000),
        ("Air / Treble (5-10 kHz)", 5000, 10000),
        ("Top Brilliance (>10 kHz)", 10000, sr//2)
    ]
    
    print(f"\n--- SPECTRAL ENERGY DISTRIBUTION (Normalized to equal overall RMS) ---")
    for name, low, high in bands:
        idx = (f >= low) & (f < high)
        e_base = np.sum(p_base[idx])
        e_burn = np.sum(p_burn[idx])
        db_diff = 10 * np.log10(e_burn / e_base) if e_base > 0 else 0
        print(f"{name:30s}: Burnished vs Base = {db_diff:+5.2f} dB")

    # 2. Spectral moments (Centroid, Spread, Rolloff, Flatness)
    sc_base = librosa.feature.spectral_centroid(y=base_norm, sr=sr)
    sc_burn = librosa.feature.spectral_centroid(y=burn_norm, sr=sr)
    
    ro_base = librosa.feature.spectral_rolloff(y=base_norm, sr=sr, roll_percent=0.85)
    ro_burn = librosa.feature.spectral_rolloff(y=burn_norm, sr=sr, roll_percent=0.85)
    
    sf_base = librosa.feature.spectral_flatness(y=base_norm)
    sf_burn = librosa.feature.spectral_flatness(y=burn_norm)
    
    print(f"\n--- SPECTRAL FEATURES ---")
    print(f"Mean Spectral Centroid : Base = {np.mean(sc_base):.1f} Hz | Burnished = {np.mean(sc_burn):.1f} Hz ({np.mean(sc_burn)-np.mean(sc_base):+.1f} Hz)")
    print(f"Mean Spectral Rolloff  : Base = {np.mean(ro_base):.1f} Hz | Burnished = {np.mean(ro_burn):.1f} Hz ({np.mean(ro_burn)-np.mean(ro_base):+.1f} Hz)")
    print(f"Mean Spectral Flatness : Base = {np.mean(sf_base):.6f} | Burnished = {np.mean(sf_burn):.6f}")

    # 3. Slew-Rate Analysis
    slew_base = np.abs(np.diff(base_norm)) * sr
    slew_burn = np.abs(np.diff(burn_norm)) * sr
    
    print(f"\n--- SLEW RATE & DERIVATIVE DYNAMICS (Normalized) ---")
    print(f"Peak Slew Rate : Base = {np.max(slew_base):.1f} V/s | Burnished = {np.max(slew_burn):.1f} V/s ({20*np.log10(np.max(slew_burn)/np.max(slew_base)):+.2f} dB)")
    print(f"99th %ile Slew : Base = {np.percentile(slew_base, 99):.1f} V/s | Burnished = {np.percentile(slew_burn, 99):.1f} V/s ({20*np.log10(np.percentile(slew_burn, 99)/np.percentile(slew_base, 99)):+.2f} dB)")
    print(f"95th %ile Slew : Base = {np.percentile(slew_base, 95):.1f} V/s | Burnished = {np.percentile(slew_burn, 95):.1f} V/s ({20*np.log10(np.percentile(slew_burn, 95)/np.percentile(slew_base, 95)):+.2f} dB)")
    print(f"Mean Slew Rate : Base = {np.mean(slew_base):.1f} V/s | Burnished = {np.mean(slew_burn):.1f} V/s")

    # 4. Transient Envelope / Pick Attack Analysis on Onsets
    onsets_base = librosa.onset.onset_detect(y=base_m, sr=sr, units='samples', backtrack=True)
    onsets_burn = librosa.onset.onset_detect(y=burn_m, sr=sr, units='samples', backtrack=True)
    
    def onset_attack_metrics(audio, onsets, sr):
        attack_len = int(0.025 * sr) # 25ms
        body_len = int(0.100 * sr)   # 100ms
        
        attack_rms_list = []
        body_rms_list = []
        attack_peak_list = []
        attack_slew_list = []
        rise_times = []
        
        for o in onsets:
            if o + attack_len + body_len >= len(audio):
                continue
            window = audio[o : o + attack_len]
            body_window = audio[o + attack_len : o + attack_len + body_len]
            
            pk = np.max(np.abs(window))
            if pk < 1e-4:
                continue
            
            att_rms = np.sqrt(np.mean(window**2))
            bd_rms = np.sqrt(np.mean(body_window**2))
            
            attack_rms_list.append(att_rms)
            body_rms_list.append(bd_rms)
            attack_peak_list.append(pk)
            attack_slew_list.append(np.max(np.abs(np.diff(window))) * sr)
            
            thresh_10 = 0.10 * pk
            thresh_90 = 0.90 * pk
            idx_10 = np.where(np.abs(window) >= thresh_10)[0]
            idx_90 = np.where(np.abs(window) >= thresh_90)[0]
            if len(idx_10) > 0 and len(idx_90) > 0 and idx_90[0] > idx_10[0]:
                rise_times.append((idx_90[0] - idx_10[0]) / sr * 1000)
                
        return {
            "attack_rms": np.array(attack_rms_list),
            "body_rms": np.array(body_rms_list),
            "attack_peak": np.array(attack_peak_list),
            "attack_slew": np.array(attack_slew_list),
            "rise_times": np.array(rise_times),
        }

    m_base = onset_attack_metrics(base_m, onsets_base, sr)
    m_burn = onset_attack_metrics(burn_m, onsets_burn, sr)
    
    print(f"\n--- ONSET ATTACK METRICS across notes ---")
    print(f"Notes analyzed: Base={len(m_base['attack_peak'])}, Burnished={len(m_burn['attack_peak'])}")
    print(f"Mean Attack Peak-to-RMS (Attack Crest): Base = {np.mean(20*np.log10(m_base['attack_peak']/m_base['attack_rms'])):.2f} dB | Burnished = {np.mean(20*np.log10(m_burn['attack_peak']/m_burn['attack_rms'])):.2f} dB")
    print(f"Mean Attack-to-Body RMS Ratio : Base = {np.mean(20*np.log10(m_base['attack_rms']/m_base['body_rms'])):+.2f} dB | Burnished = {np.mean(20*np.log10(m_burn['attack_rms']/m_burn['body_rms'])):+.2f} dB")
    print(f"Mean 10%-90% Rise Time : Base = {np.mean(m_base['rise_times']):.2f} ms | Burnished = {np.mean(m_burn['rise_times']):.2f} ms")
    print(f"Median 10%-90% Rise Time : Base = {np.median(m_base['rise_times']):.2f} ms | Burnished = {np.median(m_burn['rise_times']):.2f} ms")

if __name__ == "__main__":
    analyze()
