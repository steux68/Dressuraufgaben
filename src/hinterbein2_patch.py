# Anatomie: Bildsatz "Hinterbein (Zeichnung)" – Meysey-Thompson, The Horse, S. 155, Plate III (BHL, gemeinfrei) mit Buchlegende. Idempotent. 02.11.2026
import re,sys,shutil,os
from PIL import Image
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/84eb61da-image.jpg'
Q='img/quellen/meysey_thompson_p155.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');k=im.width/1221           # Koordinaten unten: Vorschau mit Breite 1221
x0,y0,x1,y1=120,380,880,1225
c=im.crop((round(x0*k),round(y0*k),round(x1*k),round(y1*k)))
f=1200/(x1-x0);W=1200;H=round((y1-y0)*f)
c.resize((W,H),Image.LANCZOS).save('img/hinterbein_plate3.jpg',quality=86,optimize=True)
def pt(x,y):return round((x-x0)*f),round((y-y0)*f)
P=[
 ('of','Oberschenkelknochen','Femur (E)',pt(776,597),'Der kräftigste Knochen des Pferdes. Er liegt so tief unter der Muskulatur, dass ihn viele Reiter kaum kennen.','The strongest bone of the horse. It lies so deep under the muscles that many riders hardly know it.'),
 ('ks','Kniescheibe und Kniegelenk','Stifle joint and patella (F)',pt(826,697),'Das Kniegelenk liegt beim Pferd weit vorn oben in der Flanke. Davor sitzt die Kniescheibe. Sie kann einrasten, damit das Pferd im Stehen ruht.','The stifle lies far forward and high in the flank. The kneecap sits in front of it. It can lock so the horse rests while standing.'),
 ('sc','Schienbein','Tibia (G)',pt(752,828),'Der lange Knochen zwischen Kniegelenk und Sprunggelenk.','The long bone between stifle and hock.'),
 ('wb','Wadenbein','Fibula (H)',pt(765,742),'Beim Pferd nur ein dünner Rest neben dem Schienbein.','In the horse only a thin remnant beside the tibia.'),
 ('sp','Sprunggelenk','Hock (I)',pt(715,917),'Die „Ferse“ des Pferdes, weit oben am Bein. Sie federt und schiebt kräftig ab. Viele Lahmheiten der Hinterhand kommen von hier.','The horse\'s heel, high up the leg. It springs and pushes strongly. Many hind-leg lamenesses start here.'),
 ('rb','Röhrbein','Cannon bone (K)',pt(718,987),'Der lange, glatte Knochen unter dem Sprunggelenk.','The long smooth bone below the hock.'),
 ('gb','Griffelbein','Splint bone (L)',pt(690,957),'Der schmale Knochen, der seitlich am Röhrbein anliegt. Eine Verdickung heißt „Überbein“.','The slim bone that lies against the cannon bone. A swelling there is called a splint.'),
 ('gl','Gleichbeine','Sesamoids (M)',pt(705,1110),'Zwei kleine Knochen hinten am Fesselgelenk. Sie führen die Sehnen und fangen Druck ab.','Two small bones at the back of the fetlock. They guide the tendons and take pressure.'),
 ('fb','Fesselbein','Long pastern (O)',pt(738,1107),'Der Knochen zwischen Fesselgelenk und Kronbein.','The bone between fetlock joint and short pastern.'),
 ('kb','Kronbein','Short pastern (Q)',pt(745,1135),'Der kurze Knochen zwischen Fesselbein und Hufbein.','The short bone between long pastern and coffin bone.'),
 ('hb','Hufbein','Coffin bone (P)',pt(790,1147),'Der Knochen im Huf, ganz vom Horn umgeben. Er trägt das Gewicht des Pferdes mit.','The bone inside the hoof, completely enclosed by horn. It helps carry the horse\'s weight.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PZ=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PZ=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'hz',g:'Die Knochen des Hinterbeins als klare Zeichnung, von hinten und von der Seite. Die Buchstaben im Bild gehören zur Legende des Buches, in den Punkten stehen sie in Klammern.',"
     "gE:'The bones of the hind leg as a clear drawing, from behind and from the side. The letters in the picture belong to the book legend; in the points they are given in brackets.',"
     "src:'Meysey-Thompson, The Horse, its origin and development combined with stable practice, S. 155, Plate III (Biodiversity Heritage Library; gemeinfrei)',"
     "srcE:'Meysey-Thompson, The Horse, its origin and development combined with stable practice, p. 155, Plate III (Biodiversity Heritage Library; public domain)',"
     "de:'Hinterbein (Zeichnung)',en:'Hind leg (drawing)',img:'img/hinterbein_plate3.jpg',W:%d,H:%d,P:PZ,pos:'center 50%%',\n"
     "  alt:'Knochen des Hinterbeins, Zeichnung, von hinten und von der Seite',altE:'Bones of the hind leg, drawing, from behind and from the side',"
     "cap:'Die Knochen des Hinterbeins, Plate III aus Meysey-Thompson. Namen nach der Buchlegende, übersetzt. Punkte nur an der Seitenansicht (rechts).',"
     "capE:'The bones of the hind leg, Plate III from Meysey-Thompson. Names after the book legend, translated. Points only on the side view (right).'},\n ")%(W,H)
    s=s.replace(" {k:'ko',"," "+new+"{k:'ko',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz50'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
