# Galerie: 13 weitere Tafeln (01.11.2026). Idempotent. Aufruf im Repo-Hauptordner:
#   python3 -I src/galerie3_patch.py <ordner-mit-den-originalen>
import sys,os,re,shutil,json
from PIL import Image
SRC=sys.argv[1]
OLD='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären'
NEU=[
 dict(src='cc87be6b-image.jpg',id='china_weinwagen',n='Ein Wagen, der Wein transportiert',a='Zhou Peichun (周培春), Maler (Signatur rot, unten links)',w='Chinesisches Aquarell auf Papier, Bleistiftnotiz „A cart used for carrying wine“',j='',
  l='Altes Bild (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Sieben weiße Pferde ziehen einen Karren mit drei riesigen Weinfässern. Der Fuhrmann geht zu Fuß neben dem Gespann und hält eine lange Peitsche mit roten Quasten. Die chinesische Aufschrift oben bedeutet sinngemäß: „Das ist das Bild des Wagens, der Wein fährt.“',
  c=['Geschichte','Kunst','Stall']),
 dict(src='5b1f20ad-image.jpg',id='indien_handschrift_1',n='Pferde und Reiter in einer indischen Handschrift',a='Zeichner unbekannt',w='Handschrift in Devanagari-Schrift mit Pferdebildern, Doppelseite',j='',
  l='Alte Handschrift (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Links ein Pferd mit gemusterter Decke und ein Krieger mit Bogen, Speer und Schild, darunter ein Mann, der sein gesatteltes Pferd an langer Leine führt. Rechts ein Reiter mit Bogen und Köcher auf einem Pferd mit Quasten am Sattel. Der Text darüber sind Verse.',
  c=['Geschichte','Kunst','Reitkunst']),
 dict(src='a324c495-image.jpg',id='indien_handschrift_2',n='Gesattelte Pferde: Seite aus einer indischen Handschrift',a='Zeichner unbekannt',w='Handschrift in Devanagari-Schrift mit Pferdebildern, Doppelseite',j='',
  l='Alte Handschrift (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Links vier gesattelte Pferde, die sich paarweise anschauen. Rechts hält ein Mann in weitem Gewand ein Pferd mit gemusterter Decke am Kopf und am Maul fest.',
  c=['Geschichte','Kunst','Stall']),
 dict(src='78cf2969-image.jpg',id='alter_zaehne',n='Das Alter des Pferdes an den Zähnen',a='Verlag Fores, Sporting Repository (Zeichner nicht genannt)',w='„The Ages of the Horse“, Kolorierter Stich',j='London, 24. April 1848',
  l='Gemeinfrei · Wellcome Collection · Nachweis noch zu prüfen',
  x='Acht Schneidezahn-Reihen von „2 Jahre“ bis „8 Jahre“ und in der Mitte das Gebiss mit zehn bis zwölf Jahren. Die Buchstaben A–E bezeichnen die Zähne (A = Zangen, B = Mittelzähne, C = Eckzähne, E = Haken). Mit etwa 2 Jahren kommen die ersten Zähne, mit 5 Jahren die Eckzähne, danach schleifen sich die Gruben ab.',
  c=['Anatomie','Geschichte']),
 dict(src='1b535e38-image.jpg',id='hawkins_tafel5',n='Pferd und Mensch: gleiche Knochen, anderes Gerüst (Tafel V)',a='Benjamin Waterhouse Hawkins (1807–1894)',w='Comparative View of the Human and Animal Frame, Plate V',j='London, Chapman & Hall',
  l='Gemeinfrei · Wellcome Collection · Nachweis noch zu prüfen',
  x='Das Pferdeskelett steigt, daneben steht ein Menschenskelett. Gleiche Buchstaben bezeichnen gleiche Knochen: H = Oberarm- bzw. Oberschenkelknochen, R = Speiche, U = Elle, W = Handwurzel, MC = Mittelhand. Der Mittelfinger des Menschen wurde im Pferd zum Huf.',
  c=['Anatomie','Geschichte','Kunst']),
 dict(src='2a9ad045-image.jpg',id='hawkins_tafel4',n='Skelett von Reiter und Pferd (Tafel IV)',a='Benjamin Waterhouse Hawkins (1807–1894)',w='Comparative View of the Human and Animal Frame, Plate IV',j='London, Chapman & Hall',
  l='Gemeinfrei · Wellcome Collection · Nachweis noch zu prüfen',
  x='Ein Menschenskelett sitzt im Sattelsitz auf dem Pferdeskelett. Links daneben das Hinterbein des Menschen und des Pferdes: T = Oberschenkel bzw. Schienbein, K = Knie, C = Fersenbein (beim Pferd der Sprunggelenkhöcker), MT = Mittelfuß, D = Zehe bzw. Huf.',
  c=['Anatomie','Reitkunst','Kunst']),
 dict(src='576df55a-image.jpg',id='muybridge_reiter',n='Ein Reiter in Bewegung: Reihenaufnahmen',a='Eadweard Muybridge (1830–1904)',w='Animal Locomotion, Plate 619',j='1887',
  l='Gemeinfrei (Druck von 1887) · Scan über Wellcome Collection',
  x='Oben und in der Mitte je zwölf Bilder von der Seite, unten zwölf Bilder von vorn. Die Bilder sind nummeriert, so sieht man jede Phase der Bewegung des Pferdes und wie der Reiter mitgeht.',
  c=['Bewegung','Geschichte']),
 dict(src='ff6fc1fe-image.jpg',id='muybridge_maultier',n='Ein Maultier schlägt aus',a='Eadweard Muybridge (1830–1904)',w='Animal Locomotion (Reihenaufnahme, 16 Bilder)',j='um 1887',
  l='Gemeinfrei (Druck des 19. Jh.) · Scan über Wellcome Collection',
  x='Vier Reihen zu je vier Bildern zeigen, wie sich das Tier aufbäumt und mit beiden Hinterbeinen ausschlägt. Man sieht: Das Hinterteil geht hoch, der Hals und der Kopf gehen nach unten.',
  c=['Bewegung','Kurioses']),
 dict(src='494b4a42-image.jpg',id='elgin_kopf',n='Zwei Pferdeköpfe der Antike: Elgin und Venedig',a='John Landseer (um 1769–1852), Stecher; Notiz von Benjamin Robert Haydon',w='„The Elgin Horse’s Head“, Radierung mit handgeschriebenem Text',j='London, 18. Februar 1817',
  l='Gemeinfrei · Wellcome Collection · Nachweis noch zu prüfen',
  x='Links der Pferdekopf vom Parthenon-Fries („Elgin“), rechts ein Kopf der Pferde von San Marco in Venedig, die man Lysipp zuschrieb. Der Maler Haydon schreibt darunter: Der Elgin-Kopf sei „all truth“ (ganz Wahrheit), der andere „all manner“ (ganz Manier).',
  c=['Kunst','Geschichte']),
 dict(src='075ed6d5-image.jpg',id='korea_gutes_pferd',n='Die Merkmale eines guten Pferdes: koreanischer Holzschnitt',a='Zeichner unbekannt',w='Holzdruck-Seite mit Körperteilen und Beschriftung in Hanja und Hangul',j='',
  l='Alter Druck (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Von jedem Körperteil führt eine Linie zu einer Beschreibung: wie das Auge, der Rücken, der Huf oder das Röhrbein eines guten Pferdes sein sollen. Ein alter Beurteilungsbogen, wie es ihn auch in Europa gab.',
  c=['Anatomie','Geschichte','Kunst']),
 dict(src='29426970-image.jpg',id='regionen_profil',n='Die Körperregionen des Pferdes von der Seite',a='Zeichner unbekannt',w='„The Exterior of the Horse“, Fig. 11, S. 24 (Scan: Internet Archive)',j='19. Jahrhundert',
  l='Alte Druckseite (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Die Zahlen 0–37 benennen die Regionen, z. B. 2 Widerrist (Withers), 3 Rücken (Back), 5 Kruppe (Croup), 9 Schulter (Shoulder), 15 Vorderfußwurzelgelenk (Knee), 17 Fesselgelenk (Fetlock), 29 Knie (Stifle), 31 Sprunggelenk (Hock).',
  c=['Anatomie']),
 dict(src='6baf1c51-image.jpg',id='skelett_mensch_vorn',n='Mensch und Pferd von vorn: die Skelette',a='Mitchell (Stecher, Signatur unten Mitte)',w='Anatomisches Tafelwerk, Plate I',j='um 1800',
  l='Alte Tafel (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Das Menschenskelett von vorn, daneben das Pferd von vorn: schmale Brust, die Vorderbeine stehen eng zusammen und der Brustkorb ist hoch und schmal. Die Buchstaben verweisen auf die Liste am Rand.',
  c=['Anatomie']),
 dict(src='e78fc21d-image.jpg',id='pferdekoepfe_radierung',n='Neun Pferdeköpfe: Studienblatt',a='Zeichner unbekannt, Verlagssignatur „Israel excud.“ (herausgegeben von Israël)',w='Radierung mit Pferdeköpfen',j='17. Jahrhundert',
  l='Alte Radierung (gemeinfrei durch Alter) · genaue Quelle noch zu klären',
  x='Neun Köpfe, jeder in anderer Haltung: gesenkt, aufgerichtet, mit Trense und mit Halfter. Ein Blatt zum Abzeichnen, so lernte man früher, den Ausdruck eines Pferdes zu zeichnen.',
  c=['Kunst','Geschichte']),
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
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-01zzz34'+m.group(3),s,count=1)
open(P,'w',encoding='utf-8').write(s)
