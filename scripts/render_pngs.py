"""HTML slides → PNG (1280×720)

새 Claude 프로젝트에서 사용:
1. handoff 패키지 압축 해제 후 디렉터리 진입
2. python scripts/render_pngs.py 실행
3. ./png/ 디렉터리에 22개 PNG 생성

요구 사항:
- pip install playwright
- playwright install chromium
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

# 스크립트 위치 기준 상대 경로
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SLIDES_DIR = ROOT / "slides"
PNG_DIR = ROOT / "png"
PNG_DIR.mkdir(parents=True, exist_ok=True)

# 22 슬라이드 순서 (display order)
SLIDES = [
    "slide-01-cover.html",
    "slide-03-the-brief.html",
    "slide-04-section01-divider.html",
    "slide-05-mega-trends.html",
    "slide-06-group-architecture.html",
    "slide-07-four-channels.html",
    "slide-08-operating-philosophy.html",
    "slide-09-section02-divider.html",
    "slide-10-position-diagnosis.html",
    "slide-11-differentiation-3axes.html",
    "slide-12-imc-blesure-journey.html",
    "slide-13-imc-family-day.html",
    "slide-14-live-curation-programs.html",
    "slide-15-folio-monthly.html",
    "slide-16-ac-atelier.html",
    "slide-17-pool-rooms-two-tiers.html",
    "slide-18-ac-palace-living.html",
    "slide-20-ac-kitchen-brand-definition.html",
    "slide-22-kloud-brand-definition.html",
    "slide-23-kloud-channel-viral.html",
    "slide-24-recap-direction.html",
    "slide-25-working-calendar.html",
]


async def render(html_file, out_png):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context(
            viewport={"width": 1280, "height": 720},
            device_scale_factor=2,
        )
        page = await ctx.new_page()
        await page.goto(f"file://{html_file}", wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(500)
        slide = page.locator(".slide").first
        await slide.screenshot(path=str(out_png), omit_background=False)
        await browser.close()


async def main():
    print(f"렌더링: {len(SLIDES)} 슬라이드 → {PNG_DIR}\n")
    for i, fname in enumerate(SLIDES, 1):
        src = SLIDES_DIR / fname
        if not src.exists():
            print(f"  ⚠ MISSING: {src}")
            continue
        out = PNG_DIR / f"slide-{i:02d}.png"
        print(f"  [{i:02d}/{len(SLIDES)}] {fname} → {out.name}")
        await render(src, out)
    print(f"\n완료. {len(SLIDES)} PNGs → {PNG_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
