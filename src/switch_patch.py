#!/usr/bin/env python3
"""Kopfzeile im dasein-Stil (Monogramm "P a-x" + Schriftzug + Schalter lernen/staunen),
Galerie aus der langen Startseite herausgenommen (eigene Ansicht, ueber den Schalter).
Aufruf: python3 src/switch_patch.py <version> index.html
Bricht ab, wenn schon angewendet."""
import sys, re

ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="msw"' in s:
    sys.exit('schon angewendet')


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, f'{s.count(old)}x statt {count}x: {old[:70]}'
    s = s.replace(old, new)


# ---- 1. Galerie raus aus dem Scroll-Stapel (Dock: 5 Balken) ----
rep("['g','Geschichte und Zitate'],['b','Galerie'],['m','Materialien']", "['g','Geschichte und Zitate'],['m','Materialien']")
rep("const PB=mk('p-b','hsec');PB.appendChild($('gal'));", "")
rep("const PAGES=[PA,PW,PG,PB,PM,PX];", "const PAGES=[PA,PW,PG,PM,PX];")
rep("['home','mat','gal','xyz','intro'].forEach", "['home','mat','xyz','intro'].forEach")
rep("const IDX={mat:4,gal:3,gesch:2,xyz:5};", "const IDX={mat:3,gesch:2,xyz:4};")
rep("window.openMat=()=>toHome(4);window.openGal=()=>toHome(3);window.openGesch=()=>toHome(2);window.openXyz=()=>toHome(5);",
    "window.openMat=()=>toHome(3);window.openGesch=()=>toHome(2);window.openXyz=()=>toHome(4);")
rep("window.galRaw=()=>{_show('home');goSec(3);};window.geschRaw=()=>{_show('home');goSec(2);};window.xyzRaw=()=>{_show('home');goSec(5);};",
    "window.geschRaw=()=>{_show('home');goSec(2);};window.xyzRaw=()=>{_show('home');goSec(4);};")
rep("const m={'#material':4,'#galerie':3,'#geschichte':2,'#xyz':5,'#links':5};",
    "const m={'#material':3,'#geschichte':2,'#xyz':4,'#links':4};")
# Titelseite: Schriftzug steht jetzt in der Kopfzeile
s, n = re.subn(r'<h2 class="ilogo">.*?</h2>', '', s, count=1)
assert n == 1, 'ilogo nicht gefunden'
rep("height:clamp(180px,42vh,380px)", "height:clamp(200px,46vh,420px)")

# Galerie-Pop-up: Quellenlink nur wenn vorhanden (eigene Zeichnungen haben keinen)
rep("$('gpu').href=x.u;", "$('gpu').hidden=!x.u;if(x.u)$('gpu').href=x.u;")

# ---- 2. Kopfzeile ----
MARK = ('<svg class="bmark" viewBox="0 0 44 30" aria-hidden="true"><rect width="44" height="30" fill="#e30613"/>'
        '<text x="5" y="23.5" font-size="23" font-weight="700" fill="#fff">P</text>'
        '<text x="19.5" y="23.5" font-size="11.5" font-weight="700" fill="#fff">a–x</text></svg>')
BRAND = ('<a class="brand" id="brand" role="link" tabindex="0" aria-label="passage a–x, zur Titelseite">' + MARK +
         '<span class="bw">passage</span></a>')
MODE = ('<div class="mode" id="mode"><span class="ml on" id="mlL">lernen</span>'
        '<button id="msw" role="switch" aria-checked="false" aria-label="Zwischen Lernen und Staunen (Galerie) wechseln"><i></i></button>'
        '<span class="ml" id="mlR">staunen</span></div>')
rep('<h1 id="title">Dressuraufgaben</h1>\n<button class="help" id="infoBtn" aria-expanded="false">',
    '<h1 id="title">Dressuraufgaben</h1>\n' + BRAND + MODE + '\n<button class="help" id="infoBtn" aria-expanded="false" aria-label="Info">')

CSS = '''
/* ---- Kopfzeile wie dasein-design: Marke + Schriftzug links, Schalter rechts ---- */
.titlebar #brand,.titlebar #mode{display:none}
body.bv .titlebar #brand,body.bv .titlebar #mode{display:flex}
body.bv #title,body.bv #backBtn{display:none!important}
#brand{align-items:center;gap:8px;min-width:0;color:#e30613;cursor:pointer;text-decoration:none;-webkit-tap-highlight-color:transparent}
#brand .bmark{width:44px;height:30px;flex:none;display:block}
#brand .bw{font-size:clamp(1.3rem,6vw,1.6rem);font-weight:400;letter-spacing:-.01em;line-height:1;white-space:nowrap}
#mode{align-items:center;gap:7px;flex:none;font-size:.92rem;margin-left:auto}
#mode .ml{color:#9a9a9a;font-weight:400;white-space:nowrap}
#mode .ml.on{color:#000;font-weight:700}
#msw{width:36px;height:20px;border:1.5px solid #111;border-radius:999px;background:#fff;position:relative;padding:0;flex:none;cursor:pointer;-webkit-tap-highlight-color:transparent}
#msw i{position:absolute;top:2px;left:2px;width:13px;height:13px;border-radius:50%;background:#cdff3e;border:1.5px solid #111;box-sizing:border-box;transition:left .2s}
#msw[aria-checked="true"] i{left:19px}
#msw:focus-visible{outline:2px solid #e30613;outline-offset:2px}
body.bv #infoBtn{font-size:0;padding:2px;gap:0}
body.bv #infoBtn .i{font-size:.85rem}
@media (prefers-reduced-motion:reduce){#msw i{transition:none}}
'''

JS = '''
<script>
/* Schalter lernen / staunen: Galerie ist eine eigene Ansicht, nicht mehr Teil der langen Seite */
(function(){
 const $=id=>document.getElementById(id);
 function bv(){const v=view;document.body.classList.toggle('bv',v==='home'||v==='gal'||v==='intro');
  const on=v==='gal';$('msw').setAttribute('aria-checked',on?'true':'false');$('mlL').classList.toggle('on',!on);$('mlR').classList.toggle('on',on);}
 const _s=window.show;window.show=function(v){_s(v);bv();};
 const _i=window.info;window.info=function(o){_i(o);bv();};
 $('msw').onclick=()=>{if(view==='gal')$('backBtn').click();else window.openGal();};
 $('mlL').onclick=()=>{if(view==='gal')$('backBtn').click();};
 $('mlR').onclick=()=>{if(view!=='gal')window.openGal();};
 const brand=()=>{if($('title').onclick)$('title').onclick();};
 $('brand').onclick=brand;$('brand').onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();brand();}};
 /* Nach dem ersten Layout (Kopfzeile aendert die Hoehe) erneut an den Abschnitt andocken, wenn per Adresse angesprungen wurde */
 const ANCH={'#material':3,'#geschichte':2,'#xyz':4,'#links':4},ST=(window.START_H||'');
 if(ST in ANCH){const snap=()=>{if(view!=='home')return;const S=$('hscroll'),P=S&&S.querySelectorAll('section.hsec')[ANCH[ST]];if(P)S.scrollTop=P.offsetTop-parseFloat(P.style.scrollMarginTop||0);};
  setTimeout(snap,120);setTimeout(snap,500);}
 bv();
})();
</script>
'''
i = s.rfind('</style>')
assert i > 0
s = s[:i] + CSS + s[i:]
rep('</body></html>', JS + '</body></html>')
s = re.sub(r'(<meta name="app-version" content=")[^"]*"', r'\g<1>' + ver + '"', s, count=1)
open(path, 'w', encoding='utf8').write(s)
print('ok', path)
