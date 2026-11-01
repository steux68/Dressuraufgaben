# Popups 1:1 wie Dasein Design (phone): Panel ab y=50, feste Bildflaeche, Pfeile auf dem Bild, mehr Info
import re
f='index.html'; s=open(f,encoding='utf8').read()
# Galerie: Absatz + Meta-Tabelle
if 'id="gpj"' not in s:
    s=re.sub(r'<div class="mt">.*?</div>',lambda m:'<div class="gtx" id="gpd"></div><div class="mt"><span>Von</span><span id="gpa"></span><span>Werk</span><span id="gpw"></span><span>Jahr</span><span id="gpj"></span><span>Lizenz</span><span id="gpl"></span><span>Thema</span><span id="gpc"></span><span>Bild</span><span id="gpk"></span></div>',s,count=1,flags=re.S)
    old="$('gpw').textContent=x.w+(x.j?', '+x.j:'');$('gpl').textContent=x.l+(x.x?' · '+x.x:'');"
    new="""$('gpw').textContent=x.w;$('gpj').textContent=x.j||'–';$('gpl').textContent=x.l;$('gpc').textContent=(x.c||[]).join(' · ')||'–';$('gpk').textContent=(gi+1)+' von '+GAL.length;
  {const d=$('gpd');d.textContent='';const p1=document.createElement('p');p1.textContent='Aus „'+x.w+'“'+(x.j?' ('+x.j+')':'')+'. Urheber: '+x.a.split(' (')[0]+'.';d.appendChild(p1);if(x.x){const p2=document.createElement('p');p2.textContent=x.x;d.appendChild(p2);}}"""
    assert old in s; s=s.replace(old,new)
css='''/* popfull */
.tlpop,#gpop.tlpop,#pwhat.tlpop{inset:50px 0 0 0;padding:0 8px;align-items:flex-start;--ph:calc(100dvh - 50px);background:rgba(255,255,255,.35);-webkit-backdrop-filter:blur(5px);backdrop-filter:blur(5px)}
.tlpop .tlcard{height:var(--ph);max-width:520px;margin:0 auto;background:rgba(255,255,255,.88);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);box-shadow:none}
.tlpop .tlbody .gfig,.tlpop .tlbody .tlfig,#gpop .gpfig,.anaStage{height:calc(var(--ph) * .47);flex:none}
.anaStage{background:#f6f6f6;outline:1px dotted #b8b8b8;outline-offset:-1px}
.anaStage .anaScroll{border:0;background:transparent}
.tlpop .tlbody{padding:0 10px calc(env(safe-area-inset-bottom,0px) + 40px);gap:6px}
.tlpop .tlbody h4,.tlpop .anaPanel .nm,.tlpop .viT,.tlpop #viPT,#gpop #gpt,#gpop .gpcap b{font-size:18px;line-height:1.15}
.tlpop .tlbody p,.anaPanel .ds,.anaPanel .alt,#gpop .gtx p{font-size:13.5px;line-height:1.36;color:#222;margin:5px 0 0}
#gpop .gtx{display:flex;flex-direction:column}
#gpop .gpcap .mt,.anaDl,.tlpop .anaDl{font-size:12px}
#gpop .gpcap{gap:4px}
#gpop .gpcap .mt{margin-top:6px;padding-top:6px}
.tlpop #viDl{margin-top:8px}
.anapop #aCap{display:none}
/* /popfull */'''
s=re.sub(r'/\* popfull \*/.*?/\* /popfull \*/\n?','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+css+'\n'+s[i:]
open(f,'w',encoding='utf8').write(s)
