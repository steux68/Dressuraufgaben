# Anatomie: Buchseiten-Satz 'as' entfernt; Augen-Laengsschnitt 'ab' bekommt die restlichen Legendenteile als Punkte. Idempotent. 03.11.2026
import re,sys,os
s=open('index.html',encoding='utf-8').read()
if "{k:'as'" in s:
    i=s.index("{k:'as'");j=s.index("\n {k:",i+5)
    s=s[:i].rstrip(' ')+s[j+2:] if False else s[:i]+s[j+2:]
    s=s.replace(",as:'Kopf und Auge'}","}",1)
    s=re.sub(r"const PS2=\[.*?\n\];\n","",s,count=1,flags=re.S)
if os.path.exists('img/auge_ballou_seite.jpg'): os.remove('img/auge_ballou_seite.jpg')
X=[
 ('lk','Linsenkapsel','Lens capsule',(885,540),'Die dünne, klare Hülle um die Linse.','The thin, clear envelope around the lens.'),
 ('zf','Ansatz der Ziliarfortsätze','Ciliary processes',(852,618),'Hier sitzen die feinen Fortsätze des Ziliarkörpers an der Linse an. Sie halten die Linse in ihrer Lage.','Here the fine processes of the ciliary body attach to the lens. They hold the lens in place.'),
 ('bh','Bindehaut','Conjunctiva',(905,232),'Die dünne, feuchte Haut innen im Lid. Sie überzieht auch den vorderen Augapfel. Ist sie gerötet, ist das Auge gereizt oder entzündet.','The thin, moist lining inside the lid. It also covers the front of the eyeball. If it is red, the eye is irritated or inflamed.'),
 ('fl','Faserhaut des Lides','Fibrous layer of the eyelid',(945,262),'Eine feste Bindegewebsschicht im Lid. Sie gibt dem Lid Halt.','A firm layer of connective tissue in the lid. It gives the lid support.'),
 ('rm','Ringmuskel des Lides','Orbicularis muscle',(880,100),'Der Muskel, der das Auge schließt. Er läuft ringförmig um die Lidspalte.','The muscle that closes the eye. It runs in a ring around the eye opening.'),
 ('hm','Hinterer gerader Augenmuskel','Posterior rectus muscle',(315,300),'Ein weiterer Muskel, der den Augapfel bewegt und ihn in der Augenhöhle führt.','Another muscle that moves the eyeball and guides it in the orbit.'),
]
def q(t):return "'"+t.replace("\\","\\\\").replace("'","\\'")+"'"
if "['lk'," not in s:
    e=s.rindex('\n];',0,s.index('const SETS=['))
    add=",\n"+",\n".join("['%s',%s,%s,%d,%d,%s,%s]"%(p[0],q(p[1]),q(p[2]),p[3][0],p[3][1],q(p[4]),q(p[5])) for p in X)
    s=s[:e]+add+s[e:]
s=s.replace("Die Beschriftung der alten Tafel (Buchstaben a–z) ist hier in Punkte mit deutschen Namen übersetzt.","Die Buchstaben der alten Tafel (a–z) sind hier in Punkte mit deutschen Namen übersetzt.")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-03zzz69'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
