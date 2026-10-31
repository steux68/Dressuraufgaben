# Galerie: 8 weitere alte Tafeln (31.10.2026). Idempotent. Aufruf im Repo-Hauptordner:
#   python3 -I src/galerie2_patch.py <ordner-mit-den-originalen>
# Erwartet die Originale unter den Namen in NEU (Quelle -> Datei). Erzeugt img/galerie/<n>.jpg (max. 1600 px), <n>_k.jpg (480 px, Zuschnitt aufs Kachelraster), Original in img/quellen/.
import sys,os,re,shutil,json
from PIL import Image
SRC=sys.argv[1]
NEU=[
 dict(src='17e2ddc8-image.jpg',id='masse_studie',
  n='Das Pferd vermessen: Studien zu Maßen und Proportionen',a='Zeichner unbekannt',w='Federzeichnung mit Maßangaben in Händen und Zoll',j='',
  l='Alte Zeichnung (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Das Pferd von der Seite, von vorn und von hinten, dazu Kopfbilder und ein Mensch zum Größenvergleich. Gemessen wird in „Händen“ (1 Hand = 4 Zoll, etwa 10 cm): „66 in or 16½ hands“ steht über dem Rücken – bis heute das Maß für die Höhe von Pferden.',
  c=['Anatomie','Geschichte','Kunst']),
 dict(src='5db4be96-image.jpg',id='larousse_cheval',
  n='Pferdekörper und Pferderassen: Tafel „Cheval“',a='Zeichner unbekannt (Signatur unten rechts)',w='Französisches Lexikon, Seite 767, Stichwort „Cheval“',j='um 1900',
  l='Alte Druckseite (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Nr. 16 benennt die Körperteile (Crinière = Mähne, Garrot = Widerrist, Croupe = Kruppe, Sabot = Huf), Nr. 17 das Skelett. Dazu viele Rassen, z. B. Shetlandpony (3), Araber (4), Percheron (7), Trakehner (27), Pinzgauer (29).',
  c=['Rassen','Anatomie','Geschichte']),
 dict(src='05a5bdc5-image.jpg',id='vorderbein_knochen_muskeln',
  n='Vorderbein: Knochen und Muskeln',a='Zeichner unbekannt',w='Anatomisches Tafelwerk (Scan: Internet Archive Book Images)',j='19. Jahrhundert',
  l='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Links die Knochen, rechts dieselbe Ansicht mit Muskeln und Sehnen. Von unten nach oben: Hufbein (32), Kronbein (31), Fesselbein (30), Röhrbein (28), Vorderfußwurzelgelenk (26).',
  c=['Anatomie','Geschichte']),
 dict(src='aa90e0f1-image.jpg',id='kopf_hals_muskeln_skelett',
  n='Kopf und Hals: Muskeln und Knochen',a='Zeichner unbekannt',w='Anatomisches Tafelwerk, Fig. 5 (Scan: Internet Archive Book Images)',j='19. Jahrhundert',
  l='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Links die Muskeln von Kopf und Hals, rechts Schädel, Halswirbel und Schulterblatt (33). Die Hals-Muskeln sind die, die beim Reiten „am Zügel“ arbeiten.',
  c=['Anatomie','Geschichte']),
 dict(src='7cdb4bc9-image.jpg',id='fessel_laengsschnitt',
  n='Längsschnitt durch Fessel und Huf',a='Zeichner unbekannt',w='„Section of the Pastern and other Bones, Ligaments, etc.“, Nr. 33',j='19. Jahrhundert',
  l='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Die Buchstaben verweisen auf die Beschreibung im Buch. Man sieht, wie Röhrbein, Fesselbein, Kronbein und Hufbein übereinander stehen und von Sehnen und Bändern gehalten werden.',
  c=['Anatomie']),
 dict(src='73bf04da-image.jpg',id='skelett_plate3',
  n='Das Skelett des Pferdes, Seitenansicht',a='Meignen (Signatur links unten)',w='„Skeleton of the horse“, Plate III',j='um 1900',
  l='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Die Umrisse von Körper und Schweif sind dünn nachgezogen, so sieht man, wo die Knochen im Pferd liegen.',
  c=['Anatomie']),
 dict(src='d2c2e089-image.jpg',id='gatti_krankheiten',
  n='Alle Krankheiten des Pferdes und ihre Heilmittel',a='Monogramm „A. G.“ (Verleger Gatti)',w='„Tutte le infermità che possano venire al cavallo con li soi rimedii“',j='Bologna / Florenz 1594',
  l='Public Domain Mark · Wellcome Collection · Nachweis noch zu prüfen',
  x='Rund um das Pferd stehen etwa 60 Krankheiten in Kreisen, Strahlen führen zur betroffenen Körperstelle. Unten stehen die Rezepte.',
  c=['Geschichte','Kunst','Kurioses']),
 dict(src='f0fa085d-image.png',id='seton_proportionen',
  n='Die Proportionen eines typischen Pferdes',a='Ernest Thompson Seton (1860–1946), Naturforscher und Zeichner',w='Studies in the Art Anatomy of Animals',j='London 1896',
  l='Gemeinfrei',
  x='Alles in „Kopflängen“ gemessen: Die Buchstaben bezeichnen Punkte am Körper, die Brüche die Länge der Linien in Teilen einer Kopflänge. Der Rumpf ergibt etwa ein Quadrat von 2½ Kopflängen.',
  c=['Anatomie','Geschichte']),
]
os.makedirs('img/galerie',exist_ok=True);os.makedirs('img/quellen',exist_ok=True)
ents=[]
for d in NEU:
    ext=os.path.splitext(d['src'])[1].lower()
    q=f"img/quellen/{d['id']}{ext}"
    shutil.copy(os.path.join(SRC,d['src']),q)
    im=Image.open(q).convert('RGB');W,H=im.size
    big=im.copy();big.thumbnail((1600,1600));big.save(f"img/galerie/{d['id']}.jpg",quality=84,optimize=True)
    rows=max(2,round(3*H/W))
    cw=480;ch=round(cw*rows/3);sc=max(cw/W,ch/H)
    t=im.resize((round(W*sc),round(H*sc)),Image.LANCZOS);l=(t.width-cw)//2;u=(t.height-ch)//2
    t.crop((l,u,l+cw,u+ch)).save(f"img/galerie/{d['id']}_k.jpg",quality=82,optimize=True)
    e={'f':f"img/galerie/{d['id']}.jpg",'k':f"img/galerie/{d['id']}_k.jpg",'n':d['n'],'a':d['a'],'w':d['w'],'j':d['j'],'l':d['l'],'x':d['x'],'c':d['c'],'s':[3,rows]}
    ents.append(e)
P='index.html';s=open(P,encoding='utf-8').read()
add=''
for e in ents:
    if e['f'] in s: continue
    add+=",\n "+json.dumps(e,ensure_ascii=False).replace('"f":','f:',1)
if add:
    i=s.index('const GAL=[');j=s.index('\n];',i)
    s=s[:j]+add+s[j:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-10-31zp'+m.group(3),s,count=1)
open(P,'w',encoding='utf-8').write(s)
