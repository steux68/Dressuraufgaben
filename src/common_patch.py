# Audit 27.11., Punkte 7 & 8: gemeinsame common.js (AppBack = Zurück-Taste, AppSwipe = Wischen), gleich in DOCH, PASSAGE & dasein-design.
# PASSAGE: Seiten-Navigation (#r1, #wissen, #galerie …, Galerie-Pop-up, „erst nach oben“) bleibt wie sie ist (das Vorbild).
# Neu: die Pop-ups ohne eigenen Verlaufseintrag (Zeit, Anatomie, Zitate, „P a–x?“ …) schließen zuerst mit Zurück;
# Wischen auf der Lernkarte R1–R6 (nicht beim Zeichnen).
# Aufruf: python3 src/common_patch.py index.html NEUE_VERSION   danach: python3 src/version_sync.py
import sys,re
f,VER=sys.argv[1],sys.argv[2]
s=open(f,encoding='utf-8').read()
if 'src="common.js' not in s:
    m=re.search(r'<meta name="app-version" content="[^"]+">',s);assert m
    s=s[:m.end()]+'<script src="common.js?v=%s"></script>'%VER+s[m.end():]
WIRE='''<script id="common-wire">/* Audit 27.11., Punkte 7 & 8 (common.js): Zurück schließt zuerst ein offenes Pop-up; Wischen auf der Lernkarte */
(function(){if(!window.AppBack||!window.AppSwipe)return;const $=id=>document.getElementById(id),P=AppCommon.press;
 const OWN={gpop:1,gfs:1};   /* Galerie & Vollbild führen ihren Verlauf selbst */
 const dlg=()=>{const a=[].filter.call(document.querySelectorAll('.tlpop:not([hidden]),[role=dialog]:not([hidden])'),e=>!OWN[e.id]&&e.getClientRects().length>0);return a.length?a[a.length-1]:null;};
 AppBack.add({open:()=>!!dlg(),close:()=>{const p=dlg();if(!p)return;const x=p.querySelector('.tlx,[aria-label="Schließen"],[aria-label="schließen"]');if(x)x.click();else p.hidden=true;}}).init();
 /* Lernkarte R1–R6: waagrecht wischen = W/E-Pfeil; nicht beim Zeichnen, nicht im Spiel/Theorie */
 const dz=$('dz'),ln=$('learn');
 AppSwipe(document.querySelector('.app'),{when:()=>view==='test'&&!!ln&&!ln.classList.contains('off')&&!(dz&&dz.dataset.on==='1')&&!dlg()&&$('info').hidden,
  prev:()=>P('pv'),next:()=>P('nx'),ignore:'.titlebar,#seg,.seg,.btns,.tipbar'});
})();</script>'''
if 'id="common-wire"' in s:
    s=re.sub(r'<script id="common-wire">.*?</script>',lambda m:WIRE,s,flags=re.S)
else:
    s=s.rstrip('\n')+'\n'+WIRE+'\n'
s=re.sub(r'(<meta name="app-version" content=")[^"]+(")',lambda m:m.group(1)+VER+m.group(2),s,count=1)
open(f,'w',encoding='utf-8').write(s)
print(f,'ok',VER,'common.js-Tags:',s.count('src="common.js'))
