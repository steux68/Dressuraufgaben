"""Titelseite: Buchstaben als pulsierende "Pins" wie in dasein-design / Deutsch-App (Kreis wird in Limette hell, zwei feine Ringe laufen aus),
in verstreuter Reihenfolge. Ersetzt den wandernden Kreis (lhi-js)."""
import re,sys
f='index.html'; s=open(f,encoding='utf8').read()
if 'class="an pin"' in s: sys.exit('schon angewendet')
# Reihenfolge verstreut: H F C K B M A E, dann X
ORDER=['H','F','C','K','B','M','A','E']
POS={'A':(100,287),'K':(21,238),'E':(21,154),'H':(21,70),'C':(100,13),'M':(179,70),'B':(179,154),'F':(179,238)}
PAIRS=[('#ffd400','#2f8cff'),('#2fbf4a','#ffd400'),('#2f8cff','#cdff3e'),('#e30613','#2fbf4a'),('#cdff3e','#e30613'),('#3a3c37','#ffd400')]
def grp(L):
    x,y=POS[L]; k=ORDER.index(L); c1,c2=PAIRS[k%6]
    return ('<g class="an pin" style="--k:%d;--c1:%s;--c2:%s"><circle class="pb" cx="%d" cy="%d" r="10"/><circle class="r1" cx="%d" cy="%d" r="10"/><circle class="r2" cx="%d" cy="%d" r="10"/>'
            '<text x="%d" y="%d" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="700" fill="#111">%s</text></g>')%(k,c1,c2,x,y,x,y,x,y,x,y,L)
for L in POS:
    pat=re.compile(r'<text class="an" x="\d+" y="\d+" text-anchor="middle" dominant-baseline="central" font-size="17" font-weight="700" fill="#111">%s</text>'%L)
    assert len(pat.findall(s))==1,L
    s=pat.sub(grp(L),s)
# Ringe für X (Mitte), als letzter Schritt
xr='<circle class="r1 xr" cx="100" cy="150" r="11" style="--k:8;--c1:#ffd400;--c2:#2f8cff"/><circle class="r2 xr" cx="100" cy="150" r="11" style="--k:8;--c1:#ffd400;--c2:#2f8cff"/>'
a='<circle class="an" cx="100" cy="150" r="11" fill="#ffd400"'
assert s.count(a)==1; s=s.replace(a,xr+a)
# alten wandernden Kreis entfernen
s=re.sub(r'\n<script id="lhi-js">.*?</script>','',s,flags=re.S)
s=re.sub(r'\n\.lhi\{.*?@media \(prefers-reduced-motion:reduce\)\{\.lhi\.lhp\{animation:none\}\}\n','\n',s,flags=re.S)
css='''
/* Titelseite: Buchstaben als Pins (Animation nach dasein-design). Sie leuchten nur, wenn die rote Spur an ihnen vorbeiläuft (trails.js setzt .lit) */
.vier .pin .pb{fill:#bfbfbf;stroke:#000;stroke-width:.8}
.vier .pin .r1,.vier .pin .r2,.vier .xr{fill:none;stroke:var(--c1);stroke-width:1.2;opacity:0;pointer-events:none;transform-box:fill-box;transform-origin:center}
.vier .pin .r2,.vier .xr.r2{stroke:var(--c2)}
.vier .pin.lit .pb{animation:pinlit 1.8s ease-in-out}
.vier .pin.lit .r1,.vier .xr.lit.r1{animation:pinringh 1.5s ease-out}
.vier .pin.lit .r2,.vier .xr.lit.r2{animation:pinringh 1.5s ease-out .25s}
@keyframes pinlit{0%{fill:#bfbfbf}8%{fill:#cdff3e}70%{fill:#cdff3e}100%{fill:#bfbfbf}}
@keyframes pinringh{0%{transform:scale(1);opacity:.9}100%{transform:scale(2.3);opacity:0}}
@media (prefers-reduced-motion:reduce){.vier .pin.lit .pb,.vier .pin.lit .r1,.vier .pin.lit .r2,.vier .xr.lit{animation:none}}
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-10-31zd"',s,count=1)
open(f,'w',encoding='utf8').write(s)
