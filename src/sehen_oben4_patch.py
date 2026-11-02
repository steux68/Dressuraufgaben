# Sehen: "Pferd von oben". Nur die Tafel (Fig. 10), keine eigene Zeichnung mehr, keine Punkte.
# Das ganze Pferd liegt im Kreis; die Keile (beide Augen, ein Auge, toter Winkel) gehen von den Augen der Tafel aus
# (Augenreihe der Tafel = Kreismitte). Toter Winkel = einfarbig graue Flaeche. Idempotent. 02.11.2026
import re,sys
from PIL import Image
import numpy as np
# 1) Tafel: Flecken entfernen, linken Ohrrand (3 px abgeschnitten) aus der rechten Seite spiegeln
im=Image.open('img/sehen_oben.png').convert('LA');arr=np.array(im)
from scipy import ndimage
lab,n=ndimage.label(arr[:,:,1]>40)
if n>1:
    sizes=ndimage.sum(arr[:,:,1]>40,lab,range(1,n+1));keep=1+int(np.argmax(sizes))
    arr[:,:,1]=np.where(lab==keep,arr[:,:,1],0)
AX=113.5
if arr[90,73,1]<40:
    for r in range(30,136):
        for x in range(70,77):
            xm=int(round(2*AX-x))
            if arr[r,x,1]<20 and arr[r,xm,1]>60: arr[r,x]=arr[r,xm]
Image.fromarray(arr,'LA').save('img/sehen_oben.png',optimize=True)
# 2) Pferd: ganze Tafel, Augenreihe (Zeile 90) auf Kreismitte (160,150), Achse auf x=160
k=.225
new='''const h=g('thEh');
 el('image',{href:'img/sehen_oben.png',x:%.2f,y:%.2f,width:%.2f,height:%.2f,preserveAspectRatio:'none'},h);
 '''%(160-AX*k,150-90*k,222*k,716*k)
s=open('index.html',encoding='utf-8').read()
a0=s.index("const h=g('thEh');");b0=s.index("const l=g('thEl');",a0)
s=s[:a0]+new+s[b0:]
# 3) toter Winkel: einfarbig grau statt Schraffur
s=s.replace('#thEye .zh,#thEye .zv{fill:url(#thHatch)}','#thEye .zh,#thEye .zv{fill:#8a8a8a;fill-opacity:.38}',1)
# 4) Hoehe und Beschriftung
s=s.replace('viewBox="0 0 320 324" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gesichtsfeld','viewBox="0 0 320 330" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gesichtsfeld',1)
s=s.replace("['toter Winkel',160,319]","['toter Winkel',160,324]").replace("['toter Winkel',160,312]","['toter Winkel',160,324]")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz41'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
