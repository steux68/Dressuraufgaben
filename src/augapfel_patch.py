# Anatomie: Bildsatz "Augapfel im Laengsschnitt" – McFadyean, The Anatomy of the Horse: A Dissection Guide, 1884, Fig. 32 (nach A. Thomson), MENSCHLICHES Auge. Flickr Commons. Idempotent. 02.11.2026
import re,sys,shutil,os
from PIL import Image
SRC='/mnt/user-data/attachments/84727e50-3613-58a1-bff4-1f3faf43c207/0174936d-image.jpg'
Q='img/quellen/mcfadyean_1884_fig32_auge.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');W=1200;H=round(im.height*W/im.width)
im.resize((W,H),Image.LANCZOS).save('img/augapfel.jpg',quality=84,optimize=True)
f=W/im.width
def pt(x,y):return round(x*f),round(y*f)
P=[
 ('hh','Hornhaut','Cornea',pt(1000,72),'Die klare, gewölbte Vorderseite des Auges. Sie lässt das Licht herein und schützt das Auge. Kratzer und Trübungen hier sind schmerzhaft: sofort zum Tierarzt.','The clear, curved front of the eye. It lets light in and protects the eye. Scratches and clouding here are painful: see the vet at once.'),
 ('vk','Vordere Augenkammer','Anterior chamber',pt(905,150),'Der Raum hinter der Hornhaut. Er ist mit klarem Kammerwasser gefüllt.','The space behind the cornea. It is filled with clear aqueous fluid.'),
 ('ir','Regenbogenhaut (Iris)','Iris',pt(730,222),'Die Blende des Auges. Sie macht die Pupille weiter oder enger. Beim Menschen ist die Pupille rund, beim Pferd ein liegendes Rechteck.','The aperture of the eye. It makes the pupil wider or narrower. In humans the pupil is round, in horses a horizontal oval.'),
 ('li','Linse','Lens',pt(900,340),'Die klare Linse bündelt das Licht auf der Netzhaut, ähnlich wie bei einer Kamera.','The clear lens focuses light onto the retina, much like a camera.'),
 ('zk','Ziliarkörper','Ciliary body',pt(455,345),'Ein Muskelring um die Linse. Er steuert die Linse und bildet das Kammerwasser.','A ring of muscle around the lens. It controls the lens and makes the aqueous fluid.'),
 ('gk','Glaskörper','Vitreous body',pt(680,775),'Die klare Gelmasse im Augeninneren. Sie gibt dem Auge seine runde Form.','The clear gel inside the eye. It gives the eye its round shape.'),
 ('ld','Lederhaut','Sclera',pt(120,720),'Die feste, weiße Außenhaut des Augapfels. Beim Pferd sieht man sie normalerweise kaum. Zeigt es viel Weiß, ist das Pferd oft erschrocken.','The tough white outer coat of the eyeball. In horses it is normally barely visible. If a horse shows a lot of white, it is often frightened.'),
 ('nh','Netzhaut und Aderhaut','Retina and choroid',pt(1568,950),'Die Netzhaut fängt das Licht auf und gibt es als Signal weiter. Die Aderhaut darunter versorgt sie mit Blut.','The retina catches the light and passes it on as a signal. The choroid beneath supplies it with blood.'),
 ('bf','Blinder Fleck','Blind spot (optic disc)',pt(840,1445),'Hier verlassen die Nervenfasern das Auge. An dieser Stelle gibt es keine Lichtsinneszellen, man sieht dort nichts.','Here the nerve fibres leave the eye. There are no light-sensing cells at this spot, so nothing is seen there.'),
 ('sn','Sehnerv','Optic nerve',pt(500,1560),'Das Kabel zum Gehirn. Es leitet das Bild vom Auge weiter.','The cable to the brain. It carries the image from the eye.')
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
arr="const PX=[\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in P)+"\n];\n"
s=open('index.html',encoding='utf-8').read()
if 'const PX=[' not in s:
    s=s.replace('const SETS=[',arr+'const SETS=[',1)
    new=(",\n {k:'ap',g:'Der Augapfel im Längsschnitt. Achtung: Das ist ein menschliches Auge, so wie es ein altes Lehrbuch für das Pferd als Vergleich zeigt. Das Pferdeauge ist ähnlich aufgebaut, aber viel größer, mit liegender Pupille.',"
     "gE:'The eyeball in section. Note: this is a human eye, as an old textbook shows it for comparison. The horse eye is built similarly but is much larger, with a horizontal pupil.',"
     "src:'McFadyean, The Anatomy of the Horse: A Dissection Guide, New York: Jenkins, 1884, Fig. 32, nach A. Thomson (Internet Archive / NCSU Libraries über Flickr Commons; No known copyright restrictions)',"
     "srcE:'McFadyean, The Anatomy of the Horse: A Dissection Guide, New York: Jenkins, 1884, Fig. 32, after A. Thomson (Internet Archive / NCSU Libraries via Flickr Commons; no known copyright restrictions)',"
     "de:'Augapfel (menschlich)',en:'Eyeball (human)',img:'img/augapfel.jpg',W:%d,H:%d,P:PX,pos:'center 50%%',\n"
     "  alt:'Augapfel im Längsschnitt, menschliches Auge',altE:'Eyeball in section, human eye',"
     "cap:'Der Augapfel im Längsschnitt. Es ist ein menschliches Auge (Fig. 32 nach A. Thomson, aus McFadyean 1884). Die Teile sind beim Pferd gleich, nur die Größe und die Pupille unterscheiden sich.',"
     "capE:'The eyeball in section. It is a human eye (Fig. 32 after A. Thomson, from McFadyean 1884). The parts are the same in horses; only size and pupil shape differ.'}")%(W,H)
    marker="\n];\nconst UI={"
    assert marker in s
    s=s.replace(marker,new+marker,1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz55'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
