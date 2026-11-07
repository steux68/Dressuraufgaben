# Pferdewissen-Kacheln: Vorschaubild = Ausschnitt aus dem echten Hauptbild; Titel oben buendig mit dem Foto; 8px Abstand oben/unten. Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="wthumbs-css"' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:60]
    s=s.replace(old,new,1)
# 1. Ausschnitt statt verkleinertem Bild
rep("{const KB={thsV:'img/kreis_sehen.jpg',thsA:'img/kreis_anatomie.jpg',thsB:'img/kreis_viereck.svg',thsP:'img/kreis_pferde.jpg'}[id];",
    "{const KB={thsV:'img/kreis_sehen.jpg',thsA:'img/skelett.jpg',thsB:'img/viereck_real.svg',thsP:'img/kreis_pferde.jpg'}[id];const CR={thsA:'#fff url(img/skelett.jpg) 0% 4%/300% no-repeat',thsB:'#fff url(img/viereck_real.svg) 22% 58%/185% no-repeat',thsV:'#fff url(img/sehen_real.svg) 50% 50%/118% no-repeat'}[id];")
rep("cd.style.setProperty('background','#fff url('+KB+') center/'+(KB.slice(-4)==='.svg'?'118%':'cover')+' no-repeat','important');}}",
    "cd.style.setProperty('background',CR||('#fff url('+KB+') center/cover no-repeat'),'important');}}")
CSS='''<style id="wthumbs-css">
#p-w{gap:0!important}
#p-w .tline.intro{margin-bottom:8px!important}
#p-w .tile{align-items:start!important}
#p-w .tile .nm{line-height:1.1;margin-top:-1px}
#p-w .tile .st{align-self:center}
</style>
'''
assert s.count('</head>')==1
s=s.replace('</head>',CSS+'</head>',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz108'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
