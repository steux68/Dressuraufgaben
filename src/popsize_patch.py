import re
f='index.html'; s=open(f,encoding='utf8').read()
css='''/* popsize */
.tlpop{--ph:min(calc(100dvh - 28px - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px)),700px)}
.tlpop .tlcard{height:var(--ph);max-height:none;max-width:520px}
.tlpop .tlbody .gfig,.tlpop .tlbody .tlfig{aspect-ratio:auto;height:calc(var(--ph) * .52);flex:none}
#gpop .gpfig{height:calc(var(--ph) * .52)}
.tlpop .gfig .viSvg{position:absolute;inset:0;margin:auto;height:94%;width:auto;max-width:90%;max-height:none;pointer-events:none}
.tlpop .gfig .viSvg .vl{pointer-events:none}
.tlpop .tlar{border-radius:50%!important}
/* /popsize */
'''
s=re.sub(r'/\* popsize \*/.*?/\* /popsize \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
open(f,'w',encoding='utf8').write(s)
