# Freistellen einer Zeichnung (heller Papiergrund) -> PNG mit Alpha. Aufruf: python3 -I src/rasse_cut.py quelle.jpg ziel.png [schwelle] [ymax]
import sys,numpy as np,cv2
from PIL import Image
from scipy import ndimage as ndi
src,dst=sys.argv[1],sys.argv[2];thr=float(sys.argv[3]) if len(sys.argv)>3 else 200;ymax=int(sys.argv[4]) if len(sys.argv)>4 else 10**6
im=Image.open(src).convert('RGB');a=np.array(im).astype(float);L=a.mean(2)
m=ndi.gaussian_filter(L,1.2)<thr;m[ymax:]=False
m=ndi.binary_opening(m,structure=np.ones((3,3)))
lab,n=ndi.label(m);sz=ndi.sum(m,lab,range(1,n+1));m=lab==(1+int(np.argmax(sz)))
m=ndi.binary_fill_holes(ndi.binary_closing(m,structure=np.ones((7,7))))
al=(ndi.gaussian_filter(m.astype(float),1.1)*255).clip(0,255).astype(np.uint8)
ys,xs=np.where(m);box=(xs.min(),ys.min(),xs.max()+1,ys.max()+1)
out=Image.fromarray(np.dstack([np.array(im),al]),'RGBA').crop(box)
w=700;out=out.resize((w,round(out.height*w/out.width)),Image.LANCZOS);out.save(dst,optimize=True);print(out.size)
bg=Image.new('RGB',out.size,(250,250,250));bg.paste(out.convert('RGB'),mask=out.split()[3]);bg.save('/tmp/cut_prev.png')
