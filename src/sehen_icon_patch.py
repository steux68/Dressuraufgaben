# Sehen-Kachel: Symbol = Gesichtsfeld-Grafik (Kopf von vorn mit toter Winkel / ein Auge / beide Augen) statt Augenschnitt. Idempotent. 03.11.2026
import re,sys,os
from PIL import Image
SRC='/mnt/user-data/attachments/8046c1e5-9810-5025-8ac0-4892ed0066fc/d5fb32ec-image.jpg'
Q='img/quellen/sehen_gesichtsfeld_screenshot.jpg'
if not os.path.exists(Q):
    import shutil;shutil.copy(SRC,Q)
im=Image.open(Q).convert('RGB');w,h=im.size;k=w/990
from PIL import ImageDraw
pale=im.getpixel((round(300*k),round(985*k)));d=ImageDraw.Draw(im)
for x0,x1 in((40,172),(808,940)):
    r=(round(x0*k),round(925*k),round(x1*k),round(1055*k));d.rectangle(r,fill=(255,255,255))
    m=Image.new('L',im.size,0);ImageDraw.Draw(m).ellipse((round(80*k),round(535*k),round(900*k),round(1355*k)),fill=255)
    rm=Image.new('L',im.size,0);ImageDraw.Draw(rm).rectangle(r,fill=255)
    from PIL import ImageChops
    im.paste(pale,mask=ImageChops.multiply(m,rm))
box=(round(60*k),round(520*k),round(920*k),round(1380*k))
im.crop(box).resize((420,420),Image.LANCZOS).save('img/kreis_sehen.jpg',quality=88,optimize=True)
s=open('index.html',encoding='utf-8').read()
s=s.replace("thsV:'img/kreis_auge.jpg'","thsV:'img/kreis_sehen.jpg'")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-03zzz70'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
