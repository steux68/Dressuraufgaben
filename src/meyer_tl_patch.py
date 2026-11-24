# 1) Geschichte: 1748 Meyers Pferdeskelett bekommt das kolorierte Bild aus der Galerie (lokal, statt Platzhalter "JM").
# 2) Hilfen: Name aus der Quellenzeile entfernt (Vorlage vermutlich ein Plakat aus dem Netz). 24.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'startsWith(\'img/\')' in s: sys.exit('schon angewendet')
OLD="if(cache[key]){show(cache[key]);return;}"
NEW="if(list[0].startsWith('img/')){show(list[0]);return;}"+OLD
assert s.count(OLD)==3
s=s.replace(OLD,NEW)
A='ini:"JM",w:["de:Johann_Daniel_Meyer"]'
assert s.count(A)==1
s=s.replace(A,'ini:"JM",w:["img/galerie/meyer_skelett_kol.jpg","de:Johann_Daniel_Meyer"]')
B="Piktogramme neu gezeichnet, nach der Hilfentafel von S. Steinbach (2000). Entwurf, mit Reitlehrer abgleichen."
assert s.count(B)==1
s=s.replace(B,"Piktogramme neu gezeichnet, nach einer Hilfentafel. Entwurf, mit Reitlehrer abgleichen.")
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24f"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
h=open('src/hilfen_patch.py',encoding='utf-8').read()
h=h.replace("nach der Hilfentafel von S. Steinbach (2000)","nach einer Hilfentafel").replace("nach der Hilfentafel von S. Steinbach 2000, neu gezeichnet","nach einer Hilfentafel, neu gezeichnet")
open('src/hilfen_patch.py','w',encoding='utf-8').write(h)
