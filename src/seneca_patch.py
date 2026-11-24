# Seneca: Gemaelde (Wawel-Schloss, Foto Scotch Mist, CC BY-SA 4.0) als Portrait bei den Zitaten + Eintrag in der Galerie (ans Ende von GAL). 24.11.2026
import re,sys
from PIL import Image
s=open('index.html',encoding='utf-8').read()
if 'seneca_gemaelde' in s: sys.exit('schon angewendet')
im=Image.open('img/quellen/seneca_wawel_original.jpg').convert('RGB')
im.crop((640,250,1600,1210)).resize((640,640),Image.LANCZOS).save('img/zitate/seneca_gemaelde.jpg',quality=84)
g=im.copy(); g.thumbnail((1800,1800),Image.LANCZOS); g.save('img/galerie/seneca_gemaelde.jpg',quality=86)
x0=(im.width-im.height)//2+100; im.crop((x0,0,x0+im.height,im.height)).resize((480,480),Image.LANCZOS).save('img/galerie/seneca_gemaelde_k.jpg',quality=80)
A="'Seneca':['de:Lucius_Annaeus_Seneca'"
assert s.count(A)==1
s=s.replace(A,"'Seneca':['img/zitate/seneca_gemaelde.jpg','de:Lucius_Annaeus_Seneca'")
ENTRY="""{f:'img/galerie/seneca_gemaelde.jpg',k:'img/galerie/seneca_gemaelde_k.jpg',n:'Seneca, Porträtgemälde',a:'Unbekannter Maler',w:'Wawel-Schloss, Krakau',j:'17. Jh. (?)',l:'CC BY-SA 4.0 · Foto: Scotch Mist · Wikimedia Commons · Bild unverändert verkleinert; Ausschnitt bei den Zitaten',x:'Seneca (um 4 v. Chr. bis 65 n. Chr.) schrieb: Ein goldener Zaum macht das Pferd nicht besser. Der alte Mann mit dem Buch gilt hier als Seneca; die Zuschreibung des Gemäldes ist nicht gesichert.',u:'https://commons.wikimedia.org/wiki/File:Krakow_2024_389_Wawel_Castle_Museum_-_Seneca_Portrait_Painting.jpg',c:['Geschichte','Kunst'],s:[3,3]}"""
END='\n];\nGAL.reverse();'
assert s.count(END)==1
i=s.index(END); head=s[:i].rstrip()
s=head+('' if head.endswith(',') else ',')+'\n '+ENTRY+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24g"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
