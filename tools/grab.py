"""Rebuild base64 chunks returned by the browser (C|key|i|...|E) into files.
Usage: python3 grab.py '{"key": ["/out/path.jpg", expected_b64_len]}'"""
import glob, json, re, base64, sys, os
D='/root/.claude/projects/-home-claude/5ab535d1-cd2a-591e-b076-cfd768350c06/tool-results/'
chunks={}
lens={}
for f in glob.glob(D+'*.txt')+glob.glob(D+'*.json'):
    raw=open(f).read()
    if 'C|' not in raw: continue
    try: t="".join(x.get("text","") for x in json.loads(raw))
    except Exception: t=raw
    for m in re.finditer(r'L\|(\w+)\|(\d+)\|', t):
        lens[m.group(1)]=int(m.group(2))
    for m in re.finditer(r'C\|(\w+)\|(\d+)\|([A-Za-z0-9+/=]*)\|E', t):
        chunks.setdefault(m.group(1),{})[int(m.group(2))]=m.group(3)
for k,(out,L) in json.loads(sys.argv[1]).items():
    L = L or lens.get(k, -1)
    c=chunks.get(k,{}); s="".join(c[i] for i in sorted(c))
    print(k,len(c),len(s),L,'OK' if len(s)==L else 'MISSING')
    if len(s)==L:
        os.makedirs(os.path.dirname(out),exist_ok=True); open(out,'wb').write(base64.b64decode(s))
