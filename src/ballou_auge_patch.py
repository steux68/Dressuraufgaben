# Anatomie: Bildsatz "Auge des Pferdes im Laengsschnitt" - Ballou, A Compend of Equine Anatomy and Physiology, S. 164, Fig. 26 (BHL ueber Wikimedia Commons, gemeinfrei). Dazu rundes Kachel-Symbol fuer "Sehen". Idempotent. 03.11.2026
import re,sys,shutil,os
from PIL import Image
PAGE='/mnt/user-data/uploads/1000063193.jpg'
QP='img/quellen/ballou_p164_auge.jpg'
if not os.path.exists(QP): shutil.copy(PAGE,QP)
pg=Image.open(QP).convert('RGB')
fig=pg.crop((31,531,1489,1616))            # nur die Abbildung (1458x1085)
fig.save('img/quellen/ballou_fig26_ausschnitt.jpg',quality=92)
W=1200;H=round(fig.height*W/fig.width);f=W/fig.width
fig.resize((W,H),Image.LANCZOS).save('img/auge_ballou.jpg',quality=84,optimize=True)
# rundes Symbol: Augapfel mit Linse, quadratisch
S=420;cx,cy=round(0.50*fig.width),round(0.47*fig.height);r=round(0.50*fig.height)
ic=fig.crop((cx-r,cy-r,cx+r,cy+r)).resize((S,S),Image.LANCZOS);ic.save('img/kreis_auge.jpg',quality=86,optimize=True)
# Punkte: Koordinaten im Vorschaubild (1100 px breit, Seite ab y=500) -> Abbildung -> 1200 px
def pv(px,py):
    ox=px/0.7152-31;oy=py/0.7152+500-531
    return round(ox*f),round(oy*f)
P=[
 ('sn','Sehnerv','Optic nerve',(250,340),'Das Kabel zum Gehirn. Er trägt das Bild vom Auge ins Gehirn.','The cable to the brain. It carries the picture from the eye to the brain.'),
 ('ld','Lederhaut','Sclera',pv(535,622),'Die feste, weiße Außenhaut des Augapfels. Sie hält das Auge in Form.','The tough white outer coat of the eyeball. It keeps the eye in shape.'),
 ('ah','Aderhaut','Choroid',pv(573,622),'Die Schicht unter der Lederhaut. Sie ist voller Blutgefäße und versorgt die Netzhaut.','The layer beneath the sclera. It is full of blood vessels and feeds the retina.'),
 ('nh','Netzhaut','Retina',pv(607,624),'Die innerste Schicht. Sie fängt das Licht auf und macht daraus Signale für das Gehirn.','The innermost layer. It catches the light and turns it into signals for the brain.'),
 ('hh','Hornhaut','Cornea',(993,470),'Die klare, gewölbte Vorderseite des Auges. Kratzer und Trübungen hier sind schmerzhaft: sofort zum Tierarzt.','The clear, curved front of the eye. Scratches and clouding here are painful: see the vet at once.'),
 ('ir','Regenbogenhaut (Iris)','Iris',pv(838,372),'Die Blende des Auges. Sie macht die Pupille weiter oder enger. Beim Pferd ist die Pupille ein liegendes Oval.','The aperture of the eye. It makes the pupil wider or narrower. In the horse the pupil is a horizontal oval.'),
 ('li','Linse','Crystalline lens',pv(760,430),'Die klare Linse bündelt das Licht auf der Netzhaut, ähnlich wie bei einer Kamera.','The clear lens focuses light onto the retina, much like a camera.'),
 ('gk','Glaskörper','Vitreous body',pv(600,400),'Die klare Gelmasse im Augeninneren. Sie füllt den größten Teil des Auges und gibt ihm seine runde Form.','The clear gel inside the eye. It fills most of the eye and gives it its round shape.'),
 ('vk','Augenkammern','Chambers of the eye',pv(828,445),'Die Räume zwischen Hornhaut, Iris und Linse. Sie sind mit klarem Kammerwasser gefüllt.','The spaces between cornea, iris and lens. They are filled with clear aqueous fluid.'),
 ('zk','Ziliarkörper','Ciliary body',pv(738,630),'Ein Ring um die Linse. Er hält die Linse und bildet das Kammerwasser.','A ring around the lens. It holds the lens and makes the aqueous fluid.'),
 ('lp','Lidplatte (Tarsus)','Tarsus (lid plate)',(990,326),'Die feste Platte im Augenlid. Sie gibt dem Lid seine Form.','The firm plate inside the eyelid. It gives the lid its shape.'),
 ('lh','Lidhaut','Skin of the eyelid',pv(826,128),'Die dünne Haut außen am Augenlid.','The thin skin on the outside of the eyelid.'),
 ('le','Lidheber','Elevator of the upper eyelid',pv(347,236),'Der Muskel, der das obere Augenlid hebt.','The muscle that lifts the upper eyelid.'),
 ('om','Oberer gerader Augenmuskel','Superior rectus muscle',pv(210,262),'Einer der Muskeln, die den Augapfel bewegen. Er dreht das Auge nach oben.','One of the muscles that move the eyeball. It turns the eye upward.'),
 ('um','Unterer gerader Augenmuskel','Inferior rectus muscle',pv(337,485),'Ein Augenmuskel, der das Auge nach unten dreht.','An eye muscle that turns the eye downward.'),
 ('oh','Hülle der Augenhöhle','Fibrous sheath of the orbit',(420,618),'Eine feste Bindegewebshülle. Sie polstert und hält den Augapfel in der Augenhöhle.','A firm sheath of connective tissue. It cushions and holds the eyeball in the orbit.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PO=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PO=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=(",\n {k:'ab',g:'Das Auge im Längsschnitt. Du siehst, wie der Augapfel von innen gebaut ist, dazu die Lider und die Muskeln, die ihn bewegen.',"
     "gE:'The eye in section. You see how the eyeball is built inside, plus the eyelids and the muscles that move it.',"
     "src:'Ballou, A Compend of Equine Anatomy and Physiology, S. 164, Fig. 26 \"Theoretical section of the horse\\'s eye\" (Biodiversity Heritage Library über Wikimedia Commons; gemeinfrei)',"
     "srcE:'Ballou, A Compend of Equine Anatomy and Physiology, p. 164, Fig. 26 \"Theoretical section of the horse\\'s eye\" (Biodiversity Heritage Library via Wikimedia Commons; public domain)',"
     "de:'Auge im Längsschnitt',en:'Eye in section',img:'img/auge_ballou.jpg',W:%d,H:%d,P:PO,pos:'center 50%%',\n"
     "  alt:'Längsschnitt durch das Pferdeauge mit Lidern und Augenmuskeln',altE:'Section through the horse eye with eyelids and eye muscles',"
     "cap:'Das Pferdeauge im Längsschnitt (Ballou, Fig. 26). Die Beschriftung der alten Tafel (Buchstaben a–z) ist hier in Punkte mit deutschen Namen übersetzt.',"
     "capE:'The horse eye in section (Ballou, Fig. 26). The old plate\\'s lettered legend (a–z) is turned into points with names.'}")%(W,H)
    marker="\n];\nconst UI={"
    assert marker in s
    s=s.replace(marker,new+marker,1)
# Gruppenfilter: Kopf und Auge
if "ap:'Kopf und Auge'}" in s: s=s.replace("ap:'Kopf und Auge'}","ap:'Kopf und Auge',ab:'Kopf und Auge'}",1)
# Kachel-Symbol Sehen: Ausschnitt statt SVG
s=s.replace("thsV:'img/kreis_auge.svg'","thsV:'img/kreis_auge.jpg'")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-03zzz65'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
