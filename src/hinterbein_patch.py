# Anatomie: neuer Bildsatz "Hinterbein" – Foto "Horse leg, bones.JPG" von HTO (2009, Wikimedia Commons, gemeinfrei). Idempotent. 02.11.2026
import re,sys,shutil,os
from PIL import Image
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/2d7df49f-image.jpg'
Q='img/quellen/hto_horse_leg_bones.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');k=im.width/710          # Koordinaten unten: Vorschau mit Breite 710
r=im.rotate(90,expand=True)                               # Bein liegt: Becken links, Huf rechts
f=1400/r.width;W,H=1400,round(r.height*f)
r.resize((W,H),Image.LANCZOS).save('img/hinterbein.jpg',quality=84,optimize=True)
def pt(x,y):                                              # (x,y) der Vorschau -> gedrehtes, verkleinertes Bild
    X,Y=x*k,y*k;return round(Y*f),round((im.width-X)*f)
P=[
 ('kb','Kreuzbein','Sacrum',pt(410,235),'Das Kreuzbein ist mit dem Becken fest verwachsen. Über diese Verbindung geht die Kraft der Hinterhand auf die Wirbelsäule und den Rücken.','The sacrum is fused with the pelvis. The power of the hindquarters passes through this joint to the spine and back.'),
 ('hh','Hüfthöcker','Point of the hip',pt(210,250),'Der Knochenvorsprung seitlich vorn an der Kruppe. Man kann ihn außen am Pferd ertasten.','The bony point at the side of the croup. You can feel it from the outside.'),
 ('hg','Hüftgelenk','Hip joint',pt(430,515),'Das Kugelgelenk, in dem der Oberschenkel am Becken sitzt. Beim Untertreten der Hinterbeine arbeitet es besonders stark.','The ball-and-socket joint where the thigh bone meets the pelvis. It works hard when the hind legs step under.'),
 ('sb','Sitzbein','Ischium',pt(610,535),'Der hintere Teil des Beckens. Das Ende bildet den „Sitzbeinhöcker“, den hintersten Punkt der Hinterhand.','The rear part of the pelvis. Its end is the point of the buttock, the rearmost point of the hindquarters.'),
 ('of','Oberschenkelknochen','Femur',pt(330,670),'Der kräftigste Knochen des Pferdes. Er liegt versteckt unter der großen Muskulatur der Hinterhand.','The strongest bone in the horse. It lies hidden under the large muscles of the hindquarters.'),
 ('ks','Kniescheibe','Patella',pt(110,775),'Sie sitzt vorn am Kniegelenk, das beim Pferd hoch oben in der Flanke liegt. Sie kann einrasten, damit das Pferd im Stehen ruht. Bleibt sie hängen, wird das Bein steif nach hinten gestreckt.','It sits at the front of the stifle joint, high up in the flank. It can lock so the horse rests while standing. If it catches, the leg is stuck stiffly backwards.'),
 ('sc','Schienbein','Tibia',pt(270,1100),'Der lange Knochen zwischen Knie und Sprunggelenk. Das dünne Wadenbein daneben ist nur noch ein kleiner Rest.','The long bone between stifle and hock. The thin fibula beside it is only a small remnant.'),
 ('fb','Fersenbein','Calcaneus (point of the hock)',pt(445,1255),'Die Spitze des Sprunggelenks. An ihr setzt die kräftige Sehne an, die das Sprunggelenk streckt. Es ist die „Ferse“ des Pferdes, weit oben am Bein.','The point of the hock. The strong tendon that extends the hock attaches here. It is the horse\'s heel, high up the leg.'),
 ('sg','Sprunggelenk','Hock (tarsal bones)',pt(385,1370),'Mehrere kleine Knochen, die wie ein Scharnier arbeiten. Sie fangen bei jedem Schritt Stöße ab. Hier treten häufig Gelenkprobleme auf, zum Beispiel Spat.','Several small bones that work like a hinge. They absorb the shock of every step. Joint problems such as spavin are common here.'),
 ('rb','Röhrbein','Cannon bone',pt(385,1520),'Der lange, glatte Knochen unter dem Sprunggelenk. Seitlich liegen die beiden schmalen Griffelbeine.','The long smooth bone below the hock. The two slim splint bones lie beside it.'),
 ('fg','Fesselgelenk','Fetlock joint',pt(365,1730),'Das Gelenk zwischen Röhrbein und Fesselbein. Hier sitzen die Gleichbeine. Es federt bei jedem Tritt stark ein.','The joint between cannon bone and pastern. The sesamoid bones sit here. It gives way a lot with every step.'),
 ('fs','Fesselbein und Kronbein','Pastern bones',pt(340,1810),'Die beiden Knochen in der Fessel, zwischen Fesselgelenk und Huf. Sie machen den Tritt weich.','The two bones of the pastern between fetlock and hoof. They soften the stride.'),
 ('hb','Hufbein','Coffin bone',pt(305,1890),'Der Knochen im Huf. Er ist ganz vom Horn umgeben und trägt das Gewicht des Pferdes mit.','The bone inside the hoof. It is completely enclosed by horn and carries the horse\'s weight.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PB=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PB=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'hb',g:'Das Hinterbein vom Becken bis zum Huf. Die Hinterhand schiebt das Pferd nach vorn und trägt beim Untertreten das Gewicht, darum lohnt es sich, die Knochen und Gelenke zu kennen.',"
     "gE:'The hind leg from pelvis to hoof. The hindquarters push the horse forward and carry weight when stepping under, so it pays to know the bones and joints.',"
     "src:'Foto: HTO, „Horse leg, bones.JPG“, 22. Mai 2009, Wikimedia Commons, gemeinfrei (vom Urheber freigegeben)',"
     "srcE:'Photo: HTO, “Horse leg, bones.JPG”, 22 May 2009, Wikimedia Commons, public domain (released by the author)',"
     "de:'Hinterbein',en:'Hind leg',img:'img/hinterbein.jpg',W:%d,H:%d,P:PB,pos:'center 50%%',\n"
     "  alt:'Knochen des Hinterbeins, Becken links, Huf rechts',altE:'Bones of the hind leg, pelvis left, hoof right',"
     "cap:'Die Knochen des Hinterbeins (Foto: HTO, gemeinfrei). Das Bild ist gedreht: links das Becken, rechts der Huf.',"
     "capE:'The bones of the hind leg (photo: HTO, public domain). The picture is rotated: pelvis on the left, hoof on the right.'},\n ")%(W,H)
    s=s.replace(" {k:'ko',"," "+new+"{k:'ko',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz48'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
