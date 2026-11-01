# Sehen: "Pferd von oben" mit der alten Tafel (Fig. 10 aus img/quellen/pferd_von_oben.jpg) statt eigener Zeichnung;
# Kopf davor ist eigene Zeichnung (auf der Tafel fehlt der Kopf). Idempotent. 01.11.2026
import re
from PIL import Image, ImageFilter
im=Image.open('img/quellen/pferd_von_oben.jpg').convert('L')
c=im.crop((0,0,296,955))
px=c.load();W,H=c.size
def white(x0,y0,x1,y1):
    for y in range(max(0,y0),min(H,y1)):
        for x in range(max(0,x0),min(W,x1)):px[x,y]=255
white(0,0,104,360);white(0,360,72,560);white(0,800,56,900);white(0,560,50,800)
# Beschriftung "16'" in der Mitte (um 160,865): aus der Zeile darueber uebernehmen
for y in range(852,880):
    for x in range(146,176):px[x,y]=px[x,y-30]
# Papierweiss -> transparent (wie "multiply"): Alpha = Dunkelheit, Farbe = Schwarz
# Koerper als undurchsichtige Silhouette (Papierweiss ausserhalb wird transparent)
from PIL import ImageDraw
bl=c.filter(ImageFilter.GaussianBlur(2)).point(lambda v:255 if v>243 else 0)
ImageDraw.floodfill(bl,(0,0),128,thresh=0);ImageDraw.floodfill(bl,(W-1,0),128,thresh=0)
for yy in (60,200,500,900):
    ImageDraw.floodfill(bl,(0,yy),128,thresh=0) if bl.getpixel((0,yy))==255 else None
    ImageDraw.floodfill(bl,(W-1,yy),128,thresh=0) if bl.getpixel((W-1,yy))==255 else None
a=bl.point(lambda v:0 if v==128 else 255)
a=a.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.8))
out=Image.merge('LA',(c,a)).resize((222,716),Image.LANCZOS)
out.save('img/sehen_oben.png',optimize=True)
S=.155;X0=160-148*S;Y0=163.8-110*S
def half(pts):
    pts=[(x*1.2,150+(y-150)*1.2) for x,y in pts]
    d=[(160+x,y) for x,y in pts]+[(160-x,y) for x,y in pts[::-1]]
    p='M%.1f,%.1f'%d[0]
    for i in range(len(d)-1):
        p0=d[max(i-1,0)];p1=d[i];p2=d[i+1];p3=d[min(i+2,len(d)-1)]
        p+='C%.1f,%.1f %.1f,%.1f %.1f,%.1f'%(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6,p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6,p2[0],p2[1])
    return p+'Z'
head=half([(0,129),(2.6,129.4),(4.4,132),(5,137),(6,143),(7.6,148),(8.2,152),(7.6,158),(7,164),(6,170)])
new='''const h=g('thEh');
 el('path',{d:'%s',fill:'url(#thHg)',stroke:'#555','stroke-width':.5},h);
 el('image',{href:'img/sehen_oben.png',x:%.2f,y:%.2f,width:%.2f,height:%.2f,preserveAspectRatio:'none'},h);
 el('circle',{cx:150.4,cy:150,r:2,fill:'#111'},h);el('circle',{cx:169.6,cy:150,r:2,fill:'#111'},h);
 el('ellipse',{cx:156.9,cy:126,rx:1.1,ry:1.5,fill:'#333'},h);el('ellipse',{cx:163.1,cy:126,rx:1.1,ry:1.5,fill:'#333'},h);
 '''%(head,X0,Y0,296*S,955*S)
s=open('index.html',encoding='utf-8').read()
a0=s.index("const h=g('thEh');");b0=s.index("const l=g('thEl');",a0)
s=s[:a0]+new+s[b0:]
if 'id="thHg"' not in s:
    s=s.replace('</pattern></defs><g id="thEz">','</pattern><linearGradient id="thHg" x1="0" x2="1"><stop offset="0" stop-color="#8f8f8f"/><stop offset=".5" stop-color="#bdbdbd"/><stop offset="1" stop-color="#8f8f8f"/></linearGradient></defs><g id="thEz">',1)
# Beschriftung und Hoehe
s=s.replace('viewBox="0 0 320 320" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gesichtsfeld','viewBox="0 0 320 324" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gesichtsfeld')
s=s.replace("['toter Winkel',160,312]","['toter Winkel',160,319]")
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-01zzz38'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
