"""Healthspan Club renderer: carousels (1080x1350), Healthspan Hoy, reels (1080x1920, 12 s).

Usage:
  python3 tools/hc_render.py content/NN.json          -> out/NN/ (slides or reel.mp4 + portada.jpg)

Spec (JSON):
  {"id": "80", "type": "carousel" | "reel",
   "photo": "img/80.png",              # optional for carousels (typographic cover if missing)
   ... see build_carousel / build_reel}
Text markup: *gold words*  **bold words**  \n = line break.
"""
import base64, json, math, os, re, subprocess, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
BG = "#141814"
GOLD = "#F2C14E"
RING = "#2A2E2A"


def b64(path):
    return base64.b64encode(Path(path).read_bytes()).decode()


def font_css():
    out = []
    for w in (300, 400, 500, 600, 700, 800, 900):
        out.append(
            f"@font-face{{font-family:Outfit;font-weight:{w};src:url(data:font/woff2;base64,"
            f"{b64(FONTS / f'outfit-latin-{w}-normal.woff2')}) format('woff2');}}"
        )
    return "\n".join(out)


def md(text):
    t = html.escape(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S)
    t = re.sub(r"\*(.+?)\*", r"<span class='g'>\1</span>", t, flags=re.S)
    return t.replace("\n", "<br>")


def rings_svg(size, radii, stroke, dot_r, color=RING, angle=135, dot_color=None):
    """Circles all internally tangent at one point (the brand mark)."""
    a = math.radians(angle)
    ux, uy = math.cos(a), math.sin(a)
    R = radii[0]
    cx0, cy0 = size / 2, size / 2
    parts = []
    for r in radii:
        d = (R - r) * 0.72
        cx, cy = cx0 + d * ux, cy0 + d * uy
        parts.append(f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r:.1f}' fill='none' stroke='{color}' stroke-width='{stroke}'/>")
    r = radii[-1]
    d = (R - r) * 0.72 + r * 0.45
    parts.append(f"<circle cx='{cx0 + d*ux:.1f}' cy='{cy0 + d*uy:.1f}' r='{dot_r}' fill='{dot_color or color}'/>")
    return f"<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}' viewBox='0 0 {size} {size}'>{''.join(parts)}</svg>"


def logo_svg(size=40, stroke=None):
    s = size
    stroke = stroke or max(1.2, s / 34)
    R = s / 2 - stroke
    radii = [R * f for f in (1, 0.8, 0.61, 0.43, 0.27)]
    return rings_svg(s, radii, stroke, dot_r=R * 0.1, color="#fff", angle=135, dot_color=GOLD)


def deco(size):
    R = size / 2 - 4
    return rings_svg(size, [R * f for f in (1, 0.8, 0.6, 0.4, 0.22)], 5, dot_r=R * 0.07)


BASE_CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:{BG};font-family:Outfit,sans-serif;color:#fff;overflow:hidden}}
.g{{color:{GOLD}}}
b{{font-weight:700;color:#fff}}
.brand{{display:flex;align-items:center;gap:14px;font-weight:600;letter-spacing:.24em;font-size:22px}}
.kicker{{color:{GOLD};font-weight:700;letter-spacing:.2em;font-size:22px;text-transform:uppercase}}
.title{{font-weight:800;text-transform:uppercase;line-height:.98;letter-spacing:-.02em}}
.rule{{width:64px;height:6px;background:{GOLD};border-radius:3px}}
.body{{font-weight:300;font-size:34px;line-height:1.42;color:#e9ebe7}}
"""


def page(inner, w, h, extra_css=""):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}{BASE_CSS}"
            f"body{{width:{w}px;height:{h}px;position:relative}}{extra_css}</style></head><body>{inner}</body></html>")


def photo_uri(path):
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64(p)}"


# ---------------------------------------------------------------- carousel
def header(page_no=None, total=None, center=False):
    num = f"<div style='color:#8b8f8a;font-weight:500;letter-spacing:.12em;font-size:21px'>{page_no:02d} / {total:02d}</div>" if page_no else ""
    just = "center" if center else "space-between"
    return (f"<div style='position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:{just};align-items:center;z-index:5'>"
            f"<div class='brand'>{logo_svg(40)}HEALTHSPAN CLUB</div>{num}</div>")


def footer(source=None):
    src = f"<div>Fuente: {html.escape(source)}</div>" if source else "<div></div>"
    return (f"<div style='position:absolute;bottom:52px;left:64px;right:64px;display:flex;justify-content:space-between;"
            f"font-size:19px;color:#8b8f8a;z-index:5'>{src}<div style='color:#fff;font-weight:600'>@healthspanclub.es</div></div>")


def deco_corner():
    return f"<div style='position:absolute;right:-180px;bottom:-200px;opacity:1'>{deco(620)}</div>"


def slide_cover_photo(s, photo):
    return page(
        f"<img src='{photo_uri(photo)}' style='position:absolute;left:0;top:250px;width:1080px;height:1100px;object-fit:cover'>"
        f"<div style='position:absolute;inset:0;background:linear-gradient(180deg,{BG} 0%,{BG} 22%,rgba(20,24,20,.55) 36%,rgba(20,24,20,0) 52%,rgba(20,24,20,0) 82%,rgba(20,24,20,.75) 100%)'></div>"
        + header(center=True)
        + f"<div style='position:absolute;top:150px;left:60px;right:60px;text-align:center;z-index:5'>"
        f"<div class='kicker'>{md(s['kicker'])}</div>"
        f"<div class='title' style='font-size:{s.get('size', 96)}px;margin-top:22px'>{md(s['title'])}</div></div>"
        + f"<div style='position:absolute;bottom:64px;left:0;right:0;display:flex;justify-content:center;z-index:5'>"
        f"<div style='background:{GOLD};color:#141814;font-weight:700;letter-spacing:.12em;font-size:24px;padding:16px 30px;border-radius:40px'>DESLIZA &rarr;</div></div>",
        1080, 1350)


def slide_cover_type(s):
    big = f"<div class='title g' style='font-size:{s.get('big_size', 300)}px;line-height:.85'>{md(s['big'])}</div>" if s.get("big") else ""
    return page(
        f"<div style='position:absolute;right:-260px;top:-140px'>{deco(900)}</div>" + header(center=True)
        + f"<div style='position:absolute;left:64px;right:64px;top:380px;z-index:5'>"
        f"<div class='kicker'>{md(s['kicker'])}</div><div style='margin-top:36px'>{big}</div>"
        f"<div class='title' style='font-size:{s.get('size', 84)}px;margin-top:36px'>{md(s['title'])}</div></div>"
        + f"<div style='position:absolute;bottom:64px;left:0;right:0;display:flex;justify-content:center;z-index:5'>"
        f"<div style='background:{GOLD};color:#141814;font-weight:700;letter-spacing:.12em;font-size:24px;padding:16px 30px;border-radius:40px'>DESLIZA &rarr;</div></div>",
        1080, 1350)


def slide_content(s, n, total):
    return page(
        deco_corner() + header(n, total)
        + f"<div style='position:absolute;left:64px;right:64px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;z-index:5'>"
        f"<div class='kicker'>{md(s['kicker'])}</div>"
        f"<div class='title' style='font-size:{s.get('size', 96)}px;margin-top:26px'>{md(s['title'])}</div>"
        f"<div class='rule' style='margin:38px 0 34px'></div>"
        f"<div class='body'>{md(s['body'])}</div></div>"
        + footer(s.get("source")),
        1080, 1350)


ICONS = {
    "save": "<path d='M7 4h10v16l-5-4-5 4z' fill='none' stroke='#F2C14E' stroke-width='1.8' stroke-linejoin='round'/>",
    "share": "<path d='M21 3 10 14M21 3l-7 18-4-7-7-4z' fill='none' stroke='#F2C14E' stroke-width='1.8' stroke-linejoin='round'/>",
    "follow": "<circle cx='9' cy='8' r='4' fill='none' stroke='#F2C14E' stroke-width='1.8'/><path d='M2 20c1-4 4-6 7-6s6 2 7 6M19 7v6M16 10h6' fill='none' stroke='#F2C14E' stroke-width='1.8'/>",
}


def slide_end(note):
    btn = lambda ic, label: (f"<div style='flex:1;border:2px solid #3a3f3a;border-radius:22px;padding:30px 0;text-align:center'>"
                             f"<svg width='40' height='40' viewBox='0 0 24 24'>{ICONS[ic]}</svg>"
                             f"<div style='font-weight:600;font-size:26px;margin-top:10px'>{label}</div></div>")
    return page(
        f"<div style='position:absolute;left:-60px;top:20px'>{deco(1200)}</div>"
        + f"<div style='position:absolute;top:200px;left:0;right:0;text-align:center;z-index:5'>{logo_svg(120)}"
        f"<div class='title' style='font-size:120px;margin-top:50px'>VIVE MÁS.<br><span class='g'>VIVE MEJOR.</span></div>"
        f"<div style='font-size:34px;font-weight:300;margin-top:34px'>Ciencia de la longevidad, sin humo.</div></div>"
        + f"<div style='position:absolute;left:64px;right:64px;bottom:200px;display:flex;gap:24px;z-index:5'>"
        f"{btn('save', 'Guárdalo')}{btn('share', 'Compártelo')}{btn('follow', 'Síguenos')}</div>"
        + f"<div style='position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:5'>"
        f"<div style='font-weight:700;font-size:26px'>@healthspanclub.es</div>"
        f"<div style='color:{GOLD};font-size:24px;margin-top:12px'>{html.escape(note)}</div></div>",
        1080, 1350)


def build_carousel(spec, out):
    slides = spec["slides"]
    total = len(slides) + 2
    pages = [slide_cover_photo(spec["cover"], spec["photo"]) if spec.get("photo") else slide_cover_type(spec["cover"])]
    for i, s in enumerate(slides):
        pages.append(slide_content(s, i + 2, total))
    pages.append(slide_end(spec.get("end_note", "Medimos todo esto en The Longevity Weekend · enlace en la bio")))
    return shoot(pages, out, 1080, 1350, prefix="slide")


# ---------------------------------------------------------------- reel
def reel_frame(photo, inner, zoom=1.0):
    return page(
        f"<img src='{photo_uri(photo)}' style='position:absolute;left:0;top:0;width:1080px;height:1240px;object-fit:cover;transform:scale({zoom});transform-origin:50% 40%'>"
        f"<div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,24,20,.55) 0%,rgba(20,24,20,0) 14%,rgba(20,24,20,0) 42%,rgba(20,24,20,.85) 58%,{BG} 66%)'></div>"
        + f"<div style='position:absolute;top:150px;left:0;right:0;display:flex;justify-content:center;z-index:5'><div class='brand' style='font-size:24px'>{logo_svg(44)}HEALTHSPAN CLUB</div></div>"
        + f"<div style='position:absolute;left:90px;right:90px;top:1050px;text-align:center;z-index:5'>{inner}</div>",
        1080, 1920)


def reel_pages(spec):
    p = spec["photo"]
    f = spec["frames"]
    stamp = f[1]
    pages = [
        reel_frame(p, f"<div class='kicker' style='font-size:30px'>{md(f[0].get('kicker', '¿Mito o ciencia?'))}</div>"
                      f"<div class='title' style='font-size:{f[0].get('size', 104)}px;margin-top:30px'>{md(f[0]['title'])}</div>"),
        reel_frame(p, f"<div style='display:inline-block;transform:rotate(-6deg);border:10px solid {GOLD};border-radius:20px;padding:10px 46px;"
                      f"color:{GOLD};font-weight:800;font-size:{stamp.get('size', 150)}px;letter-spacing:.02em'>{md(stamp['stamp'])}</div>"
                      f"<div class='body' style='margin-top:56px;font-size:38px'>{md(stamp['body'])}</div>", 1.02),
        reel_frame(p, f"<div class='title' style='font-size:{f[2].get('size', 84)}px'>{md(f[2]['title'])}</div>"
                      f"<div class='body' style='margin-top:30px;font-size:36px'>{md(f[2]['body'])}</div>", 1.04),
        reel_frame(p, f"<div class='title' style='font-size:{f[3].get('size', 84)}px'>{md(f[3]['title'])}</div>"
                      f"<div class='body' style='margin-top:30px;font-size:36px'>{md(f[3]['body'])}</div>", 1.06),
        page(f"<div style='position:absolute;left:-560px;top:180px'>{deco(2200)}</div>"
             f"<div style='position:absolute;top:640px;left:0;right:0;text-align:center;z-index:5'>{logo_svg(160)}"
             f"<div class='title' style='font-size:116px;margin-top:40px'>SÍGUENOS PARA<br><span class='g'>VIVIR MÁS</span></div>"
             f"<div style='font-size:42px;font-weight:300;margin-top:40px'>Ciencia de la longevidad, sin humo.</div>"
             f"<div style='display:inline-block;margin-top:50px;background:{GOLD};color:#141814;border-radius:50px;padding:22px 44px;font-weight:800;font-size:34px;letter-spacing:.04em'>SÍGUENOS · @healthspanclub.es</div></div>",
             1080, 1920),
    ]
    return pages


def build_reel(spec, out):
    out.mkdir(parents=True, exist_ok=True)
    frames = shoot(reel_pages(spec), out / "frames", 1080, 1920, prefix="f", ext="png")
    (out / "portada.jpg").write_bytes(Path(shoot([reel_pages(spec)[0]], out / "frames", 1080, 1920, prefix="cover", ext="jpg")[0]).read_bytes())
    seg, fade = 2.6, 0.25
    inputs, filters = [], []
    for i, fr in enumerate(frames):
        inputs += ["-loop", "1", "-t", str(seg), "-i", str(fr)]
        z = "1+0.012*t/2.6" if i < 4 else "1"
        filters.append(f"[{i}:v]scale=1080:1920,setsar=1,fps=30,format=yuv420p[v{i}]")
    chain, last = [], "v0"
    for i in range(1, len(frames)):
        off = round(i * (seg - fade), 3)
        chain.append(f"[{last}][v{i}]xfade=transition=fade:duration={fade}:offset={off}[x{i}]")
        last = f"x{i}"
    fc = ";".join(filters + chain)
    cmd = ["ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", fc, "-map", f"[{last}]",
           "-t", "12", "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
           str(out / "reel.mp4")]
    subprocess.run(cmd, check=True)
    return [out / "reel.mp4", out / "portada.jpg"]


# ---------------------------------------------------------------- shoot
def shoot(pages, out, w, h, prefix="slide", ext="jpg"):
    from playwright.sync_api import sync_playwright
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    files = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": h})
        for i, htm in enumerate(pages, 1):
            pg.set_content(htm, wait_until="load")
            pg.evaluate("document.fonts.ready")
            f = out / f"{prefix}{i:02d}.{ext}"
            if ext == "jpg":
                pg.screenshot(path=str(f), type="jpeg", quality=92)
            else:
                pg.screenshot(path=str(f), type="png")
            files.append(f)
        b.close()
    return files


if __name__ == "__main__":
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text())
    out = ROOT / "out" / spec["id"]
    if spec["type"] == "reel":
        print(build_reel(spec, out))
    else:
        print(build_carousel(spec, out))
