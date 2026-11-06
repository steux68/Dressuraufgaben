# PASSAGE: Textoberkante = Fotooberkante, gleicher Abstand 8px in Zitaten und Pferdewissen. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* photo-gap */' in s:
    print('schon angewendet'); sys.exit(0)
CSS='''
/* photo-gap */
.zqt{padding:8px 0!important;min-height:0!important}
.zqt .zpic{margin:0!important}
.zqt>:last-child{padding:0 8px 0 0!important}
.zqt b.who{line-height:1.1;display:block;margin-top:-1px}
#p-w .tile{padding-top:8px!important;padding-bottom:8px!important;min-height:0!important}
#p-w .tile .code{margin:0!important}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06zzz104'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
