# Lernen-Ansicht: runde W/E-Pfeile links/rechts in der Mitte des Vierecks (wie in den Popups) statt der Knöpfe Zurück/Weiter.
# Die Originalknöpfe #pv/#nx bleiben versteckt im Code, die Pfeile klicken sie. Idempotent. 25.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="lnpf-css"' in s: sys.exit('schon angewendet')

# Pfeil-Symbole aus der App übernehmen (identisch zu den Popups)
w=re.search(r"const WSVG='(.*?)';",s); e=re.search(r"const ESVG='(.*?)';",s)
assert w and e
WS,ES=w.group(1),e.group(1)

old='<div class="stage" id="stage">\n'
assert s.count(old)==1
new=(old+'<button type="button" class="tlar pw" id="lnA" aria-label="Zurück">'+WS+'</button>'
        '<button type="button" class="tlar pe" id="lnE" aria-label="Weiter">'+ES+'</button>\n')
s=s.replace(old,new,1)

CSS='''<style id="lnpf-css">
/* Lernen: Pfeile auf dem Viereck, kein Knopf Zurück/Weiter mehr (25.11.) */
#stage{position:relative}
#pv,#nx{display:none!important}
body:has(#learn.off) #lnA,body:has(#learn.off) #lnE{display:none}
.panels:has(#learn:not(.off)){height:166px}
@media (max-height:720px){.panels:has(#learn:not(.off)){height:152px}}
#lnA,#lnE{z-index:3;border-radius:50%!important}
#lnA{left:2px}#lnE{right:2px}
</style>
'''
i=s.rindex('</style>')+len('</style>')
s=s[:i]+'\n'+CSS+s[i:]

JS='''<script id="lnpf-js">
(function(){var a=document.getElementById('lnA'),e=document.getElementById('lnE');
if(!a||!e)return;
a.addEventListener('click',function(){document.getElementById('pv').click()});
e.addEventListener('click',function(){document.getElementById('nx').click()});
})();
</script>
'''
k=s.rfind('</body>')
assert k>0
s=s[:k]+JS+s[k:]

if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-25f'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
print('ok')
