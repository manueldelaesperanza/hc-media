"""Print Metricool createScheduledPost info JSON for a piece (raw GitHub URLs)."""
import json, sys
from pathlib import Path
R = "https://raw.githubusercontent.com/manueldelaesperanza/hc-media/main/out/"
ROOT = Path(__file__).resolve().parent.parent
for id in sys.argv[1:]:
    d = json.loads((ROOT / "content" / f"{id}.json").read_text())
    date = d["date"]
    base = {"draft": False, "descendants": [], "firstCommentText": "", "hasNotReadNotes": False, "mediaAltText": [],
            "providers": [{"network": "instagram"}, {"network": "facebook"}],
            "publicationDate": {"dateTime": date, "timezone": "Europe/Madrid"}, "shortener": False,
            "smartLinkData": {"ids": []}, "text": d["caption"]}
    if d["type"] == "reel":
        base.update(autoPublish=False, media=[R + f"{id}/reel.mp4"], videoThumbnailUrl=R + f"{id}/portada.jpg",
                    instagramData={"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True, "autoPublish": False},
                    facebookData={"type": "REEL"})
    else:
        n = len(d["slides"]) + 2
        base.update(autoPublish=True, media=[R + f"{id}/slide{i:02d}.jpg" for i in range(1, n + 1)],
                    instagramData={"type": "POST", "isAiGenerated": bool(d.get("photo"))}, facebookData={"type": "POST"})
    print(f"=== {id} {date}+01:00")
    print(json.dumps(base, ensure_ascii=False))
