# Anatomie-Kacheln: Ausschnitt (Zoom + Position) pro Bild statt Mittel-Crop; drei neue Tafeln. Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'tbs:' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:60]
    s=s.replace(old,new,1)
rep("im.style.backgroundPosition=s.pos;","im.style.backgroundPosition=s.pos;if(s.tbs)im.style.backgroundSize=s.tbs;")
rep("img:'img/hebel_axe_1905.jpg',W:1500,H:979,P:[],pos:'center 50%'","img:'img/hebel_axe_1905.jpg',W:1500,H:979,P:[],pos:'center 45%',tbs:'cover'")
rep("img:'img/pferd_tafel6_kopf.jpg',W:1500,H:1170,P:[],pos:'center 50%'","img:'img/pferd_tafel6_kopf.jpg',W:1500,H:1170,P:[],pos:'53% 44%',tbs:'170%'")
rep("img:'img/pferd_tafel15_huf.jpg',W:1170,H:1500,P:[],pos:'center 50%'","img:'img/pferd_tafel15_huf.jpg',W:1170,H:1500,P:[],pos:'0% 33%',tbs:'190%'")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz107'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
