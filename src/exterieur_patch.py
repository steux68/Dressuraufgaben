import re
f='index.html'; s=open(f,encoding='utf8').read()
js=open('src/anatomie.js',encoding='utf8').read()
a=s.index('<script id="ana-js">'); b=s.index('</script>',a)
s=s[:a]+'<script id="ana-js">\n'+js+'\n'+s[b:]
css='''<style id="ext-css">
#aBr,#aBl{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:1}
#aBr[hidden],#aBl[hidden]{display:none}
#aBr path{fill:none;stroke:#e30613;stroke-width:1.6;vector-effect:non-scaling-stroke;stroke-linejoin:round}
.abl{position:absolute;transform:translate(-50%,-100%);margin-top:-3px;font-size:11px;font-weight:700;color:#e30613;white-space:nowrap;background:#ffffffd9;padding:0 3px}
.anaBar+.anaBar{margin-top:-2px}
</style>
'''
s=re.sub(r'<style id="ext-css">.*?</style>\n','',s,flags=re.S)
i=s.rfind('</head>'); s=s[:i]+css+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzp"',s,count=1)
open(f,'w',encoding='utf8').write(s)
