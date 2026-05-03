"""PNG → 단일 HTML (22 슬라이드 base64 인라인)

새 Claude 프로젝트에서 사용:
1. python scripts/render_pngs.py 먼저 실행 (PNG 생성)
2. python scripts/build_deck_html.py 실행
3. ./output/heensun-marketing-strategy-2026-deck.html 생성

요구 사항: 표준 라이브러리만
"""
import base64
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
PNG_DIR = ROOT / "png"
OUT_DIR = ROOT / "output"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "heensun-marketing-strategy-2026-deck.html"

png_files = sorted(PNG_DIR.glob("slide-*.png"))
if not png_files:
    raise SystemExit(f"⚠ PNG 없음. 먼저 render_pngs.py 실행 필요. ({PNG_DIR})")

assert len(png_files) == 22, f"expected 22 PNGs, got {len(png_files)}"

TITLES = [
    "Cover · More Than Hotels.",
    "The Brief",
    "Section 01 · Operating Lifestyle",
    "Mega Trends",
    "Group Architecture",
    "Communication 4 Channels",
    "Operating Philosophy",
    "Section 02 · Premium Select",
    "Position Diagnosis",
    "Differentiation 3 Axes",
    "IMC · Blesure Journey",
    "IMC · Family Day",
    "Live Curation",
    "Folio Monthly",
    "AC Atelier",
    "Pool Rooms · Two Tiers",
    "AC Palace · Living",
    "AC Kitchen · Brand Definition",
    "KLOUD · Brand Definition",
    "KLOUD · Channel & Viral",
    "Recap & Direction",
    "Working Calendar · Jun→Dec",
]

slides_html = []
for i, png in enumerate(png_files, 1):
    b64 = base64.b64encode(png.read_bytes()).decode("ascii")
    title = TITLES[i - 1]
    slides_html.append(f'''
  <div class="slide-wrapper" id="slide-{i:02d}">
    <div class="slide-meta">
      <span class="slide-num">{i:02d} / 22</span>
      <span class="slide-title">{title}</span>
    </div>
    <img src="data:image/png;base64,{b64}" alt="Slide {i}: {title}" loading="lazy" />
  </div>''')

slides_blob = "\n".join(slides_html)

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>희앤썬 · Marketing Strategy 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{
    background:#1a1a1a;
    color:#FAF7F2;
    font-family:'Inter','Noto Sans KR',sans-serif;
    padding:60px 20px 80px;
    -webkit-font-smoothing:antialiased;
  }}
  .cover-block{{text-align:center;max-width:1280px;margin:0 auto 60px;padding:30px 20px}}
  .cover-block .eyebrow{{font-family:'Inter';font-size:11px;letter-spacing:.3em;color:#B8945A;text-transform:uppercase;font-weight:600;margin-bottom:18px}}
  .cover-block h1{{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:48px;color:#FAF7F2;font-weight:500;line-height:1;margin-bottom:14px;letter-spacing:-.02em}}
  .cover-block .sub{{font-family:'Noto Sans KR';font-size:13px;color:#a8a29a;letter-spacing:-.01em;line-height:1.6}}
  .cover-block .author{{margin-top:18px;font-family:'Inter';font-size:11px;letter-spacing:.25em;color:#8a8580;text-transform:uppercase;font-weight:500}}
  .toc{{max-width:880px;margin:0 auto 60px;padding:24px 32px;background:rgba(184,148,90,.08);border-top:1px solid rgba(184,148,90,.4);border-bottom:1px solid rgba(184,148,90,.4)}}
  .toc-title{{font-family:'Inter';font-size:10px;letter-spacing:.3em;color:#B8945A;text-transform:uppercase;font-weight:700;margin-bottom:14px}}
  .toc-grid{{display:grid;grid-template-columns:1fr 1fr;gap:6px 24px}}
  .toc-item{{display:flex;gap:10px;align-items:baseline;font-family:'Noto Sans KR';font-size:11.5px;color:#d8d3c8;text-decoration:none;padding:3px 0;transition:color .15s}}
  .toc-item:hover{{color:#B8945A}}
  .toc-num{{font-family:'Inter';color:#8a8580;font-size:10px;font-weight:600;letter-spacing:.1em;min-width:22px}}
  .deck-container{{display:flex;flex-direction:column;align-items:center;gap:36px}}
  .slide-wrapper{{position:relative;width:1280px;max-width:95vw;aspect-ratio:16/9;box-shadow:0 20px 60px rgba(0,0,0,.55);background:#FAF7F2}}
  .slide-wrapper img{{width:100%;height:100%;display:block;object-fit:contain}}
  .slide-meta{{position:absolute;top:-26px;left:0;right:0;display:flex;justify-content:space-between;align-items:baseline;padding:0 4px}}
  .slide-num{{font-family:'Inter';font-size:10px;letter-spacing:.28em;color:#8a8580;text-transform:uppercase;font-weight:600}}
  .slide-title{{font-family:'Inter';font-size:10px;letter-spacing:.18em;color:#a8a29a;text-transform:uppercase;font-weight:500}}
  .footer-credit{{text-align:center;margin-top:80px;padding:30px;font-family:'Inter';font-size:10px;letter-spacing:.28em;color:#5a5550;text-transform:uppercase}}
  @media (max-width:1340px){{.toc-grid{{grid-template-columns:1fr}}}}
  @media print{{
    body{{background:#fff;padding:0}}
    .cover-block,.toc,.footer-credit{{display:none}}
    .slide-wrapper{{page-break-after:always;box-shadow:none;max-width:100%;margin:0}}
    .slide-meta{{display:none}}
    .deck-container{{gap:0}}
  }}
</style>
</head>
<body>

<div class="cover-block">
  <div class="eyebrow">Marketing Strategy 2026</div>
  <h1>More Than Hotels.</h1>
  <div class="sub">희앤썬 · 토탈 호스피탈리티 그룹<br>AC Hotel · AC Palace · AC Kitchen · KLOUD</div>
  <div class="author">Jay Moon · 문수진</div>
</div>

<div class="toc">
  <div class="toc-title">Contents · 22 Slides</div>
  <div class="toc-grid">
{chr(10).join(f'    <a class="toc-item" href="#slide-{i:02d}"><span class="toc-num">{i:02d}</span><span>{TITLES[i-1]}</span></a>' for i in range(1, 23))}
  </div>
</div>

<div class="deck-container">
{slides_blob}
</div>

<div class="footer-credit">
  희앤썬 · Marketing Strategy 2026 · Jay Moon
</div>

</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(f"완료: {OUT}")
print(f"크기: {OUT.stat().st_size / 1024 / 1024:.2f} MB")
