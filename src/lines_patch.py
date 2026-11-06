# Linien aufraeumen: Popups deckend weiss (keine Seitenlinien dahinter), ein Strich statt doppelt.
# Idempotent. 06.11.2026. Aufruf: python3 -I src/lines_patch.py [--noversion]
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* lines-clean */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* lines-clean */
.tlpop,#gpop.tlpop,#pwhat.tlpop{background:#fff!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important}
.anapop .tlcard>.anaBar{border-top:0}
.anapop .tltop{border-bottom:0}
.anapop .tlcard>.anaBar{border-top:0!important}
.anapop .anaStage,.anapop .anaScroll{border:0!important;outline:0!important;background:#fff!important}
'''
i = s.rindex('</style>')
s = s[:i] + CSS + s[i:]
JS = '<script id="pop-top">(function(){var was=false;function chk(){var o=[].some.call(document.querySelectorAll(".tlpop"),function(e){return !e.hidden&&getComputedStyle(e).display!=="none"});if(o&&!was)window.scrollTo(0,0);was=o;}new MutationObserver(chk).observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:["class","hidden","style"]});})();</script>\n'
j = s.rindex('</body>')
s = s[:j] + JS + s[j:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06zzz84'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
