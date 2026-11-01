# Galerie: 1 weitere Tafeln (01.11.2026). Idempotent. Aufruf im Repo-Hauptordner:
#   python3 -I src/galerie3_patch.py <ordner-mit-den-originalen>
import sys,os,re,shutil,json
from PIL import Image
SRC=sys.argv[1]
OLD='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären'
NEU=[
 dict(src='704ebdb5-image.jpg',id='pferd_von_oben',n='Das Pferd von oben: Haut, Muskeln, Skelett',a='Zeichner unbekannt',w='Anatomische Tafel, Fig. 10–12 (Rücken, Muskeln und Knochen)',j='um 1900',
  l='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Dasselbe Pferd dreimal von oben: links die Haut mit Mähne und Schweif, in der Mitte die Muskeln des Rückens, rechts das Skelett mit Schädel, Halswirbeln, Rippen, Becken und Schulterblättern. Gut zu sehen, wie schmal der Hals und wie breit der Rumpf von oben wirkt. Die Zeichen am Rand verweisen auf die Liste im Buch.',
  c=['Anatomie']),
]
os.makedirs('img/galerie',exist_ok=True);os.makedirs('img/quellen',exist_ok=True)
ents=[]
for d in NEU:
    ext=os.path.splitext(d['src'])[1].lower()
    q=f"img/quellen/{d['id']}{ext}"
    shutil.copy(os.path.join(SRC,d['src']),q)
    im=Image.open(q).convert('RGB');W,H=im.size
    big=im.copy();big.thumbnail((1600,1600));big.save(f"img/galerie/{d['id']}.jpg",quality=84,optimize=True)
    rows=max(2,min(4,round(3*H/W)))
    cw=480;ch=round(cw*rows/3);sc=max(cw/W,ch/H)
    t=im.resize((round(W*sc),round(H*sc)),Image.LANCZOS);l=(t.width-cw)//2;u=(t.height-ch)//2
    t.crop((l,u,l+cw,u+ch)).save(f"img/galerie/{d['id']}_k.jpg",quality=82,optimize=True)
    ents.append({'f':f"img/galerie/{d['id']}.jpg",'k':f"img/galerie/{d['id']}_k.jpg",'n':d['n'],'a':d['a'],'w':d['w'],'j':d['j'],'l':d['l'],'x':d['x'],'c':d['c'],'s':[3,rows]})
P='index.html';s=open(P,encoding='utf-8').read()
add=''
for e in ents:
    if e['f'] in s: continue
    add+=",\n "+json.dumps(e,ensure_ascii=False).replace('"f":','f:',1)
if add:
    i=s.index('const GAL=[');j=s.index('\n];',i)
    s=s[:j]+add+s[j:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-01zzz37'+m.group(3),s,count=1)
open(P,'w',encoding='utf-8').write(s)
