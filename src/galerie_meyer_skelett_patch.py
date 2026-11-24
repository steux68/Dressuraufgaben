# Galerie: Meyer, Pferd mit Menschenskelett, koloriert (Commons "Meyer1 Skelet.jpg", gemeinfrei), ans Ende der Liste GAL (wird umgedreht). Bild = Ausschnitt aus Screenshot der Commons-Seite. 24.11.2026
import re,sys
from PIL import Image
s=open('index.html',encoding='utf-8').read()
if 'meyer_skelett_kol.jpg' in s: sys.exit('schon angewendet')
im=Image.open('img/quellen/meyer1_skelet_ausschnitt.png').convert('RGB'); w,h=im.size
im.save('img/galerie/meyer_skelett_kol.jpg',quality=90)
x0=(w-h)//2; im.crop((x0,0,x0+h,h)).resize((360,360),Image.LANCZOS).save('img/galerie/meyer_skelett_kol_k.jpg',quality=82)
ENTRY="""{f:'img/galerie/meyer_skelett_kol.jpg',k:'img/galerie/meyer_skelett_kol_k.jpg',n:'Pferd mit Reiter als Skelett, groß und koloriert',a:'Johann Daniel Meyer (1713–1752), Maler und Kupferstecher in Nürnberg',w:'Angenehmer und nützlicher Zeit-Vertreib',j:'Nürnberg 1748',l:'Gemeinfrei · Wikimedia Commons, „Meyer1 Skelet.jpg“ · Bild aus der Commons-Seite ausgeschnitten, deshalb kleiner',x:'Dieselbe Zeichnung gibt es auch als ganze Buchseite mit Titelzeile. Hier sieht man die Knochen von Pferd und Reiter groß und in den Farben der Kolorierung.',u:'https://commons.wikimedia.org/wiki/File:Meyer1_Skelet.jpg',c:['Anatomie','Kunst','Kurioses'],s:[3,3]}"""
END='\n];\nGAL.reverse();'
assert s.count(END)==1
i=s.index(END); head=s[:i].rstrip()
s=head+('' if head.endswith(',') else ',')+'\n '+ENTRY+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24e"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
