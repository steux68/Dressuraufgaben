"""Deutsch-App: Abstand über jeder Kapitelleiste von 39 px auf 22 px (gleich für alle Kapitel, nicht zu groß).
Aufruf im Repo-Hauptordner: python3 src/gap_deutsch_patch.py  (idempotent)"""
import re,sys
f='deutsch/index.html'; s=open(f,encoding='utf8').read()
a='.hb.hl{margin:39px 50% -1px 0}'; b='.hb.hr{margin:39px 0 -1px calc(50% - 1px)}'
if a not in s: sys.exit('schon angewendet')
assert s.count(a)==1 and s.count(b)==1
s=s.replace(a,'.hb.hl{margin:22px 50% -1px 0}',1).replace(b,'.hb.hr{margin:22px 0 -1px calc(50% - 1px)}',1)
mm=re.search(r'(<meta name="app-version" content=")(\d{4}-\d{2}-\d{2})([a-z]+)(">)',s); nv=mm.group(3)[:-1]+chr(ord(mm.group(3)[-1])+1)
s=s.replace(mm.group(0),mm.group(1)+mm.group(2)+nv+mm.group(4),1)
open(f,'w',encoding='utf8').write(s); print('ok ->',mm.group(2)+nv)
