#!/usr/bin/env python3
"""Healthspan Club · plantillas de carrusel (1080x1350) y reel (1080x1920, 12 s).

Uso:
  python3 tools/hc_render.py spec.json OUT_DIR

spec.json (carrusel):
  {"type": "carousel", "image": "ruta/portada.png" | null,
   "slides": [
     {"kind": "cover", "kicker": "EL DATO", "title": "TU <g>AGARRE</g> PREDICE", "sub": "..."},
     {"kind": "news",  "label": "HEALTHSPAN HOY · 10 NOV", "title": "...", "sub": "..."},
     {"kind": "text",  "kicker": "...", "big": "-16%", "title": "...", "body": "..."},
     {"kind": "cta",   "title": "GUÁRDALO Y <g>EMPIEZA HOY</g>", "sub": "..."}]}
spec.json (reel):
  {"type": "reel", "image": "ruta/imagen.png",
   "beats": [{"kicker": "...", "title": "...", "sub": "..."}, x4]}
  -> OUT_DIR/reel.mp4 (4 frases + cierre, 2,4 s cada uno) y OUT_DIR/portada.jpg

En los títulos, <g>texto</g> va en dorado.
"""
import base64, json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BG, GOLD, WHITE, SOFT = "#141814", "#F2C14E", "#FFFFFF", "#D7DACF"


def _font_css():
    css = []
    for w in (400, 500, 700, 800):
        for sub in ("latin", "latin-ext"):
            f = ROOT / "fonts" / f"outfit-{sub}-{w}-normal.woff2"
            if f.exists():
                b = base64.b64encode(f.read_bytes()).decode()
                css.append(f"@font-face{{font-family:Outfit;font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}")
    return "\n".join(css)


FONTS = _font_css()


def logo_svg(size=150, stroke="#fff", dot=GOLD, sw=3.2):
    # Espiral de círculos que se van desplazando hacia abajo a la izquierda.
    rs = [75, 58, 42, 27, 14]
    end = (-25, 24)
    parts = []
    for i, r in enumerate(rs):
        t = i / (len(rs) - 1)
        cx, cy = end[0] * t, end[1] * t
        parts.append(f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r}' fill='none' stroke='{stroke}' stroke-width='{sw}'/>")
    parts.append(f"<circle cx='{end[0]}' cy='{end[1]}' r='5' fill='{dot}'/>")
    return f"<svg width='{size}' height='{size}' viewBox='-80 -80 160 160'>{''.join(parts)}</svg>"


def rings_svg(w, h, cx, cy, op=0.07):
    rs = [170, 340, 510, 680, 850]
    out = []
    for i, r in enumerate(rs):
        dx, dy = -i * 22, i * 30
        out.append(f"<circle cx='{cx+dx}' cy='{cy-dy}' r='{r}' fill='none' stroke='rgba(255,255,255,{op})' stroke-width='6'/>")
    return f"<svg class='rings' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>{''.join(out)}</svg>"


def gold(s):
    return (s or "").replace("<g>", "<span class='g'>").replace("</g>", "</span>")


def img_uri(path):
    p = Path(path)
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"


BASE_CSS = f"""
{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:{BG};font-family:Outfit,sans-serif;color:{WHITE}}}
.page{{position:relative;overflow:hidden;background:{BG}}}
.g{{color:{GOLD}}}
.rings{{position:absolute;left:0;top:0}}
.brand{{position:absolute;top:58px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:18px;
  font-weight:700;letter-spacing:.32em;font-size:24px}}
.photo{{position:absolute;left:0;top:0;width:100%;object-fit:cover}}
.fade{{position:absolute;left:0;width:100%}}
.kicker{{color:{GOLD};font-weight:700;letter-spacing:.2em;font-size:30px;text-transform:uppercase;margin-bottom:26px}}
.title{{font-weight:800;line-height:.98;letter-spacing:-.01em;text-transform:uppercase}}
.sub{{color:{SOFT};font-weight:400;font-size:34px;line-height:1.3;margin-top:28px}}
.block{{position:absolute;left:80px;right:80px;text-align:center}}
.pill{{display:inline-block;background:{GOLD};color:{BG};font-weight:800;letter-spacing:.06em;border-radius:60px}}
.mid{{position:absolute;left:84px;right:84px;top:150px;bottom:100px;display:flex;flex-direction:column;justify-content:center}}
.num{{position:absolute;top:58px;right:70px;color:rgba(255,255,255,.45);font-weight:500;font-size:26px}}
"""


def brand(sz=46):
    return f"<div class='brand'>{logo_svg(sz, sw=5)}<span>HEALTHSPAN CLUB</span></div>"


def end_card_html(w, h, title, sub, pill):
    cy = h // 2 - 60
    return f"""<div class='page' style='width:{w}px;height:{h}px'>{rings_svg(w, h, w//2 - 40, cy + 220)}
<div class='block' style='top:{cy-310}px'>{logo_svg(170)}
<div class='title' style='font-size:112px;margin-top:40px'>{gold(title)}</div>
<div class='sub' style='color:#fff;font-size:40px'>{sub}</div>
<div class='pill' style='margin-top:46px;font-size:34px;padding:22px 46px'>{pill}</div></div></div>"""


def reel_beat_html(image, b):
    return f"""<div class='page' style='width:1080px;height:1920px'>
<img class='photo' src='{img_uri(image)}' style='height:1180px'>
<div class='fade' style='top:640px;height:560px;background:linear-gradient(to bottom,rgba(20,24,20,0),{BG} 92%)'></div>
{brand()}
<div class='block' style='top:1100px'>
{f"<div class='kicker'>{b['kicker']}</div>" if b.get('kicker') else ''}
<div class='title' style='font-size:{b.get('size', 100)}px'>{gold(b['title'])}</div>
{f"<div class='sub'>{b['sub']}</div>" if b.get('sub') else ''}
</div></div>"""


def carousel_slide_html(s, image, i, n):
    w, h = 1080, 1350
    k = s["kind"]
    num = f"<div class='num'>{i}/{n}</div>"
    if k == "cover":
        photo = f"<img class='photo' src='{img_uri(image)}' style='height:880px'><div class='fade' style='top:420px;height:480px;background:linear-gradient(to bottom,rgba(20,24,20,0),{BG} 92%)'></div>" if image else rings_svg(w, h, 760, 420)
        top = 800 if image else 420
        return f"""<div class='page' style='width:{w}px;height:{h}px'>{photo}{brand()}
<div class='block' style='top:{top}px'>{f"<div class='kicker'>{s['kicker']}</div>" if s.get('kicker') else ''}
<div class='title' style='font-size:{s.get('size', 96)}px'>{gold(s['title'])}</div>
{f"<div class='sub'>{s['sub']}</div>" if s.get('sub') else ''}
<div class='sub' style='font-size:26px;margin-top:40px;color:rgba(255,255,255,.5)'>DESLIZA →</div></div></div>"""
    if k == "news":
        return f"""<div class='page' style='width:{w}px;height:{h}px'>{rings_svg(w, h, 780, 380, 0.08)}{brand()}
<div class='mid'>
<div><div class='pill' style='font-size:28px;padding:14px 30px;margin-bottom:46px'>{s['label']}</div>
<div class='title' style='font-size:{s.get('size', 92)}px'>{gold(s['title'])}</div>
{f"<div class='sub' style='font-size:36px'>{s['sub']}</div>" if s.get('sub') else ''}
<div class='sub' style='font-size:26px;margin-top:46px;color:rgba(255,255,255,.5)'>DESLIZA →</div></div></div></div>"""
    if k == "text":
        big = f"<div class='title g' style='font-size:{s.get('bigsize', 250)}px;margin-bottom:18px'>{s['big']}</div>" if s.get("big") else ""
        return f"""<div class='page' style='width:{w}px;height:{h}px'>{rings_svg(w, h, 980, 1280, 0.05)}{brand()}{num}
<div class='mid'><div>
{f"<div class='kicker'>{s['kicker']}</div>" if s.get('kicker') else ''}{big}
<div class='title' style='font-size:{s.get('size', 78)}px;line-height:1.02'>{gold(s.get('title',''))}</div>
{f"<div class='sub' style='font-size:44px;line-height:1.36'>{s['body']}</div>" if s.get('body') else ''}
{f"<div class='sub' style='font-size:26px;margin-top:44px;color:rgba(255,255,255,.45)'>{s['source']}</div>" if s.get('source') else ''}
</div></div></div>"""
    if k == "cta":
        return end_card_html(w, h, s.get("title", "SÍGUENOS PARA <g>VIVIR MÁS</g>"),
                             s.get("sub", "Ciencia de la longevidad, sin humo."),
                             s.get("pill", "SÍGUENOS · @healthspanclub.es"))
    raise ValueError(k)


def shoot(htmls, sizes, outs):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        for html, (w, h), out in zip(htmls, sizes, outs):
            pg.set_viewport_size({"width": w, "height": h})
            pg.set_content(f"<html><head><meta charset='utf-8'><style>{BASE_CSS}</style></head><body>{html}</body></html>")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(out), type="png")
        br.close()


def render_carousel(spec, out):
    out.mkdir(parents=True, exist_ok=True)
    n = len(spec["slides"])
    htmls = [carousel_slide_html(s, spec.get("image"), i + 1, n) for i, s in enumerate(spec["slides"])]
    pngs = [out / f"slide_{i+1:02d}.png" for i in range(n)]
    shoot(htmls, [(1080, 1350)] * n, pngs)
    for p in pngs:  # JPG para Instagram
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(p), "-q:v", "2", str(p.with_suffix(".jpg"))], check=True)
        p.unlink()


def render_reel(spec, out, seg=2.4, xf=0.25):
    out.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp())
    htmls = [reel_beat_html(spec["image"], b) for b in spec["beats"]]
    htmls.append(end_card_html(1080, 1920, "SÍGUENOS PARA <g>VIVIR MÁS</g>", "Ciencia de la longevidad, sin humo.", "SÍGUENOS · @healthspanclub.es"))
    pngs = [tmp / f"b{i}.png" for i in range(len(htmls))]
    shoot(htmls, [(1080, 1920)] * len(htmls), pngs)
    n = len(pngs)
    inputs = []
    for p in pngs:
        inputs += ["-loop", "1", "-t", f"{seg + xf:.2f}", "-i", str(p)]
    # Zoom muy lento en cada plano y fundido corto entre planos.
    f = []
    for i in range(n):
        f.append(f"[{i}:v]scale=1188:-1,zoompan=z='min(zoom+0.0006,1.06)':d={int((seg+xf)*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,setsar=1,format=yuv420p[v{i}]")
    last = "v0"
    for i in range(1, n):
        off = i * seg
        f.append(f"[{last}][v{i}]xfade=transition=fade:duration={xf}:offset={off - xf * 0 :.2f}[x{i}]")
        last = f"x{i}"
    total = n * seg
    cmd = ["ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", ";".join(f), "-map", f"[{last}]",
           "-t", f"{total:.2f}", "-r", "30", "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", str(out / "reel.mp4")]
    subprocess.run(cmd, check=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(pngs[0]), "-q:v", "2", str(out / "portada.jpg")], check=True)


if __name__ == "__main__":
    spec = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2])
    base = Path(sys.argv[1]).resolve().parent
    if spec.get("image"):
        spec["image"] = str((base / spec["image"]).resolve())
    (render_reel if spec["type"] == "reel" else render_carousel)(spec, out)
    print("ok", out)
