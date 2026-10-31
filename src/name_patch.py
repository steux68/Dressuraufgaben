#!/usr/bin/env python3
"""Name EQUUS a-x + Viereck-Titelbild (eigene Zeichnung) + Buchstabenzeile.
Aufruf: python3 src/name_patch.py <version> theorie.html theorie/index.html
Bricht ab, wenn schon angewendet."""
import sys,re
ver=sys.argv[1]
# Viereck 20x40 m, Massstab 6: Rechteck 120x240; Buchstaben A K E H C M B F am Hufschlag, X in der Mitte
L=[('A',100,286),('K',27,238),('E',27,154),('H',27,70),('C',100,20),('M',173,70),('B',173,154),('F',173,238)]
ticks=[(100,270,100,276),(100,30,100,24),(40,234,34,234),(40,150,34,150),(40,66,34,66),(160,66,166,66),(160,150,166,150),(160,234,166,234)]
svg=['<svg class="vier" viewBox="0 0 200 300" role="img" aria-label="Viereck 20 mal 40 Meter von oben, mit den Buchstaben A K E H C M B F am Hufschlag und X in der Mitte">',
 '<rect x="40" y="30" width="120" height="240" fill="#fff" stroke="#8c918a" stroke-width="1.4"/>',
 '<line x1="100" y1="30" x2="100" y2="270" stroke="#b8b8b8" stroke-width="1" stroke-dasharray="1 3"/>',
 '<line x1="40" y1="150" x2="160" y2="150" stroke="#b8b8b8" stroke-width="1" stroke-dasharray="1 3"/>']
for x1,y1,x2,y2 in ticks: svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#8c918a" stroke-width="1.4"/>')
for t,x,y in L: svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="700" fill="#111">{t}</text>')
svg.append('<circle cx="100" cy="150" r="11" fill="#ffd400" stroke="#111" stroke-width="1.2"/><text x="100" y="150" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="700" fill="#111">X</text></svg>')
SVG=''.join(svg)
CSS=('#intro .ipic{flex:0 0 auto!important;height:clamp(180px,42vh,380px)}#intro .vier{width:100%;height:100%;display:block}'
 '#intro .iabc{margin:0;text-align:center;font-size:1.05rem;font-weight:700;letter-spacing:.32em;color:#111}'
 '#intro .iabc span{background:#ffd400;padding:0 .25em;margin-left:.1em;letter-spacing:0}'
 '#intro .ilogo{letter-spacing:.01em}')
for f in sys.argv[2:]:
    s=open(f,encoding='utf8').read()
    if 'class="vier"' in s: sys.exit('schon angewendet: '+f)
    s,n=re.subn(r'<img id="introImg"[^>]*><span class="iph">.*?</span>',SVG,s,count=1,flags=re.S); assert n==1,'Titelbild nicht gefunden'
    s,n=re.subn(r'<h2 class="ilogo"><b>DRESSUR</b>aufgaben</h2><p class="isub">[^<]*</p>',
      '<h2 class="ilogo"><b>EQUUS</b> a–x</h2><p class="iabc">A K E H C M B F – <span>X</span></p><p class="isub">Dressuraufgaben R1–R6 · Lernen, Spiel, Theorie · Pferdewissen</p>',s,count=1); assert n==1,'Logo nicht gefunden'
    s=s.replace('aria-label="Weiter zu den Dressuraufgaben"','aria-label="Weiter zu den Dressuraufgaben"',1)
    s=s.replace('<title>Dressuraufgaben · Theorie</title>','<title>EQUUS a–x · Theorie</title>',1)
    s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>'+ver+'"',s,count=1)
    i=s.rfind('</style>'); s=s[:i]+CSS+s[i:]
    open(f,'w',encoding='utf8').write(s); print('ok',f)
