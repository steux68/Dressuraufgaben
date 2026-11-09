# "Was heißt PASSAGE?"-Link: von Geschichte & Zitate ans Ende der Links-Seite (kurz vor dem Copyright). Idempotent. 09.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
old="var g=$('p-g');if(g&&!$('pwhatG')){"
if old not in s: sys.exit('schon angewendet')
assert s.count(old)==1
s=s.replace(old,"var g=$('xyz');if(g&&!$('pwhatG')){",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-09zzz117'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
