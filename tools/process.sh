#!/bin/bash
# usage: tools/process.sh ID   (grab image iID, render, preview sheet, commit+push)
set -e
cd /home/claude/hc-media
ID=$1
python3 tools/grab.py "{\"i$ID\":[\"/home/claude/hc-media/img/$ID.jpg\",0]}"
python3 content/q_9nov.py >/dev/null
python3 tools/hc_render.py content/$ID.json >/dev/null
python3 - "$ID" <<'PY'
import sys, json
from PIL import Image
from pathlib import Path
id=sys.argv[1]; d=json.loads(Path(f'content/{id}.json').read_text())
if d['type']=='reel':
    ims=[Image.open(f'out/{id}/frames/f0{i}.png').convert('RGB').resize((270,480)) for i in (1,2,3,4)]
    sheet=Image.new('RGB',(1080,480)); [sheet.paste(im,(k*270,0)) for k,im in enumerate(ims)]
else:
    n=len(d['slides'])+2
    ims=[Image.open(f'out/{id}/slide{i:02d}.jpg').resize((360,450)) for i in range(1,n+1)]
    sheet=Image.new('RGB',(1080,450*((n+2)//3))); [sheet.paste(im,((k%3)*360,(k//3)*450)) for k,im in enumerate(ims)]
sheet.save('/tmp/claude-0/-home-claude/5ab535d1-cd2a-591e-b076-cfd768350c06/scratchpad/look/p.jpg')
PY
git add -A >/dev/null; git commit -qm "Add piece $ID

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0189LKGzZcQmhpSHzyCbdKu4"; git push -q 2>&1 | tail -1
echo "done $ID"
