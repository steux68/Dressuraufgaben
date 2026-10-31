"""Immer auf der Startseite starten: Kommt jemand nach mehr als LIM ms zur App zurück (Android hält installierte Apps im
Speicher und setzt sie dort fort, wo man aufgehört hat), wird die Seite ohne Adressanhang neu geladen. Außerdem kein
automatisches Wiederherstellen der Scroll-Position und Neuladen aus dem Zurück-Cache. Der Link-Anhang (#...) beim ersten
Öffnen bleibt erhalten. Deutsch-App: gemerkte Gruppe (store.grp) wird beim Start auf die erste zurückgesetzt.
Aufruf im Repo-Hauptordner: python3 src/start_patch.py  (wirkt auf index.html und deutsch/index.html, idempotent)"""
import re,sys
SNIP=('<script id="start-top">(function(){try{if("scrollRestoration" in history)history.scrollRestoration="manual";'
 'var K="start-hidden",LIM=30000,base=location.pathname+location.search;'
 'addEventListener("pageshow",function(e){if(e.persisted)location.reload();});'
 'document.addEventListener("visibilitychange",function(){if(document.visibilityState==="hidden"){try{sessionStorage.setItem(K,String(Date.now()));}catch(e){}}'
 'else{var t=0;try{t=+sessionStorage.getItem(K)||0;sessionStorage.removeItem(K);}catch(e){}if(t&&Date.now()-t>LIM)location.replace(base);}});}catch(e){}})();</script>')
META=re.compile(r'(<meta name="app-version" content=")([^"]*)(">)')
def bump(v):
    m=re.fullmatch(r'(\d{4}-\d{2}-\d{2})([a-z]+)',v); assert m,v
    L=m.group(2); nxt=L[:-1]+chr(ord(L[-1])+1) if L[-1]!='z' else L+'a'
    return m.group(1)+nxt
for f in ('index.html','deutsch/index.html'):
    s=open(f,encoding='utf8').read()
    if 'id="start-top"' in s: print('schon angewendet',f); continue
    m=META.search(s); assert m,f
    new=bump(m.group(2))
    s=META.sub(lambda mm:mm.group(1)+new+mm.group(3)+SNIP,s,count=1)
    if f.startswith('deutsch'):
        a='try{store=JSON.parse(localStorage.getItem("deutsch.v1")||"{}")}catch(e){}'
        assert s.count(a)==1; s=s.replace(a,a+'store.grp=0;',1)
    open(f,'w',encoding='utf8').write(s); print(f,m.group(2),'->',new)
