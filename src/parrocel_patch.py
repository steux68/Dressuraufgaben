# 06.11.2026: Viereck > Geschichte: Radierung "La course des tetes & de la bague" (C. Parrocel, Wellcome V0021787, CC BY 4.0, ueber Wikimedia Commons). Idempotent.
import re,sys,os,shutil
from PIL import Image
SRC='/mnt/user-data/attachments/8046c1e5-9810-5025-8ac0-4892ed0066fc/f73d11ae-image.jpg'
Q='img/quellen/parrocel_course_des_tetes_wellcome_V0021787.jpg'
if not os.path.exists(Q): shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');W=1200;H=round(im.height*W/im.width)
im.resize((W,H),Image.LANCZOS).save('img/parrocel_bahn.jpg',quality=82,optimize=True)
s=open('index.html',encoding='utf-8').read()
old="const im=el('div','viImgs');w.appendChild(im);\n (window.VIER_BILDER||[])"
new=("H('Eine Reitbahn früher');\n"
" P('So sah eine Reitbahn auf einer alten Radierung aus: Reiter üben, in der Mitte stehen Zuschauer, am Rand stehen Pfosten mit Zielen. Auf dem Bild gibt es noch keine Dressurbuchstaben. Aber es sind schon feste Punkte beschriftet, an denen die Reiter wenden („1e Demi-Volte“, „Tête de Méduse“, „Tête du Pistolet“). Das Bild zeigt Kopf- und Ringstechen, ein Reiterspiel, und keine Dressur im heutigen Sinn.');\n"
" const VB=[['img/parrocel_bahn.jpg','Alte Radierung einer Reitbahn: Reiter üben Wendungen an beschrifteten Punkten, Zuschauer stehen in der Mitte','„La course des têtes et de la bague“, Radierung von C. Parrocel. Wellcome Collection, V0021787, CC BY 4.0, über Wikimedia Commons (Bild verkleinert).']];\n"
" const im=el('div','viImgs');w.appendChild(im);\n (window.VIER_BILDER||VB)")
if "const VB=[['img/parrocel_bahn.jpg'" not in s:
    assert s.count(old)==1
    s=s.replace(old,new)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06zzz75'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
