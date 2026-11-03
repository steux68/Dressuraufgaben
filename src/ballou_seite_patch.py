# Anatomie: ganze Buchseite (Ballou S. 164) als eigener Bildsatz 'as' mit denselben Punkten, beide Augensaetze an den Anfang. Idempotent. 03.11.2026
import re,sys,os
from PIL import Image
QP='img/quellen/ballou_p164_auge.jpg'
pg=Image.open(QP).convert('RGB');W2=1200;H2=round(pg.height*W2/pg.width)
pg.resize((W2,H2),Image.LANCZOS).save('img/auge_ballou_seite.jpg',quality=84,optimize=True)
s=open('index.html',encoding='utf-8').read()
if "k:'as'" not in s:
    fig_f=1200/1458;sc=W2/pg.width
    a=s[s.index('const PO=['):s.index('const SETS=[')]
    def tr(m):
        x,y=int(m.group(2)),int(m.group(3))
        ox,oy=x/fig_f+31,y/fig_f+531
        return "%s%d,%d,"%(m.group(1),round(ox*sc),round(oy*sc))
    b=re.sub(r"(\['\w+','[^']*','[^']*',)(\d+),(\d+),",tr,a).replace('const PO=[','const PS2=[',1)
    s=s.replace('const SETS=[',b+'const SETS=[',1)
    new=(" {k:'as',g:'Die ganze Buchseite mit der alten Tafel und ihrer Beschriftung. Tippe auf die Punkte: Sie zeigen dir, was die Teile des Auges sind.',"
     "gE:'The whole book page with the old plate and its lettering. Tap the points to see what the parts of the eye are.',"
     "src:'Ballou, A Compend of Equine Anatomy and Physiology, S. 164 (Biodiversity Heritage Library über Wikimedia Commons; gemeinfrei)',"
     "srcE:'Ballou, A Compend of Equine Anatomy and Physiology, p. 164 (Biodiversity Heritage Library via Wikimedia Commons; public domain)',"
     "de:'Auge: Buchseite',en:'Eye: book page',img:'img/auge_ballou_seite.jpg',W:%d,H:%d,P:PS2,pos:'center 30%%',\n"
     "  alt:'Buchseite 164 mit dem Längsschnitt durch das Pferdeauge',altE:'Book page 164 with the section through the horse eye',"
     "cap:'Die Originalseite aus Ballou: oben der Text, in der Mitte die Tafel, unten die Legende mit den Buchstaben a–z.',"
     "capE:'The original page from Ballou: text above, the plate in the middle, the lettered legend below.'},\n")%(W2,H2)
    s=s.replace('const SETS=[\n','const SETS=[\n'+new,1)
    # 'ab' direkt hinter 'as': aus dem Ende nach vorn
    m=re.search(r"\n \{k:'ab'.*?\}(?=\n\];\nconst UI=)",s,re.S);blk=m.group(0)
    s=s.replace(blk,'',1);s=s.replace("'center 30%'},\n","'center 30%'},\n"+blk.strip('\n')+",\n",1) if False else s
    i=s.index("{k:'as'");j=s.index("\n {k:",i+5)
    s=s[:j]+"\n"+blk.strip('\n')+","+s[j:]
    s=s.replace("ab:'Kopf und Auge'}","ab:'Kopf und Auge',as:'Kopf und Auge'}",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-03zzz66'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
