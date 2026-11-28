# Muybridge Animal Locomotion Plate 619 (gemeinfrei) -> zwei Bildstreifen zum Abspielen (Seitenansicht Galopp, Frontalansicht)
from PIL import Image
im=Image.open('img/galerie/muybridge_reiter.jpg').convert('L')
def cells(y0,y1,x0,x1,n):
    w=(x1-x0)/n;return [im.crop((round(x0+i*w)+3,y0+3,round(x0+(i+1)*w)-3,y1-3)) for i in range(n)]
r1=cells(356,490,297,1327,6);r2=cells(497,628,297,1327,6)
side=(r1[::-1]+r2[::-1])           # Nummerierung 1..6 laeuft in der Reihe von rechts nach links
front=cells(640,797,295,1326,12)[::-1]
def strip(fr,h,name,q=72):
    W=round(fr[0].width*h/fr[0].height);S=Image.new('L',(W*len(fr),h),235)
    for i,f in enumerate(fr):S.paste(f.resize((W,h),Image.LANCZOS),(i*W,0))
    S.save(name,quality=q,optimize=True);print(name,S.size,W)
strip(side,120,'img/anim_galopp_seite.jpg');strip(front,170,'img/anim_front.jpg')
