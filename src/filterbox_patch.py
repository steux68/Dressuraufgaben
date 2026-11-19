# Filterboxen einheitlich (wie Pferdewissen): grau, fett, 14 px, 32 px, 2 px Abstand, aktiv lime; Farb-Kacheln 32 px, 2 px Abstand. 19.11.2026.
import re, sys
VER = sys.argv[1]
s = open('index.html', encoding='utf-8').read()
if '/* fbx */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* fbx */
#theo .sub button{min-height:32px!important;line-height:1.2}
.zch{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));gap:2px!important;padding:2px 0 8px}
.zch button{background:#ebebeb!important;color:#222;padding:6px 8px!important;min-height:32px;font-size:14px;font-weight:700!important;line-height:1.2;text-align:left;border:0!important;border-radius:0!important;box-shadow:none!important;min-width:0}
.zch button[aria-pressed="true"]{background:#cdff3e!important}
.wchips:not(.zch){gap:2px!important}
.wchip{height:32px!important;padding:0 8px!important;text-align:left}
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+VER+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
