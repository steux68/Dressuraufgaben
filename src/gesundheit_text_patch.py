# Gesundheit: Texte abgeglichen (Warnwerte, Digitalpuls, Darmgeraeusche, Hautfalte, Tierarzt-Angaben). Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if "['Digitalpuls'" in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:60]
    s=s.replace(old,new,1)
rep("Eine halbe Minute zählen und mal 2 rechnen.'],","Eine halbe Minute zählen und mal 2 rechnen. Über 50 in Ruhe: Stress, Schmerz, Fieber oder beginnende Kolik.'],")
rep("ein Zug = heben und senken.'],","ein Zug = heben und senken. Über 20 in Ruhe, weite Nüstern oder doppeltes Heben der Flanke: den Tierarzt anrufen.'],")
rep("(festhalten, Schweif zur Seite).'],","(festhalten, Schweif zur Seite). Über 38,5 °C ist Fieber, unter 37,0 °C ein Warnzeichen (Schock).'],")
rep("nach 1 bis 2 Sekunden wieder rosa.']]},","nach 1 bis 2 Sekunden wieder rosa. Blass oder weiß, dunkelrot oder violett, gelblich: nicht normal, Tierarzt anrufen.']]},")
rep("  ['Kot & Wasser',","  ['Digitalpuls','Hinten am Fesselgelenk fühlen. Ein kräftig pochender Puls zeigt eine Entzündung im Huf (zum Beispiel Hufrehe oder einen Abszess). Tierarzt anrufen.'],\n  ['Darmgeräusche','Ohr oder Stethoskop an die Flanke, auf beiden Seiten oben und unten. Es gluckert und rumpelt regelmäßig. Stille ist ein Notfall.'],\n  ['Hautfalte','Eine Hautfalte am Hals anheben. Sie springt innerhalb von 2 Sekunden flach zurück. Bleibt sie stehen, fehlt dem Pferd Wasser.'],\n  ['Kot & Wasser',")
rep("Fieber über 38,5 °C, Atemnot,","Fieber über 38,5 °C, Puls in Ruhe dauernd über 50, dunkle oder violette Schleimhaut, Atemnot,")
rep("  ['Merke',","  ['Das sagst du am Telefon','Puls, Atmung und Temperatur. Seit wann die Zeichen bestehen. Wann das Pferd zuletzt Kot und Urin abgesetzt hat. Ob sich Futter oder Training geändert haben.'],\n  ['Merke',")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz112'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
