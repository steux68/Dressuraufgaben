#!/usr/bin/env python3
"""Eigene Galerie-Tafeln im Hochformat (Handy): Fussfolge, Viereck, Fellfarben.
Schreibt SVG nach img/quellen/, PNG + Kachel nach img/galerie/.
Aufruf (aus dem Repo-Ordner): python3 -I src/mk_tafeln.py"""
import os
from playwright.sync_api import sync_playwright
from PIL import Image

FONT = 'font-family="Carlito, Calibri, Arial, sans-serif"'
INK, MUTE, RED, GREY = '#111', '#6b6b6b', '#e30613', '#f4f4f2'
FOOT = '© Steuart JM HARRISON (steux) · eigene Zeichnung'


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {FONT}>'
            f'<rect width="{w}" height="{h}" fill="#fff"/>{body}'
            f'<text x="{w-36}" y="{h-20}" text-anchor="end" font-size="20" fill="{MUTE}">{FOOT}</text></svg>')


def t(x, y, s, size=24, fill=INK, weight=400, anchor='start', extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{s}</text>'


# ------------------------------------------------------------------ 1. Fussfolge (800 x 1100)
def fussfolge():
    W, H = 800, 1100
    b = [t(36, 66, 'Die Fußfolge der', 46, RED, 700), t(36, 118, 'Grundgangarten', 46, RED, 700),
         t(36, 158, 'schematisch · ein Durchgang von links nach rechts.', 24, MUTE),
         t(36, 190, 'Die Balken zeigen, wann der Huf am Boden ist.', 24, MUTE)]
    rows = ['hinten links', 'vorn links', 'hinten rechts', 'vorn rechts']
    x0, x1 = 230, 764
    rh, gap = 38, 8
    gaits = [
        ('Schritt', 'Viertakt', '#7d7a70', [(0, 1), (25, 2), (50, 3), (75, 4)], [62] * 4, []),
        ('Trab', 'Zweitakt, Schwebephase', '#0b5fa5', [(0, 1), (50, 2), (50, 2), (0, 1)], [40] * 4, [(40, 50), (90, 100)]),
        ('Galopp', 'Dreitakt (Rechtsgalopp), Schwebephase', '#e07b00', [(0, 1), (25, 2), (25, 2), (50, 3)], [38, 37, 37, 35], [(85, 100)]),
    ]
    xs = lambda p: x0 + (x1 - x0) * p / 100
    for gi, (name, sub, col, starts, dur, susp) in enumerate(gaits):
        top = 292 + gi * 262
        ch = 4 * rh + 3 * gap
        b.append(f'<text x="36" y="{top-44}"><tspan font-size="40" font-weight="700" fill="{col}">{name}</tspan><tspan dx="16" font-size="22" fill="{MUTE}">{sub}</tspan></text>')
        for a, c in susp:
            b.append(f'<rect x="{xs(a):.1f}" y="{top-6}" width="{xs(c)-xs(a):.1f}" height="{ch+12}" fill="#fff3bf"/>')
            if c - a >= 14:
                b.append(t((xs(a) + xs(c)) / 2, top + ch / 2 + 7, 'Schwebe', 21, '#8a6d00', 400, 'middle'))
            else:
                cx_, cy_ = (xs(a) + xs(c)) / 2, top + ch / 2
                b.append(t(cx_, cy_ + 7, 'Schwebe', 20, '#8a6d00', 400, 'middle', f'transform="rotate(-90 {cx_} {cy_})"'))
        for p in (0, 25, 50, 75, 100):
            b.append(f'<line x1="{xs(p):.1f}" y1="{top-10}" x2="{xs(p):.1f}" y2="{top+ch+10}" stroke="#c9c9c9" stroke-width="1.4" stroke-dasharray="1 5" stroke-linecap="round"/>')
        for ri, rname in enumerate(rows):
            y = top + ri * (rh + gap)
            b.append(t(x0 - 14, y + rh / 2 + 8, rname, 23, INK, 400, 'end'))
            st, no = starts[ri]
            ends = st + dur[ri]
            segs = [(st, min(ends, 100))] + ([(0, ends - 100)] if ends > 100 else [])
            for a, c in segs:
                b.append(f'<rect x="{xs(a):.1f}" y="{y}" width="{xs(c)-xs(a):.1f}" height="{rh}" fill="{col}"/>')
            b.append(f'<circle cx="{xs(st)+22:.1f}" cy="{y+rh/2}" r="15" fill="#fff" stroke="{INK}" stroke-width="1.6"/>')
            b.append(t(xs(st) + 22, y + rh / 2 + 8, str(no), 22, INK, 700, 'middle'))
    b.append(t(36, 1040, 'Die Zahl im Kreis zeigt die Reihenfolge, in der die Hufe aufsetzen.', 22, MUTE))
    b.append(t(36, 1068, 'Gleiche Zahl = gleichzeitig.', 22, MUTE))
    return svg(W, H, ''.join(b)), W, H


# ------------------------------------------------------------------ 2. Viereck (800 x 1100)
def viereck():
    W, H = 800, 1140
    b = [t(36, 66, 'Das Viereck und', 46, RED, 700), t(36, 118, 'seine Buchstaben', 46, RED, 700)]
    S = 9.0
    bottom = 700

    def arena(x, length, outer_l, outer_r, mid, title):
        top = bottom - length * S
        b.append(f'<rect x="{x}" y="{top}" width="{20*S}" height="{length*S}" fill="#fff" stroke="#8c918a" stroke-width="2.6"/>')
        cx = x + 10 * S
        b.append(f'<line x1="{cx}" y1="{top}" x2="{cx}" y2="{bottom}" stroke="#b8b8b8" stroke-width="1.8" stroke-dasharray="1 5" stroke-linecap="round"/>')
        for m, c in outer_l:
            y = bottom - m * S
            b.append(f'<line x1="{x}" y1="{y}" x2="{x-9}" y2="{y}" stroke="#8c918a" stroke-width="2.6"/>')
            b.append(t(x - 30, y + 10, c, 32, INK, 700, 'middle'))
        for m, c in outer_r:
            y = bottom - m * S
            b.append(f'<line x1="{x+20*S}" y1="{y}" x2="{x+20*S+9}" y2="{y}" stroke="#8c918a" stroke-width="2.6"/>')
            b.append(t(x + 20 * S + 30, y + 10, c, 32, INK, 700, 'middle'))
        b.append(t(cx, bottom + 38, 'A', 32, INK, 700, 'middle'))
        b.append(f'<line x1="{cx}" y1="{bottom}" x2="{cx}" y2="{bottom+9}" stroke="#8c918a" stroke-width="2.6"/>')
        b.append(t(cx, top - 18, 'C', 32, INK, 700, 'middle'))
        b.append(f'<line x1="{cx}" y1="{top}" x2="{cx}" y2="{top-9}" stroke="#8c918a" stroke-width="2.6"/>')
        for m, c in mid:
            y = bottom - m * S
            if c == 'X':
                b.append(f'<circle cx="{cx}" cy="{y}" r="17" fill="#ffd400" stroke="{INK}" stroke-width="2"/>')
                b.append(t(cx, y + 9, 'X', 24, INK, 700, 'middle'))
            else:
                b.append(f'<circle cx="{cx}" cy="{y}" r="4.5" fill="#8c918a"/>')
                b.append(t(cx + 14, y + 9, c, 26, '#555', 700))
        b.append(t(cx, top - 62, title, 24, MUTE, 400, 'middle'))

    arena(120, 40, [(6, 'K'), (20, 'E'), (34, 'H')], [(6, 'F'), (20, 'B'), (34, 'M')],
          [(6, 'D'), (20, 'X'), (34, 'G')], 'klein: 20 × 40 m')
    arena(470, 60, [(6, 'K'), (18, 'V'), (30, 'E'), (42, 'S'), (54, 'H')],
          [(6, 'F'), (18, 'P'), (30, 'B'), (42, 'R'), (54, 'M')],
          [(10, 'D'), (20, 'L'), (30, 'X'), (40, 'I'), (50, 'G')], 'groß: 20 × 60 m')
    y0 = 772
    b.append(f'<line x1="36" y1="{y0-18}" x2="764" y2="{y0-18}" stroke="#c9c9c9" stroke-width="1.6" stroke-dasharray="1 5" stroke-linecap="round"/>')
    b.append(t(36, y0 + 6, 'Rund um das Viereck, von A aus zuerst nach links (K):', 24, RED, 700))
    b.append(t(36, y0 + 52, 'groß', 22, MUTE)); b.append(t(130, y0 + 54, 'A K V E S H C M R B P F', 32, INK, 700, 'start', 'letter-spacing="2"'))
    b.append(t(36, y0 + 100, 'klein', 22, MUTE)); b.append(t(130, y0 + 102, 'A K E H C M B F', 32, INK, 700, 'start', 'letter-spacing="2"'))
    b.append(t(36, y0 + 160, 'Auf der Mittellinie, von A nach C:', 24, RED, 700))
    b.append(t(36, y0 + 206, 'groß', 22, MUTE)); b.append(t(130, y0 + 208, 'D L X I G', 32, INK, 700, 'start', 'letter-spacing="2"'))
    b.append(t(36, y0 + 254, 'klein', 22, MUTE)); b.append(t(130, y0 + 256, 'D X G', 32, INK, 700, 'start', 'letter-spacing="2"'))
    b.append(t(36, y0 + 300, 'A ist der Eingang, C liegt gegenüber, X genau in der Mitte.', 22, INK))
    return svg(W, H, ''.join(b)), W, H


# ------------------------------------------------------------------ 3. Fellfarben (800 x 1100)
def fellfarben():
    W, H = 800, 1160
    b = [t(36, 66, 'Fellfarben beim Pferd', 46, RED, 700),
         t(36, 106, 'Auswahl · oben Mähne und Schweif, in der Mitte das Fell,', 23, MUTE),
         t(36, 136, 'unten die Beine.', 23, MUTE)]
    chips = [
        ('Rappe', 'ganz schwarz', '#1d1b1b', '#1d1b1b', '#1d1b1b'),
        ('Brauner', 'braunes Fell, schwarze Mähne, Schweif und Beine', '#6b3f26', '#1d1b1b', '#1d1b1b'),
        ('Fuchs', 'rotbraunes Fell, Mähne und Schweif rot bis hellblond', '#b5622b', '#c98a4a', '#b5622b'),
        ('Schimmel', 'wird mit den Jahren weiß, Fohlen werden dunkel geboren', '#e6e4df', '#d5d2cb', '#e6e4df'),
        ('Falbe', 'sandfarben, dunkler Aalstrich auf dem Rücken, dunkle Mähne', '#d0a96a', '#2a2420', '#7a6a58'),
        ('Palomino', 'goldgelb, Mähne und Schweif fast weiß', '#d9a441', '#f3ead0', '#d9a441'),
    ]
    cw, chh = 352, 270
    gx, gy = 36, 170
    for i, (name, desc, fell, mane, legs) in enumerate(chips):
        x = gx + (i % 2) * (cw + 24)
        y = gy + (i // 2) * (chh + 22)
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{chh}" fill="{GREY}"/>')
        sx, sy, sw, sh = x + 18, y + 18, cw - 36, 130
        b.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="{fell}" stroke="#bdbdbd" stroke-width="1.2"/>')
        b.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="32" fill="{mane}" stroke="#bdbdbd" stroke-width="1.2"/>')
        b.append(f'<rect x="{sx}" y="{sy+sh-28}" width="{sw}" height="28" fill="{legs}" stroke="#bdbdbd" stroke-width="1.2"/>')
        if name == 'Falbe':
            b.append(f'<rect x="{sx}" y="{sy+32}" width="{sw}" height="7" fill="#2a2420"/>')
        b.append(t(x + 18, y + 188, name, 32, RED, 700))
        words, lines, cur = desc.split(' '), [], ''
        for w in words:
            if len(cur + ' ' + w) > 29 and cur:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + ' ' + w).strip()
        lines.append(cur)
        for k, ln in enumerate(lines[:3]):
            b.append(t(x + 18, y + 216 + k * 25, ln, 21, INK))
    b.append(t(36, 1066, 'Dazu kommen Schecken (weiße und farbige Flecken) und', 22, MUTE))
    b.append(t(36, 1094, 'viele Mischformen. Die Farben sind Näherungen.', 22, MUTE))
    return svg(W, H, ''.join(b)), W, H


def render(name, res, p):
    text, w, h = res
    os.makedirs('img/quellen', exist_ok=True)
    os.makedirs('img/galerie', exist_ok=True)
    open(f'img/quellen/{name}.svg', 'w', encoding='utf8').write(text)
    page = p.new_page(viewport={'width': w, 'height': h})
    page.set_content(f'<html><body style="margin:0;background:#fff">{text}</body></html>')
    page.wait_for_timeout(300)
    out = f'img/galerie/{name}.png'
    page.screenshot(path=out, clip={'x': 0, 'y': 0, 'width': w, 'height': h})
    page.close()
    im = Image.open(out).convert('RGB')
    im.save(out, optimize=True)
    # Kachel im Seitenverhaeltnis 3:4 (Mosaik s:[3,4])
    kw, kh = 360, 480
    im.resize((kw, round(kw * h / w))).crop((0, 0, kw, min(kh, round(kw * h / w)))).save(f'img/galerie/{name}_k.png', optimize=True)
    print(name, os.path.getsize(out) // 1024, 'KB')


if __name__ == '__main__':
    with sync_playwright() as p:
        b = p.chromium.launch()
        render('fussfolge', fussfolge(), b)
        render('viereck', viereck(), b)
        render('fellfarben', fellfarben(), b)
        b.close()
