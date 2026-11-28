# Gangarten/Sehen: Pferd von oben (Fig. 10, Tafel img/quellen/pferd_von_oben.jpg) sauber freigestellt, mit Schweif
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
im=Image.open('img/quellen/pferd_von_oben.jpg').convert('L')
c=im.crop((0,20,300,1073));g=np.array(c).astype(float)
# Beschriftung "16'" im Kreuz uebermalen (aus Zeile darueber)
import cv2
g8=g.astype(np.uint8);mk=np.zeros(g8.shape,np.uint8)
y0_,y1_,x0_,x1_=846-20,892-20,152,174
mk[y0_:y1_,x0_:x1_]=255
mk=cv2.dilate(mk,np.ones((3,3),np.uint8))
g=cv2.inpaint(g8,mk,5,cv2.INPAINT_TELEA).astype(float)
b=ndi.gaussian_filter(g,1.5)
m=b<232
m=ndi.binary_opening(m,structure=np.ones((7,7)))
lab,n=ndi.label(m);sz=ndi.sum(m,lab,range(1,n+1));m=lab==(1+int(np.argmax(sz)))
m=ndi.binary_fill_holes(ndi.binary_closing(m,structure=np.ones((5,5))))
m=ndi.binary_erosion(m,iterations=1)
ys,xs=np.where(m);x0,x1,y0,y1=xs.min(),xs.max()+1,ys.min(),ys.max()+1
a=ndi.gaussian_filter(m.astype(float),1.0)
a=(np.clip(a,0,1)*255).astype(np.uint8)
out=Image.merge('LA',(Image.fromarray(g.astype(np.uint8)),Image.fromarray(a))).crop((x0,y0,x1,y1))
print(out.size)
out=out.resize((round(out.width*0.9),round(out.height*0.9)),Image.LANCZOS)
out.save('img/pferd_oben_voll.png',optimize=True);print(out.size)
bg=Image.new('RGB',out.size,(250,250,250));bg.paste(out.convert('RGB'),mask=out.split()[1]);bg.save('/tmp/cut_prev.png')
