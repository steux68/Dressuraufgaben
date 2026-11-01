# Popups im Dasein-Design-Standard: grosses Bild, Pfeile darueber, roter Titel in Grossbuchstaben, Meta-Tabelle
import re
f='index.html'; s=open(f,encoding='utf8').read()
new_cap='<div class="gpcap"><b id="gpt"></b><div class="mt"><span>Von</span><span id="gpa"></span><span>Werk</span><span id="gpw"></span><span>Lizenz</span><span id="gpl"></span></div><a id="gpu" target="_blank" rel="noopener">mehr ↗</a></div></div></div>'
s=re.sub(r'<div class="gpcap">.*?</div></div></div>',lambda m:new_cap,s,count=1,flags=re.S) if 'class="mt"' not in s else s
css='''/* popstd */
.tlpop .tlbody .gfig,.tlpop .tlbody .tlfig,#gpop .gpfig{height:calc(var(--ph) * .56)}
.tlpop .tlbody{padding:0 12px 44px;gap:8px}
.tlpop .tlar{z-index:20;width:42px;height:42px}
.tlpop .tlbody h4,.tlpop .anaPanel .nm,.tlpop .viT,.tlpop #viPT,#gpop #gpt{margin:0;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
.tlpop .tlbody p{font-size:.98rem;line-height:1.45;color:#222}
#gpop .gpcap{gap:8px}
#gpop .gpcap b{font-size:1.35rem}
#gpop .gpcap .mt{display:grid;grid-template-columns:auto 1fr;gap:3px 14px;border-top:1px dotted #b8b8b8;padding-top:8px;font-size:.88rem;line-height:1.35}
#gpop .gpcap .mt span:nth-child(odd){color:#8a8a86}
#gpop .gpcap .mt span:nth-child(even){color:#111}
#gpop .gpcap a{align-self:flex-start;margin-top:2px}
/* /popstd */'''
s=re.sub(r'/\* popstd \*/.*?/\* /popstd \*/\n?','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+css+'\n'+s[i:]
open(f,'w',encoding='utf8').write(s)
# Anatomie: Pfeile ueber dem Bild
a=open('src/anatomie.js',encoding='utf8').read()
a=a.replace('bw=st.clientWidth-76','bw=st.clientWidth-4'); open('src/anatomie.js','w',encoding='utf8').write(a)
a=open('src/anatomie.js',encoding='utf8').read()
a=a.replace("const st=$('aStage'),bw=st.clientWidth-4,bh=st.clientHeight-4;f.style.maxWidth='none';f.style.width=Math.max(60,Math.round(Math.min(bw,bh*W/H)))+'px';","const st=$('aStage');st.style.height='';const bw=st.clientWidth-4,bh=st.clientHeight-4;f.style.maxWidth='none';const fw=Math.max(60,Math.round(Math.min(bw,bh*W/H)));f.style.width=fw+'px';st.style.height=(Math.round(fw*H/W)+6)+'px';")
open('src/anatomie.js','w',encoding='utf8').write(a)
c=open('src/anatomie2.css',encoding='utf8').read()
c=c.replace('height:calc(var(--ph) * .46)','height:calc(var(--ph) * .56)'); open('src/anatomie2.css','w',encoding='utf8').write(c)
