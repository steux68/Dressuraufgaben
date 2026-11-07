# Situationen: Infokarte "Wenn das Pferd erschrickt" (aufklappbar, ueber dem Quiz). Eigene Worte nach allgemeinen Verhaltensratgebern. Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="schreck"' in s: sys.exit('schon angewendet')
ROWS=[
('Warum es erschrickt','Das Pferd ist ein Fluchttier. Plötzliche Geräusche, flatternde Dinge oder schnelle Bewegungen lösen den Fluchtreflex aus, noch bevor es nachdenkt.'),
('Warnzeichen','Kopf hoch, Hals gespannt, die Ohren zeigen auf das Geräusch, das Weiße im Auge ist zu sehen, die Nüstern sind weit, die Atmung ist schnell, der Schweif ist eingeklemmt.'),
('Tote Winkel','Direkt hinter dem Pferd und direkt vor seiner Nase sieht es nichts. Von dort nie schnell oder ohne Ansprache kommen.'),
('Ruhig bleiben','Pferde spüren deine Anspannung. Leise und gleichmäßig sprechen, ruhig atmen, keine hektischen Bewegungen.'),
('Wo du stehst','Neben der Schulter, nie direkt hinter dem Pferd und nie zwischen Pferd und Wand oder Zaun. Den Strick nie um die Hand wickeln.'),
('Platz zum Ausweichen','Nicht festhalten und nicht in die Enge treiben. Ein eingeengtes Pferd drängt oder tritt. Gib ihm Raum, bis es sich beruhigt, und hol Hilfe.'),
('Im Sattel','Ruhig sitzen bleiben, Zügel aufnehmen, durchparieren. Nicht festklammern und nicht an den Zügeln reißen.')]
dl=''.join('<dt>%s</dt><dd>%s</dd>'%r for r in ROWS)
HTML='<details class="schreck" id="schreck"><summary>Wenn das Pferd erschrickt</summary><dl class="schdl">'+dl+'</dl><p class="schnote">Entwurf, mit Reitlehrer abgleichen. Nach allgemeinen Verhaltensratgebern, in eigenen Worten.</p></details>\n'
a='<div class="card">\n<div class="top"><span class="badge" id="thQch">'
assert s.count(a)==1
s=s.replace(a,HTML+a,1)
CSS='''/* schreck-css */
#thQuest{overflow-y:auto}
#thQuest .schreck{margin:0 0 8px}
#thQuest .schreck summary{list-style:none;display:flex;align-items:center;justify-content:space-between;min-height:44px;padding:0 12px;background:#fff;outline:1px dotted #9a9a96;outline-offset:-1px;font-weight:700;font-size:.95rem;color:#111;cursor:pointer}
#thQuest .schreck summary::-webkit-details-marker{display:none}
#thQuest .schreck summary::after{content:"";width:16px;height:16px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M5 8l5 5 5-5' fill='none' stroke='%23555' stroke-width='2'/%3E%3C/svg%3E") center/16px no-repeat;transition:transform .15s}
#thQuest .schreck[open] summary::after{transform:rotate(180deg)}
#thQuest .schreck[open] summary{background:#cdff3e}
#thQuest .schdl{margin:8px 0 0;display:flex;flex-direction:column;gap:0}
#thQuest .schdl dt{margin:8px 0 0;font-weight:700;font-size:14px;color:#111}
#thQuest .schdl dd{margin:0;font-size:14px;line-height:1.4;color:#222}
#thQuest .schnote{margin:10px 0 0;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:12px;color:#888}
/* /schreck-css */
'''
i=s.rindex('</style>')
s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz116'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
