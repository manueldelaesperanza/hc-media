"""Música genérica original para los reels de Hope Longevity (sintetizada, sin derechos de terceros).

Uso: python3 tools/music_gen.py <salida_dir>  -> genera pista_1.wav ... pista_4.wav (12 s, 44.1 kHz, estéreo)
"""
import sys
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt, fftconvolve

SR = 44100
DUR = 12.0
rng = np.random.default_rng(7)


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def env(n, a, r):
    e = np.ones(n)
    ai = max(1, int(a * SR)); ri = max(1, int(r * SR))
    e[:ai] = np.linspace(0, 1, ai)
    e[-ri:] *= np.linspace(1, 0, ri)
    return e


def lp(x, fc, order=2):
    return sosfilt(butter(order, fc, "low", fs=SR, output="sos"), x)


def hp(x, fc, order=2):
    return sosfilt(butter(order, fc, "high", fs=SR, output="sos"), x)


def saw(f, n, detune=0.0):
    t = np.arange(n) / SR
    ph = (f * (1 + detune)) * t
    return 2 * (ph - np.floor(ph + 0.5))


def pad(notes, n, bright):
    x = np.zeros(n)
    for m in notes:
        for d in (-0.004, 0.0, 0.0045):
            x += saw(midi(m), n, d)
    x = lp(x, bright, 2)
    return x * env(n, 0.35, 0.4) / (len(notes) * 3)


def pluck(m, n):
    t = np.arange(n) / SR
    f = midi(m)
    x = 2 * np.abs(2 * ((f * t) % 1) - 1) - 1  # triángulo
    x += 0.3 * np.sin(2 * np.pi * 2 * f * t)
    return x * np.exp(-t * 7) * env(n, 0.004, 0.02)


def kick(n):
    t = np.arange(n) / SR
    f = 50 + 70 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


def hat(n):
    t = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7000) * np.exp(-t * 60)


def reverb(x, secs=1.6, mix=0.25):
    n = int(secs * SR)
    ir = rng.standard_normal(n) * np.exp(-np.arange(n) / SR * 4)
    ir = lp(ir, 5000)
    wet = fftconvolve(x, ir)[: len(x)]
    wet /= np.max(np.abs(wet)) + 1e-9
    return (1 - mix) * x / (np.max(np.abs(x)) + 1e-9) + mix * wet


# (tónica MIDI, bpm, progresión en grados de acorde, brillo del pad, patrón del arpegio)
TRACKS = [
    (62, 100, [(0, 4, 7, 11), (-3, 0, 4, 7), (-7, -3, 0, 4), (-5, -1, 2, 7)], 1800, [0, 2, 1, 3, 2, 1, 3, 2]),   # Re mayor 7, cálido
    (57, 108, [(0, 3, 7, 10), (-4, 0, 3, 7), (-2, 2, 5, 9), (-5, -2, 2, 5)], 2200, [0, 1, 2, 3, 2, 1, 0, 2]),   # La menor 7, sereno
    (60, 96, [(0, 4, 7, 14), (5, 9, 12, 16), (-3, 0, 4, 9), (7, 11, 14, 17)], 1500, [0, 2, 3, 2, 1, 2, 3, 1]),  # Do mayor add9, luminoso
    (64, 104, [(0, 3, 7, 10), (-4, 0, 3, 8), (-9, -5, -2, 3), (-2, 2, 5, 10)], 2000, [3, 2, 1, 0, 1, 2, 3, 2]), # Mi menor, enérgico suave
]


def track(idx):
    root, bpm, prog, bright, arp = TRACKS[idx]
    N = int(DUR * SR)
    beat = 60 / bpm
    bar = 4 * beat
    L = np.zeros(N); R = np.zeros(N)
    nb = int(np.ceil(DUR / bar))
    for b in range(nb):
        ch = prog[b % len(prog)]
        s = int(b * bar * SR); n = min(int(bar * SR) + int(0.3 * SR), N - s)
        if n <= 0:
            break
        p = pad([root + c for c in ch], n, bright)
        L[s:s + n] += 0.9 * p; R[s:s + n] += 0.9 * p
        # bajo
        t = np.arange(n) / SR
        bass = np.sin(2 * np.pi * midi(root + ch[0] - 24) * t) * env(n, 0.05, 0.3)
        L[s:s + n] += 0.55 * bass; R[s:s + n] += 0.55 * bass
        # arpegio en corcheas
        for k in range(8):
            ps = s + int(k * beat / 2 * SR)
            if ps >= N:
                break
            m = root + 12 + ch[arp[k] % len(ch)]
            pn = min(int(0.5 * SR), N - ps)
            x = pluck(m, pn) * 0.22
            pan = 0.35 if k % 2 else -0.35
            L[ps:ps + pn] += x * (1 - pan); R[ps:ps + pn] += x * (1 + pan)
    # percusión suave (entra en el 2º compás)
    nbeats = int(DUR / beat)
    for k in range(nbeats):
        st = int(k * beat * SR)
        if st >= N:
            break
        if k >= 4:
            kn = min(int(0.35 * SR), N - st)
            kk = kick(kn) * (0.55 if k % 2 == 0 else 0.35)
            L[st:st + kn] += kk; R[st:st + kn] += kk
        hs = int((k + 0.5) * beat * SR)
        if hs < N and k >= 2:
            hn = min(int(0.08 * SR), N - hs)
            h = hat(hn) * 0.12
            L[hs:hs + hn] += h; R[hs:hs + hn] += h * 0.8
    L = reverb(L); R = reverb(R)
    fade = env(N, 0.25, 1.2)
    st = np.stack([L * fade, R * fade], 1)
    st /= np.max(np.abs(st)) + 1e-9
    return (st * 0.89 * 32767).astype(np.int16)


if __name__ == "__main__":
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for i in range(len(TRACKS)):
        wavfile.write(out / f"pista_{i+1}.wav", SR, track(i))
        print("ok", out / f"pista_{i+1}.wav")
