# Zitate-Portraits: Shakespeare (Cobbe-Portrait, gemeinfrei) und Bodenstedt (Stich nach C. Kolb 1876, gemeinfrei); je ein Galerie-Eintrag. 24.11.2026
import re,sys
from PIL import Image
s=open('index.html',encoding='utf-8').read()
if 'shakespeare_cobbe_q' in s: sys.exit('schon angewendet')
sh=Image.open('img/quellen/shakespeare_cobbe_original.jpg').convert('RGB')
sh.crop((300,380,1500,1580)).resize((640,640),Image.LANCZOS).save('img/zitate/shakespeare_cobbe_q.jpg',quality=84)
g=sh.copy(); g.thumbnail((1400,1400)); g.save('img/galerie/shakespeare_cobbe.jpg',quality=86)
sh.crop((0,300,1596,1896)).resize((480,480),Image.LANCZOS).save('img/galerie/shakespeare_cobbe_k.jpg',quality=80)
bo=Image.open('img/quellen/bodenstedt_kolb_original.jpg').convert('RGB')
bo.crop((0,0,360,360)).resize((640,640),Image.LANCZOS).save('img/zitate/bodenstedt_kolb_q.jpg',quality=86)
bo.save('img/galerie/bodenstedt_kolb.jpg',quality=90)
bo.crop((0,20,360,380)).resize((360,360),Image.LANCZOS).save('img/galerie/bodenstedt_kolb_k.jpg',quality=82)
A="'Seneca':'img/zitate/seneca_gemaelde.jpg'"; assert s.count(A)==1
s=s.replace(A,A+",'William Shakespeare':'img/zitate/shakespeare_cobbe_q.jpg','Friedrich von Bodenstedt':'img/zitate/bodenstedt_kolb_q.jpg'")
E1="""{f:'img/galerie/shakespeare_cobbe.jpg',k:'img/galerie/shakespeare_cobbe_k.jpg',n:'William Shakespeare, Cobbe-Porträt',a:'Unbekannter Maler',w:'Hatchlands Park (Cobbe Collection)',j:'um 1610',l:'Gemeinfrei · Wikimedia Commons, „Cobbe portrait of Shakespeare.jpg“ · Bild verkleinert; Ausschnitt bei den Zitaten',x:'Ob das Bild wirklich Shakespeare zeigt, ist nicht gesichert. Es wurde 2009 als mögliches Porträt vorgestellt.',u:'https://commons.wikimedia.org/wiki/File:Cobbe_portrait_of_Shakespeare.jpg',c:['Geschichte','Kunst'],s:[3,4]}"""
E2="""{f:'img/galerie/bodenstedt_kolb.jpg',k:'img/galerie/bodenstedt_kolb_k.jpg',n:'Friedrich von Bodenstedt',a:'Stich von 1876 nach einem Porträt von C. Kolb',w:'Dichter, Übersetzer und Orientalist',j:'1876',l:'Gemeinfrei · Wikimedia Commons, „Friedrich von Bodenstedt - C. Kolb 1876.jpg“ · kleine Auflösung (360 × 450)',x:'Bodenstedt (1819–1892) schrieb „Die Lieder des Mirza-Schaffy“ (1851), aus denen das Zitat vom Paradies der Erde auf dem Rücken der Pferde stammt.',u:'https://commons.wikimedia.org/wiki/File:Friedrich_von_Bodenstedt_-_C._Kolb_1876.jpg',c:['Geschichte','Kunst'],s:[3,4]}"""
END='\n];\nGAL.reverse();'; assert s.count(END)==1
i=s.index(END); head=s[:i].rstrip()
s=head+('' if head.endswith(',') else ',')+'\n '+E1+',\n '+E2+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24j"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
