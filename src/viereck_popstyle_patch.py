# Viereck-Spiel im Popup-Look (roter Grossbuchstaben-Titel, gepunktete Punktezeile, Rueckmeldung in Rot). Nur CSS. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if '/* Viereck-Spiel Popup-Look */' not in s:
    css='''
/* Viereck-Spiel Popup-Look */
#thVi .viQ{text-align:left;margin:2px 0 0;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
#thVi .viBar{min-height:0;padding:0 4px;border-bottom:1px dotted #b8b8b8;padding-bottom:6px}
#thVi .viScore{font-size:12px;color:#888}
#thVi .viFb,#thVi .viFb.ok,#thVi .viFb.bad{color:#e30613;text-transform:uppercase;font-size:1.15rem;line-height:1.15;letter-spacing:.01em}
'''
    i=s.index('</style>',s.index('#thVi .viOpt{font-size:1.05rem'))
    s=s[:i]+css+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda mm:mm.group(1)+'2026-11-02zzz58'+mm.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
