import re,sys
p='index.html'
s=open(p,encoding='utf-8').read()
if 'theorie-luecken-2026-11-27' in s: print('already'); sys.exit()
N=[
# Fütterung
('Pferdehaltung & Fütterung','Wie oft sollte ein Pferd am Tag Futter bekommen?','Mehrmals täglich in kleinen Portionen',['Einmal am Tag eine große Portion','Nur abends'],'Der Magen des Pferdes ist klein und das Pferd ist ein Dauerfresser. Viele kleine Mahlzeiten und möglichst lange Fresszeiten sind besser als wenige große.'),
('Pferdehaltung & Fütterung','Wie stellt man das Futter um, zum Beispiel auf eine neue Heucharge oder neues Kraftfutter?','Langsam über mehrere Tage',['Von heute auf morgen','Nur bei Vollmond'],'Die Darmbakterien müssen sich an neues Futter gewöhnen. Ein abrupter Wechsel kann Koliken oder Durchfall auslösen.'),
('Pferdehaltung & Fütterung','Wann sollte ein Pferd nach dem Reiten Wasser und Futter bekommen?','Erst wenn es abgekühlt und ruhig geatmet hat',['Sofort im heißen Zustand eine große Portion','Nie am selben Tag'],'Nach der Arbeit lässt man das Pferd zuerst trockenreiten bzw. abkühlen. Danach darf es trinken und fressen.'),
('Pferdehaltung & Fütterung','Warum gehört Salz oder ein Leckstein ins Futterangebot?','Pferde verlieren Mineralstoffe über den Schweiß',['Salz macht das Fell glänzend','Salz ersetzt das Heu'],'Beim Schwitzen gehen Salze verloren. Ein Salzleckstein erlaubt dem Pferd, seinen Bedarf selbst zu decken.'),
('Pferdehaltung & Fütterung','Wie sollte die Qualität von Heu aussehen und riechen?','Staubfrei, aromatisch, ohne Schimmel',['Muffig und leicht grau','Möglichst feucht'],'Schimmeliges oder staubiges Heu schadet Atemwegen und Magen. Gutes Heu riecht würzig und ist trocken.'),
('Pferdehaltung & Fütterung','Was ist bei Äpfeln und Karotten als Leckerli wichtig?','Nur in kleinen Mengen und klein geschnitten',['Beliebig viele am Stück','Nur als ganze Frucht auf einmal'],'Zu große Stücke können im Hals stecken bleiben, zu große Mengen belasten den Magen und den Zuckerhaushalt.'),
('Pferdehaltung & Fütterung','Welche Pflanzen oder Reste dürfen Pferde nicht bekommen, zum Beispiel vom Rasenschnitt?','Rasenschnitt und giftige Pflanzen',['Frisches Gras von der Koppel','Heu'],'Rasenschnitt gärt schnell und kann Koliken auslösen. Manche Pflanzen wie die Eibe sind giftig und gehören nicht in Pferdenähe.'),
# Gesundheit
('Pferdekrankheiten & Erste Hilfe','Wie erkennt man ein gesundes Pferd im Stall?','Aufmerksam, frisst gern, glänzendes Fell, klare Augen',['Steht apathisch mit gesenktem Kopf','Frisst nicht und schwitzt im Stall'],'Verhalten, Appetit, Augen, Nase und Fell zeigen, wie es dem Pferd geht. Veränderungen sollte man ernst nehmen.'),
('Pferdekrankheiten & Erste Hilfe','Wie oft ist die Atemfrequenz eines Pferdes in Ruhe ungefähr?','Etwa 8 bis 16 Atemzüge pro Minute',['30 bis 40 Atemzüge pro Minute','1 bis 2 Atemzüge pro Minute'],'Zählen kann man die Flankenbewegung oder den Atem an den Nüstern. Deutlich schnellere Atmung in Ruhe ist ein Warnzeichen.'),
('Pferdekrankheiten & Erste Hilfe','Was ist bei einer blutenden Wunde am Pferd das Wichtigste?','Ruhe bewahren, Pferd sichern, Tierarzt oder Stallbesitzer informieren',['Wunde mit Hausmitteln selbst nähen','Pferd sofort reiten'],'Stark blutende oder tiefe Wunden gehören in die Hand des Tierarztes. Bis dahin hält man das Pferd ruhig und hilft nur im Rahmen dessen, was man gelernt hat.'),
('Pferdekrankheiten & Erste Hilfe','Was bedeutet Lahmheit?','Das Pferd bewegt sich nicht taktrein oder entlastet ein Bein',['Das Pferd ist müde','Das Pferd hat gute Laune'],'Lahmheit sieht man oft am Kopfnicken im Trab. Ursache können Hufe, Sehnen, Gelenke oder Muskeln sein. Der Tierarzt klärt es ab.'),
('Pferdekrankheiten & Erste Hilfe','Wie oft sollte ein Pferd zum Hufschmied oder zur Hufpflege?','Etwa alle 6 bis 8 Wochen',['Einmal im Jahr','Alle 2 Wochen'],'Das Horn wächst ständig nach. Regelmäßige Pflege hält die Hufform und beugt Lahmheiten vor.'),
('Pferdekrankheiten & Erste Hilfe','Warum kontrolliert man vor dem Reiten die Hufe?','Steine oder Fremdkörper können Schmerzen verursachen',['Damit das Pferd gleich zu Beginn müde wird','Aus reiner Gewohnheit ohne Nutzen'],'Hufe auskratzen gehört zu jedem Reiten dazu. Dabei sieht man Steine, lockere Eisen oder Verletzungen.'),
('Pferdekrankheiten & Erste Hilfe','Was gehört in eine Stallapotheke?','Verbandmaterial, Desinfektionsmittel, Fieberthermometer',['Nur Hufschmiere','Nur Futterzusätze'],'Einfache Grundausstattung für den Notfall. Medikamente gibt nur der Tierarzt.'),
# Umgang
('Umgang mit dem Pferd','Warum bleibt man nie direkt hinter dem Pferd stehen?','Es kann ausschlagen und man steht im toten Winkel',['Weil dort die Sonne blendet','Weil das Pferd es nicht mag zu beißen'],'Hinter dem Pferd sieht es einen schlecht und tritt im Schreck aus. Wenn man vorbeigehen muss, bleibt man mit Kontakt am Pferd und geht nah vorbei.'),
('Umgang mit dem Pferd','Wie hält man den Führstrick richtig?','Locker in der Hand, nie um Hand oder Arm wickeln',['Um das Handgelenk gewickelt','Ganz kurz um die Faust gebunden'],'Bei einem Schreck würde man sonst mitgeschleift. Der Strick wird in Schlaufen gehalten, nicht aufgewickelt.'),
('Umgang mit dem Pferd','Womit bindet man ein Pferd beim Putzen an?','Mit Panikhaken oder Knoten, der sich im Notfall lösen lässt',['Mit einem festen Knoten','Gar nicht, man hält den Kopf fest'],'Das Pferd soll sich im Notfall befreien können, ohne sich zu verletzen. Man bindet an einem festen Ring mit Sollbruchstelle oder Panikhaken.'),
('Umgang mit dem Pferd','Wie nimmt man einen Huf zum Auskratzen auf?','Von der Seite an das Bein streichen und Gewicht verlagern lassen',['Von vorne am Huf ziehen','Hinter dem Pferd stehen und reißen'],'Man steht seitlich zum Pferd, streicht am Bein entlang und nimmt den Huf in die Hand, wenn das Pferd das Gewicht verlagert.'),
('Umgang mit dem Pferd','Wie zeigt ein Pferd Unwohlsein oder Ärger im Gesicht?','Ohren angelegt, Nüstern gebläht, Zähne gezeigt',['Ohren nach vorn gerichtet, ruhiger Blick','Weicher Blick und halb geschlossene Augen'],'Angelegte Ohren sind eine Warnung. Die Ohren sind ein gutes Zeichen für Stimmung und Aufmerksamkeit des Pferdes.'),
('Umgang mit dem Pferd','Was tut man, wenn ein Pferd sich beim Führen erschreckt?','Ruhig bleiben, Distanz halten und ruhig sprechen',['Laut schreien und zerren','Festhalten und Strick aufwickeln'],'Pferde sind Fluchttiere und spüren die Ruhe ihres Menschen. Ruhige Stimme und ruhige Bewegungen helfen am meisten.'),
('Umgang mit dem Pferd','Wie belohnt man ein Pferd richtig nach einer gelungenen Übung?','Mit Lob, Streicheln oder Pause im richtigen Moment',['Nach einer halben Stunde','Gar nicht'],'Pferde verknüpfen Lob mit dem Moment, in dem es geschieht. Schnelle Belohnung festigt das Gelernte.'),
# Tierschutz
('Tierschutz','Welche Freiheiten gehören zum Wohlbefinden eines Tieres, zum Beispiel Freiheit von Hunger und Durst?','Bedürfnisgerechte Haltung, Fütterung und Gesundheit',['Nur eine große Box','Möglichst viel Training'],'Die Fünf Freiheiten beschreiben, was Tiere brauchen: Futter und Wasser, passende Umgebung, Gesundheit, normales Verhalten und Schutz vor Angst und Leid.'),
('Tierschutz','Warum ist Sozialkontakt für Pferde wichtig?','Pferde sind Herdentiere und brauchen Artgenossen',['Pferde leben am liebsten allein','Nur Fohlen brauchen andere Pferde'],'Wenn möglich sollen Pferde Kontakt zu Artgenossen haben, zum Beispiel in Gruppen- oder Paddockhaltung.'),
('Tierschutz','Wie viel Bewegung braucht ein Pferd täglich?','Möglichst täglich Auslauf und Bewegung',['Einmal pro Woche reicht','Nur im Sommer'],'Pferde sind Lauftiere. Regelmäßige Bewegung hält Muskeln, Kreislauf, Verdauung und Psyche gesund.'),
('Tierschutz','Was ist bei Hitze für Reitpferde wichtig?','Schatten, Wasser und kürzere ruhigere Einheiten',['Gerade mittags besonders hart arbeiten','Wasser entziehen'],'Bei Hitze kann das Pferd schnell überlastet werden. Man reitet in kühleren Tageszeiten oder kürzer und achtet auf Trinken.'),
('Tierschutz','Warum wird ein Pferd nach dem Reiten trockengeritten oder abgekühlt?','Damit Kreislauf und Muskeln langsam herunterfahren',['Damit es mehr schwitzt','Damit es schneller müde wird'],'Eine ruhige Schrittphase am Ende der Stunde schont Herz, Kreislauf und Muskulatur.'),
('Tierschutz','Wer ist für das Wohl des Pferdes verantwortlich?','Jeder, der mit dem Pferd umgeht',['Nur der Tierarzt','Nur der Besitzer'],'Reiter, Pfleger und Betreiber tragen gemeinsam Verantwortung. Auffälligkeiten meldet man rechtzeitig weiter.'),
]
for c,q,a,w,x in N:
    assert len(w)==2 and a not in w and "'" not in (c+q+a+x+''.join(w)), (q)
# duplicates vs existing
for c,q,a,w,x in N:
    assert q not in s, q
rows=''.join(" {c:'%s',q:'%s',a:'%s',w:['%s','%s'],x:'%s'},\n"%(c,q,a,w[0],w[1],x) for c,q,a,w,x in N)
anchor="\n];\n"
i=s.index("const Q=[")
j=s.index(anchor,i)
s=s[:j]+",\n /*theorie-luecken-2026-11-27*/\n"+rows.rstrip('\n')+s[j:]
s=s.replace('2026-11-26-sprache','2026-11-27-theorie')
open(p,'w',encoding='utf-8').write(s)
open('version.txt','w').write('2026-11-27-theorie')
print('ok',len(N))
