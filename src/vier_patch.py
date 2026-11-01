import re
f='index.html'; s=open(f,encoding='utf8').read()
def rep(a,b,mark):
    global s
    if mark in s: return
    assert s.count(a)==1,(a,s.count(a)); s=s.replace(a,b)
rep('<button id="thsA" aria-pressed="false">Anatomie</button>\n','<button id="thsA" aria-pressed="false">Anatomie</button>\n<button id="thsB" aria-pressed="false">Viereck</button>\n','id="thsB"')
rep('<div class="tp" id="thAna" hidden aria-label="Anatomie"></div>','<div class="tp" id="thAna" hidden aria-label="Anatomie"></div>\n<div class="tp" id="thVi" hidden aria-label="Das Viereck"></div>','id="thVi"')
rep("'thsA','thsH','thsZ','thsP'],SUBT","'thsA','thsB','thsH','thsZ','thsP'],SUBT",'thsB\',')
rep("SUBG=['thsS','thsV','thsA','thsP']","SUBG=['thsS','thsV','thsA','thsB','thsP']","'thsA','thsB','thsP']")
rep("g('thAna').hidden=which!=='thsA';","g('thAna').hidden=which!=='thsA';g('thVi').hidden=which!=='thsB';","g('thVi').hidden")
rep("['thsP','thsH','thsZ','thsA'].includes(which)","['thsP','thsH','thsZ','thsA','thsB'].includes(which)","'thsA','thsB'].includes")
rep("else if(which==='thsA')anaOpen();","else if(which==='thsA')anaOpen();else if(which==='thsB'&&window.vierOpen)vierOpen();","vierOpen();")
rep("  ['thsP','Pf','Unsere Pferde',","  ['thsB','Vi','Das Viereck','Buchstaben, Maße, Spiel und Geschichte der Bahn'],\n  ['thsP','Pf','Unsere Pferde',","'thsB','Vi'")
rep("thsA:'img/kreis_anatomie.jpg',","thsA:'img/kreis_anatomie.jpg',thsB:'img/kreis_viereck.svg',","thsB:'img/kreis_viereck")
js=open('src/vier.js',encoding='utf8').read()
s=re.sub(r'<script id="vier-js">.*?</script>\n','',s,flags=re.S)
a=s.index('<script id="ana-js">'); s=s[:a]+'<script id="vier-js">\n'+js+'\n</script>\n'+s[a:]
css=open('src/vier.css',encoding='utf8').read()
s=re.sub(r'/\* vier-css \*/.*?/\* /vier-css \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+'/* vier-css */\n'+css+'/* /vier-css */\n'+s[i:]
open(f,'w',encoding='utf8').write(s)
