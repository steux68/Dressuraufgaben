# Anatomie: Augen-Längsschnitt (ab) vor die Buchseite (as); Buchseite ohne Punkte. Idempotent. 03.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
i=s.index("{k:'as'");j=s.index("{k:'ab'");k=s.index("\n {k:",j+5)
if i<j:
    asb=s[i:j];abb=s[j:k]
    s=s[:i]+abb.rstrip().rstrip(',')+",\n "+asb.rstrip().rstrip(',')+s[k:] if False else s[:i]+abb.rstrip('\n')+("" if abb.rstrip().endswith(',') else ",")+"\n "+asb.rstrip('\n ')+s[k:]
s=s.replace("P:PS2,","P:[],")
s=re.sub(r"const PS2=\[.*?\n\];\n","",s,count=1,flags=re.S)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-03zzz67'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
