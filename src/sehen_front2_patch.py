# Sehen: "Der Kopf von vorn" mit dem Kopf aus der Anatomie (img/kopf.jpg) statt eigener Zeichnung. Idempotent. 02.11.2026
from PIL import Image, ImageDraw, ImageFilter
import re
im=Image.open('img/kopf.jpg').convert('L');W,H=im.size
bw=im.filter(ImageFilter.GaussianBlur(3)).point(lambda v:255 if v>245 else 0)
for pt in [(0,0),(W-1,0),(0,H-1),(W-1,H-1),(0,H//2),(W-1,H//2),(W//2,0)]:
    if bw.getpixel(pt)==255: ImageDraw.floodfill(bw,pt,128,thresh=0)
a=bw.point(lambda v:0 if v==128 else 255).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
Image.merge('LA',(im,a)).resize((540,824),Image.LANCZOS).save('img/sehen_kopf.png',optimize=True)
s=open('index.html',encoding='utf-8').read()
a0=s.index('<g id="thEf" style="display:none">');b0=s.index('<g id="thEl">',a0)
# Augen des Bildes (240/830 | 630 von 1080x1648) auf die Augenpunkte (136/184 | 126)
new='<g id="thEf" style="display:none"><image href="img/sehen_kopf.png" x="116.5" y="74.7" width="87.9" height="134.1" preserveAspectRatio="none"/></g>'
s=s[:a0]+new+s[b0:]
open('index.html','w',encoding='utf-8').write(s)
