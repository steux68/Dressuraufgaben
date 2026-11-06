# Baender schlicht: aktiv gelb, inaktiv hellgrau, keine Linien; sitzen direkt unter der Linie der Titelleiste.
# Gilt fuer Anatomie-Popup-Leiste, Viereck-Leiste und die Filterleiste (Alle/Koerper/...). 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* bands-grey */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* bands-grey */
.anapop .anaBar,#thVi .viTabs{display:flex;gap:1px;margin:0;padding:0;background:#fff;border:0!important}
.anapop .anaBar button,#thVi .viTabs button{background:#efefef!important;border:0!important;outline:0!important;color:#333;font-size:14px;font-weight:400;min-height:34px;box-shadow:none}
.anapop .anaBar button[aria-pressed="true"],#thVi .viTabs button[aria-pressed="true"]{background:#ffec99!important;color:#111;font-weight:700}
.anapop .anaBar #aLang button[aria-pressed="false"] .fl{opacity:.55}
#thAna .blseg{display:flex;flex-wrap:nowrap;gap:1px;width:100%;margin:2px 0 12px;padding:0;background:#fff;border:0!important}
#thAna .blseg button{flex:1 1 auto;min-width:0;white-space:nowrap;margin:0!important;padding:8px 4px;background:#efefef!important;border:0!important;outline:0!important;border-radius:0;font-size:14px;font-weight:400;color:#333;box-shadow:none}
#thAna .blseg button[aria-pressed="true"]{background:#ffec99!important;color:#111;font-weight:700}
.anapop .tltop{border-top:0}
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06zzz86'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
