#!/usr/bin/env python3
"""Reconstruye imágenes troceadas desde los resultados guardados del navegador.
Uso: python3 tools/img_assemble.py 80 84 ...  -> carruseles/NN/portada.jpg o reels/NN/imagen.jpg
"""
import glob, json, re, base64, sys
from pathlib import Path
D = '/root/.claude/projects/-home-claude/5ab535d1-cd2a-591e-b076-cfd768350c06/tool-results/'
ROOT = Path(__file__).resolve().parent.parent
chunks = {}
for f in glob.glob(D + '*.txt') + glob.glob(D + '*.json'):
    raw = open(f).read()
    if 'C|' not in raw: continue
    try: t = "".join(x.get("text", "") for x in json.loads(raw))
    except Exception: t = raw
    for m in re.finditer(r'C\|(\w+)\|(\d+)\|([A-Za-z0-9+/=]*)\|E', t):
        chunks.setdefault(m.group(1), {})[int(m.group(2))] = m.group(3)
for k in sys.argv[1:]:
    c = chunks.get(k, {})
    s = "".join(c[i] for i in sorted(c))
    data = base64.b64decode(s)
    car = ROOT / 'carruseles' / k
    out = (car / 'portada.jpg') if car.exists() else (ROOT / 'reels' / k / 'imagen.jpg')
    out.write_bytes(data)
    spec = out.parent / 'spec.json'
    if spec.exists():
        j = json.loads(spec.read_text()); j['image'] = out.name; spec.write_text(json.dumps(j, ensure_ascii=False, indent=1))
    print(k, len(c), 'chunks', len(data), 'bytes ->', out)
