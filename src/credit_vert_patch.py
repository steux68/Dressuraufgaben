# Startseite: Urheberhinweis (Kaefer, (c) Steuart JM HARRISON, Info) senkrecht am linken Rand unter "Was heisst PASSAGE?",
# unten bleiben nur die Reiter (wie bei DOCH! und dasein-design). 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* credit-vert */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* credit-vert */
footer.copy{position:fixed;left:8px;top:calc(50% + var(--head)/2 + 12px);width:22px;height:230px;z-index:46;border:0;padding:0;margin:0;
 writing-mode:vertical-rl;transform:rotate(180deg);display:flex;flex-direction:row;align-items:center;justify-content:flex-end;gap:6px;white-space:nowrap;text-align:left}
footer.copy .cimg{position:relative;flex:none;width:22px;height:57px}
footer.copy .cimg img{position:absolute;left:50%;top:50%;height:20px;width:auto;max-width:none;transform:translate(-50%,-50%) rotate(90deg)}
footer.copy span{font-size:12px;color:var(--muted)}
footer.copy .ilink{margin:0;padding:2px 4px;font-size:12px}
@media (max-height:700px){footer.copy{top:calc(50% + var(--head)/2 + 6px);height:200px}footer.copy .cimg{display:none}footer.copy span,footer.copy .ilink{font-size:11px}}
'''
m = re.search(r'<footer class="copy">(<img [^>]*>)(.*?)</footer>', s, re.S)
assert m
foot = '<footer class="copy"><span class="cimg">' + m.group(1) + '</span>' + m.group(2) + '</footer>'
s = s[:m.start()] + s[m.end():]
k = s.index('id="pwhatBtn"'); k = s.index('</button>', k) + len('</button>')
s = s[:k] + foot + s[k:]
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06zzz89'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
