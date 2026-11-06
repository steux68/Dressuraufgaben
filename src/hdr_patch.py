# Popups beginnen unter der echten Kopfleiste (statt fest 50px), damit das Logo nicht angeschnitten wird. Idempotent. 06.11.2026
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="hdr-js"' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* hdr-follow */
.tlpop,#gpop.tlpop,#pwhat.tlpop{inset:var(--hdr,50px) 0 0 0;--ph:calc(100dvh - var(--hdr,50px))}
'''
i = s.index('</style>', s.index('/* fullscreen-tap */'))
s = s[:i] + CSS + s[i:]
JS = '''<script id="hdr-js">(function(){
var raf=0;function set(){raf=0;var t=document.querySelector('.titlebar');if(!t)return;
 var m=t.getBoundingClientRect().bottom;t.querySelectorAll('*').forEach(function(e){if(e.offsetParent!==null){var b=e.getBoundingClientRect().bottom;if(b>m&&b<200)m=b;}});
 var v=Math.ceil(m)+2;if(v<50)v=50;document.documentElement.style.setProperty('--hdr',v+'px');}
function q(){if(!raf)raf=requestAnimationFrame(set);}
new MutationObserver(q).observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['class','hidden','style']});
addEventListener('resize',q);addEventListener('load',q);if(document.fonts&&document.fonts.ready)document.fonts.ready.then(q);setInterval(q,700);q();
})();</script>
'''
i = s.rindex('</body>')
s = s[:i] + JS + s[i:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-06zzz81' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
