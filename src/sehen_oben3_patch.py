# Sehen: eigene, saubere Zeichnung "Pferd von oben". Die Breiten (Hals, Widerrist, Rumpf, Kruppe) sind von der
# alten Tafel (img/quellen/pferd_von_oben.jpg, Fig. 10) abgemessen, der Kopf ist nach normalen Proportionen ergaenzt. Idempotent. 01.11.2026
import re
S=.155;PY=163.8                      # 1 Tafel-Pixel = S Einheiten; Genick (Ohransatz) bei Tafel-y 110 = Einheit 163.8
FX=1.3
X=lambda dx:160+dx*S*FX
Y=lambda y:PY+(y-110)*S
R=[(0,-120),(17,-118),(27,-104),(33,-80),(37,-50),(43,-20),(49,2),(51,18),(49,40),(46,70),(44,100),(43,140),(41,185),(38,225),(36,262),(38,296),(42,330),(46,352),(56,368),(72,382),(80,400),(82,450),(80,510),(84,550),(92,590),(100,640),(104,690),(105,740),(103,790),(110,822),(114,842),(110,885),(102,915),(88,940),(60,958),(30,966),(0,968)]
def cr(d,closed=True):
    p='M%.2f,%.2f'%d[0]
    for i in range(len(d)-1):
        p0=d[max(i-1,0)];p1=d[i];p2=d[i+1];p3=d[min(i+2,len(d)-1)]
        p+='C%.2f,%.2f %.2f,%.2f %.2f,%.2f'%(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6,p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6,p2[0],p2[1])
    return p+('Z' if closed else '')
def pts(L,sg=1):return [(X(sg*x),Y(y)) for x,y in L]
body=cr(pts(R)+pts(R[::-1][1:-1],-1))
def side(L):
    return cr(pts(L,1),False)+' '+cr(pts(L,-1),False)
ear=lambda sg:cr(pts([(-26,128),(-23,100),(-31,72),(-46,50),(-58,68),(-63,96),(-58,122),(-42,132)],1) if sg>0 else pts([(-26,128),(-23,100),(-31,72),(-46,50),(-58,68),(-63,96),(-58,122),(-42,132)],-1)).replace('M','M',1)
# Ohren: rechts = Spiegel von links (x negativ -> sg=-1 ergibt rechts)
EAR=[(-20,128),(-23,100),(-34,70),(-52,46),(-64,72),(-64,106),(-48,130)]
earL=cr(pts(EAR,1));earR=cr(pts(EAR,-1))
earIL=cr(pts([(-27,120),(-33,96),(-43,68)],1),False);earIR=cr(pts([(-27,120),(-33,96),(-43,68)],-1),False)
mane=''.join('M%.2f,%.2f l%.2f,%.2f'%(X(2+(i%3)),Y(y),(5+(i*7)%6)*S*1.3,4*S*1.3) for i,y in enumerate(range(130,372,15)))
spine='M%.2f,%.2f L%.2f,%.2f'%(X(0),Y(60),X(0),Y(960))
muskel=''.join(cr(pts(L,sg),False)+' ' for sg in (1,-1) for L in (
  [(34,520),(70,525),(95,570),(100,680),(98,760),(76,796),(52,806)],        # Lendenmuskel
  [(46,352),(60,380),(66,420),(58,470)],                                      # Schulterblatt
  [(108,830),(96,880),(70,930),(28,955)],                                     # Kruppe
))
new='''const h=g('thEh');
 el('path',{class:'hz',d:'M%.2f,%.2f L%.2f,%.2f L%.2f,%.2f L%.2f,%.2f Z'},h);
 el('path',{class:'hz',d:'%s'},h);
 el('path',{class:'hz',d:'%s'},h);el('path',{class:'hz',d:'%s'},h);
 el('path',{d:'%s',fill:'none',stroke:'var(--muted)','stroke-width':.8,'stroke-linecap':'round'},h);
 el('path',{d:'%s',fill:'none',stroke:'var(--fg)','stroke-width':.5,'stroke-linecap':'round',opacity:.55},h);
 el('path',{d:'%s',fill:'none',stroke:'var(--muted)','stroke-width':.7,'stroke-dasharray':'1 3','stroke-linecap':'round'},h);
 el('path',{d:'%s',fill:'none',stroke:'var(--fg)','stroke-width':.6,'stroke-linecap':'round'},h);
 el('ellipse',{cx:%.2f,cy:%.2f,rx:1.1,ry:1.6,fill:'#222'},h);el('ellipse',{cx:%.2f,cy:%.2f,rx:1.1,ry:1.6,fill:'#222'},h);
 el('circle',{cx:%.2f,cy:%.2f,r:1.9,fill:'#111'},h);el('circle',{cx:%.2f,cy:%.2f,r:1.9,fill:'#111'},h);
 '''%(X(-6),Y(955),X(6),Y(955),X(5),Y(1000),X(-5),Y(1000),
     body,earL,earR,muskel,mane,spine,earIL+' '+earIR,
     X(-11),Y(-108),X(11),Y(-108),X(-50),Y(14),X(50),Y(14))
s=open('index.html',encoding='utf-8').read()
a0=s.index("const h=g('thEh');");b0=s.index("const l=g('thEl');",a0)
s=s[:a0]+new+s[b0:]
s=s.replace('viewBox="0 0 320 320" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gesichtsfeld','viewBox="0 0 320 324" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gesichtsfeld')
s=s.replace("['toter Winkel',160,312]","['toter Winkel',160,319]")
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-01zzz39'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
