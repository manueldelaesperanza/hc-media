"""Recorta 12 s de una pista (la ventana con más energía dentro de los primeros 60 s) y la deja lista para un reel.

Uso: python3 -I tools/music_cut.py <entrada.mp3> <salida.wav>
"""
import subprocess
import sys

import numpy as np

SR = 44100
DUR = 12.0
src, out = sys.argv[1], sys.argv[2]
raw = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", src, "-t", "75", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(raw, dtype=np.float32)
total = len(x) / SR
if total <= DUR + 1:
    start = 0.0
else:
    hop = int(0.5 * SR); win = int(DUR * SR)
    e = np.convolve(x ** 2, np.ones(hop), "valid")[::hop]
    k = int(DUR / 0.5)
    sums = np.convolve(e, np.ones(k), "valid")
    lim = min(len(sums), int((min(total, 62) - DUR) / 0.5) + 1)
    best = sums[:lim]
    # preferir el principio si está cerca del máximo (las pistas suelen arrancar con el tema)
    cand = np.where(best >= 0.85 * best.max())[0]
    start = float(cand[0] * 0.5)
af = f"atrim={start}:{start + DUR},asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={DUR - 1.2}:d=1.2,loudnorm=I=-15:TP=-1.5:LRA=11"
subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", src, "-af", af, "-ar", str(SR), "-ac", "2", out], check=True)
print(f"start={start:.1f}s total={total:.0f}s")
