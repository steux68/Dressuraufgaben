# Galerie und Pferde: neueste Eintraege zuerst. Neue Bilder werden weiter hinten ans Array angehaengt, die Anzeige dreht um. Idempotent. 01.11.2026
import re
P='index.html';s=open(P,encoding='utf-8').read()
for name in ('GAL','P'):
    st=s.index('\nconst %s=['%name);e=s.index('\n];',st)+3
    tag='\n%s.reverse();/* neueste zuerst: neue Eintraege ans Ende der Liste schreiben */'%name
    if tag not in s[e:e+200]:
        s=s[:e]+tag+s[e:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-01zzz36'+m.group(3),s,count=1)
open(P,'w',encoding='utf-8').write(s)
