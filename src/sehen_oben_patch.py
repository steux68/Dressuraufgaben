# Sehen: bessere eigene Zeichnung "Pferd von oben" (Ohren, Hals mit Maehne, Schulter, Kruppe, Schweif). Idempotent. 01.11.2026
import re
P='index.html';s=open(P,encoding='utf-8').read()
def cr(pts):
    # Catmull-Rom -> Bezier, offene Kurve
    d='M%.1f,%.1f'%pts[0]
    for i in range(len(pts)-1):
        p0=pts[max(i-1,0)];p1=pts[i];p2=pts[i+1];p3=pts[min(i+2,len(pts)-1)]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6);c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+='C%.1f,%.1f %.1f,%.1f %.1f,%.1f'%(c1+c2+p2)
    return d
R=[(0,108),(5,108.5),(9,112),(11.5,119),(14,129),(16,139),(15.5,148),(12,156),(11,166),(13.5,176),(16,189),(19,202),(24,213),(30,221),(32,232),(31,244),(29,254),(27,262),(30,268),(31,276),(27,284),(18,289),(8,291),(0,291.5)]
right=[(160+x,y) for x,y in R]
left=[(160-x,y) for x,y in R][::-1]
body=cr(right)+cr(left[:1]+left[1:])[len('M%.1f,%.1f'%left[0]):]
# zweiter Teil: von rechts unten (0,291.5) nach links hoch: left liegt schon umgekehrt; Kurve ab left[0]=(160,291.5)
body=cr(right)+'C'+cr(left)[len('M%.1f,%.1f'%left[0])+1:]+'Z'
body=cr(right)+cr(left).replace('M','L',1)+'Z'
def mir(f):return f
ear=lambda sg:'M%.1f,157C%.1f,150 %.1f,144 %.1f,140C%.1f,146 %.1f,152 %.1f,157Z'%(160+sg*5,160+sg*5.5,160+sg*8.2,160+sg*9,160+sg*11.5,160+sg*11.8,160+sg*11)
mane=''.join('M%.1f,%d l%.1f,3'%(160-.5,y,1.6*(1 if i%2 else 1)) for i,y in enumerate(range(160,214,5)))
new='''const h=g('thEh');
 el('path',{class:'hz',d:'M157,289C156,294 157,299 160,301C163,299 164,294 163,289Z'},h);
 el('path',{class:'hz',d:'%s'},h);
 el('path',{class:'hz',d:'%s'},h);el('path',{class:'hz',d:'%s'},h);
 el('path',{d:'M160,160L160,286',fill:'none',stroke:'var(--muted)','stroke-width':1.2,'stroke-dasharray':'1.5 4','stroke-linecap':'round'},h);
 el('path',{d:'M153,166C151,178 152,196 154,214M167,166C169,178 168,196 166,214',fill:'none',stroke:'var(--muted)','stroke-width':1,'stroke-linecap':'round'},h);
 el('path',{d:'M138,222C142,232 148,242 154,246M182,222C178,232 172,242 166,246M134,268C140,262 148,262 154,266M186,268C180,262 172,262 166,266',fill:'none',stroke:'var(--muted)','stroke-width':1,'stroke-linecap':'round'},h);
 el('circle',{cx:144.6,cy:138,r:2.4,fill:'var(--fg)'},h);el('circle',{cx:175.4,cy:138,r:2.4,fill:'var(--fg)'},h);
 el('path',{d:'M155,113C158,112 162,112 165,113',fill:'none',stroke:'var(--fg)','stroke-width':1.2,'stroke-linecap':'round'},h);
 '''%(body,ear(-1),ear(1))
a=s.index("const h=g('thEh');");b=s.index("const l=g('thEl');",a)
s=s[:a]+new+s[b:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-01zzz38'+m.group(3),s,count=1)
open(P,'w',encoding='utf-8').write(s)
