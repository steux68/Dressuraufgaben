#!/usr/bin/env python3
"""Zitate (PASSAGE) wie in DOCH!: Liste unveraendert, aber in einer Box (ca. 3,5 Zitate hoch) mit rotem Schieber am rechten Rand,
ohne 'mehr Zitate'; Antippen oeffnet ein Popup im Stil der dasein-design-Popups (W Zaehler E, grosses Bild, Text mit eigenem Schieber).
Dazu: Seite rastet am Abschnittsanfang (Menueleiste) ein. Idempotent. Aus dem Repo-Stamm: python3 src/zitate_box_patch.py"""
f="index.html"
s=open(f,encoding="utf8").read()
if "qbox-css" in s:
    print("already patched"); raise SystemExit
def rep(old,new,n=1):
    global s
    assert s.count(old)==n,(s.count(old),old[:90])
    s=s.replace(old,new)
Z0=s.index('<script id="zitate-js">');Z1=s.index('</script>',Z0)
z=s[Z0:Z1]
def zrep(old,new):
    global z
    assert z.count(old)==1,(z.count(old),old[:90])
    z=z.replace(old,new)
# no cap: the slider replaces 'mehr Zitate'
zrep("const CAP=6,PERSEC=2;","const CAP=1e4,PERSEC=1e4;")
zrep("function render(){let sec='',qi=0;","function render(){VIS=[];let sec='',qi=0;")
zrep("shown++;","shown++;VIS.push(x);")
zrep("""'</div><div class="zql">'+rows.join('')+'</div>'""","""'</div><div class="qbw"><div class="qbs" tabindex="0" role="region" aria-label="Zitate"><div class="zql">'+rows.join('')+'</div></div><div class="qsl" aria-hidden="true"><i></i></div></div>'""")
zrep("Antippen öffnet die Quelle. Bilder","Antippen zeigt Bild und Quelle. Bilder")
zrep("loadPics(c);}\n","""loadPics(c);
    {const sc=c.querySelector('.qbs'),sl=c.querySelector('.qbw>.qsl');if(sc&&sl&&window.qSlider)window.qSlider(sc,sl);}
    c.querySelectorAll('a.zqt').forEach((a,i)=>a.addEventListener('click',e=>{if(e.metaKey||e.ctrlKey||e.shiftKey||e.button)return;e.preventDefault();openQ(i);}));}
""")
popup=r"""
 /* Popup im Stil der dasein-design-Popups */
 const QW='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31"/><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="-9.50" y="0">W</text></svg>',QE='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>',QX='<svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg>';
 let QP=null,qi2=0,qUpd=null,VIS=[];
 function qBuild(){QP=document.createElement('div');QP.className='tlpop qpop';QP.hidden=true;QP.setAttribute('role','dialog');QP.setAttribute('aria-modal','true');QP.setAttribute('aria-label','Zitat');
  QP.innerHTML='<div class="tlcard qv2"><div class="tltop"><span class="qvc"><button type="button" class="qva" id="qw" aria-label="Zurück">'+QW+'</button><span class="count" id="qc"></span><button type="button" class="qva" id="qe" aria-label="Weiter">'+QE+'</button></span><button type="button" class="tlx" id="qx" aria-label="Schließen">'+QX+'</button></div><div class="qvimg" id="qv" aria-hidden="true"></div><div class="qvw"><div class="tlbody" id="qb"></div><div class="qsl" id="qvsl" aria-hidden="true"><i></i></div></div></div>';
  document.body.appendChild(QP);qUpd=window.qSlider?window.qSlider($('qb'),$('qvsl')):null;
  $('qx').onclick=qClose;$('qw').onclick=()=>qGo(-1);$('qe').onclick=()=>qGo(1);QP.addEventListener('click',e=>{if(e.target===QP)qClose();});
  addEventListener('keydown',e=>{if(QP.hidden)return;if(e.key==='Escape')qClose();else if(e.key==='ArrowLeft')qGo(-1);else if(e.key==='ArrowRight')qGo(1);});
  let tx=0,ty=0;QP.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
  QP.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.6)qGo(dx<0?1:-1);},{passive:true});}
 function qPaint(){const x=VIS[qi2];if(!x)return;const w=WIKI[x.who],qv=$('qv');
  qv.classList.remove('has');qv.innerHTML='<i>'+esc(x.ini)+'</i>'+(w?'<img alt="" data-w="'+w.join('|')+'">':'');
  $('qb').innerHTML='<h4>'+esc(x.who)+'</h4><p class="qq">„'+esc(x.q)+'“</p>'+(x.o?'<p class="qo">'+esc(x.o)+'</p>':'')+(x.n?'<p class="qn">'+esc(x.n)+'</p>':'')+'<dl class="qd"><dt>Quelle</dt><dd>'+esc(x.when)+' <a class="wk" href="'+esc(x.u)+'" target="_blank" rel="noopener" aria-label="Quelle öffnen: '+esc(x.who)+'">mehr ↗</a></dd>'+(x.sec?'<dt>Thema</dt><dd>'+esc(x.sec)+'</dd>':'')+(w?'<dt>Bild</dt><dd>Wikipedia / Wikimedia Commons</dd>':'')+'</dl>';
  loadPics(qv);$('qc').innerHTML='Zitate <b>'+(qi2+1)+'</b> / '+VIS.length;$('qb').scrollTop=0;if(qUpd)qUpd();}
 function openQ(i){if(!QP)qBuild();qi2=i;qPaint();QP.hidden=false;}
 function qClose(){if(QP)QP.hidden=true;}
 function qGo(d){const n=VIS.length;qi2=(qi2+n+d)%n;qPaint();}
"""
zrep(" function build(){",popup+" function build(){")
s=s[:Z0]+z+s[Z1:]
# slider helper (global), before zitate-js
helper='''<script id="qslider-js">/* roter Schieber: duenne gepunktete Spur, roter Balken; ziehen oder antippen */
window.qSlider=function(sc,sl){var th=sl.querySelector("i"),dr=false,tH=0;
 function upd(){var h=sc.clientHeight,t=sc.scrollHeight;if(!h||t<=h+2){sl.style.visibility="hidden";return;}sl.style.visibility="visible";var H=sl.clientHeight;tH=Math.max(28,h/t*H);th.style.height=tH+"px";th.style.top=(sc.scrollTop/(t-h))*(H-tH)+"px";}
 function mv(e){var r=sl.getBoundingClientRect(),H=sl.clientHeight,t=sc.scrollHeight,h=sc.clientHeight,k=(e.clientY-r.top-tH/2)/Math.max(1,H-tH);k=Math.max(0,Math.min(1,k));sc.scrollTop=k*(t-h);}
 sl.addEventListener("pointerdown",function(e){dr=true;try{sl.setPointerCapture(e.pointerId);}catch(x){}mv(e);e.preventDefault();});
 sl.addEventListener("pointermove",function(e){if(dr)mv(e);});
 sl.addEventListener("pointerup",function(){dr=false;});sl.addEventListener("pointercancel",function(){dr=false;});
 sc.addEventListener("scroll",upd,{passive:true});window.addEventListener("resize",upd);
 if(window.ResizeObserver){var ro=new ResizeObserver(upd);ro.observe(sc);if(sc.firstElementChild)ro.observe(sc.firstElementChild);}
 upd();return upd;};
</script>
'''
css='''<style id="qbox-css">
.qbw{position:relative}
.qbs{height:min(372px,58svh);overflow-y:auto;scrollbar-width:none;overscroll-behavior-y:auto}
.qbs::-webkit-scrollbar{display:none}
.qbs:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.qbs .zqt>:last-child{padding-right:14px!important}
.qsl{position:absolute;top:0;bottom:0;width:14px;touch-action:none;cursor:pointer;z-index:3}
.qsl::before{content:"";position:absolute;left:6px;top:0;bottom:0;width:1px;background:repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px)}
.qsl i{position:absolute;left:4px;top:0;width:5px;min-height:28px;background:var(--red)}
.qbw>.qsl{right:0;width:10px}.qbw>.qsl::before{left:7px}.qbw>.qsl i{left:5px}
.qv2 .qvc{grid-column:2;display:flex;align-items:center;gap:10px}
.qv2 .qvc .count{font-size:14px;color:#555;letter-spacing:.06em;font-variant-numeric:tabular-nums}.qv2 .qvc .count b{color:var(--red);font-weight:400}
.qv2 .qva{border:0;background:none;padding:6px;margin:-6px 0;display:flex;min-height:0;-webkit-tap-highlight-color:transparent}
.qvimg{flex:none;position:relative;aspect-ratio:1/1;width:min(calc(100% - 24px),34svh);margin:0 auto 10px;background:#f4f4f2;outline:1px dotted #b8b8b8;outline-offset:-1px;display:grid;place-items:center;font-size:34px;font-weight:700;color:var(--ink);overflow:hidden}
.qvimg i{font-style:normal}
.qvimg img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;opacity:0;filter:grayscale(1)}
.qvimg.has img{opacity:1}.qvimg.has i{visibility:hidden}
.qvw{position:relative;flex:1 1 auto;min-height:0;display:flex}
.qpop .qvw .tlbody{flex:1;padding:0 24px 12px 12px;scrollbar-width:none}
.qpop .qvw .tlbody::-webkit-scrollbar{display:none}
.qvw>.qsl{right:6px}
.qpop .tlbody p.qo{font-style:italic;font-size:14px;color:#555}.qpop .tlbody p.qn{font-size:14px;color:#555}
.tlbody dl.qd{margin:6px 0 0;padding-top:8px;display:grid;grid-template-columns:auto 1fr;gap:3px 10px;font-size:12px;line-height:1.35;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left top/100% 1px no-repeat}
.tlbody dl.qd dt{color:#8a8a86}.tlbody dl.qd dd{margin:0;color:#222}
</style>
'''
rep('<script id="zitate-js">',helper+'<script id="zitate-js">')
rep('<script id="vier-js">',css+'<script id="vier-js">')
# auto-snap inside the long-page IIFE
snap=""" /* rastet am Abschnittsanfang ein, wenn das Scrollen aufhoert und ein Anfang nah ist (vorwaerts bis 45 %, zurueck bis 18 % der Hoehe) */
 {let last=SC.scrollTop,dir=0,timer=0,touching=false,busy=0;
  const pts=()=>[0].concat(PAGES.map((_,i)=>Math.round(secTop(i))));
  const settle=()=>{if(touching||HBODY.hidden||document.querySelector('.tlpop:not([hidden])'))return;const y=SC.scrollTop,V=SC.clientHeight,max=SC.scrollHeight-V;let best=null,bd=1e9;
   pts().forEach(p=>{if(p>max+2)return;const d=p-y,a=Math.abs(d);if(a<3)return;const lim=d>0?(dir>=0?.45:.18):(dir<=0?.45:.18);if(a<lim*V&&a<bd){bd=a;best=p;}});
   if(best===null)return;busy=Date.now()+900;SC.scrollTo({top:best,behavior:reduceM?'auto':'smooth'});};
  SC.addEventListener('scroll',()=>{const y=SC.scrollTop;if(y!==last){dir=y>last?1:-1;last=y;}if(Date.now()<busy)return;clearTimeout(timer);timer=setTimeout(settle,160);},{passive:true});
  SC.addEventListener('touchstart',()=>{touching=true;clearTimeout(timer);},{passive:true});
  SC.addEventListener('touchend',()=>{touching=false;clearTimeout(timer);timer=setTimeout(settle,220);},{passive:true});
  SC.addEventListener('touchcancel',()=>{touching=false;},{passive:true});window.__snapSettle=settle;}
"""
anchor=" new ResizeObserver(()=>{lastFit();upd();}).observe(SC);\n"
rep(anchor,anchor+snap)
rep('content="2026-11-11b"','content="2026-11-13a"')
open(f,"w",encoding="utf8").write(s)
print("patched")
