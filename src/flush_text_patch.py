# PASSAGE: wie dasein-design – Text buendig, Zitat-Fotos buendig mit gepunktetem Rahmen. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* flush-text */' in s:
    print('schon angewendet'); sys.exit(0)
CSS='''
/* flush-text */
.lkhead{padding-left:0!important;padding-right:0!important}
.zqt{padding:0!important;grid-template-columns:92px minmax(0,1fr)!important;align-items:start!important;min-height:92px;gap:10px!important}
.zqt .zpic{width:92px!important;height:92px!important}
.zqt .zpic::after{content:"";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}
.zqt>:last-child{padding:8px 8px 8px 0}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06zzz102'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
