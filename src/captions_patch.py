# Bildunterschriften als weisses Band auf dem Foto (ohne extra Linie/Rahmen), einheitliche Schriftgroessen,
# Vollbild: "‹ Zurueck" (zurueck zum Kasten) + "✕" (Popup schliessen).
# Idempotent. 06.11.2026. Aufruf: python3 -I src/captions_patch.py [--noversion]
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* captions-band */' in s:
    print('schon angewendet'); sys.exit(0)
def rep(old, new):
    global s
    assert s.count(old) == 1, f'{s.count(old)}x: {old[:70]}'
    s = s.replace(old, new)
# 1) Anatomie-Galerie: Name + Zaehler in ein Band
rep("b.append(im,n,c);b.onclick=()=>openSet(i);", "const bd=el('span','agb');bd.append(n,c);b.append(im,bd);b.onclick=()=>openSet(i);")
# 2) Liste der Gesundheits-/Huf-Bilder
rep("b.append(im,n,k);b.onclick=()=>open(i);", "const bd=document.createElement('span');bd.className='agb';bd.append(n,k);b.append(im,bd);b.onclick=()=>open(i);")
# 3) Vollbild-Knoepfe
rep('<span class="aHint" id="aHint"></span><button id="aFull" type="button" hidden></button>',
    '<button id="aFull" type="button" hidden></button><span class="aHint" id="aHint"></span><button id="aXc" type="button" aria-label="Schließen">✕</button>')
rep("$('aFull').textContent=u.close;", "$('aFull').textContent='‹ '+u.prevT;")
rep("$('aX').onclick=closeSet;", "$('aX').onclick=closeSet;$('aXc').onclick=closeSet;")
CSS = '''
/* captions-band */
.agc{position:relative;gap:0;align-self:start}
.agc .agi{border:0!important;outline:0!important}
.agc .agb{position:absolute;left:0;right:0;bottom:0;display:flex;flex-direction:row;flex-wrap:wrap;align-items:baseline;gap:0 6px;padding:5px 7px;background:rgba(255,255,255,.96);text-align:left}
.agc .agn{margin:0;font-size:13.5px;font-weight:700;line-height:1.2;color:#111}
.agc .agk{font-size:12px;line-height:1.2;color:#777}
.tline.intro{font-size:12.5px}
.tline.intro .inter{font-size:12px}
.anapop #aXc{display:none}
.anapop.full #aXc{display:block;pointer-events:auto;flex:none;margin:0;padding:2px 10px;font-size:14px;line-height:18px;color:#fff;background:transparent;border:0}
.anapop.full .aOv{justify-content:space-between;background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,0))!important;padding:8px 10px 18px}
.anapop.full .aOv #aFull{order:-1}
'''
i = s.rindex('</style>')
s = s[:i] + CSS + s[i:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06zzz85'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
