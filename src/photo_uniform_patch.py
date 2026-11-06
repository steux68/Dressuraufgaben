# PASSAGE: Fotos einheitlich 92px, Abstand oben/unten wie Text, gepunktet statt gestrichelt (Rahmen aussen). 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* photo-uniform */' in s:
    print('schon angewendet'); sys.exit(0)
CSS='''
/* photo-uniform */
.zqt .zpic{box-sizing:border-box;border:1px dotted #b8b8b8;margin:8px 0}
.zqt .zpic::after{display:none!important}
.zqt{min-height:108px!important}
.tlth{box-sizing:border-box;border:1px dotted #b8b8b8}
.tlth::after{display:none!important}
#p-w .tile .code{width:92px!important;height:92px!important;box-sizing:border-box;border:1px dotted #b8b8b8;margin:8px 0;overflow:hidden}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06zzz103'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
