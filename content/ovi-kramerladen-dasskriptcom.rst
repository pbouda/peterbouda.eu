Ovi-Krämerladen
###############
:date: 2010-12-01 10:51
:slug: ovi-kramerladen-dasskriptcom

Ich bin ja von Nokia mittlerweile so einiges gewohnt, durch zahlreichen
Workarounds für alle möglichen Bugs in Qt und Qt Mobility für Maemo und
Symbian gestählt, aber was im Moment im Ovi Store passiert übertrifft
alles Andere bei Weitem. Entgegen meiner Gewohnheit muss ich deswegen in
diesem Blog meinem Ärger mal Luft machen. Ich hätte mich bisher
tatsächlich als Nokia-Fan bezeichnet. Mein erstes Handy war von Nokia,
mein Jetziges sowieso, dazwischen hab ich immer mal wieder andere
Hersteller ausprobiert, und bin dann reumütig zurückgekehrt. Nokia war
halt das Beste. Seit einiger Zeit entwickle ich nun auch Software für
Nokia-Handys, zuerst Java-Anwendungen, dann Qt; denn großer Qt-Fan war
ich sowieso schon immer. Und so kommt man eben irgendwann auf die Idee,
dass man ja auch mal eine Anwendung verkaufen möchte, und der Ovi Store
soll sowas ja unterstützen. Und man hat ja auch schon Anwendungen
drinnen, die sind nicht so toll, aber hey: die Entwicklung hat Spaß
gemacht, und ein paar Leut' laden sie auch runter. Also programmiert man
fleißig, testet alles konsequent, baut um Bugs herum, und nach
wochenlanger Arbeit stellt man das Ganze in die QA-Queue bei Ovi
Publish. Dann heißts warten: 5 Wochen hat's gedauert, bis Nokia endlich
mal soweit war, für eine Anwendung mit exakt einem (in Zahlen: 1)
Fenster, eine kleine Ewigkeit, während rundherum die tollsten
Anwendungen für Android und iPhone erscheinen, sogar Microsoft bringt in
der Zwischenzeit ein mehr als konkurrenzfähiges Betriebssystem auf den
Markt, der Qt-Entwickler schielt darauf mit neidischen Blicken; trotzdem
große Freude zuerst, aber dann: irgendein Nokia-Mitarbeiter setzt das
Veröffentlichungsdatum noch einmal vier Wochen in die Zukunft.
Kommentarlos. Also eine Mail an den Ovi Publish Support, die Antwort
dauert nur 3 Tage, erfolgt aber in Form einer Standardmail. Thema
verfehlt. Also noch eine Mail hinterher, und dieses Mal antwortet
tatsächlich jemand und sagt::

    After investigating further we found the QA team had indeed change the
    start date to December 1, 2010 as OVI Store Maemo firmware PR1.3 mode
    for N900 is unavailable so instead of failing your app QA team instead
    changed the date till the new firmware PR1.3 is ready. Since QA team
    found your application only works with PR1.3, it cannot be published
    until the store is set to PR1.3 therefore QA team will update the start
    date again on your behalf.

Aber Nokia: was genau funktioniert denn nicht? Ich habe alles für PR 1.2
programmiert, warum sollte es dann nur mit PR 1.3 funktionieren?
Außerdem ist PR 1.3 doch offiziell erschienen, mittlerweile...? Diese
Fragen bleiben offen, nähere Informationen bekommt man nicht. Aber was
sind schon 4 Wochen für Nokia? Also heißt es noch einmal warten,
geduldig, bis 1.12., der Tag an dem die Anwendung laut Nokia erscheinen
soll. Aber was passiert am 30.11.? Das Startdatum wird wieder geändert,
kommentarlos, auf den 31.12., wieder keine weiteren Informationen für
den kooperationswilligen Entwickler; verdammt, Nokia: dann sagt mir
wenigstens, was ich bei der Anwendung korrigieren soll, damit ihr sie in
den Store aufnehmt! Bei anderen Anwendungen habe ich nichts anderes
hineinprogrammiert, und die habt ihr ohne Probleme angenommen. Und
jetzt? Soll ich noch einmal 4 Wochen warten? Und dann noch einmal? Gibt
es Nokia dann überhaupt noch?

Was im Moment bei Nokia los ist, weiß der Teufel. Für mich als
Entwickler ist es aber mehr als frustrierend, wenn man nicht einmal ein
vernünftiges Feedback bekommen, um eine einfache Anwendung vernünftig
für den Ovi Store vorbereiten zu können. Ich habe nichts gegen eine
strenge QA, gegen ein bisschen Qualität im Laden. Aber sagt doch
wenigstens, was man tun muss, um in die geheiligten Hallen vorgelassen
zu werden. Und bestimmt nicht einfach hinter meinem Rücken über meine
Anwendung. Erst nach dem Login bei Ovi Publish und Blick in die
Anwendungsdaten habe ich vom geänderten Startdatum erfahren. Das ist
einfach keine Art und Weise mit Entwicklern für das eigene System
umzugehen, finde ich. Schließlich nehmt ihr dafür auch noch 30 Prozent,
da darf man wohl ein bisschen Entgegenkommen erwarten.

Der Frust hat sich jetzt schon länger bei mir aufgebaut: die
QA-Wartezeiten bei Nokia sind katastrophal, mein zu Entwicklungszwecken
erstandenes C7 funktioniert immer noch nicht, und kein Mensch weiß, wie
man denn in einem Jahr Software für Nokia-Handys entwicklen wird. Qt
wird's wohl sein, aber die bisherigen Widgets und Layout passen einfach
nicht zu einem mobilen Betriebssystem, es gibt immer noch keine
vernünftige Lösung für Portrait-Landscape-Darstellung; QML ist gut, aber
sollen wir in Zukunft alle Widgets selber malen? Da muss ich noch einmal
auf Microsoft verweisen, die ein sowohl für Anwender als auch Entwickler
mehr als innovatives System auf die Beine gestellt hat, dass sich meiner
Ansicht nach gerade durch eine klare Definition von GUI-Vorgaben mit
äußerst benutzerfreundlichen und bisher nicht gesehenen Oberflächen und
technischen Schnittstellen auszeichnet und für das man schon mehr als
ein halbes Jahr vor Veröffentlichung ein (fast) definitives SDK bekommen
hat, um seine Anwendungen zu schreiben. So einfach wie Qt, dank
Silverlight mehr oder weniger plattformunabhängig, technisch dank
Zugriff auf zahlreichen Web-APIs und Datenmodelle weit voraus und
trotzdem leicht zu programmieren. Und die restliche Konkurrenz schläft
ja auch nicht. Nokia, ich habe bisher treu zu dir gehalten, und nichts
auf dich kommen lassen, aber mal ganz ehrlich: der Glaube, dass du in
zwei Jahren noch bzw. wieder konkurrenzfähige Mobiltelefone produzieren
wirst schwindet bedenklich, und das nicht erst mit Blick auf die
Konkurrenz.
