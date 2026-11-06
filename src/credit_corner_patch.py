# Urheberhinweis: senkrecht unten rechts auf der Titelseite, am Seitenende waagrecht (animiert).
# "Was heisst PASSAGE?" nicht mehr auf der Titelseite: 3x auf das PASSAGE-Logo tippen oder Link unter Geschichte. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* credit-corner */' in s:
    print('schon angewendet'); sys.exit(0)
# altes Block-CSS (credit-vert) entfernen
a = s.index('/* credit-vert */'); b = s.index('@media (max-height:700px){footer.copy{', a); b = s.index('\n', b) + 1
s = s[:a] + s[b:]
CSS = '''
/* credit-corner */
#pwhatBtn{display:none!important}
footer.copy{position:fixed;left:auto;top:auto;right:14px;bottom:calc(10px + env(safe-area-inset-bottom,0px));width:var(--cw,270px);height:24px;z-index:46;
 border:0;padding:0;margin:0;display:flex;flex-direction:row;align-items:center;justify-content:center;gap:8px;white-space:nowrap;
 writing-mode:horizontal-tb;transform-origin:100% 100%;transform:translateY(0) rotate(0);opacity:0;pointer-events:none;
 transition:transform .65s cubic-bezier(.4,.1,.2,1),width .65s,right .65s,bottom .65s cubic-bezier(.4,.1,.2,1),opacity .35s}
footer.copy.cv,footer.copy.ch{opacity:1;pointer-events:auto}
footer.copy.ch{right:8px;width:calc(100vw - 16px);border-top:1px dotted #b8b8b8;box-sizing:border-box;height:28px;padding-top:2px;gap:6px;background:#fff}
footer.copy.ch .cimg img{height:13px}
footer.copy.ch span,footer.copy.ch .ilink{font-size:11px}
footer.copy.cv{bottom:var(--cb,150px);transform:translateY(calc(var(--cw,270px) * -1)) rotate(-90deg)}
footer.copy .cimg{position:static;flex:none;width:auto;height:auto;display:block}
footer.copy .cimg img{position:static;display:block;height:20px;width:auto;max-width:none;transform:none}
footer.copy span{font-size:12px;color:var(--muted)}
footer.copy .ilink{margin:0;padding:2px 4px;font-size:12px}
#p-x{padding-bottom:40px!important}
.pwlink{display:block;margin:14px 0 6px;font:inherit;font-size:14px;font-style:italic;color:#0057d8;background:none;border:0;padding:6px 0;cursor:pointer;text-align:left}
@media (max-height:700px){footer.copy{--cw:240px}footer.copy .cimg{display:none}footer.copy span,footer.copy .ilink{font-size:11px}}
'''
JS = '''<script id="credit-corner-js">(function(){var $=function(i){return document.getElementById(i)},f=document.querySelector('footer.copy'),h=$('hscroll'),t=$('p-title');
if(!f||!h||!t)return;
function upd(){var r=t.getBoundingClientRect(),on=r.bottom>innerHeight*.6&&r.top<innerHeight*.4,
 end=h.scrollTop+h.clientHeight>=h.scrollHeight-6&&h.scrollHeight>h.clientHeight+40,ab=document.querySelector('#intro .iabc');
 if(ab){var tp=ab.getBoundingClientRect().top;if(tp>0)f.style.setProperty('--cb',Math.max(60,innerHeight-tp+10)+'px');}
 f.classList.toggle('cv',on);f.classList.toggle('ch',!on&&end);}
upd();h.addEventListener('scroll',upd,{passive:true});document.addEventListener('scroll',upd,true);addEventListener('resize',upd);
[300,1200,2500].forEach(function(ms){setTimeout(upd,ms)});
var br=$('brand'),n=0,t0=0;
if(br)br.addEventListener('click',function(){var now=Date.now();n=(now-t0<900)?n+1:1;t0=now;if(n>=3){n=0;var d=$('pwhat');if(d)d.hidden=false;}},true);
var g=$('p-g');if(g&&!$('pwhatG')){var bt=document.createElement('button');bt.type='button';bt.id='pwhatG';bt.className='pwlink';bt.textContent='Was heißt PASSAGE? ↗';
 bt.onclick=function(){var d=$('pwhat');if(d)d.hidden=false;};g.appendChild(bt);}
})();</script>'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = s.rstrip('\n') + '\n' + JS if '</body>' not in s else s.replace('</body>', JS + '</body>', 1)
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06zzz90'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
