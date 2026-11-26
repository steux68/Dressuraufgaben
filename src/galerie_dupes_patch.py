"""Wunder-Galerie: 7 Eintraege entfernen, die schon in Zitate/Geschichte vorkommen. Bilddateien bleiben."""
import re,sys
p=sys.argv[1]; s=open(p,encoding='utf8').read()
i=s.index('const GAL=['); j=s.index('\n];',i); blk=s[i:j]
keys=['bodenstedt_kolb','shakespeare_cobbe','karl_v_tizian','churchill_karsh','steinbrecht','seneca_gemaelde','meyer_skelett_kol','xenophon_buste']
for k in keys:
    m=re.search(r"\n *\{f:'img/galerie/%s\.jpg'"%k,blk)
    if not m: print('schon weg',k); continue
    n=re.search(r"\n *\{f:'",blk[m.end():])
    e=m.end()+n.start() if n else len(blk)
    blk=blk[:m.start()]+blk[e:]
s=s[:i]+blk+s[j:]
open(p,'w',encoding='utf8').write(s)
print('ok',blk.count("{f:'"),'Eintraege')
