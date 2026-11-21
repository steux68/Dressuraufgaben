# 21.11.2026: (1) Hinweis auf alte Aufgabenblätter + Link zu oeps.at, (2) zwei Situationsfragen vorsichtiger formuliert
# (hinter dem Pferd vorbeigehen; angelegte Ohren). Idempotent. Aufruf: python3 -I src/stand_sicherheit_patch.py [--noversion]
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'stand-hinweis' in s: sys.exit('schon angewendet')

def rep(a,b):
    global s
    assert s.count(a)==1,('nicht eindeutig',a[:60],s.count(a))
    s=s.replace(a,b,1)

# 1a) Fusszeile: oeps.at als Link
rep('Bitte vor der Prüfung die aktuelle Aufgabe auf oeps.at (Dressur → Aufgaben) prüfen',
    'Bitte vor der Prüfung die aktuelle Aufgabe auf <a href="https://www.oeps.at/dressur-aufgaben" target="_blank" rel="noopener">oeps.at (Dressur → Aufgaben)</a> prüfen')

# 1b) Quellenzeile: bei Blaettern von 2012 oder aelter zusaetzlicher Hinweis (/*stand-hinweis*/)
rep("$('src').textContent=v==='test'&&T.src?T.src:'Dressuraufgaben des Österreichischen Pferdesportverbands (OEPS).';",
    "$('src').textContent=v==='test'&&T.src?T.src:'Dressuraufgaben des Österreichischen Pferdesportverbands (OEPS).';\n/*stand-hinweis*/{const y=v==='test'&&T.src&&(T.src.match(/Stand \\d\\d\\.\\d\\d\\.(\\d{4})/)||[])[1];if(y&&+y<=2012)$('src').textContent+=' Das Blatt ist älter: bitte die aktuelle Fassung auf oeps.at prüfen.';}")

# 2a) hinter dem Pferd vorbeigehen
rep("a:'Mit großem Abstand oder ganz nah, die Hand auf der Kruppe, und dabei ansprechen',w:['Leise und schnell, damit es nicht gestört wird','Mit etwa einem Meter Abstand'],x:'Etwa einen Meter hinter dem Pferd trifft ein Huftritt mit voller Wucht. Ganz nah, mit der Hand auf der Kruppe, weiß das Pferd, wo du bist.'",
    "a:'Am besten mit großem Abstand und dabei ansprechen',w:['Leise und schnell, damit es nicht gestört wird','Mit etwa einem Meter Abstand'],x:'Etwa einen Meter hinter dem Pferd trifft ein Huftritt mit voller Wucht. Am sichersten ist großer Abstand. Geht es nicht anders, sprich das Pferd an und geh ganz nah vorbei, die Hand auf der Kruppe – nur bei einem ruhigen Pferd, das du kennst. Im Zweifel frag den Reitlehrer.'")

# 2b) angelegte Ohren
rep("x:'Angelegte Ohren heißen „Lass mich in Ruhe“. Wer weitergeht, riskiert einen Biss oder Tritt.'",
    "x:'Angelegte Ohren heißen oft „Lass mich in Ruhe“, besonders wenn das Pferd dir auch das Hinterteil zudreht. Ein Zeichen allein reicht aber nicht: Achte auch auf Haltung, Augen und Anspannung. Wer trotzdem weitergeht, riskiert einen Biss oder Tritt.'")

if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-21a'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
print('ok')
