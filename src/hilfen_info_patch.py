# Hilfen: zu jedem Zeichen ein Hinweis "Gut zu wissen" (eigene Formulierung nach allgemeiner Reitlehre) + Grundregeln im Reiter Zeichen. 25.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'hilfen-info-css' in s: sys.exit('schon angewendet')
W={
'Halten':'Das Pferd soll durch das Treiben an die Hand herangeschoben werden und nicht durch Zug nach hinten stehen bleiben. Ein gutes Halten ist gerade, ruhig und auf allen vier Beinen gleichmäßig belastet.',
'Anreiten aus dem Halten':'Das Pferd soll sofort und ohne Zögern antreten, ohne zu rucken oder zu eilen. Die Hand darf es dabei nicht bremsen.',
'Schritt & Trab ohne Tempoverstärkung':'Die Hände bleiben ruhig und gleichmäßig. Sie halten die Verbindung, ziehen aber nicht zurück. Der Takt ändert sich nicht.',
'Tempoverstärkung im Schritt & Trab':'Mehr Tempo kommt aus dem Treiben, nicht aus dem Nachgeben allein. Die Tritte werden länger, der Takt bleibt gleich.',
'Leichttraben, Einsitzen':'Aufgestanden wird, wenn das äußere Vorderbein nach vorn schwingt („auf der richtigen Diagonale“). Die Bewegung kommt aus dem Mitgehen, nicht aus den Händen oder den Bügeln.',
'Erheben des Gesäßes aus dem Sattel':'Der Oberkörper neigt sich leicht vor, das Gewicht geht in die Bügel und der Rücken des Pferdes wird entlastet. Die Hände bleiben ruhig neben dem Mähnenkamm.',
'Angaloppieren (links)':'Das Pferd wird vorher nach links gestellt und gebogen, zum Beispiel in der Ecke oder auf dem Zirkel. Der verwahrende äußere Schenkel hindert die Hinterhand am Ausweichen.',
'Galopp ohne Tempoveränderung (Linksgalopp)':'Der Galopp ist ein Dreitakt mit einer Schwebephase. Der Reiter geht mit den Hüften mit, die Hand folgt der Nickbewegung des Kopfes.',
'Tempoverstärkung im Galopp (Linksgalopp)':'Die Sprünge sollen länger werden, nicht nur schneller. Wird das Pferd eilig, helfen halbe Paraden.',
'Parade, 1. Phase':'Eine Parade wirkt von hinten nach vorn: erst treiben, dann halten. Ohne die treibenden Hilfen wird sie zum Zug am Maul.',
'Parade, 2. Phase':'Das Nachgeben ist die Belohnung. Bleibt es aus, lernt das Pferd, sich gegen die Hand zu stemmen.',
'Schenkelweichen (links)':'Das Pferd tritt vorwärts-seitwärts und weicht dem Schenkel. Es soll im Takt bleiben und nicht über die Schulter ausfallen.',
'Vorhandwendung (linksum kehrt)':'Sie wird aus dem sicheren Halten begonnen. Die Hinterhand zieht einen Halbkreis um die Vorhand, die Beine treten dabei weiter im Takt.',
'Hinterhandwendung (linksum kehrt)':'Die Hinterhand bleibt fast auf der Stelle und tritt weiter. Das Pferd soll dabei nicht rückwärts gehen.',
'Wendungen in der Bewegung':'Der innere Zügel stellt, der äußere führt die Schulter und begrenzt sie. Der innere Schenkel treibt am Gurt, der äußere verwahrt dahinter.',
'Rückwärtsrichten, 1. Phase':'Rückwärts tritt das Pferd diagonal im Zweitakt. Es soll gerade bleiben und die Hinterhand nicht seitlich ausweichen lassen.',
'Rückwärtsrichten, 2. Phase':'Das Pferd soll gerade und mit gleichmäßigen Tritten zurückgehen, ohne den Kopf hochzuwerfen. Danach tritt es wieder vorwärts an.',
'Rückwärtsrichten, junges Pferd, 1. Phase':'Bei jungen Pferden wirkt der Reiter besonders leicht auf den Rücken ein. Verlangt werden nur wenige Tritte.',
'Rückwärtsrichten, junges Pferd, 2. Phase':'Nach den wenigen Tritten wird das Pferd gelobt. So bleibt die Übung für das junge Pferd eine angenehme Erfahrung.',
'Überstreichen':'Die Übung zeigt, ob sich das Pferd selbst trägt: Haltung und Tempo bleiben gleich, auch wenn die Hand kurz nicht einwirkt.',
'Zügel aus der Hand kauen lassen':'Das Pferd dehnt Hals und Kopf vorwärts-abwärts und streckt dabei den Rücken. Es bleibt im Takt und im Gleichgewicht. Danach werden die Zügel ruhig wieder aufgenommen.'
}
for n,w in W.items():
    a=s.index("{n:'"+n+"'"); e=s.index("'}",a)
    s=s[:e+1]+",w:'"+w.replace("'","\\'")+"'"+s[e+1:]
OLD="+'<p class=\"hiT\">'+p.t+'</p>"
assert s.count(OLD)==1
s=s.replace(OLD,OLD+"<p class=\"hiW\"><b>Gut zu wissen</b>'+p.w+'</p>")
OL="p.style.minHeight='';t.style.minHeight='';const kp=p.textContent,kt=t.textContent;let a=0,b=0;\n HL.forEach(x=>{p.textContent=x.t;t.textContent=x.n;a=Math.max(a,p.offsetHeight);b=Math.max(b,t.offsetHeight);});\n p.textContent=kp;t.textContent=kt;p.style.minHeight=a+'px';t.style.minHeight=b+'px';"
assert s.count(OL)==1
NL="p.style.minHeight='';t.style.minHeight='';const kp=p.textContent,kt=t.textContent,pw=root.querySelector('.hiW'),kw=pw?pw.innerHTML:'';let a=0,b=0,c=0;if(pw)pw.style.minHeight='';\n HL.forEach(x=>{p.textContent=x.t;t.textContent=x.n;a=Math.max(a,p.offsetHeight);b=Math.max(b,t.offsetHeight);if(pw){pw.innerHTML='<b>Gut zu wissen</b>'+x.w;c=Math.max(c,pw.offsetHeight);}});\n p.textContent=kp;t.textContent=kt;p.style.minHeight=a+'px';t.style.minHeight=b+'px';if(pw){pw.innerHTML=kw;pw.style.minHeight=c+'px';}"
s=s.replace(OL,NL)
Z="if(hls.m==='z'){o+='<div class=\"hiLeg\">'+HLK.map(q=>'<div>'+hlMini(q[0])+'<span>'+q[1]+'</span></div>').join('')+'</div>';}"
assert s.count(Z)==1
s=s.replace(Z,Z[:-1]+"\n  o+='<div class=\"hiRules\"><p class=\"hiRh\">Grundregeln</p><ul><li>Die Hilfen wirken zusammen. Die treibenden Hilfen überwiegen, die Hand ist nur das Gegenüber.</li><li>Die Hand arbeitet aus dem Handgelenk. Arm und Schulter bleiben ruhig.</li><li>Ein ausbalancierter, losgelassener Sitz ist die Voraussetzung für jede feine Hilfe.</li><li>Die Gerte wird nur hinter dem Schenkel eingesetzt, und nur als Unterstützung.</li><li>Loben gehört dazu: Nach jeder gelungenen Hilfe gibt der Reiter nach.</li></ul></div>';}")
S1="Piktogramme neu gezeichnet, nach einer Hilfentafel. Entwurf, mit Reitlehrer abgleichen."
assert s.count(S1)==1
s=s.replace(S1,"Piktogramme neu gezeichnet, nach einer Hilfentafel. Die Hinweise „Gut zu wissen“ und die Grundregeln sind in eigenen Worten nach allgemeiner Reitlehre geschrieben. Entwurf, mit Reitlehrer abgleichen.")
CSS='<style id="hilfen-info-css">#thHi .hiW{font-size:.9rem;line-height:1.45;color:#555;margin:10px 0 0;padding-left:10px;border-left:3px solid #cdff3e}#thHi .hiW b{display:block;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:#222;margin-bottom:2px}#thHi .hiRules{background:var(--surface);padding:12px;margin-top:8px}#thHi .hiRh{margin:0 0 6px;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;font-weight:700}#thHi .hiRules ul{margin:0;padding-left:18px;font-size:.9rem;line-height:1.45;color:#444}#thHi .hiRules li{margin:0 0 6px}</style>\n'
i=s.rindex('</head>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-25a"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
