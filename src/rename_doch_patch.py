"""Deutsch-App heißt jetzt „DOCH!“ mit dem Zusatz „Deutsche Grammatik“ (31.10.2026, Entscheidung von Steuart).
Kopfzeile, <title>, Name unter dem Symbol auf dem Handy (apple-mobile-web-app-title) und Manifest.
Aufruf im Repo-Hauptordner: python3 src/rename_doch_patch.py  (idempotent)"""
import re,sys,json
f='deutsch/index.html'; s=open(f,encoding='utf8').read()
if 'DOCH!</b>' in s: sys.exit('schon angewendet')
def rep(a,b):
    global s
    assert s.count(a)==1,a[:70]; s=s.replace(a,b,1)
rep('<h1 class="logo"><b>DEUTSCH</b><span>grammatik</span></h1>','<h1 class="logo"><b>DOCH!</b><span>Deutsche Grammatik</span></h1>')
rep('<title>Deutsch Grammatik</title>','<title>DOCH! Deutsche Grammatik</title>')
rep('<meta name="apple-mobile-web-app-title" content="Deutsch">','<meta name="apple-mobile-web-app-title" content="DOCH!">')
a='.home h1.logo span{font-family:DdCor,Georgia,serif;font-weight:500;font-size:1.42rem;letter-spacing:0;color:var(--ink)}'
rep(a,a+'\n.home h1.logo b{font-size:min(1.5rem,calc(8.6vw - 12.8px));letter-spacing:.06em}.home h1.logo span{font-size:min(1.08rem,calc(6.2vw - 9.2px))}')
mm=re.search(r'(<meta name="app-version" content=")(\d{4}-\d{2}-\d{2})([a-z]+)(">)',s); nv=mm.group(3)[:-1]+chr(ord(mm.group(3)[-1])+1)
s=s.replace(mm.group(0),mm.group(1)+mm.group(2)+nv+mm.group(4),1)
open(f,'w',encoding='utf8').write(s)
mf='deutsch/manifest.webmanifest'; m=json.load(open(mf,encoding='utf8')); m['name']='DOCH! Deutsche Grammatik'; m['short_name']='DOCH!'
json.dump(m,open(mf,'w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
print('ok ->',mm.group(2)+nv)
