# 06.11.2026: Pferdewissen-Reihenfolge: Viereck, Anatomie, Sehen, Koerpersprache, Situationen, Gesundheit (Kacheln, Reiter, Standard-Reiter). Idempotent.
import re,sys
s=open('index.html',encoding='utf-8').read()
def rep(old,new):
    global s
    if new in s: return
    assert s.count(old)==1,old[:70]
    s=s.replace(old,new)
# Reiter im Kopf
old=''.join(re.findall(r'<button id="ths(?:S|V|K|Ge|A|B)" aria-pressed="false">[^<]*</button>\n',s)[:6])
lines=dict(re.findall(r'(<button id="ths(S|V|K|Ge|A|B)" aria-pressed="false">[^<]*</button>\n)',s) and [(m[1],m[0]) for m in re.findall(r'(<button id="ths(S|V|K|Ge|A|B)" aria-pressed="false">[^<]*</button>\n)',s)])
new=''.join(lines[k] for k in ['B','A','V','K','S','Ge'])
if old!=new:
    assert s.count(old)==1 and old.count('\n')==6
    s=s.replace(old,new)
# Reihenfolge-Listen
rep("SUBG=['thsS','thsV','thsK','thsGe','thsA','thsB']","SUBG=['thsB','thsA','thsV','thsK','thsS','thsGe']")
rep("curG='thsS'","curG='thsB'")
# Kacheln der Startseite
m=re.search(r" \[\['thsS'.*?\]\]\.forEach\(\(\[id,c,n,d\]\)=>\{",s,re.S)
if "[['thsB'" not in s:
    items=re.findall(r"\['(ths\w+)','[^']*','[^']*','[^']*'\]",m.group(0))
    rows={r[0]:r[0:0] for r in items}
    full=dict((x[0],x[1]) for x in re.findall(r"(\['(ths\w+)','[^']*','[^']*','[^']*'\])",m.group(0)) for x in [(x[1],x[0])])
    order=['thsB','thsA','thsV','thsK','thsS','thsGe']
    blk=" [" + ",\n  ".join(full[k] for k in order)+"].forEach(([id,c,n,d])=>{"
    s=s.replace(m.group(0),blk)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06zzz74'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
