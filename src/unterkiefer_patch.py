# Anatomie: neues Bild "Unterkiefer" (Axe 1906, Abb. 290) mit 6 Punkten. Idempotent. 02.11.2026
import re,sys,shutil
from PIL import Image,ImageEnhance
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/b65a8024-image.jpg'
import os
if not os.path.exists('img/quellen/axe_unterkiefer_1906.jpg'): shutil.copy(SRC,'img/quellen/axe_unterkiefer_1906.jpg')
im=Image.open('img/quellen/axe_unterkiefer_1906.jpg').convert('RGB')
# dunkles Foto dezent aufhellen (Gamma), damit es auf dem Tablet lesbar ist
im=im.point(lambda v:int(255*((v/255)**0.8)))
im=ImageEnhance.Contrast(im).enhance(1.05)
K=1400/im.width;W,H=1400,round(im.height*K)
im.resize((W,H),Image.LANCZOS).save('img/unterkiefer.jpg',quality=84,optimize=True)
def pt(x,y):return round(x*K),round(y*K)
P=[
 ('kf','Kronenfortsatz','Coronoid process',pt(1122,172),'Der vordere Fortsatz am Kieferast. Hier setzt ein Kaumuskel (Schläfenmuskel) an.','The front process of the jaw branch. A chewing muscle (temporalis) attaches here.'),
 ('gf','Gelenkfortsatz','Condyle',pt(1190,288),'Das runde Ende, das mit dem Schädel das Kiefergelenk bildet. Beim Kauen gleitet es hin und her.','The rounded end that forms the jaw joint with the skull. It glides back and forth when chewing.'),
 ('bz','Backenzähne','Molar teeth',pt(655,528),'Sechs Backenzähne pro Seite mahlen das Futter. Das Gebiss braucht regelmäßig Kontrolle durch den Zahnarzt.','Six molars on each side grind the feed. The teeth need regular checks by the equine dentist.'),
 ('kl','Kinnloch','Mental foramen',pt(392,690),'Eine kleine Öffnung, durch die ein Nerv austritt. Darüber liegt beim Pferd die Lade, auf der das Gebiss ruht.','A small opening where a nerve leaves the bone. Above it lies the bar on which the bit rests.'),
 ('sz','Schneidezähne','Incisor teeth',pt(168,648),'Sechs Schneidezähne vorn. An ihnen erkennt man das Alter des Pferdes.','Six incisors at the front. They show the horse\'s age.'),
 ('km','Ansatz des Kaumuskels','Attachment of the masseter',pt(1045,592),'Die breite Fläche am Kieferast, an der der kräftige Kaumuskel (Masseter) ansetzt.','The broad surface of the jaw branch where the strong chewing muscle (masseter) attaches.')
]
def js(p):
    q=lambda t:"'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
    return "['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5]))
arr="const PU=[\n"+",\n".join(js(p) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PU=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'uk',g:'Der Unterkiefer trägt die unteren Zähne und ist über das Kiefergelenk beweglich. Auf der zahnlosen Lade zwischen Schneide- und Backenzähnen liegt beim Reiten das Gebiss.',"
     "gE:'The lower jaw carries the lower teeth and moves at the jaw joint. The bit rests on the toothless bar between incisors and molars.',"
     "src:'Axe, The Horse, London: Gresham, 1906, Abb. 290 (Internet Archive / NCSU Libraries über Flickr Commons; No known copyright restrictions)',"
     "srcE:'Axe, The Horse, London: Gresham, 1906, Fig. 290 (Internet Archive / NCSU Libraries via Flickr Commons; no known copyright restrictions)',"
     "de:'Unterkiefer',en:'Lower jaw',img:'img/unterkiefer.jpg',W:%d,H:%d,P:PU,pos:'center 50%%',\n"
     "  alt:'Unterkiefer des Pferdes von innen',altE:'Horse lower jaw, inner side',"
     "cap:'Unterkiefer von innen. Foto aus Axe, The Horse (1906), Abb. 290; Begriffe nach der Bildlegende, übersetzt.',"
     "capE:'Lower jaw, inner side. Photo from Axe, The Horse (1906), Fig. 290; terms after the figure legend, translated.'},\n ")%(W,H)
    s=s.replace(" {k:'au',"," "+new+"{k:'au',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz44'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
