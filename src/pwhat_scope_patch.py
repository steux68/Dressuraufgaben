import re
f='index.html'; s=open(f,encoding='utf8').read()
mark='/*pwscope*/'
if mark not in s:
    a='if(!d||!b)return;'
    i=s.index('<script id="pwhat-js">'); j=s.index(a,i)+len(a)
    add=mark+'var tp=document.getElementById("p-title");function upd(){if(!tp){return;}var r=tp.getBoundingClientRect();b.style.display=(r.bottom>innerHeight*.6&&r.top<innerHeight*.4)?"":"none";}upd();document.addEventListener("scroll",upd,true);addEventListener("resize",upd);setTimeout(upd,300);setTimeout(upd,1200);'
    s=s[:j]+add+s[j:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzz"',s,count=1)
open(f,'w',encoding='utf8').write(s)
