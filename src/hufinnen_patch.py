# Anatomie: neues Bild "Huf von innen" (Magner 1899, Plate XV; Flickr Commons, No known copyright restrictions). Idempotent. 02.11.2026
import re,sys,shutil,os
from PIL import Image
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/1fe7242f-image.jpg'
Q='img/quellen/magner_1899_plate15.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');k=im.width/1210   # Koordinaten unten: Bildschirmmasse der Vorschau (Breite 1210)
x0,y0,x1,y1=60,350,1150,1660
c=im.crop((round(x0*k),round(y0*k),round(x1*k),round(y1*k)))
f=1000/(x1-x0);W=1000;H=round((y1-y0)*f)
c.resize((W,H),Image.LANCZOS).save('img/huf_innen.jpg',quality=84,optimize=True)
def pt(x,y):return round((x-x0)*f),round((y-y0)*f)
P=[
 ('ss','Strahlstütze','Frog stay (central ridge)',pt(650,522),'Der kräftige Mittelgrat des Strahls. Der Strahl trägt mit und federt den Tritt ab.','The strong central ridge of the frog. The frog helps carry weight and cushions each step.'),
 ('sf','Strahlfurchen','Frog grooves (collateral grooves)',pt(572,611),'Die Furchen links und rechts vom Strahl. Hier setzen sich Schmutz und Feuchtigkeit fest. Beim Auskratzen immer mitreinigen.','The grooves either side of the frog. Dirt and moisture settle here. Always clean them when picking out.'),
 ('es','Eckstreben','Bars',pt(865,753),'Zwei Hornleisten, die von den Trachten nach vorn neben dem Strahl laufen. Sie stützen die Trachten, wenn das Pferd den Huf belastet.','Two ridges of horn that run forward from the heels beside the frog. They support the heels under load.'),
 ('tw','Trachtenwinkel','Angle of the heel (inflection)',pt(935,706),'Hier knickt die Hufwand nach innen und geht in die Eckstrebe über.','Here the hoof wall turns inwards and becomes the bar.'),
 ('wl','Weiße Linie','White line (sole edge)',pt(470,1360),'Der helle Streifen, an dem Wand und Sohle zusammenwachsen. Der Hufschmied setzt die Nägel in dieser Nähe, darum darf nur er sie einschlagen.','The pale band where wall and sole join. The farrier places the nails close to it, so only the farrier should drive them.'),
 ('sw','Übergang Sohle – Wand','Sole–wall junction',pt(390,1256),'Die Rinne rundum, wo Sohle und Hufwand zusammentreffen. Steinchen können sich hier einklemmen.','The groove all round where sole meets wall. Small stones can wedge in here.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PI=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PI=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'hi',g:'So sieht der Huf von oben aus, wenn man die Wand an der Sohle abschneidet: die Hornsohle mit Strahl und Eckstreben. Wer das kennt, versteht, warum der Strahl sauber und die Trachten gesund bleiben müssen.',"
     "gE:'This is the hoof from above with the wall cut off at the sole: the horn sole with frog and bars. Knowing it explains why the frog must stay clean and the heels healthy.',"
     "src:'Magner, ABC Guide to Sensible Horseshoeing, New York: Werner, 1899, Plate XV (Internet Archive / Tufts University über Flickr Commons; No known copyright restrictions)',"
     "srcE:'Magner, ABC Guide to Sensible Horseshoeing, New York: Werner, 1899, Plate XV (Internet Archive / Tufts University via Flickr Commons; no known copyright restrictions)',"
     "de:'Huf von innen',en:'Hoof from above',img:'img/huf_innen.jpg',W:%d,H:%d,P:PI,pos:'center 40%%',\n"
     "  alt:'Hornsohle und Strahl von oben, Wand abgeschnitten',altE:'Horn sole and frog seen from above, wall cut off',"
     "cap:'Der Hornschuh von oben. Stich aus Magner (1899), Plate XV; Begriffe nach der Bildlegende, übersetzt. Die Farbe stammt vom Scan.',"
     "capE:'The hoof capsule seen from above. Engraving from Magner (1899), Plate XV; terms after the plate legend, translated. The colour comes from the scan.'},\n ")%(W,H)
    s=s.replace(" {k:'au',"," "+new+"{k:'au',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz46'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
