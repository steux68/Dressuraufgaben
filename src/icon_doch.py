# Erzeugt DOCH!-Symbole (rotes "!" mit weissem D) per Playwright. Aufruf: python3 src/icon_doch.py
from playwright.sync_api import sync_playwright
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100"><rect width="100" height="100" fill="#fff"/>
<path d="M36 12h28a5 5 0 0 1 5 5.5l-4 42a5 5 0 0 1-5 4.5H40a5 5 0 0 1-5-4.5l-4-42A5 5 0 0 1 36 12z" fill="#e30613"/>
<circle cx="50" cy="82" r="11" fill="#e30613"/>
<text x="50" y="52" font-family="DejaVu Serif,Georgia,serif" font-weight="bold" font-size="40" fill="#fff" text-anchor="middle">D</text></svg>'''
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,sz in (("icon-192",192),("icon-512",512),("apple-touch-icon",180)):
        pg=b.new_page(viewport={'width':sz,'height':sz})
        pg.set_content(f'<body style="margin:0">{svg.replace("width=\"100\" height=\"100\"",f"width=\"{sz}\" height=\"{sz}\"")}</body>')
        pg.screenshot(path=f"deutsch/{n}.png")
    b.close()
