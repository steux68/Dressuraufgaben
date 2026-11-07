# Sehen- und Anatomie-Quiz im Kartenstil (weiss, gepunktete Linie, Neon richtig). Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if '/* quizcards-css */' in s: sys.exit('schon angewendet')
def sel(b): 
    return ','.join(x+b for x in ['#theo #thSee #thVopts','#theo .anaOpts','.anaOpts'])
CSS='/* quizcards-css */\n'
CSS+=','.join(x+' .opt' for x in ['#theo #thSee #thVopts','#theo .anaOpts','.anaOpts'])+'''{height:auto!important;min-height:44px!important;overflow:visible!important;padding:10px 12px!important;font-size:.95rem!important;line-height:1.35!important;color:#222;background:#fff!important;border:0!important;outline:1px dotted #9a9a96;outline-offset:-1px;border-radius:0!important;box-shadow:none!important;text-decoration:none}
'''
CSS+=','.join(x+' .opt span' for x in ['#theo #thSee #thVopts'])+'{display:block!important;-webkit-line-clamp:unset!important;overflow:visible!important}\n'
CSS+='#theo #thSee #thVopts .opt{text-align:left}\n'
CSS+=','.join(x+' .opt:disabled' for x in ['#theo #thSee #thVopts','#theo .anaOpts','.anaOpts'])+'{opacity:1;color:#222}\n'
CSS+=','.join(x+' .opt.ok' for x in ['#theo #thSee #thVopts','#theo .anaOpts','.anaOpts'])+'{background:#cdff3e!important;outline:1px solid #7a9a00;font-weight:700}\n'
CSS+=','.join(x+' .opt.bad' for x in ['#theo #thSee #thVopts','#theo .anaOpts','.anaOpts'])+'{background:#fbe3e1!important;outline:1px dotted #e30613;color:#e30613;text-decoration:none}\n'
CSS+='#theo #thSee #thVopts{gap:6px}\n#theo #thSee #thVfb{margin:10px 0 2px;font-size:.98rem;line-height:1.3;text-transform:none;letter-spacing:0;font-weight:700;color:#1a7f37}\n#theo #thSee .card:has(.opt.bad) #thVfb,#theo #thSee:has(.opt.bad) #thVfb{color:#e30613}\n/* /quizcards-css */\n'
i=s.rindex('</style>')
s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz115'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
