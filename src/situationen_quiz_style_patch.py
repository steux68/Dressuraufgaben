# Situationen-Quiz im Stil des Koerpersprache-Quiz: weisse Antwortkarten mit gepunkteter Linie, Neon fuer richtig. Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if '/* sitquiz-css */' in s: sys.exit('schon angewendet')
CSS='''<style id="sitquiz-css">
#thQuest>.score{display:flex;align-items:center;gap:10px;margin:8px 0 0;padding:0 0 8px;border-top:0;font-size:12px;color:#888}
#thQuest>.score select{flex:1 1 auto;min-width:0;height:44px;padding:0 10px;background:#fff;color:#222;border:0;outline:1px dotted #9a9a96;outline-offset:-1px;border-radius:0;font-size:14px}
#thQuest>.score>span{flex:none;white-space:nowrap}
#thQuest #thChap{-webkit-appearance:none;appearance:none;height:44px;padding:0 34px 0 10px;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M5 8l5 5 5-5' fill='none' stroke='%23555' stroke-width='2'/%3E%3C/svg%3E") right 10px center/16px no-repeat!important;border:0!important;outline:1px dotted #9a9a96;outline-offset:-1px;border-radius:0!important;box-shadow:none!important;color:#222;font-size:14px}\n#thQuest .q{margin:10px 0 8px;font-size:1.05rem;line-height:1.3;font-weight:700;color:#111}
#thQuest .opts{gap:6px}
#thQuest .opt{height:auto!important;min-height:44px!important;overflow:visible!important;padding:10px 12px!important;font-size:.95rem!important;line-height:1.35!important;color:#222;background:#fff!important;border:0!important;outline:1px dotted #9a9a96;outline-offset:-1px;border-radius:0!important;box-shadow:none!important;text-align:left}
#thQuest .opt span{display:block!important;-webkit-line-clamp:unset!important;overflow:visible!important}
#thQuest .opt:disabled{opacity:1;color:#222}
#thQuest .opt.ok{background:#cdff3e!important;outline:1px solid #7a9a00;font-weight:700}
#thQuest .opt.bad{background:#fbe3e1!important;outline:1px dotted #e30613;color:#e30613}
#thQuest .fb{margin:10px 0 2px;font-size:.98rem;line-height:1.3;text-transform:none;letter-spacing:0;font-weight:700;color:#1a7f37}
#thQuest .card:has(.opt.bad) .fb{color:#e30613}
#thQuest .why{margin:0 0 4px}
</style>
'''
i=s.rindex('</style>')
s=s[:i]+CSS.replace('<style id="sitquiz-css">','/* sitquiz-css */').replace('</style>\n','/* /sitquiz-css */\n')+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz114'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
