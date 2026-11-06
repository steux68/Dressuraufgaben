# Baender statt Kacheln: (1) Viereck Lernen/Spiel/Geschichte als durchgehendes Band,
# (2) Anatomie-Leiste als Band mit kleinen Flaggen (DE/UK) rechts, ohne Vollbild-Knopf,
# (3) Tippen aufs Bild oeffnet Vollbild, Hinweisband (weiss auf dunkel) oben auf dem Bild.
# Idempotent. 06.11.2026. Aufruf: python3 -I src/band_flags_patch.py [--noversion]
import re, sys

s = open('index.html', encoding='utf-8').read()
if '/* band-flags */' in s:
    print('schon angewendet')
    sys.exit(0)


def rep(old, new):
    global s
    assert s.count(old) == 1, f'{s.count(old)}x statt 1x: {old[:80]}'
    s = s.replace(old, new)


# ---------- Flaggen (Inline-SVG, keine Fremdserver) ----------
DE = ('<svg class="fl" viewBox="0 0 5 3" width="30" height="18" aria-hidden="true"><rect width="5" height="3" fill="#000"/>'
      '<rect y="1" width="5" height="2" fill="#d00"/><rect y="2" width="5" height="1" fill="#ffce00"/></svg>')
UK = ('<svg class="fl" viewBox="0 0 60 30" width="36" height="18" aria-hidden="true"><clipPath id="ukc"><path d="M0 0v30h60V0z"/></clipPath>'
      '<clipPath id="ukt"><path d="M30 15h30v15zv15H0zH0V0zV0h30z"/></clipPath><g clip-path="url(#ukc)"><path d="M0 0v30h60V0z" fill="#012169"/>'
      '<path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" clip-path="url(#ukt)" stroke="#c8102e" stroke-width="4"/>'
      '<path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#c8102e" stroke-width="6"/></g></svg>')

# ---------- Markup der Anatomie-Leiste ----------
rep('<div class="anaSeg" id="aLang"><button data-l="de" type="button">DE</button><button data-l="en" type="button">EN</button></div>'
    '<button id="aNames" type="button" class="abt"></button><button id="aFull" type="button" class="abt"></button></div>\'+\n'
    ' \'<p class="aHint" id="aHint"></p><div class="anaStage" id="aStage">',
    '<button id="aNames" type="button" class="abt"></button>'
    '<div class="anaSeg" id="aLang"><button data-l="de" type="button" aria-label="Deutsch" title="Deutsch">' + DE + '</button>'
    '<button data-l="en" type="button" aria-label="English" title="English">' + UK + '</button></div></div>\'+\n'
    ' \'<div class="anaStage" id="aStage"><div class="aOv" id="aOv" hidden><span class="aHint" id="aHint"></span>'
    '<button id="aFull" type="button" hidden></button></div>')

# ---------- Verhalten ----------
# Hinweisband und Vollbild-Knopf
rep("$('aFull').textContent=full?u.close:u.full;", "$('aFull').textContent=u.close;$('aFull').hidden=!full;")
rep("{const h=$('aHint');h.textContent=u.tip;h.style.visibility=(mode==='lern'&&sel<0&&!full)?'visible':'hidden';}",
    "{const h=$('aHint'),o=$('aOv'),en=lang==='en',D=en?'Tap a dot: description':'Punkt tippen: Beschreibung',F=en?'tap picture: full screen':'Bild tippen: Vollbild';"
    "let x='';if(full)x=mode==='lern'&&P.length?D:'';else if(mode==='lern')x=P.length?D+' · '+F:F;else if(qtype!=='where')x=F;"
    "h.textContent=x;o.hidden=!(full||x);}")
rep("['aLern','aQuiz','aNames','aHint'].forEach(", "['aLern','aQuiz','aNames'].forEach(")
# Tippen aufs Bild (nicht auf einen Punkt) = Vollbild
rep(" sc.addEventListener('touchstart',",
    " sc.addEventListener('click',e=>{if(full||e.target.closest('.ad'))return;if(mode==='quiz'&&qtype==='where'&&!answered)return;setFull(true);});\n"
    " sc.addEventListener('touchstart',")

# ---------- CSS ----------
CSS = '''
/* band-flags */
/* Viereck: Lernen / Spiel / Geschichte als schmales durchgehendes Band (wie Lernen/Quiz bei Sehen, nur ueber die ganze Breite) */
#thVi .viTabs{display:flex;gap:0;justify-content:stretch;padding:0;margin:10px 0 6px;background:#fff;border:0;border-top:1px dotted #b8b8b8;border-bottom:1px dotted #b8b8b8}
#thVi .viTabs button{flex:1 1 0;min-height:30px;padding:5px 0;font-size:.9rem;font-weight:400;color:#444;background:#fff!important;border:0!important;border-left:1px dotted #b8b8b8!important;border-radius:0}
#thVi .viTabs button:first-child{border-left:0!important}
#thVi .viTabs button[aria-pressed="true"]{background:#ffec99!important;color:#111;font-weight:700}
/* Anatomie: Leiste als schmales Band, Flaggen rechts */
.anapop .anaBar{display:flex;flex-wrap:nowrap;align-items:stretch;gap:0;margin:0 -10px;background:#fff;border:0;border-top:1px dotted #b8b8b8;border-bottom:1px dotted #b8b8b8}
.anapop .anaBar .anaSeg{display:contents}
.anapop .anaBar button{flex:1 1 0;min-height:30px;margin:0;padding:5px 6px;font-size:.9rem;font-weight:400;color:#444;background:#fff;border:0;border-left:1px dotted #b8b8b8;border-radius:0}
.anapop .anaBar>button:first-child,.anapop .anaBar #aMode button:first-child{border-left:0}
.anapop .anaBar button[aria-pressed="true"]{background:#ffec99;color:#111;font-weight:700}
.anapop .anaBar #aLang button{flex:0 0 44px;display:flex;align-items:center;justify-content:center;padding:0}
.anapop .anaBar #aLang .fl{display:block;height:14px;width:auto;box-shadow:0 0 0 1px rgba(0,0,0,.3)}
.anapop .anaBar #aLang button[aria-pressed="false"] .fl{opacity:.45}
/* Hinweisband auf dem Bild: weisse Schrift auf dunklem, halbdurchsichtigem Band */
.anapop .aOv{position:absolute;left:0;right:0;top:0;z-index:4;display:flex;justify-content:flex-end;align-items:center;gap:8px;padding:3px 8px;background:rgba(0,0,0,.62);color:#fff;pointer-events:none}
.anapop .aOv[hidden]{display:none}
.anapop .aOv .aHint{margin:0;height:auto;text-align:right;font-size:12px;line-height:18px;color:#fff;letter-spacing:.02em}
.anapop .aOv button{pointer-events:auto;flex:none;min-height:0;margin:0;padding:2px 10px;font-size:12px;line-height:18px;color:#fff;background:transparent;border:1px solid #fff;border-radius:0}
.anapop .aOv button[hidden]{display:none}
.anapop:not(.full) .anaScroll{cursor:zoom-in}
'''
i = s.index('</style>', s.index('.anapop #aCap{display:none}'))
s = s[:i] + CSS + s[i:]

if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-06zzz78' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
