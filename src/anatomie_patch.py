import re,sys
f='index.html'; s=open(f,encoding='utf8').read()
if 'id="thAna"' in s: sys.exit('schon angewendet')
def rep(a,b):
    global s
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
rep('<button id="thsV" aria-pressed="false">Sehen</button>','<button id="thsV" aria-pressed="false">Sehen</button>\n<button id="thsA" aria-pressed="false">Anatomie</button>')
rep('<div class="tp" id="thHist" hidden>','<div class="tp" id="thAna" hidden aria-label="Anatomie"></div>\n<div class="tp" id="thHist" hidden>')
rep("'thsS','thsV','thsH','thsZ','thsP'],SUBT","'thsS','thsV','thsA','thsH','thsZ','thsP'],SUBT")
rep("SUBG=['thsS','thsV','thsP']","SUBG=['thsS','thsV','thsA','thsP']")
rep("g('thHorse').hidden=which!=='thsP';","g('thHorse').hidden=which!=='thsP';g('thAna').hidden=which!=='thsA';if(which!=='thsA'&&window.anaClose)anaClose();")
rep("['thsP','thsH','thsZ'].includes(which)","['thsP','thsH','thsZ','thsA'].includes(which)")
rep("else if(which==='thsP')horses();else if(!wip)","else if(which==='thsP')horses();else if(which==='thsA')anaOpen();else if(!wip)")
rep("  ['thsP','Pf','Unsere Pferde',","  ['thsA','An','Anatomie','Skelett des Pferdes: Knochen benennen, Quiz (Deutsch / English)'],\n  ['thsP','Pf','Unsere Pferde',")
css=open('src/anatomie.css',encoding='utf8').read()
js=open('src/anatomie.js',encoding='utf8').read()
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
i=s.rfind('</body>'); s=s[:i]+'<script id="ana-js">\n'+js+'\n</script>\n'+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-10-31w"',s,count=1)
open(f,'w',encoding='utf8').write(s)
