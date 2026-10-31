#!/usr/bin/env python3
"""App-Icon "P a-x": rotes Feld, weisse Schrift (Carlito Bold). Schreibt icon-512.png, icon-192.png,
apple-touch-icon.png (180) und img/quellen/icon_pax.svg.  Aufruf aus dem Repo-Ordner: python3 -I src/mk_icon.py"""
import os
from playwright.sync_api import sync_playwright
from PIL import Image

SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" '
       'font-family="Carlito, Calibri, Arial, sans-serif">'
       '<rect width="512" height="512" fill="#e30613"/>'
       '<text x="84" y="342" font-size="272" font-weight="700" fill="#fff">P</text>'
       '<text x="238" y="342" font-size="128" font-weight="700" fill="#fff">a–x</text></svg>')

os.makedirs('img/quellen', exist_ok=True)
open('img/quellen/icon_pax.svg', 'w', encoding='utf8').write(SVG)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 512, 'height': 512})
    pg.set_content(f'<html><body style="margin:0">{SVG}</body></html>')
    pg.wait_for_timeout(300)
    pg.screenshot(path='icon-512.png', clip={'x': 0, 'y': 0, 'width': 512, 'height': 512})
    b.close()
im = Image.open('icon-512.png').convert('RGB')
im.save('icon-512.png', optimize=True)
im.resize((192, 192), Image.LANCZOS).save('icon-192.png', optimize=True)
im.resize((180, 180), Image.LANCZOS).save('apple-touch-icon.png', optimize=True)
print('ok')
