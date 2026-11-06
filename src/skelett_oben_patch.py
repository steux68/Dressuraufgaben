# 06.11.2026: Anatomie: neuer Satz 'sh' "Skelett von oben (alte Zeichnung)" - Wellcome Collection "Skeleton of a Horse", CC BY 4.0. Punkte nach dem Bild gesetzt (Entwurf). Idempotent.
import re,sys,os,shutil
from PIL import Image
SRC='/mnt/user-data/attachments/8046c1e5-9810-5025-8ac0-4892ed0066fc/309d1cf2-image.jpg'
Q='img/quellen/wellcome_skeleton_of_a_horse.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');W=1000;H=round(im.height*W/im.width)
im.resize((W,H),Image.LANCZOS).save('img/skelett_oben_wellcome.jpg',quality=84,optimize=True)
f=W/1422.0   # Koordinaten unten in der Anzeigegroesse 1422 x 2000
P=[
('kf','Kopf (Schädel)','Head (skull)',(700,310),'Der Schädel von oben gesehen: vorn die Nase, an den Seiten Augen und Ohren.','The skull seen from above: the nose at the front, eyes and ears at the sides.'),
('au','Auge','Eye',(605,305),'Die Augen sitzen seitlich am Kopf. Darum sieht das Pferd fast rundherum.','The eyes sit at the sides of the head. That is why the horse sees almost all around.'),
('oh','Ohr','Ear',(535,415),'Die Ohren drehen sich einzeln. Sie zeigen, worauf das Pferd gerade achtet.','The ears turn independently. They show what the horse is paying attention to.'),
('hw','Halswirbel','Neck vertebrae',(700,660),'Sieben Wirbel bilden den Hals. Sie machen ihn beweglich: für Biegung und Dehnung.','Seven vertebrae form the neck. They make it flexible, for bending and stretching.'),
('sb','Schulterblatt','Shoulder blade',(430,830),'Der flache Knochen an der Schulter. Das Vorderbein hängt nur an Muskeln am Rumpf, darum schwingt die Schulter beim Gehen mit.','The flat bone at the shoulder. The foreleg is attached to the trunk only by muscles, so the shoulder swings with every step.'),
('oa','Oberarmbein','Upper arm bone',(255,955),'Der kurze, kräftige Knochen zwischen Schulter und Ellbogen.','The short, strong bone between shoulder and elbow.'),
('ua','Unterarm','Forearm',(265,1215),'Der Unterarm reicht vom Ellbogen bis zum „Knie“ des Pferdes, dem Vorderfußwurzelgelenk.','The forearm runs from the elbow to the horse\'s "knee", the carpal joint.'),
('hv','Huf (vorn)','Front hoof',(250,1388),'Der Huf ist die Hornkapsel um das Hufbein. Hier trägt das Pferd sein ganzes Gewicht.','The hoof is the horn capsule around the coffin bone. The horse carries its whole weight here.'),
('ri','Rippen','Ribs',(545,1015),'Pferde haben meist 18 Rippenpaare. Sie schützen Herz und Lunge. Auf der Zeichnung sind weniger zu sehen.','Horses usually have 18 pairs of ribs. They protect heart and lungs. The drawing shows fewer.'),
('ws','Wirbelsäule','Spine',(705,1110),'Die Wirbelsäule läuft vom Kopf bis zur Schweifspitze. Der Rücken zwischen Widerrist und Kreuz trägt den Sattel.','The spine runs from the head to the tip of the tail. The back between withers and croup carries the saddle.'),
('be','Becken','Pelvis',(560,1485),'Das Becken verbindet die Wirbelsäule mit den Hinterbeinen. Von hier kommt die Schubkraft.','The pelvis joins the spine to the hind legs. The pushing power comes from here.'),
('kz','Kreuzbein','Sacrum',(705,1470),'Fünf verwachsene Wirbel zwischen Lende und Schweif. Sie sitzen fest im Becken.','Five fused vertebrae between loin and tail. They are firmly set in the pelvis.'),
('os','Oberschenkel','Thigh bone',(410,1580),'Der kräftige Knochen im Hinterbein. Er sitzt im Hüftgelenk und treibt das Hinterbein an.','The strong bone of the hind leg. It sits in the hip joint and drives the hind leg.'),
('us','Unterschenkel','Lower leg',(350,1730),'Das Schienbein führt zum Sprunggelenk, dem großen Gelenk in der Mitte des Hinterbeins.','The tibia leads to the hock, the big joint in the middle of the hind leg.'),
('hf','Hinterfuß','Hind foot',(480,1900),'Unterhalb des Sprunggelenks folgen Röhrbein, Fessel und Huf.','Below the hock come cannon bone, fetlock and hoof.'),
('sw','Schweif','Tail',(735,1790),'Der Schweif besteht aus Schweifwirbeln und langen Haaren. Das Pferd vertreibt damit Fliegen und zeigt Stimmung.','The tail is made of tail vertebrae and long hair. The horse drives off flies with it and shows its mood.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PSH=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),round(p[3][0]*f),round(p[3][1]*f),q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PSH=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    blk=("{k:'sh',g:'Ein Pferdeskelett von oben, in einer alten Zeichnung: Kopf, Hals, Wirbelsäule, Rippen und die Beine. Die Knochen sind etwas einfach gezeichnet, aber man sieht gut, wie alles zusammenhängt. (Entwurf: Beschriftung nach dem Bild gesetzt, noch prüfen lassen.)',"
     "gE:'A horse skeleton seen from above in an old drawing: head, neck, spine, ribs and the legs. The bones are drawn rather simply, but you can see how everything fits together. (Draft: labels placed from the picture, still to be checked.)',"
     "src:'„Skeleton of a Horse“, Wellcome Collection, CC BY 4.0 (Zeichner und Datum nicht geprüft; Bild verkleinert)',"
     "srcE:'\"Skeleton of a Horse\", Wellcome Collection, CC BY 4.0 (artist and date not checked; image reduced in size)',"
     "de:'Skelett von oben (alte Zeichnung)',en:'Skeleton from above (old drawing)',img:'img/skelett_oben_wellcome.jpg',W:%d,H:%d,P:PSH,pos:'center 40%%',"
     "alt:'Alte Zeichnung eines Pferdeskeletts von oben mit roten Rippen',altE:'Old drawing of a horse skeleton from above with red ribs',"
     "cap:'Pferdeskelett von oben: Kopf, Hals, Wirbelsäule, Rippen und Beine.',capE:'Horse skeleton from above: head, neck, spine, ribs and legs.'},\n ")%(W,H)
    i=s.index("{k:'sk'");j=s.index("\n {k:",i+5)+2
    s=s[:j]+blk+s[j:]
    assert "ab:'Kopf und Auge'" in s
    s=s.replace("ab:'Kopf und Auge'","ab:'Kopf und Auge',sh:'Körper'",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06zzz76'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
