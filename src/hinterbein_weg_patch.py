# Anatomie: Hinterbein-Foto (HTO) entfernen; die Zeichnung (Meysey-Thompson) bleibt. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if "{k:'hb',g:'Das Hinterbein" not in s: sys.exit('schon angewendet')
a=s.index("const PB=[");b=s.index("const PG=[")
assert s[a:b].rstrip().endswith("];")
s=s[:a]+s[b:]
i=s.index(" {k:'hb',g:'Das Hinterbein");j=s.index(" {k:'hz',g:")
s=s[:i]+s[j:]
assert s.count("hb:'Beine',")==1
s=s.replace("hb:'Beine',","",1)
assert "P:PB" not in s
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz62'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
