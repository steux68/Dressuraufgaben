#!/usr/bin/env python3
"""Anatomie-Galerie: Vorschaubilder statt der 4,5 MB grossen Originale + Vorladen; weisses Band zwischen den beiden Zeitleisten.
python3 src/anatomie_thumbs_patch.py <version> index.html   (idempotent; erzeugt img/ana_k/*.jpg)"""
import sys, re, os
from PIL import Image
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="ana-thumbs-css"' in s:
    print('schon angewendet'); sys.exit(0)

# 1 Vorschaubilder (kurze Seite 480 px; fuer die gezoomten Karten (tbs) 800 px)
i = s.index('const SETS=') if 'const SETS=' in s else s.index('SETS=[')
seg = s[i:]
os.makedirs('img/ana_k', exist_ok=True)
names = []
for m in re.finditer(r"img:'(img/[^']+\.jpg)'([^\n]{0,200})", seg):
    f = m.group(1); zoom = 'tbs:' in seg[m.start():m.start()+400] and "tbs:'cover'" not in seg[m.start():m.start()+400]
    if f in [n[0] for n in names]: continue
    names.append((f, zoom))
tot = 0
for f, zoom in names:
    out = 'img/ana_k/' + os.path.basename(f)
    im = Image.open(f).convert('RGB'); w, h = im.size
    t = 800 if zoom else 480
    sc = min(1, t / min(w, h))
    im = im.resize((round(w * sc), round(h * sc)), Image.LANCZOS)
    im.save(out, 'JPEG', quality=72, optimize=True, progressive=True)
    tot += os.path.getsize(out)
print(len(names), 'Vorschaubilder,', tot // 1024, 'KB')

def rep(a, b):
    global s
    assert s.count(a) == 1, (a, s.count(a))
    s = s.replace(a, b)

rep("im.style.backgroundImage='url('+s.img+')';im.style.backgroundPosition=s.pos;",
    "im.style.backgroundImage='url('+s.img.replace('img/','img/ana_k/')+')';im.style.backgroundPosition=s.pos;")

CSS = '''<style id="ana-thumbs-css">
/* weisses Band (23 px, wie eine Menueleiste) zwischen den beiden Zeitleisten */
#zasec+.wsec{margin-top:23px!important;position:relative}
#zasec+.wsec::before{content:"";position:absolute;left:0;right:0;top:-23px;height:23px;background:#fff}
/* Galerie-Kacheln: das Bild ging auf eine 1-px-Linie ein (Rahmen-Verlauf setzte background-size 100% 1px); Bild = cover, Rahmen als eigene Ebene */
.agc .agi{background-size:cover;background-repeat:no-repeat;background-origin:padding-box}
.agc .agi::after{content:"";position:absolute;inset:0;pointer-events:none;z-index:1;background:var(--box)}
</style>'''
j = s.rindex('</style>') + len('</style>')
s = s[:j] + '\n' + CSS + s[j:]

files = ','.join('"%s"' % os.path.basename(f) for f, _ in names)
JS = ('<script id="ana-preload-js">addEventListener("load",function(){setTimeout(function(){[%s].forEach(function(f){var i=new Image();i.src="img/ana_k/"+f;});},600);});</script>\n' % files)
assert s.count('</body>') == 1
s = s.replace('</body>', JS + '</body>')
m = re.search(r'(<meta name="app-version" content=")([^"]*)(")', s)
s = s[:m.start(2)] + ver + s[m.end(2):]
open(path, 'w', encoding='utf8').write(s)
print('ok', m.group(2), '->', ver)
