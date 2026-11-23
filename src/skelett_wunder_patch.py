# 23.11.2026: "Skelett von oben (alte Zeichnung)" (Wellcome, CC BY 4.0) zieht von der Anatomie in die Wunder-Galerie um.
# - neuer GAL-Eintrag als neuestes Bild (GAL wird umgedreht, darum ans Ende des Arrays)
# - Anatomie-Satz 'sh' samt Punkten (PSH), Filter-Eintrag und Vorladeliste entfernt
# - Die 16 Punkte stehen weiter in src/skelett_oben_patch.py (falls sie wiederkommen sollen). Idempotent.
import re,sys,os,json
from PIL import Image
Q='img/quellen/wellcome_skeleton_of_a_horse.jpg'
F='img/galerie/skelett_oben_wellcome.jpg';K='img/galerie/skelett_oben_wellcome_k.jpg'
if not os.path.exists(F):
    im=Image.open(Q).convert('RGB')
    r=1600/max(im.size);im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS).save(F,quality=84,optimize=True)
    r=640/max(im.size);im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS).save(K,quality=82,optimize=True)
s=open('index.html',encoding='utf-8').read()
entry={"f":F,"k":K,
 "n":"Skelett eines Pferdes von oben: alte Zeichnung",
 "a":"Zeichner unbekannt",
 "w":"Skeleton of a Horse",
 "j":"",
 "l":"CC BY 4.0 · Wellcome Collection · Bild verkleinert · Zeichner und Datum noch zu klären",
 "x":"Ein Pferdeskelett von oben: Kopf, Hals, Wirbelsäule, Rippen (rot) und die Beine. Die Knochen sind etwas einfach gezeichnet, aber man sieht gut, wie alles zusammenhängt.",
 "c":["Anatomie","Geschichte"],"s":[3,4]}
if F not in s[s.index('const GAL=['):s.index('\nGAL.reverse()')]:
    a=s.index('\nGAL.reverse()');e=s.rindex('\n];',0,a)
    line=' {f: "%s", '%F+', '.join('"%s": %s'%(k,json.dumps(v,ensure_ascii=False)) for k,v in entry.items() if k!='f')+'}'
    s=s[:e]+',\n'+line+s[e:]
# aus der Anatomie entfernen
if 'const PSH=[' in s:
    i=s.index('const PSH=[');j=s.index('\n];\n',i)+4;s=s[:i]+s[j:]
if " {k:'sh',g:" in s:
    i=s.index(" {k:'sh',g:");j=s.index("\n {k:",i+5)+1;s=s[:i]+s[j:]
s=s.replace(",sh:'Körper'","",1) if ",sh:'Körper'" in s else s
s=s.replace('"skelett_oben_wellcome.jpg",','',1)
for p in ('img/skelett_oben_wellcome.jpg','img/ana_k/skelett_oben_wellcome.jpg'):
    if os.path.exists(p):os.remove(p)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-23e'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
