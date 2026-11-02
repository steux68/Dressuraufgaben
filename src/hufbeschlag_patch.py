# Anatomie: neues Bild "Huf und Beschlag" (Barlow, Farriery Pl. 22, 1802, Wellcome, Public Domain Mark). Idempotent. 02.11.2026
import re,sys,shutil,os
from PIL import Image
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/f96c7ac6-image.jpg'
Q='img/quellen/barlow_farriery_pl22.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');k=im.width/1600
c=im.crop((0,int(70*k),im.width,int(1330*k)))
W=1400;H=round(c.height*W/c.width);c.resize((W,H),Image.LANCZOS).save('img/huf.jpg',quality=84,optimize=True)
P=[
 ('kr','Kronrand','Coronary band',225,320,'Der Übergang von der Haut zum Horn. Von hier wächst die Hufwand nach. Wärme, Schwellung oder eine Wunde hier gleich dem Tierarzt zeigen.','The line where skin meets horn. The hoof wall grows down from here. Heat, swelling or a wound here: show the vet straight away.'),
 ('hw','Hufwand','Hoof wall',165,358,'Das feste Horn außen am Huf. Nur hier sitzen die Nägel des Beschlags. Das Horn wächst ständig nach, darum kommt der Hufschmied alle 6 bis 8 Wochen.','The hard horn on the outside. Only here do the nails of a shoe go. The horn keeps growing, so the farrier comes every 6 to 8 weeks.'),
 ('st','Strahl','Frog',640,225,'Der weiche, V-förmige Keil in der Hufmitte. Er federt, gibt Halt und muss sauber und trocken bleiben. Ein übler Geruch kann Strahlfäule bedeuten.','The soft V-shaped wedge in the middle. It cushions and grips, and must stay clean and dry. A bad smell can mean thrush.'),
 ('so','Sohle','Sole',590,300,'Die leicht gewölbte Hornplatte zwischen Wand und Strahl. Beim Auskratzen von den Trachten zur Zehe arbeiten und nicht stochern.','The slightly arched horn plate between wall and frog. Clean from the heels towards the toe and do not poke.'),
 ('tr','Tragrand','Bearing edge',548,262,'Die untere Kante der Hufwand. Beim unbeschlagenen Huf trägt sie das Gewicht, beim Beschlag liegt das Eisen darauf.','The lower edge of the hoof wall. On a bare hoof it carries the weight; with a shoe, the shoe rests on it.'),
 ('ta','Trachten und Ballen','Heels and bulbs',590,95,'Der hintere Teil des Hufs. Hier sammeln sich Schmutz und Feuchtigkeit. Beim Hufe-Auskratzen immer mitkontrollieren.','The back of the hoof. Dirt and moisture collect here. Always check it when picking out the hooves.'),
 ('sk','Strahlkissen','Digital cushion',1230,335,'Das elastische Polster hinten im Huf, über dem Strahl. Es dämpft den Aufprall bei jedem Schritt.','The elastic pad at the back of the hoof, above the frog. It absorbs the impact of every step.'),
 ('he','Hufeisen','Horseshoe',652,715,'Aus Eisen oder Stahl und vom Hufschmied angepasst. Es schützt die Hufwand vor Abrieb. Nicht jedes Pferd braucht Eisen: viele gehen gut barhuf.','Made of iron or steel and fitted by the farrier. It protects the hoof wall from wear. Not every horse needs shoes; many go well barefoot.'),
 ('nl','Nagellöcher','Nail holes',745,603,'Die Nägel gehen nur durch die Hufwand. Ein loses Eisen klappert oder verrutscht: nicht mehr reiten und den Hufschmied rufen.','The nails go through the hoof wall only. A loose shoe clatters or shifts: stop riding and call the farrier.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PH=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3],p[4],q(p[5]),q(p[6])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PH=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'hf',g:'Der Huf ist das Wichtigste am Pferd, das ein Reiter täglich pflegt: auskratzen, ansehen, fühlen. Wer Wand, Sohle und Strahl kennt, erkennt Probleme früh und versteht den Hufschmied.',"
     "gE:'The hoof is what a rider looks after every day: pick it out, look, feel. Knowing wall, sole and frog helps you spot problems early and understand the farrier.',"
     "src:'J. Barlow (Stecher), Farriery, Pl. 22, Bd. III, London: G. Kearsley, 1802; Wellcome Collection 570118i; Public Domain Mark',"
     "srcE:'J. Barlow (engraver), Farriery, Pl. 22, vol. III, London: G. Kearsley, 1802; Wellcome Collection 570118i; Public Domain Mark',"
     "de:'Huf und Beschlag',en:'Hoof and shoeing',img:'img/huf.jpg',W:%d,H:%d,P:PH,pos:'center 40%%',\n"
     "  alt:'Huf von der Seite und von unten, Hufeisen',altE:'Hoof from the side and below, horseshoes',"
     "cap:'Der Huf von der Seite und von unten, dazu Hufeisen. Kupferstich von 1802 (Barlow), die Eisenformen sind historisch; Begriffe übersetzt.',"
     "capE:'The hoof from the side and below, with horseshoes. Engraving of 1802 (Barlow); the shoe shapes are historical; terms translated.'},\n ")%(W,H)
    s=s.replace(" {k:'au',"," "+new+"{k:'au',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz45'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
