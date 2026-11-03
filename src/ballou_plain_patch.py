# Anatomie: Saetze ohne Punkte (Buchseite) zeigen nur das Bild: kein Quiz, kein Hinweis, kein Punktezaehler. Idempotent. 03.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
def rep(a,b):
    global s
    if b in s: return
    assert s.count(a)==1,a
    s=s.replace(a,b)
rep("$('aImg').src=s.img;buildDots();buildBr();if(mode==='quiz')startQuiz();fit();paint();}",
    "$('aImg').src=s.img;if(!P.length)mode='lern';buildDots();buildBr();if(mode==='quiz')startQuiz();fit();paint();['aLern','aQuiz','aNames','aHint'].forEach(i=>{const e=$(i);if(e)e.style.display=P.length?'':'none';});}")
rep("[[en?'Points':'Punkte',P.length],","[...(P.length?[[en?'Points':'Punkte',P.length]]:[]),")
rep("const c=el('span','agk',s.P.length+' '+(lang==='en'?'points':'Punkte'));","const c=el('span','agk',s.P.length?s.P.length+' '+(lang==='en'?'points':'Punkte'):(lang==='en'?'original page':'Originalseite'));")
rep("Tippe auf die Punkte: Sie zeigen dir, was die Teile des Auges sind.","Die Punkte findest du im Satz „Auge im Längsschnitt“.")
rep("Tap the points to see what the parts of the eye are.","The points are in the set “Eye in section”.")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-03zzz68'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
