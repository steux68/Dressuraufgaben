# Anatomie: Bildsatz "Nerven und Gefaesse im Huf" – Rich, Artistic Horse-Shoeing, 1907 (Flickr Commons). Punkte = unsere Deutung (Legende des Buches fehlt). Idempotent. 02.11.2026
import re,sys,shutil,os
from PIL import Image
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/83474f8b-image.jpg'
Q='img/quellen/rich_1907_nerven_gefaesse.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');k=im.width/1367          # Koordinaten unten: Vorschau mit Breite 1367
x0,y0,x1,y1=40,140,1367,1900
c=im.crop((round(x0*k),round(y0*k),round(x1*k),round(y1*k)))
f=1000/(x1-x0);W=1000;H=round((y1-y0)*f)
c.resize((W,H),Image.LANCZOS).save('img/huf_gefaesse.jpg',quality=84,optimize=True)
def pt(x,y):return round((x-x0)*f),round((y-y0)*f)
P=[
 ('nv','Nervenstrang','Nerve',pt(262,640),'Der helle, kräftige Strang an der Rückseite der Fessel ist ein Nerv. Er leitet das Gefühl aus dem Huf. Der Tierarzt kann ihn betäuben, um herauszufinden, ob die Lahmheit vom Huf kommt.','The pale, strong cord on the back of the pastern is a nerve. It carries feeling from the hoof. The vet can numb it to find out whether lameness comes from the hoof.'),
 ('vn','Vene','Vein',pt(400,930),'Das dunkelblaue Gefäß neben dem Nerv. Venen führen das Blut aus dem Huf zurück.','The dark blue vessel beside the nerve. Veins carry blood back from the hoof.'),
 ('ae','Feine Äste','Fine branches',pt(800,1450),'Viele feine Äste von Gefäßen und Nerven laufen in den Huf. Darum ist der Huf gut durchblutet: Wärme und ein starker Puls an der Fessel sind ein Warnzeichen.','Many fine branches of vessels and nerves run into the hoof. That is why the hoof has a good blood supply: heat and a strong pulse at the fetlock are a warning sign.'),
 ('kr','Kronrand','Coronary band',pt(1010,1388),'Hier treffen Haut und Horn zusammen. Die Gefäße enden dicht darunter und versorgen das nachwachsende Horn.','Here skin meets horn. The vessels end just below and feed the growing horn.'),
 ('ba','Ballen','Heel bulb',pt(190,1030),'Das weiche Polster hinten am Huf unter der Fessel. Gefäße und Nerven liegen hier gut geschützt.','The soft pad at the back of the hoof below the pastern. Vessels and nerves are well protected here.'),
 ('le','Empfindliche Schicht','Sensitive tissue',pt(850,1640),'Die gut durchblutete, empfindliche Schicht unter dem Horn. Sie lässt das Horn wachsen. Wird sie zu stark belastet, entzündet sie sich, zum Beispiel bei Hufrehe.','The well-supplied, sensitive layer beneath the horn. It makes the horn grow. If overloaded, it becomes inflamed, for example in laminitis.'),
 ('hw','Hornwand im Schnitt','Hoof wall, cut',pt(1230,1700),'Die Wand an der Zehe, längs aufgeschnitten. Das Horn ist selbst unempfindlich, deshalb spürt das Pferd die Nägel nur, wenn sie zu tief sitzen.','The toe wall, cut lengthways. Horn itself has no feeling, so the horse feels the nails only if they go too deep.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PG=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PG=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'hg',g:'Der Huf von der Seite, aufgeschnitten, mit Nerven und Blutgefäßen. Wer weiß, wo sie liegen, versteht, warum ein heißer Huf oder ein starker Puls an der Fessel ein Warnzeichen ist. (Entwurf: Beschriftung noch prüfen lassen.)',"
     "gE:'The hoof from the side, cut open, with nerves and blood vessels. Knowing where they run explains why a hot hoof or a strong pulse at the fetlock is a warning sign. (Draft: labels still to be checked.)',"
     "src:'Rich, Artistic Horse-Shoeing, Akron: Commercial Printing Co., 1907 (Library of Congress / Sloan Foundation über Flickr Commons; No known copyright restrictions)',"
     "srcE:'Rich, Artistic Horse-Shoeing, Akron: Commercial Printing Co., 1907 (Library of Congress / Sloan Foundation via Flickr Commons; no known copyright restrictions)',"
     "de:'Nerven und Gefäße im Huf',en:'Nerves and vessels in the hoof',img:'img/huf_gefaesse.jpg',W:%d,H:%d,P:PG,pos:'center 50%%',\n"
     "  alt:'Fessel und Huf im Längsschnitt mit Nerven und Gefäßen',altE:'Pastern and hoof in section with nerves and vessels',"
     "cap:'Fessel und Huf aufgeschnitten. Stich aus Rich (1907). Die Buchstaben im Bild sind ohne die Legende des Buches nicht erklärt; die Punkte sind unsere Deutung nach dem Bild und müssen noch geprüft werden.',"
     "capE:'Pastern and hoof cut open. Plate from Rich (1907). The letters in the picture are not explained without the book legend; the dots are our reading of the picture and still need checking.'},\n ")%(W,H)
    s=s.replace(" {k:'hi',"," "+new+"{k:'hi',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz49'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
