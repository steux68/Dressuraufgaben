#!/usr/bin/env python3
"""App-Icon "P a-x" als roter Kreis (wie Kopf-Logo). Rendert ueber die echte App-Seite (eingebettete Schrift).
Schreibt icon-512/192.png (any, weisser Grund), icon-maskable-512.png (rot, Vollflaeche), apple-touch-icon.png,
favicon.ico, img/quellen/icon_pax.svg. Aufruf im Repo-Ordner: python3 -I src/mk_icon.py"""
import os, http.server, threading, functools
from playwright.sync_api import sync_playwright
from PIL import Image

def mark(inner_tf=''):
    return ('<circle cx="24" cy="25.5" r="24" fill="#e30613"/>'
            '<g fill="#fff" font-family="inherit" font-weight="700">'
            '<text x="10.5" y="35.5" font-size="33">P</text>'
            '<text x="18" y="40.4" font-size="13.4" stroke="#fff" stroke-width=".5" letter-spacing=".5px">a–x</text></g>')
ANY = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2.2 -0.7 52.4 52.4" width="512" height="512"><rect x="-2.2" y="-0.7" width="52.4" height="52.4" fill="#fff"/>%s</svg>' % mark()
# maskable: rote Vollflaeche, Schrift in der Sicherheitszone (Mitte der Schrift ~ (24,27))
MASK = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512"><rect width="512" height="512" fill="#e30613"/>'
        '<g transform="translate(256 256) scale(7.4) translate(-24 -27)" fill="#fff" font-family="inherit" font-weight="700">'
        '<text x="10.5" y="35.5" font-size="33">P</text>'
        '<text x="18" y="40.4" font-size="13.4" stroke="#fff" stroke-width=".5" letter-spacing=".5px">a–x</text></g></svg>')
FAV = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 1.5 48 48" width="512" height="512">%s</svg>' % mark()

os.makedirs('img/quellen', exist_ok=True)
open('img/quellen/icon_pax.svg', 'w', encoding='utf8').write(ANY)
h = functools.partial(http.server.SimpleHTTPRequestHandler, directory='.')
h.log_message = lambda *a, **k: None
srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), h); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 512, 'height': 512})
    pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_timeout(800)
    for name, svg, omit in (('icon-512.png', ANY, False), ('icon-maskable-512.png', MASK, False), ('_fav.png', FAV, True)):
        pg.evaluate("""([s,t])=>{document.documentElement.style.cssText='';let d=document.getElementById('_ic');if(d)d.remove();
          d=document.createElement('div');d.id='_ic';d.style.cssText='position:fixed;left:0;top:0;width:512px;height:512px;z-index:99999;background:'+(t?'transparent':'#fff');
          d.innerHTML=s;document.body.appendChild(d);}""", [svg, omit])
        pg.wait_for_timeout(300)
        pg.screenshot(path=name, clip={'x':0,'y':0,'width':512,'height':512}, omit_background=omit)
    b.close()
srv.shutdown()
im = Image.open('icon-512.png').convert('RGB'); im.save('icon-512.png', optimize=True)
im.resize((192,192), Image.LANCZOS).save('icon-192.png', optimize=True)
im.resize((180,180), Image.LANCZOS).save('apple-touch-icon.png', optimize=True)
Image.open('icon-maskable-512.png').convert('RGB').save('icon-maskable-512.png', optimize=True)
from PIL import ImageDraw
os.remove('_fav.png')
im=Image.open('icon-512.png').convert('RGBA'); S=4
m=Image.new('L',(512*S,512*S),0); ImageDraw.Draw(m).ellipse([(256-234.5)*S]*2+[(256+234.5)*S]*2,fill=255)
im.putalpha(m.resize((512,512),Image.LANCZOS)); im.crop((20,20,492,492)).resize((64,64),Image.LANCZOS).save('favicon.ico')
print('ok')
