#!/usr/bin/env python3
"""Uebertrag der DOCH!-Designaenderungen vom 23.11.2026 auf PASSAGE a-x (nur Stil, kein Inhalt).
python3 src/doch_uebertrag_patch.py <version> index.html   (idempotent)

1 Reiter (Lernen/Spiel/Theorie, Wissen-Reiter, Unterreiter, Chips): jeder Reiter punktierte Linie oben+unten,
  senkrechter Teiler dazwischen, buendig (0), 23 px; gewaehlt = Lime + fett, ungewaehlt #f2f2f2.
2 Richtig = Lime + fett + Haken; falsch = #fbe3e1 + rot + Kreuz (nicht mehr gruen); Hinweistext ohne Farbwort.
3 CSS dotted/outline dotted -> repeating-linear-gradient.
4 Kleine rote Grossbuchstaben fuer die Kopfzeilen der Theorie-Karte; Selbsttest-Schalter an = Lime.
"""
import sys, re
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
MARK = 'id="doch-uebertrag-css"'
if MARK in s:
    print('schon angewendet'); sys.exit(0)

def rep(a, b):
    global s
    assert s.count(a) == 1, (a, s.count(a))
    s = s.replace(a, b)

# --- Text: kein Farbwort als einziger Hinweis (Steuart ist rot-gruen-blind) ---
rep("'Falsch – richtig ist grün.'", "'Falsch – richtig ist die Antwort mit ✓.'")
rep("$('gq').textContent='Richtig!';$('gq').style.color='var(--ok)'", "$('gq').textContent='Richtig!';$('gq').style.color='#222'")

CSS = r'''<style id="doch-uebertrag-css">
/* 23.11.2026 Uebertrag aus DOCH!: Linien, Auswahl = Fuellung, richtig/falsch farbenblind-sicher */
:root{--dd:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px);--dv:repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px);
 --box:var(--dd) left top/100% 1px no-repeat,var(--dd) left bottom/100% 1px no-repeat,var(--dv) left top/1px 100% no-repeat,var(--dv) right top/1px 100% no-repeat}
/* 1 Reiter */
:is(.seg,#theo .sub,#thVi .viTabs,.anaSeg,.anapop .anaBar){gap:0!important;column-gap:0!important;row-gap:0!important}
:is(.seg,#theo .sub,#thVi .viTabs,.anaSeg,.anapop .anaBar)>button{
 --bt:var(--dd) left top/100% 1px no-repeat;--bb:var(--dd) left bottom/100% 1px no-repeat;--bl:var(--dv) left top/1px 100% no-repeat;--bc:#f2f2f2;
 box-sizing:border-box;height:23px!important;min-height:0!important;margin:0!important;padding:0 10px!important;
 display:flex!important;align-items:center!important;justify-content:flex-start!important;text-align:left!important;
 font-size:12px!important;line-height:1!important;font-weight:400!important;color:#222!important;white-space:nowrap;overflow:hidden;text-transform:none;
 border:0!important;border-radius:0!important;box-shadow:none!important;outline:0!important;
 background:var(--bt),var(--bb),var(--bl),var(--bc)!important}
:is(.seg,#theo .sub,#thVi .viTabs,.anaSeg,.anapop .anaBar)>button[hidden]{display:none!important}
:is(.seg,#theo .sub,#thVi .viTabs,.anaSeg,.anapop .anaBar)>button:first-child{--bl:none}
#theo .sub>button:nth-child(3n+1){--bl:none}
#theo .sub>button:nth-child(n+4){--bt:none}
:is(.seg,#theo .sub,#thVi .viTabs,.anaSeg,.anapop .anaBar)>button[aria-pressed="true"]{--bc:#cdff3e;font-weight:700!important;color:#222!important;background:var(--bt),var(--bb),var(--bl),var(--bc)!important}
.anaSeg.blseg,#thVi .viTabs{margin:8px 0!important}
.anapop .anaBar #aLang>button:first-child{--bl:var(--dv) left top/1px 100% no-repeat}
/* Chip "Masse" (Viereck): gewaehlt = Lime statt Gelb */
#thVi .viChip{height:23px;box-sizing:border-box;padding:0 10px!important;border:0!important;font-size:12px!important;font-weight:400;color:#222!important;background:var(--box),#f2f2f2!important}
#thVi .viChip[aria-pressed="true"]{background:var(--box),#cdff3e!important;font-weight:700}
/* Selbsttest-Schalter: an = Lime + fett */
#qz[aria-pressed="true"]{background:#cdff3e!important;font-weight:700}
/* 2 richtig / falsch: Lime + Haken, rosa + rot + Kreuz */
.opt.ok::after{background:#222!important}
.opt.bad::after{background:#e30613!important}
#opts .opt.ok,#theo .opt.ok{background:#cdff3e!important;box-shadow:none!important;border-color:transparent!important;font-weight:700}
#opts .opt.bad,#theo .opt.bad{box-shadow:none!important;border-color:transparent!important;outline:0;color:#e30613;
 background:repeating-linear-gradient(to right,#e30613 0 1px,transparent 1px 3px) left top/100% 1px no-repeat,repeating-linear-gradient(to right,#e30613 0 1px,transparent 1px 3px) left bottom/100% 1px no-repeat,repeating-linear-gradient(to bottom,#e30613 0 1px,transparent 1px 3px) left top/1px 100% no-repeat,repeating-linear-gradient(to bottom,#e30613 0 1px,transparent 1px 3px) right top/1px 100% no-repeat,#fbe3e1!important}
/* Rueckmeldung: richtig = dunkel (nie gruen), falsch = rot */
#thGame .fb,#thVquiz .fb,#thQuest .fb,#theo #thSee #thVfb{color:#222!important}
#thGame:has(.opt.bad) .fb,#thVquiz:has(.opt.bad) .fb,#thQuest .card:has(.opt.bad) .fb,#theo #thSee:has(.opt.bad) #thVfb{color:#e30613!important}
/* 3 punktiert nur ueber Verlauf, nie CSS dotted */
#theo .zq .zqq.sep{border-top:0!important;background:var(--dd) left top/100% 1px no-repeat}
.qvimg{outline:0!important}
.qvimg::after{content:"";position:absolute;inset:0;pointer-events:none;z-index:3;background:var(--box)}
/* 4 kleine rote Grossbuchstaben fuer Kopfzeilen */
#thCx p b{color:#e30613}
</style>'''
i = s.rindex('</style>') + len('</style>')
s = s[:i] + '\n' + CSS + s[i:]

JS = '''<script id="doch-uebertrag-js">(function(){var q=document.getElementById("qz");if(!q)return;
function sync(){q.setAttribute("aria-pressed",/an$/.test(q.textContent.trim())?"true":"false");}
sync();new MutationObserver(sync).observe(q,{childList:true,characterData:true,subtree:true});})();</script>
'''
assert s.count('</body>') == 1
s = s.replace('</body>', JS + '</body>')

# Version
cur = re.search(r'(<meta name="app-version" content=")([^"]*)(")', s)
assert cur
s = s[:cur.start(2)] + ver + s[cur.end(2):]
open(path, 'w', encoding='utf8').write(s)
print('ok', cur.group(2), '->', ver)
