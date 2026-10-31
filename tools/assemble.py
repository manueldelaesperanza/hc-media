import glob, json, re, base64, sys, os
D='/root/.claude/projects/-home-claude/5ab535d1-cd2a-591e-b076-cfd768350c06/tool-results/'
chunks={}
for f in glob.glob(D+'*.txt')+glob.glob(D+'*.json'):
    raw=open(f).read()
    if 'C|' not in raw: continue
    try: t="".join(x.get("text","") for x in json.loads(raw))
    except Exception: t=raw
    for m in re.finditer(r'C\|(\w+)\|(\d+)\|([A-Za-z0-9+/=]*)\|E', t):
        chunks.setdefault(m.group(1),{})[int(m.group(2))]=m.group(3)
want=json.loads(sys.argv[1])  # {"58v":3008728,...}
out=sys.argv[2]
for k,L in want.items():
    c=chunks.get(k,{}); s="".join(c[i] for i in sorted(c))
    ok=len(s)==L
    print(k, len(c), len(s), L, 'OK' if ok else 'MISSING')
    if ok:
        nn,kind=k[:-1],k[-1]; os.makedirs(f"{out}/{nn}",exist_ok=True)
        open(f"{out}/{nn}/"+("reel.mp4" if kind=='v' else "portada.jpg"),"wb").write(base64.b64decode(s))
