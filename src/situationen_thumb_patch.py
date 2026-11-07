# Situationen-Kachel: KI-Symbolbild (Steuart Harrison, Gemini). Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'situationen_icon.jpg' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:60]
    s=s.replace(old,new,1)
rep("thsK:'img/koerper_ohren_1.jpg',","thsK:'img/koerper_ohren_1.jpg',thsS:'img/situationen_icon.jpg',")
rep("thsK:'#fff url(img/koerper_ohren_1.jpg) 52% 16%/289% no-repeat',","thsK:'#fff url(img/koerper_ohren_1.jpg) 52% 16%/289% no-repeat',thsS:'#fff url(img/situationen_icon.jpg) center/cover no-repeat',")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz110'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
