"""Música original por estado de ánimo para los reels de Hope Longevity (sintetizada, sin derechos de terceros).

Uso: python3 tools/music_gen2.py <mood> <variante:int> <salida.wav>
Moods: mito, energia, calma, natural, calido, festivo, mediterraneo, manana
Cada (mood, variante) produce una pista distinta: cambia tonalidad, tempo, progresión y orquestación.
"""
import sys

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt, fftconvolve

SR = 44100
DUR = 12.0


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def lin_env(n, a, r):
    e = np.ones(n)
    ai = max(1, min(n, int(a * SR))); ri = max(1, min(n, int(r * SR)))
    e[:ai] = np.linspace(0, 1, ai)
    e[-ri:] *= np.linspace(1, 0, ri)
    return e


def filt(x, fc, kind="low", order=2):
    return sosfilt(butter(order, fc, kind, fs=SR, output="sos"), x)


T = lambda n: np.arange(n) / SR


# ---------- instrumentos ----------
def saw(f, n, det=0.0):
    ph = f * (1 + det) * T(n)
    return 2 * (ph - np.floor(ph + 0.5))


def pad(notes, n, bright, att=0.4):
    x = sum(saw(midi(m), n, d) for m in notes for d in (-0.005, 0, 0.005))
    return filt(x, bright) * lin_env(n, att, 0.5) / (len(notes) * 3)


def pluck(m, n, decay=7, bright=1.0):
    t = T(n); f = midi(m)
    x = 2 * np.abs(2 * ((f * t) % 1) - 1) - 1 + 0.3 * bright * np.sin(2 * np.pi * 2 * f * t)
    return x * np.exp(-t * decay) * lin_env(n, 0.003, 0.02)


def pizz(m, n):
    x = filt(saw(midi(m), n), 2500) * np.exp(-T(n) * 14)
    return x * lin_env(n, 0.002, 0.02)


def marimba(m, n):
    t = T(n); f = midi(m)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 6) + 0.25 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t * 18)
    return x * lin_env(n, 0.002, 0.02)


def bell(m, n):
    t = T(n); f = midi(m)
    mod = 2.4 * np.exp(-t * 2.5) * np.sin(2 * np.pi * f * 3.5 * t)
    return np.sin(2 * np.pi * f * t + mod) * np.exp(-t * 2.2) * lin_env(n, 0.002, 0.05)


def piano(m, n):
    t = T(n); f = midi(m)
    x = sum((0.6 ** k) * np.sin(2 * np.pi * f * (k + 1) * t * (1 + 0.0004 * k * k)) for k in range(6))
    return x * (0.7 * np.exp(-t * 3) + 0.3 * np.exp(-t * 0.8)) * lin_env(n, 0.003, 0.08)


def guitar(m, n):  # cuerda pulsada Karplus-Strong
    f = midi(m); p = max(2, int(SR / f))
    buf = np.random.default_rng(m).uniform(-1, 1, p)
    out = np.empty(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = 0.996 * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    return filt(out, 4000) * lin_env(n, 0.002, 0.05)


def bass(m, n, kind="sine"):
    t = T(n); f = midi(m)
    x = np.sin(2 * np.pi * f * t) if kind == "sine" else filt(saw(f, n), 400)
    return x * lin_env(n, 0.01, 0.05)


def kick(n):
    t = T(n); f = 48 + 80 * np.exp(-t * 32)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 8)


def snare(n, rng):
    t = T(n)
    return (filt(rng.standard_normal(n), 1800, "high") * 0.7 + 0.4 * np.sin(2 * np.pi * 190 * t)) * np.exp(-t * 22)


def hat(n, rng, dec=60):
    return filt(rng.standard_normal(n), 7500, "high") * np.exp(-T(n) * dec)


def shaker(n, rng):
    return filt(rng.standard_normal(n), 5000, "high") * lin_env(n, 0.02, 0.06) * 0.6


def clap(n, rng):
    t = T(n); x = filt(rng.standard_normal(n), 1200, "high")
    e = np.exp(-t * 30) + 0.6 * np.exp(-np.maximum(t - 0.012, 0) * 30) * (t > 0.012)
    return x * e


def reverb(x, rng, secs=1.6, mix=0.25):
    n = int(secs * SR)
    ir = filt(rng.standard_normal(n) * np.exp(-T(n) * (5.5 / secs)), 5000)
    wet = fftconvolve(x, ir)[: len(x)]
    wet /= np.max(np.abs(wet)) + 1e-9
    return (1 - mix) * x / (np.max(np.abs(x)) + 1e-9) + mix * wet


# ---------- progresiones (grados en semitonos desde la tónica) ----------
MAJ = [[(0, 4, 7), (-3, 0, 4), (-7, -3, 0), (-5, -1, 2)],      # I vi IV V
       [(0, 4, 7), (-5, -1, 2), (-3, 0, 4), (-7, -3, 0)],      # I V vi IV
       [(0, 4, 7, 11), (2, 5, 9, 12), (-3, 0, 4, 7), (-5, -1, 2, 5)],  # Imaj7 ii vi V7
       [(0, 4, 7), (5, 9, 12), (-3, 0, 4), (7, 11, 14)]]      # I IV vi V
MIN = [[(0, 3, 7), (-4, 0, 3), (-9, -5, -2), (-2, 2, 5)],     # i VI III VII
       [(0, 3, 7, 10), (5, 8, 12, 15), (-4, 0, 3, 7), (-2, 2, 5, 9)],  # i7 iv7 VI VII
       [(0, 3, 7), (-2, 2, 5), (-4, 0, 3), (-5, -1, 2)]]      # i VII VI V
PHRYG = [[(0, 4, 7), (1, 5, 8), (-2, 1, 5), (-4, 0, 3)]]     # cadencia andaluza invertida (I bII bVII bVI)

MOODS = {
    #           tónicas,             bpm,        progs, instrumento lead, ritmo
    "mito":         ([60, 62, 65, 67, 57], (112, 124), MAJ, "pizz", "funky"),
    "energia":      ([57, 59, 62, 64, 55], (118, 128), MIN, "pluck", "drive"),
    "calma":        ([60, 62, 64, 65, 57], (64, 76), MAJ, "piano", "none"),
    "natural":      ([62, 64, 67, 60, 65], (88, 98), MAJ, "guitar", "soft"),
    "calido":       ([60, 65, 62, 67, 64], (80, 92), MAJ, "piano", "soft"),
    "festivo":      ([67, 62, 65, 60, 69], (100, 108), MAJ, "bell", "festive"),
    "mediterraneo": ([64, 62, 57, 59, 60], (100, 112), PHRYG, "guitar", "latin"),
    "manana":       ([62, 64, 60, 65, 67], (100, 108), MAJ, "marimba", "soft"),
}


def render(mood, var):
    roots, (b0, b1), progs, lead, rhythm = MOODS[mood]
    rng = np.random.default_rng(1000 * var + len(mood))
    root = roots[var % len(roots)]
    bpm = b0 + (var * 7) % (b1 - b0 + 1)
    prog = progs[var % len(progs)]
    if var % 2 and mood != "mediterraneo":
        prog = prog[1:] + prog[:1]
    N = int(DUR * SR); beat = 60 / bpm; bar = 4 * beat
    L = np.zeros(N); R = np.zeros(N)

    def add(x, start, gain=1.0, pan=0.0):
        s = int(start * SR)
        if s >= N:
            return
        x = x[: N - s]
        L[s:s + len(x)] += x * gain * (1 - pan); R[s:s + len(x)] += x * gain * (1 + pan)

    pad_bright = {"calma": 1100, "calido": 1400, "energia": 2600, "festivo": 2000}.get(mood, 1800)
    pad_gain = {"calma": 1.0, "calido": 0.8, "mito": 0.45, "energia": 0.55}.get(mood, 0.6)
    nb = int(np.ceil(DUR / bar)) + 1
    arp_patterns = [[0, 1, 2, 1, 0, 2, 1, 2], [0, 2, 1, 2, 0, 1, 2, 1], [2, 1, 0, 1, 2, 0, 1, 0], [0, 1, 2, 3, 2, 1, 0, 1]]
    arp = arp_patterns[var % len(arp_patterns)]
    for b in range(nb):
        ch = prog[b % len(prog)]
        t0 = b * bar
        if t0 >= DUR:
            break
        n = int((bar + 0.4) * SR)
        add(pad([root + c for c in ch], n, pad_bright, 0.6 if mood == "calma" else 0.25), t0, pad_gain)
        # bajo
        if mood in ("calma",):
            add(bass(root + ch[0] - 24, int(bar * SR)) * lin_env(int(bar * SR), 0.5, 0.6), t0, 0.5)
        elif rhythm in ("funky", "latin"):
            for k, off in enumerate((0, 1.5, 2, 3, 3.5)):
                nn = root + ch[0] - 24 + (12 if k == 3 else 0)
                add(bass(nn, int(beat * 0.45 * SR), "saw"), t0 + off * beat, 0.7)
        elif rhythm == "drive":
            for k in range(8):
                add(bass(root + ch[0] - 24, int(beat * 0.4 * SR), "saw"), t0 + k * beat / 2, 0.65)
        else:
            add(bass(root + ch[0] - 24, int(bar * 0.9 * SR)), t0, 0.55)
        # melodía / arpegio
        steps = 8 if mood not in ("calma", "calido") else 4
        for k in range(steps):
            st = t0 + k * (bar / steps)
            if mood == "calma" and k % 2 and rng.random() < 0.5:
                continue
            m = root + 12 + ch[arp[k % 8] % len(ch)]
            ln = int((0.9 if lead in ("piano", "bell", "guitar") else 0.4) * SR)
            if lead == "pizz":
                x = pizz(m + 12 if k % 4 == 3 else m, ln); g = 0.45
            elif lead == "pluck":
                x = pluck(m, ln, 9); g = 0.35
            elif lead == "piano":
                x = piano(m, ln); g = 0.32
            elif lead == "bell":
                x = bell(m + 12, ln); g = 0.3
            elif lead == "guitar":
                x = guitar(m, ln); g = 0.55
            else:
                x = marimba(m + 12, ln); g = 0.45
            add(x, st, g, 0.3 if k % 2 else -0.3)
    # percusión
    nbeats = int(DUR / beat) + 1
    for k in range(nbeats):
        st = k * beat
        if st >= DUR:
            break
        intro = k < 4
        if rhythm == "drive":
            if not intro or k % 2 == 0:
                add(kick(int(0.35 * SR)), st, 0.8)
            if k % 2 == 1 and not intro:
                add(clap(int(0.2 * SR), rng), st, 0.35)
            for h in (0.5,):
                add(hat(int(0.06 * SR), rng), st + h * beat, 0.18)
            add(hat(int(0.03 * SR), rng, 120), st + 0.25 * beat, 0.07)
            add(hat(int(0.03 * SR), rng, 120), st + 0.75 * beat, 0.07)
        elif rhythm == "funky":
            if k % 4 in (0, 2) or (k % 4 == 3 and var % 2):
                add(kick(int(0.3 * SR)), st, 0.65 if not intro else 0.3)
            if k % 2 == 1 and not intro:
                add(snare(int(0.2 * SR), rng), st, 0.3)
            add(hat(int(0.05 * SR), rng), st + 0.5 * beat, 0.14)
            add(hat(int(0.03 * SR), rng, 110), st, 0.06)
        elif rhythm == "soft":
            if not intro and k % 2 == 0:
                add(kick(int(0.3 * SR)), st, 0.4)
            add(shaker(int(0.12 * SR), rng), st + 0.5 * beat, 0.25)
            if not intro and k % 4 == 3:
                add(snare(int(0.15 * SR), rng), st, 0.12)
        elif rhythm == "festive":
            if not intro and k % 2 == 0:
                add(kick(int(0.3 * SR)), st, 0.4)
            for h in (0, 0.5):
                add(hat(int(0.12 * SR), rng, 25), st + h * beat, 0.08)  # cascabeles
        elif rhythm == "latin":
            for off in (0, 0.75, 1.5):
                if not intro or off == 0:
                    pass
            pos = k % 4
            if pos in (0, 2):
                add(kick(int(0.25 * SR)), st, 0.5)
            for off in ((0.0, 0.5) if pos % 2 == 0 else (0.25, 0.75)):
                add(clap(int(0.12 * SR), rng), st + off * beat, 0.16 if not intro else 0.08)
            add(shaker(int(0.1 * SR), rng), st + 0.5 * beat, 0.2)
    L2 = reverb(L, rng, 2.4 if mood == "calma" else 1.5, 0.35 if mood in ("calma", "calido", "festivo") else 0.22)
    R2 = reverb(R, np.random.default_rng(var + 99), 2.4 if mood == "calma" else 1.5, 0.35 if mood in ("calma", "calido", "festivo") else 0.22)
    fade = lin_env(N, 0.2, 1.2)
    st = np.stack([L2 * fade, R2 * fade], 1)
    st /= np.max(np.abs(st)) + 1e-9
    return (st * 0.89 * 32767).astype(np.int16), root, bpm


if __name__ == "__main__":
    mood, var, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    data, root, bpm = render(mood, var)
    wavfile.write(out, SR, data)
    print(mood, var, "root", root, "bpm", bpm, out)
