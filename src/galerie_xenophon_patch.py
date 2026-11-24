# Galerie: Büste des Xenophon (Carole Raddato, CC BY-SA 2.0, Wikimedia Commons), ans Ende der Liste GAL (wird umgedreht: neueste zuerst). Idempotent. 24.11.2026
import re,sys,shutil
from PIL import Image
s=open('index.html',encoding='utf-8').read()
if 'xenophon_buste.jpg' in s: sys.exit('schon angewendet')
src='img/quellen/xenophon_buste_original.jpg'
shutil.copy(src,'img/galerie/xenophon_buste.jpg')   # unverändert
im=Image.open(src).convert('RGB'); w,h=im.size; th=round(w*4/3); top=min(100,h-th)
im.crop((0,top,w,top+th)).resize((480,640),Image.LANCZOS).save('img/galerie/xenophon_buste_k.jpg',quality=82)
E="""const GAL=[
 {f:'img/galerie/xenophon_buste.jpg',k:'img/galerie/xenophon_buste_k.jpg',n:'Büste des Xenophon',a:'Bildhauer unbekannt (römische Herme)',w:'Marmorbüste, Bibliotheca Alexandrina',j:'um 120 n. Chr.',l:'CC BY-SA 2.0 · Foto: Carole Raddato · Wikimedia Commons · Bild unverändert, Vorschau beschnitten',x:'Xenophon (um 430 bis um 354 v. Chr.) schrieb das älteste erhaltene Buch über Reitkunst. Sein Name steht in griechischen Buchstaben auf dem Sockel.',u:'https://commons.wikimedia.org/wiki/File:Bust_of_Xenophon.jpg',c:['Geschichte','Kunst'],s:[3,4]},
"""
END='\n];\nGAL.reverse();'
assert s.count(END)==1
i=s.index(END); head=s[:i].rstrip()
ENTRY=E.split('\n',1)[1].strip().rstrip(',')
s=head+('' if head.endswith(',') else ',')+'\n '+ENTRY+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24d"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
