# Anatomie: neuer Bildsatz "Huf von unten (Foto)" – Alex brollo, "Hoof quoted.jpg", Wikimedia Commons, CC BY-SA 3.0. Bild bleibt unveraendert. Idempotent. 02.11.2026
import re,sys,shutil,os
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/19a4a474-image.jpg'
Q='img/quellen/hoof_quoted_brollo.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
if not os.path.exists('img/huf_unten.jpg'): shutil.copy(Q,'img/huf_unten.jpg')   # unveraendert (CC BY-SA)
W,H=738,981
P=[
 ('sb','Saumband','Periople',147,266,'Ein weicher Hornsaum am Übergang von der Haut zur Hufwand. Er schützt den Kronrand.','A soft rim of horn where the skin meets the hoof wall. It protects the coronary band.'),
 ('ba','Ballen','Bulb of the heel',202,236,'Die weichen, gepolsterten Hinterkanten des Hufs. Sie sollen sauber, trocken und ohne Risse sein.','The soft padded rear of the hoof. It should be clean, dry and free of cracks.'),
 ('st','Strahl','Frog',274,324,'Der weiche V-förmige Keil in der Hufmitte. Er federt und gibt Halt. Er soll fest, aber nicht hart sein und nicht stinken.','The soft V-shaped wedge in the middle. It cushions and grips. It should be firm, not hard, and not smell bad.'),
 ('mf','Mittlere Strahlfurche','Central groove',367,326,'Die Furche in der Mitte des Strahls. Tiefe, übel riechende Spalten sind ein Alarmzeichen für Strahlfäule.','The groove down the middle of the frog. Deep, foul-smelling cracks are a warning sign of thrush.'),
 ('sf','Seitliche Strahlfurchen','Collateral grooves',451,397,'Die Furchen links und rechts neben dem Strahl. Hier sammeln sich Schmutz und Feuchtigkeit. Beim Auskratzen gründlich, aber behutsam reinigen.','The grooves either side of the frog. Dirt and moisture collect here. Clean them thoroughly but gently.'),
 ('tr','Trachte','Heel',531,340,'Das hintere Ende der Hufwand. Zu niedrige oder untergeschobene Trachten kann der Hufschmied korrigieren.','The rear end of the hoof wall. Low or underrun heels can be corrected by the farrier.'),
 ('es','Eckstrebe','Bar',509,389,'Die Hornleiste, die von der Trachte nach vorn neben dem Strahl läuft. Sie stützt die Trachte, wenn das Pferd den Huf belastet.','The ridge of horn that runs forward from the heel beside the frog. It supports the heel under load.'),
 ('sg','Steingallenstelle','Seat of corn',523,430,'Die Stelle zwischen Eckstrebe und Wand. Hier entsteht die Steingalle, eine schmerzhafte Quetschung, bei der das Pferd plötzlich lahmen kann.','The spot between bar and wall. A corn, a painful bruise, forms here and can make the horse suddenly lame.'),
 ('aw','Äußere Wandschicht','Pigmented outer wall',573,465,'Die äußere, oft dunkle Hornschicht der Wand. Sie schützt den Huf vor Nässe und Austrocknen.','The outer, often dark horn layer of the wall. It protects the hoof from wet and from drying out.'),
 ('iw','Innere Wandschicht','Inner wall layer',543,568,'Die helle, nicht gefärbte Schicht innen an der Wand, direkt neben der Weißen Linie.','The pale, unpigmented layer on the inside of the wall, right next to the white line.'),
 ('wl','Weiße Linie','White line',510,609,'Der helle Streifen zwischen Wand und Sohle. Der Hufschmied setzt die Nägel in dieser Nähe. Darum darf nur er sie einschlagen.','The pale band between wall and sole. The farrier drives the nails close to it, so only the farrier should do it.'),
 ('ss','Strahlspitze','Apex of the frog',328,622,'Die vordere Spitze des V-förmigen Strahls. Sie zeigt zur Zehe.','The front tip of the V-shaped frog. It points towards the toe.'),
 ('so','Sohle','Sole',367,731,'Die Hornplatte zwischen Wand und Strahl. Sie ist leicht nach innen gewölbt, damit das Pferd nicht auf der Sohle steht.','The plate of horn between wall and frog. It is slightly arched so the horse does not stand on the sole.'),
 ('ze','Zehe','Toe',295,836,'Der vordere Teil des Hufs. Hier ist die Wand am dicksten. Beim Abfußen stößt das Pferd über die Zehe ab.','The front of the hoof. The wall is thickest here. The horse pushes off over the toe.'),
 ('sw','Seitenwand','Quarter',97,582,'Der seitliche Teil der Hufwand zwischen Zehe und Trachte.','The side of the hoof wall between toe and heel.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PR=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3],p[4],q(p[5]),q(p[6])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PR=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=("{k:'hr',g:'Ein echter Huf von unten, so wie ihn der Hufschmied beim Ausschneiden sieht. Wer Strahl, Sohle, Eckstreben und Weiße Linie erkennt, sieht beim täglichen Auskratzen sofort, wenn etwas nicht stimmt.',"
     "gE:'A real hoof from below, as the farrier sees it when trimming. Knowing frog, sole, bars and white line shows you straight away when something is wrong while picking out.',"
     "src:'Foto: Alex brollo, „Hoof quoted.jpg“, 2005, Wikimedia Commons, CC BY-SA 3.0 (auch GFDL), unverändert; Zahlen und Linien stammen vom Original',"
     "srcE:'Photo: Alex brollo, “Hoof quoted.jpg”, 2005, Wikimedia Commons, CC BY-SA 3.0 (also GFDL), unchanged; numbers and lines are from the original',"
     "de:'Huf von unten',en:'Hoof from below',img:'img/huf_unten.jpg',W:%d,H:%d,P:PR,pos:'center 45%%',\n"
     "  alt:'Huf von unten, Foto mit Beschriftungen',altE:'Hoof from below, photo with labels',"
     "cap:'Der Huf von unten (Foto: Alex brollo, Wikimedia Commons, CC BY-SA 3.0). Die Zahlen im Bild gehören zum Original, die gelben Punkte sind von uns.',"
     "capE:'The hoof from below (photo: Alex brollo, Wikimedia Commons, CC BY-SA 3.0). The numbers in the picture belong to the original; the yellow dots are ours.'},\n ")%(W,H)
    s=s.replace(" {k:'hi',"," "+new+"{k:'hi',",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz47'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
