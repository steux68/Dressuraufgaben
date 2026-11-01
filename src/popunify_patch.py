import re
f='index.html'; s=open(f,encoding='utf8').read()
WSVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31"/><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="-9.50" y="0">W</text></svg>'
ESVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>'
XSVG='<svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg>'
# --- Galerie-Popup
new=('<div class="gpop tlpop" id="gpop" hidden role="dialog" aria-modal="true" aria-label="Bild"><div class="tlcard"><div class="tltop"><span class="tlk" id="gpn"></span><button type="button" class="tlx" id="gpx" aria-label="Schließen">'+XSVG+'</button></div>'
 '<div class="tlbody"><figure class="gfig has gpfig"><img id="gpi" alt=""><button type="button" class="tlar pw" id="gpp" aria-label="Zurück">'+WSVG+'</button><button type="button" class="tlar pe" id="gpf" aria-label="Weiter">'+ESVG+'</button></figure>'
 '<div class="gpcap"><b id="gpt"></b><span id="gpa"></span><span id="gpw"></span><span id="gpl"></span><a id="gpu" target="_blank" rel="noopener">mehr ↗</a></div></div></div></div>')
if 'class="gpop tlpop"' not in s:
    a=s.index('<div class="gpop"');e=s.index('</div></div>',s.index('class="gpnav"',a))+len('</div></div>')
    s=s[:a]+new+s[e:]
s=s.replace("$('gpn').textContent='Galerie · '+(gi+1)+' / '+GAL.length;","$('gpn').innerHTML='Galerie <b>'+String(gi+1).padStart(2,'0')+'</b> / '+GAL.length;")
s=s.replace("document.querySelector('.gpnav').hidden=GAL.length<2;}","$('gpp').hidden=$('gpf').hidden=GAL.length<2;}")
# --- Was heißt PASSAGE
i=s.index('<div id="pwhat"'); j=s.index('<script id="pwhat-js">')
old=s[i:j]
if 'class="tlpop"' not in old:
    ps=re.findall(r'<p>.*?</p>',old,flags=re.S)
    href=re.search(r'href="([^"]+)"',old).group(1)
    nw=('<div id="pwhat" class="tlpop" role="dialog" aria-modal="true" aria-labelledby="pwhatH" hidden><div class="tlcard"><div class="tltop"><span class="tlk" id="pwhatH">Was heißt PASSAGE?</span><button type="button" class="tlx" id="pwhatX" aria-label="Schließen">'+XSVG+'</button></div>'
        '<div class="tlbody">'+''.join(ps)+'<p><a class="wk" href="'+href+'" target="_blank" rel="noopener">Beispiel ansehen ↗</a></p></div></div></div>')
    s=s[:i]+nw+s[j:]
# altes pwhat-CSS (Dialog) entfernen, Knopf-CSS behalten
i=s.index('<style id="pwhat-css">'); j=s.index('</style>',i)
t=s[i:j]
if '#pwhat{position:fixed' in t:
    t=t[:t.index('#pwhat{position:fixed')]
    s=s[:i]+t+s[j:]
css='''/* popunify */
#gpop.tlpop{background:rgba(255,255,255,.62);padding:calc(env(safe-area-inset-top,0px) + 14px) 12px calc(env(safe-area-inset-bottom,0px) + 14px);display:flex;z-index:70}
#gpop.tlpop[hidden]{display:none}
#gpop .tlbody{gap:8px}
#gpop .gpfig{aspect-ratio:auto;height:min(46vh,calc(100vw - 48px));background:#f6f6f6}
#gpop .gpfig img{opacity:1;max-width:none}
#gpop .tlar[disabled]{opacity:.28}
#gpop .tlar{background:rgba(255,255,255,.82)!important;border:0!important;border-radius:50%!important;width:42px;height:42px;padding:0}
.tlpop .tlx:focus,.tlpop .tlx:focus-visible{outline:none}
.tlpop .tlar{border-radius:50%!important}
#gpop .gpcap{background:none;padding-top:0;display:flex;flex-direction:column;gap:2px}
#gpop .gpcap b{font-size:1.05rem}
#gpop .gpcap span{font-size:.84rem}
#pwhat.tlpop{z-index:100000}
#pwhat .tlk{grid-column:2;font-size:13px}
.tlcard>.tlsc{position:absolute;left:50%;bottom:10px;transform:translateX(-50%);z-index:4;display:flex;flex-direction:column;align-items:center;gap:1px;border:0;background:rgba(255,255,255,.9);padding:4px 10px 3px;min-height:0;font:inherit;font-size:11px;letter-spacing:.06em;color:#666;-webkit-tap-highlight-color:transparent}
.tlcard>.tlsc[hidden]{display:none}
.tlsc svg{width:26px;height:26px;overflow:visible}.tlsc .rg{fill:none;stroke:#3a3c37;stroke-width:1px}.tlsc .dt{fill:#4d4f4a;stroke:#1a1a1a;stroke-width:1px;stroke-linejoin:round}
@media (prefers-reduced-motion:no-preference){.tlsc svg{animation:tlscb 1.8s ease-in-out infinite}}
@keyframes tlscb{50%{transform:translateY(3px)}}
.anapop.full .tlsc{display:none}
/* /popunify */
'''
s=re.sub(r'/\* popunify \*/.*?/\* /popunify \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
js='''<script id="popscroll-js">(function(){
var ARW='<svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="dt" transform="rotate(90)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/></svg>';
var raf=0;function upd(){raf=0;document.querySelectorAll('.tlpop:not([hidden])').forEach(function(p){
 var b=p.querySelector('.tlbody'),c=p.querySelector('.tlcard');if(!b||!c)return;
 var s=c.querySelector(':scope>.tlsc');
 if(!s){s=document.createElement('button');s.type='button';s.className='tlsc';s.setAttribute('aria-label','Nach unten scrollen');s.innerHTML=ARW+'<span>scroll</span>';
  s.addEventListener('click',function(){var bb=c.querySelector('.tlbody');bb.scrollBy({top:Math.max(120,bb.clientHeight*.8),behavior:'smooth'});});
  b.addEventListener('scroll',q,{passive:true});c.appendChild(s);}
 var h=!(b.scrollHeight-b.scrollTop-b.clientHeight>8);if(s.hidden!==h)s.hidden=h;});}
function q(){if(!raf)raf=requestAnimationFrame(upd);}
new MutationObserver(q).observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['hidden','class']});
addEventListener('resize',q);document.addEventListener('load',q,true);setInterval(q,700);q();
})();</script>
'''
s=re.sub(r'<script id="popscroll-js">.*?</script>\n','',s,flags=re.S)
s=s.replace('</body></html>',js+'</body></html>',1) if '</body></html>' in s else s+js
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzz15"',s,count=1)
open(f,'w',encoding='utf8').write(s)
