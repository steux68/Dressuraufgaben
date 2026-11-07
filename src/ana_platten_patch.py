# Anatomie: drei gemeinfreie Tafeln (Hebel 1905, Kopf Tafel 6, Fessel/Huf Tafel 15), ohne Punkte. Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if "k:'hl'" in s: sys.exit('schon angewendet')
NEW=r""" {k:'hl',g:'Knochen sind Hebel, und die Muskeln ziehen daran. Das Bild zeigt drei Beinstellungen für die drei Hebelarten. Die Buchstaben stehen unter dem Bild: F ist der Drehpunkt, P die Stelle, an der die Kraft angreift, W die Last und M der Muskel als Kraftquelle.',gE:'Bones are levers, and muscles pull on them. The picture shows three leg positions for the three kinds of lever. The letters are explained under the picture: F is the fulcrum, P the point where the power acts, W the weight and M the muscle as the source of power.',src:'The Horse: its treatment in health and disease (Gresham Publishing, London, 1905), Fig. 23–25 „The Bones as Levers“, Zeichner R. E. H.; Internet Archive Book Images über Wikimedia Commons (gemeinfrei)',srcE:'The Horse: its treatment in health and disease (Gresham Publishing, London, 1905), Figs. 23–25 "The Bones as Levers", artist R. E. H.; Internet Archive Book Images via Wikimedia Commons (public domain)',de:'Knochen als Hebel',en:'Bones as levers',img:'img/hebel_axe_1905.jpg',W:1500,H:979,P:[],pos:'center 50%',
  alt:'Drei Zeichnungen eines Hinterbeins mit Knochen und Muskel, Hebel erster, zweiter und dritter Ordnung',altE:'Three drawings of a hind leg with bones and muscle: levers of the first, second and third order',cap:'Die Knochen als Hebel: erste, zweite und dritte Ordnung (1905).',capE:'The bones as levers: first, second and third order (1905).'},
 {k:'pk',g:'Der Kopf mit seinen Muskeln (links) und der Schädel (rechts), dazu unten zwei Ausschnitte der Ohrregion. Die Zahlen und Buchstaben gehören zur Legende des Buches und sind hier nicht übersetzt.',gE:'The head with its muscles (left) and the skull (right), with two details of the ear region below. The numbers and letters belong to the legend of the book and are not translated here.',src:'Ellenberger, Baum, Dittrich: Handbuch der Anatomie der Tiere für Künstler, Band „Das Pferd“, Tafel 6 (Dieterich, Leipzig); University of Wisconsin Digital Collections über Wikimedia Commons (gemeinfrei)',srcE:'Ellenberger, Baum, Dittrich: Handbuch der Anatomie der Tiere für Künstler, volume "Das Pferd", plate 6 (Dieterich, Leipzig); University of Wisconsin Digital Collections via Wikimedia Commons (public domain)',de:'Kopf: Muskeln und Schädel',en:'Head: muscles and skull',img:'img/pferd_tafel6_kopf.jpg',W:1500,H:1170,P:[],pos:'center 50%',
  alt:'Pferdekopf mit Muskeln, Schädel und Details der Ohrregion, Lithografie',altE:'Horse head with muscles, skull and ear-region details, lithograph',cap:'Kopf und Schädel, Tafel 6 aus Ellenberger, Baum und Dittrich.',capE:'Head and skull, plate 6 from Ellenberger, Baum and Dittrich.'},
 {k:'ph',g:'Fessel und Huf in sechs Ansichten: von der Seite, präpariert, im Längsschnitt, von vorn und von hinten (hinten auch präpariert). Die Zahlen gehören zur Legende des Buches und sind hier nicht übersetzt.',gE:'Pastern and hoof in six views: from the side, dissected, in section, from the front and from behind (the last one also dissected). The numbers belong to the legend of the book and are not translated here.',src:'Ellenberger, Baum, Dittrich: Handbuch der Anatomie der Tiere für Künstler, Band „Das Pferd“, Tafel 15 (Dieterich, Leipzig); University of Wisconsin Digital Collections (gemeinfrei)',srcE:'Ellenberger, Baum, Dittrich: Handbuch der Anatomie der Tiere für Künstler, volume "Das Pferd", plate 15 (Dieterich, Leipzig); University of Wisconsin Digital Collections (public domain)',de:'Fessel und Huf',en:'Pastern and hoof',img:'img/pferd_tafel15_huf.jpg',W:1170,H:1500,P:[],pos:'center 50%',
  alt:'Fessel und Huf des Pferdes in sechs Ansichten, Lithografie',altE:'Horse pastern and hoof in six views, lithograph',cap:'Fessel und Huf, Tafel 15 aus Ellenberger, Baum und Dittrich.',capE:'Pastern and hoof, plate 15 from Ellenberger, Baum and Dittrich.'}
"""
old="];\nconst UI={"
assert s.count(old)==1
i=s.index(old)
head=s[:i].rstrip()
assert head.endswith('},') or head.endswith('}')
if not head.endswith(','): head+=','
s=head+'\n'+NEW+old+s[i+len(old):]
old2="sh:'Körper'};"
assert s.count(old2)==1
s=s.replace(old2,"sh:'Körper',hl:'Beine',pk:'Kopf & Auge',ph:'Huf'};",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz106'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
