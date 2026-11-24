# Xenophon: Buestenfoto (Raddato, CC BY-SA 2.0) als Portrait bei Zitaten und in der Geschichte. 24.11.2026
import re,sys
from PIL import Image
s=open('index.html',encoding='utf-8').read()
if 'xenophon_buste_q' in s: sys.exit('schon angewendet')
Image.open('img/quellen/xenophon_buste_original.jpg').convert('RGB').crop((100,250,1468,1618)).resize((640,640),Image.LANCZOS).save('img/zitate/xenophon_buste_q.jpg',quality=84)
P="img/zitate/xenophon_buste_q.jpg"
a="'Xenophon':['de:Xenophon'"; assert s.count(a)==1
s=s.replace(a,"'Xenophon':['"+P+"','de:Xenophon'")
b='ini:"Xe",w:["de:Xenophon"'; assert s.count(b)==1
s=s.replace(b,'ini:"Xe",w:["'+P+'","de:Xenophon"')
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24h"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
