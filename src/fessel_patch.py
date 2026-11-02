# Anatomie: Bildsatz "Die Fessel: normal und durchgetreten" – Richardson, The New Book of the Horse, 1911, Pl. 28 (Zeichnung Terzi; BHL; gemeinfrei). Idempotent. 02.11.2026
import re,sys,shutil,os
from PIL import Image
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/da3ab3b1-image.jpg'
Q='img/quellen/richardson_1911_pl28_fetlock.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');k=im.width/1999           # Koordinaten unten: Vorschau mit Breite 1999
x0,y0,x1,y1=250,70,1840,1240
c=im.crop((round(x0*k),round(y0*k),round(x1*k),round(y1*k)))
f=1400/(x1-x0);W=1400;H=round((y1-y0)*f)
c.resize((W,H),Image.LANCZOS).save('img/fessel.jpg',quality=84,optimize=True)
def pt(x,y):return round((x-x0)*f),round((y-y0)*f)
P=[
 ('kn','Vorderfußwurzelgelenk','Knee (carpus)',pt(775,350),'Das „Knie“ des Vorderbeins. Es ist eigentlich das Handgelenk des Pferdes und besteht aus mehreren kleinen Knochen.','The “knee” of the foreleg. It is really the horse\'s wrist and is made of several small bones.'),
 ('gr','Griffelbein','Splint bone',pt(738,500),'Der schmale Knochen, der seitlich am Röhrbein anliegt. Eine Verdickung heißt „Überbein“.','The slim bone beside the cannon bone. A swelling there is called a splint.'),
 ('rb','Röhrbein','Cannon bone',pt(800,620),'Der lange, glatte Knochen zwischen Knie und Fessel. Auf ihm liegen die Beugesehnen.','The long smooth bone between knee and fetlock. The flexor tendons run behind it.'),
 ('gb','Gleichbeine','Sesamoids',pt(718,835),'Zwei kleine Knochen hinten am Fesselgelenk. Sie führen die Sehnen und fangen Druck ab.','Two small bones at the back of the fetlock. They guide the tendons and take pressure.'),
 ('fg','Fesselgelenk (normal)','Fetlock joint (normal)',pt(775,815),'Hier steht das Gelenk gerade über der Fessel. Das Bein trägt gleichmäßig und die Sehnen werden nicht überdehnt.','The joint sits straight above the pastern. The leg carries evenly and the tendons are not overstretched.'),
 ('fb','Fesselbein','Long pastern bone',pt(830,945),'Der Knochen zwischen Fesselgelenk und Kronbein. Seine Neigung entscheidet, wie weich der Tritt wird.','The bone between fetlock joint and short pastern. Its angle decides how soft the stride is.'),
 ('kb','Kronbein','Short pastern bone',pt(868,1005),'Der kurze Knochen zwischen Fesselbein und Hufbein.','The short bone between long pastern and coffin bone.'),
 ('hb','Hufbein','Coffin bone',pt(905,1085),'Der Knochen im Huf, ganz vom Horn umgeben.','The bone inside the hoof, entirely enclosed by horn.'),
 ('ue','Überköten','Over-shot fetlock',pt(1645,830),'Das Fesselgelenk ist nach vorn durchgetreten, das Bein steht „über“ der Fessel. Das belastet Gelenk und Sehnen. Hufschmied und Tierarzt fragen, wenn du so etwas siehst.','The fetlock joint is pushed forward, the leg stands “over” the pastern. This strains joint and tendons. Ask the farrier and the vet if you see this.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PF=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PF=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'fe',g:'Die Fessel von der Seite, normal (links) und durchgetreten (rechts), jeweils mit Haut und mit Knochen. So sieht man, wie sich die Stellung des Fesselgelenks auf Knochen und Sehnen auswirkt.',"
     "gE:'The fetlock from the side, normal (left) and over-shot (right), each with skin and with bones. It shows how the position of the fetlock joint affects bones and tendons.',"
     "src:'Richardson, The New Book of the Horse, 1911, Pl. 28, Zeichnung: Terzi (Biodiversity Heritage Library / Webster Family Library über Flickr; gemeinfrei)',"
     "srcE:'Richardson, The New Book of the Horse, 1911, Pl. 28, drawing: Terzi (Biodiversity Heritage Library / Webster Family Library via Flickr; public domain)',"
     "de:'Die Fessel',en:'The fetlock',img:'img/fessel.jpg',W:%d,H:%d,P:PF,pos:'center 50%%',\n"
     "  alt:'Fessel normal und durchgetreten, mit Knochen',altE:'Fetlock normal and over-shot, with bones',"
     "cap:'Die Fessel: links normal, rechts durchgetreten („over-shot“). Aus Richardson (1911), Pl. 28, Zeichnung von Terzi. Namen übersetzt.',"
     "capE:'The fetlock: normal on the left, over-shot on the right. From Richardson (1911), Pl. 28, drawing by Terzi. Names translated.'},\n ")%(W,H)
    s=s.replace(" {k:'hi',"," "+new+"{k:'hi',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz51'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
