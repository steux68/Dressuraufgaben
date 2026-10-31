#!/usr/bin/env python3
"""Lernkarten R1–R6 und Aushang (A4) im Stil der App / von dasein-design: weißes Blatt, gestrichelte Leitlinien links und rechts,
Randmarken, Marke "P a–x" statt der Logos von OEPS und Steinbach, gepunktete Rahmen, Carlito.
Aufruf: python3 src/lernkarten.py <build-ordner> <ausgabe-ordner>
Build-Ordner: SS.ttf, SS-Bold.ttf, SS-Italic.ttf (= Carlito), steux.png, steps.json (aus der App: TESTS[].steps)."""
import math, re, sys, os, json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.utils import ImageReader

B = sys.argv[1]; OUTDIR = sys.argv[2]
for n in ('SS', 'SS-Bold', 'SS-Italic'):
    pdfmetrics.registerFont(TTFont(n, os.path.join(B, n + '.ttf')))
STEUX = os.path.join(B, 'steux.png')
RED = '#e30613'; DARK = HexColor('#22281f'); MUTED = HexColor('#5d6656'); LINE = HexColor('#c4c4c4'); DOT = HexColor('#b8b8b8')
PALE = '#f4f4f2'; LIME = '#cdff3e'; FRAME = '#6f746d'
CREDIT = 'App, Gestaltung und Lernkarten © Steuart JM HARRISON (steux) · Aufgabeninhalte: OEPS'
DISCLAIMER = 'Inoffizielle Lernhilfe, ohne Gewähr. Bitte vor der Prüfung die aktuelle Aufgabe auf oeps.at prüfen – Änderungen sind möglich.'
G = {'S': ('#7d7a70', [1.5, 3], 1.6, 'Mittelschritt'), 'T': ('#0b5fa5', None, 1.6, 'Arbeitstrab, aussitzen'),
     'L': ('#3a9ad6', [5, 2.5], 1.6, 'Arbeitstrab, leichttraben'), 'G': ('#e07b00', None, 2.6, 'Arbeitsgalopp')}
CRIT = ['Sitz: Losgelassenheit, Balance und', 'Bewegungsgefühl, Schenkellage, Handhaltung', '',
        'Hilfengebung: Korrektheit der Gewichts-,', 'Schenkel- und Zügelhilfen', '',
        'Ausführung der Hufschlagfiguren', '', 'Abzüge für Verreiten und Auslassungen', 'laut ÖTO', '',
        'Ergebnis: bestanden / nicht bestanden']
META = {
 'R1': dict(name='Reiterpass', date='01.01.2018', full='Reiterpass', dur='ca. 3½ Min.', merk=[
   'Start: im Arbeitstrab einreiten, bei C rechte Hand – am Anfang kein Halt.',
   'Linke Hand (Wechsel K–M): Zirkel bei C, Galopp zw. X und Tourenpunkt, dann ganze Bahn 1x herum.',
   'Rechte Hand (Wechsel H–F): Galopp zw. F–A 1x herum, danach Wendung rechts bei E und bei B.',
   'Schluss: Mittelschritt ab F, bei A auf die Mittellinie, Halt bei X.']),
 'R2': dict(name='Reiterpass', date='01.01.2018', full='Reiterpass', dur='ca. 3½ Min.', merk=[
   'Start: im Arbeitstrab einreiten, bei C linke Hand – am Anfang kein Halt.',
   'Rechte Hand (Wechsel F–H): Große Tour bei C, Galopp zw. X und Tourenpunkt, 1x herum, vor C Trab.',
   'Linke Hand (Wechsel M–K): Galopp zw. K–A, Große Tour bei A 1x herum, geradeaus bis zw. M–C.',
   'Schluss: leichttraben, vor K aussitzen, Mittelschritt ab K, bei A auf die Mittellinie, Halt bei X.']),
 'R3': dict(name='Reiternadel', date='01.01.2011', full='Reiternadel', dur='ca. 4 Min.', merk=[
   'Start: einreiten, Halt und Gruß bei X, bei C rechte Hand.',
   'Linke Hand (Wechsel K–M): Zirkel bei C, Galopp bei X, ganze Bahn, F–H wechseln, vor H Trab.',
   'Rechte Hand: Zirkel bei C, Galopp bei X, M–F verlängern, Zirkel bei A, bei X Trab.',
   'Schluss: Schritt ab A, Wechsel K–B, H–F Tritte verlängern, Halt bei X.']),
 'R4': dict(name='Dressurnadel', date='01.01.2011', full='Reiternadel Dressur', dur='ca. 4 Min.', merk=[
   'Start: einreiten, Halt bei X, rechte Hand, einfache Schlangenlinie M–F.',
   'Linke Hand (Wechsel K–M): Zirkel C, Galopp X, ganze Bahn, Zirkel A, bei X Trab und Tourenwechsel.',
   'Rechte Hand: Zirkel C, Galopp X, M–F verlängern, Zirkel A, bei X Trab.',
   'Schluss: Schritt ab A, Wechsel K–B, H–F Tritte verlängern, Halt bei X.']),
 'R5': dict(name='Lizenz R1 · Reitabzeichen', date='01.01.2012', full='Reitabzeichen und Lizenzprüfung R1', dur='ca. 4 Min.', merk=[
   'Start: Halt bei X, rechte Hand leichttraben, Schlangentour in 3 Bögen C–A.',
   'K–M Tritte verlängern, H–B wechseln, Galopp rechts ab B, K–H verlängern, Zirkel C, Trab bei X.',
   'Wechsel M–E, Galopp links ab E, F–M verlängern, zw. H–E Trab, Zirkel bei E: Zügel aus der Hand kauen lassen.',
   'Schluss: Halt bei A und rückwärts, halbe Tour F–K im Schritt, Trab ab K, Halt bei X.']),
 'R6': dict(name='Lizenzprüfung RD1', date='01.01.2011', full='Lizenzprüfung RD1', dur='ca. 4 Min.', merk=[
   'Start: Halt bei X, linke Hand, Schlangentour in 3 Bögen C–A, F–H Tritte verlängern.',
   'Wendung rechts bei B, Linksgalopp bei X, Zirkel A mit Überstreichen, F–M verlängern, Zirkel C, Tourenwechsel bei X.',
   'Rechtsgalopp ab A mit Überstreichen, zw. K–E Trab, Zirkel bei E: Zügel aus der Hand kauen lassen.',
   'Schluss: Halt bei C und rückwärts, Wechsel M–E im Schritt, Trab ab E, Halt bei X.']),
}
STEPS = {t['id']: t['steps'] for t in json.load(open(os.path.join(B, 'steps.json'), encoding='utf8'))}
W, H = A4; M = 36


def sample(d):
    toks = re.findall(r'[MLQA]|-?[\d.]+', d); pts = []; i = 0; cur = None
    def num():
        nonlocal i; v = float(toks[i]); i += 1; return v
    while i < len(toks):
        c = toks[i]; i += 1
        if c == 'M': cur = (num(), num()); pts = [cur]
        elif c == 'L': cur = (num(), num()); pts.append(cur)
        elif c == 'Q':
            cx, cy, x, y = num(), num(), num(), num(); x0, y0 = cur
            for k in range(1, 9):
                t = k / 8; pts.append(((1-t)**2*x0+2*(1-t)*t*cx+t*t*x, (1-t)**2*y0+2*(1-t)*t*cy+t*t*y))
            cur = (x, y)
        elif c == 'A':
            r = num(); num(); num(); num(); sw = num(); x, y = num(), num(); x0, y0 = cur
            mx, my = (x0+x)/2, (y0+y)/2; dx, dy = x-x0, y-y0; q = math.hypot(dx, dy)
            h = math.sqrt(max(r*r-(q/2)**2, 0)); ux, uy = -dy/q, dx/q
            for sgn in (1, -1):
                ccx, ccy = mx+sgn*h*ux, my+sgn*h*uy
                a0 = math.atan2(y0-ccy, x0-ccx); a1 = math.atan2(y-ccy, x-ccx); da = a1-a0
                if sw == 1:
                    while da <= 0: da += 2*math.pi
                else:
                    while da >= 0: da -= 2*math.pi
                if abs(da) <= math.pi+1e-6: break
            for k in range(1, 25):
                a = a0+da*k/24; pts.append((ccx+r*math.cos(a), ccy+r*math.sin(a)))
            cur = (x, y)
    return pts


def dotted_line(c, x1, y1, x2, y2, col=DOT, w=0.8):
    c.setStrokeColor(col); c.setLineWidth(w); c.setDash([0.1, 2.4]); c.setLineCap(1); c.line(x1, y1, x2, y2); c.setDash(); c.setLineCap(0)


def dotted_rect(c, x, y, w, h):
    c.setStrokeColor(DOT); c.setLineWidth(0.9); c.setDash([0.1, 2.6]); c.setLineCap(1); c.rect(x, y, w, h, stroke=1, fill=0); c.setDash(); c.setLineCap(0)


def arena(c, ox, oy, s, upto, SS, all_=False):
    T = lambda x, y: (ox+(x-80)*s, oy-(y-10)*s)
    x1, y1 = T(110, 40); x2, y2 = T(270, 360)
    c.setFillColor(HexColor('#ffffff')); c.setStrokeColor(HexColor(FRAME)); c.setLineWidth(1.3); c.setDash()
    c.rect(x1, y2, x2-x1, y1-y2, fill=1, stroke=1)
    c.setStrokeColor(HexColor('#a5a5a5')); c.setLineWidth(0.9); c.setDash([0.1, 2.6]); c.setLineCap(1)
    a, b = T(190, 40); a2, b2 = T(190, 360); c.line(a, b, a2, b2)
    a, b = T(110, 200); a2, b2 = T(270, 200); c.line(a, b, a2, b2); c.setDash(); c.setLineCap(0)
    c.setFillColor(DARK); c.setFont('SS-Bold', 9*s/0.6)
    for L, x, y in [('C', 190, 24), ('A', 190, 378), ('H', 94, 88), ('E', 94, 200), ('K', 94, 312), ('M', 286, 88), ('B', 286, 200), ('F', 286, 312)]:
        px, py = T(x, y); c.drawCentredString(px, py-3*s/0.6, L)
    c.setFont('SS', 7*s/0.6); c.setFillColor(MUTED); px, py = T(200, 212); c.drawCentredString(px, py-2, 'X')
    for k in range(upto+1):
        st = SS[k]; cur = (k == upto) and not all_
        col, dash, w, _ = G[st[2]]
        if st[3]:
            pts = sample(st[3]); p = c.beginPath(); p.moveTo(*T(*pts[0]))
            for q in pts[1:]: p.lineTo(*T(*q))
            hc = HexColor(col)
            if not cur and not all_: hc = Color(hc.red, hc.green, hc.blue, alpha=0.28)
            c.setStrokeColor(hc); c.setLineWidth((w+1.2 if cur else w)*s/0.6)
            c.setDash(dash if dash else []); c.setLineCap(1); c.drawPath(p, stroke=1, fill=0); c.setDash()
            if cur:
                (xa, ya), (xb, yb) = T(*pts[-2]), T(*pts[-1]); ang = math.atan2(yb-ya, xb-xa); L = 7*s/0.6
                c.setFillColor(HexColor(col)); ah = c.beginPath(); ah.moveTo(xb, yb)
                ah.lineTo(xb-L*math.cos(ang-0.45), yb-L*math.sin(ang-0.45)); ah.lineTo(xb-L*math.cos(ang+0.45), yb-L*math.sin(ang+0.45)); ah.close()
                c.drawPath(ah, stroke=0, fill=1)
        if len(st) > 4 and st[4] and (cur or all_):
            hx, hy = (st[4] if isinstance(st[4], list) else (190, 200))
            c.setFillColor(HexColor('#c9502a' if cur else '#7d7a70')); px, py = T(hx, hy); c.circle(px, py, 4*s/0.6, fill=1, stroke=0)


def legend(c, x, y):
    c.setFont('SS', 8.5)
    for g in 'STLG':
        col, dash, w, n = G[g]; c.setStrokeColor(HexColor(col)); c.setLineWidth(w+0.6); c.setDash(dash if dash else [])
        c.line(x, y+3, x+22, y+3); c.setDash(); c.setFillColor(DARK)
        lab = {'S': 'Schritt', 'T': 'Trab', 'L': 'Leichttraben', 'G': 'Galopp'}[g]
        c.drawString(x+27, y, lab); x += 27+c.stringWidth(lab, 'SS', 8.5)+18


def page_frame(c, right_text=None):
    """Leitlinien links/rechts, Randmarken, Marke P a–x mit Schriftzug, gestrichelte Linie darunter."""
    gx = 15
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.setDash([4.2, 3.2])
    c.line(gx, 0, gx, H); c.line(W-gx, 0, W-gx, H); c.setDash()
    c.setStrokeColor(DOT); c.setLineWidth(0.8); c.setDash([3.4, 2.4])
    for yy in (H-92, H/2-22, 70):
        for off in (0, 8):
            c.line(gx, yy+off, gx+11, yy+off); c.line(W-gx-11, yy+off, W-gx, yy+off)
    c.setDash()
    mh = 30; mw = mh*44/30; mx = M; my = H-24-mh
    c.setFillColor(HexColor(RED)); c.rect(mx, my, mw, mh, stroke=0, fill=1)
    c.setFillColor(HexColor('#ffffff')); c.setFont('SS-Bold', mh*23/30); c.drawString(mx+mw*5/44, my+mh*6.5/30, 'P')
    c.setFont('SS-Bold', mh*11.5/30); c.drawString(mx+mw*19.5/44, my+mh*6.5/30, 'a–x')
    c.setFillColor(HexColor(RED)); c.setFont('SS', 27); c.drawString(mx+mw+10, my+mh*0.2, 'passage')
    if right_text:
        c.setFillColor(MUTED); c.setFont('SS', 9); c.drawRightString(W-M, my+mh*0.45, right_text)
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.setDash([4.2, 3.2]); c.line(gx, H-66, W-gx, H-66); c.setDash()


def footer(c, line_y, small=(), right=None, logo_h=26, fs=7.5, sfs=7):
    dotted_line(c, M, line_y, W-M, line_y, HexColor('#b9beb1'))
    lw = logo_h*640/226; top = line_y-6
    c.drawImage(ImageReader(STEUX), M, top-logo_h, lw, logo_h, mask='auto')
    tx = M+lw+10; maxw = W-M-tx; y = top-fs*0.95
    c.setFillColor(DARK); c.setFont('SS-Bold', fs); c.drawString(tx, y, CREDIT)
    if right:
        c.setFont('SS', fs); c.setFillColor(MUTED); c.drawRightString(W-M, y, right)
    c.setFillColor(MUTED)
    for t in small:
        y -= sfs+2.4; f = sfs
        while c.stringWidth(t, 'SS', f) > maxw and f > 5.5: f -= 0.1
        c.setFont('SS', f); c.drawString(tx, y, t)


def wrap(c, text, font, size, width):
    words = text.split(); lines = []; line = ''
    for w in words:
        t = (line+' '+w).strip()
        if c.stringWidth(t, font, size) > width and line: lines.append(line); line = w
        else: line = t
    lines.append(line); return lines


FOOT_LINE = 60


def build(tid, out):
    T = META[tid]; SS = STEPS[tid]; N = len(SS); npages = 1+math.ceil(N/4)
    HM = H-M-74
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle(f'Dressuraufgabe {tid} {T["name"]} – Lernkarten'); c.setAuthor('Steuart JM HARRISON (steux)')
    title = f'Dressuraufgabe {tid} · {T["name"]}'
    src = f'Quelle: Dressuraufgabe {tid} ({T["full"]}) des Österreichischen Pferdesportverbands (OEPS), Aufgabenblatt Stand {T["date"]}.'

    def header(sub, pg):
        page_frame(c, 'Lernkarten')
        c.setFillColor(HexColor(RED)); c.setFont('SS-Bold', 16); c.drawString(M, HM-8, title)
        c.setFont('SS', 9); c.setFillColor(MUTED); c.drawString(M, HM-22, sub)
        legend(c, M, HM-40)
        dotted_line(c, M, HM-48, W-M, HM-48)
        footer(c, FOOT_LINE, (src, DISCLAIMER), f'Seite {pg} / {npages}')

    header(f'Übersicht · alle {N} Lektionen · {T["dur"]}', 1)
    arena(c, M-4, HM-62, 0.62, N-1, SS, all_=True)
    c.setFont('SS-Bold', 8); c.setFillColor(MUTED); c.drawString(M, HM-62-245, 'Ganze Aufgabe')
    tx = M+150; ty = HM-72; rh = 19 if N <= 20 else 16.5
    c.setFont('SS-Bold', 10); c.setFillColor(DARK); c.drawString(tx, ty, 'Index')
    c.setFont('SS', 7.5); c.setFillColor(MUTED); c.drawRightString(W-M, ty, 'Seite'); ty -= 16
    for k, st in enumerate(SS):
        if k % 2 == 1:   # Streifen grau/weiß wie in der App
            c.setFillColor(HexColor(PALE)); c.rect(tx-6, ty-rh+11.5, W-M-tx+12, rh, stroke=0, fill=1)
        if k and k % 4 == 0: dotted_line(c, tx-6, ty+11.5, W-M+6, ty+11.5)
        c.setFillColor(HexColor(G[st[2]][0])); c.circle(tx+4, ty+3, 3, fill=1, stroke=0)
        c.setFillColor(DARK); c.setFont('SS', 9); c.drawRightString(tx+24, ty, str(k+1))
        lf = 9
        while c.stringWidth(st[0], 'SS-Bold', lf) > 66: lf -= 0.25
        c.setFont('SS-Bold', lf); c.drawString(tx+30, ty, st[0])
        c.setFont('SS', 9); txt = st[1]
        while c.stringWidth(txt, 'SS', 9) > W-M-tx-128: txt = txt[:-2]
        if txt != st[1]: txt = txt.rstrip(' ,')+'…'
        c.drawString(tx+100, ty, txt); c.setFillColor(MUTED); c.drawRightString(W-M, ty, str(2+k//4)); ty -= rh
    ty -= 12; c.setFont('SS-Bold', 10); c.setFillColor(DARK); c.drawString(tx, ty, 'Merkhilfe'); ty -= 14
    for line in T['merk']:
        for l in wrap(c, line, 'SS', 8.8, W-M-tx):
            c.setFont('SS', 8.8); c.drawString(tx, ty, l); ty -= 11.5
        ty -= 2
    assert ty > FOOT_LINE+6, (tid, ty)
    c.showPage()

    cw = (W-2*M-16)/2; ch = (H-2*M-60-16-30-74)/2; crit_done = False
    for p in range(npages-1):
        header(f'Lektionen {p*4+1}–{min(p*4+4, N)}', p+2)
        for j in range(4):
            k = p*4+j; col_ = j % 2; row = j//2
            cx = M+col_*(cw+16); cy = HM-58-row*(ch+16)
            if k >= N:
                if not crit_done:
                    crit_done = True; dotted_rect(c, cx, cy-ch, cw, ch)
                    c.setFillColor(DARK); c.setFont('SS-Bold', 11); c.drawString(cx+14, cy-28, 'Bewertet werden')
                    yy = cy-50
                    for t in CRIT: c.setFont('SS', 9.5); c.drawString(cx+14, yy, t); yy -= 13
                continue
            dotted_rect(c, cx, cy-ch, cw, ch)
            s = 0.60; aw = 220*s
            arena(c, cx+(cw-aw)/2, cy-6, s, k, SS)
            st = SS[k]; by = cy-6-380*s-14
            c.setFillColor(DARK); c.setFont('SS-Bold', 10); c.drawString(cx+12, by, f'{k+1}')
            bw = c.stringWidth(st[0], 'SS-Bold', 10)+12
            c.setFillColor(HexColor(LIME)); c.rect(cx+30, by-4, bw, 15, stroke=0, fill=1)
            c.setFillColor(DARK); c.setFont('SS-Bold', 10); c.drawString(cx+36, by, st[0])
            yy = by-17
            for l in wrap(c, st[1], 'SS', 9.5, cw-24): c.setFont('SS', 9.5); c.drawString(cx+12, yy, l); yy -= 12
            sub = st[5] if len(st) > 5 and st[5] else ('Halten' if len(st) > 4 and st[4] else G[st[2]][3])
            c.setFont('SS-Italic', 8.5); c.setFillColor(HexColor(G[st[2]][0])); c.drawString(cx+12, yy, sub)
            assert yy > cy-ch+4, (tid, k, yy, cy-ch)
        c.showPage()
    c.save()


def aushang(out):
    import qrcode
    URL = 'https://steux68.github.io/Dressuraufgaben/'
    qr_png = os.path.join(B, 'qr.png')
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2); q.add_data(URL); q.make()
    q.make_image(fill_color='#22281f', back_color='white').save(qr_png)
    c = canvas.Canvas(out, pagesize=A4); c.setTitle('Dressuraufgaben R1–R6 – Aushang'); c.setAuthor('Steuart JM HARRISON (steux)')
    page_frame(c, 'Aushang')
    d = DARK; m = MUTED
    c.setFillColor(HexColor(RED)); c.setFont('SS-Bold', 30); c.drawCentredString(W/2, H-142, 'DRESSURAUFGABEN R1–R6')
    c.setFont('SS', 14); c.setFillColor(m); c.drawCentredString(W/2, H-163, 'Reiterpass bis Lizenz · Lernen und Quiz-Spiel fürs Handy')
    s = 250; c.drawImage(ImageReader(qr_png), (W-s)/2, H-182-s, s, s)
    c.setFillColor(d); c.setFont('SS-Bold', 16); c.drawCentredString(W/2, H-182-s-30, 'QR-Code mit der Handykamera scannen')
    c.setFont('SS', 10); c.setFillColor(m); c.drawCentredString(W/2, H-182-s-46, 'oder: steux68.github.io/Dressuraufgaben  ·  Anleitung in der App unter INFO')
    y = H-182-s-95; x = 90
    c.setFillColor(d); c.setFont('SS-Bold', 14); c.drawString(x, y, 'Als App auf den Startbildschirm'); y -= 26

    def arrow_text(x, y, parts, size):
        for i, p in enumerate(parts):
            c.setFont('SS', size); c.drawString(x, y, p); x += c.stringWidth(p, 'SS', size)
            if i < len(parts)-1:
                x += 6; ay = y+size*0.33; L = size*0.95
                c.setStrokeColor(d); c.setLineWidth(size*0.08); c.line(x, ay, x+L, ay)
                c.line(x+L, ay, x+L-size*0.3, ay+size*0.25); c.line(x+L, ay, x+L-size*0.3, ay-size*0.25); x += L+7
    for a, b in [('iPhone (Safari):', ['Teilen-Symbol', '„Zum Home-Bildschirm“']), ('Android (Chrome):', ['Menü (drei Punkte)', '„Zum Startbildschirm hinzufügen“'])]:
        c.setFont('SS-Bold', 12); c.setFillColor(d); c.drawString(x, y, a); arrow_text(x+120, y, b, 12); y -= 22
    y -= 12; c.setFont('SS-Bold', 14); c.drawString(x, y, 'Was drin ist'); y -= 24; c.setFont('SS', 12)
    for t in ['Alle 6 OEPS-Aufgaben: Reiterpass, Reiternadel, Dressurnadel, Lizenz', 'Lernen: jede Lektion im Viereck eingezeichnet',
              'Selbsttest: erst laut sagen, dann aufdecken', 'Spiel: „Was kommt als Nächstes?“ mit Punkten und Serie', 'Lernkarten zum Ausdrucken: bei jeder Aufgabe']:
        c.setFillColor(d); c.circle(x+4, y+4, 2.5, fill=1, stroke=0); c.setFont('SS', 12); c.drawString(x+14, y, t); y -= 20
    footer(c, 78, ('Quelle: Dressuraufgaben R1–R6 des Österreichischen Pferdesportverbands (OEPS).', DISCLAIMER), logo_h=34, fs=8.5, sfs=8)
    c.save()


if __name__ == '__main__':
    os.makedirs(OUTDIR, exist_ok=True)
    for tid in META:
        build(tid, os.path.join(OUTDIR, f'{tid}_Lernkarten.pdf')); print(tid, 'ok')
    aushang(os.path.join(OUTDIR, 'Aushang_Dressuraufgaben.pdf')); print('Aushang ok')
