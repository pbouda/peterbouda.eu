Buchempfehlung: Mastering Regular Expressions von Jeffrey E.F. Friedl
#####################################################################
:date: 2011-05-13 10:28
:category: Bücher
:slug: buchempfehlung-mastering-regular-expressions-von-jeffrey-ef-friedl-dasskriptcom

Und da dachte ich, ich weiß schon so Einiges über reguläre Ausdrücke.
Aber nichts da: spätestens im dritten Kapitel von *Mastering Regular
Expressions* von Jeffrey E.F. Friedl schwand der Glaube an meine
Fähigkeiten. Die Einsatzmöglichkeiten von *Atomic Groupings* und
*Possessive Quantifiers* waren mir gar vollkommen fremd. Nach Lektüre
des Buches war der Glaube aber wieder da.

.. raw:: html

   </p>

Das Buch beginnt mit drei sehr praxisorientierten Kapiteln über reguläre
Ausdrücke, die sich zu Beginn auch dem Anfänger erschließen. Die
Beispiele sind schön ausgewählt, werden im Laufe der Kapitel immer
komplexer, und zeigen den Einsatz der Basisfunktionen in regulären
Ausdrücken. Gleich in der Einleitung empfiehlt Herr Friedl auch dem
fortgeschrittenen Leser, das Buch von vorn bis hinten zu lesen, und dem
kann ich unbedingt zustimmen: selbst wenn man die Basis schon drauf hat,
lernt man gleich zu Beginn Vieles über die Geschwindigkeitsvorteile und
-nachteile bestimmter Alternativen bei Ausdrücken in unterschiedlichen
Einsatzgebieten.

.. raw:: html

   </p>

Ab dem vierten Kapitel geht es dann ans Eingemachte. Die interne
Verabeitung der verschiedene Implementierungen werden besprochen,
zunächst grob nach der Einteilung in deterministische bzw.
nicht-deterministische Automaten, in beiden Fällen aber auch immer
wieder mit Hinweisen auf einzelne Implementierung der verschiedenen
Programmiersprachen. Wer hätte es gedacht: Tcl hat die schnellste
Maschine für reguläre Ausdrücke, Perl dafür den umfangreichsten
Wortschatz an Ausdrücken. Das *Backtracking* als zentrale Idee des
Parsens regulärer Ausdrücke wird ausführlich und verständlich erläutert,
fast denkt der Leser daran, rasch selber eine solchen Parser zu bauen.
Gerade in diesem Kapitel merkt man die langjährige Erfahrung des Autors,
der durch den Einsatz unterschiedlicher Engines und Fehlersuche in
zahlreichen Projekten einen großen Einfluss auf die ein oder andere
Implementierung hatte.

.. raw:: html

   </p>

Nach den Interna der Verarbeitung folgen dann zwei Kapitel, nach deren
Lektüre man sich durchaus als Experte einordnen darf. Zunächst geht es
um den allgemeinen Aufbau eines regulären Ausdrucks, wiederum an
Praxisbeispielen, und dieses Mal mit dem gesamten, im vorhergegangenen
Kapitel erarbeiteten Inventar. Das darauf folgende Kapitel geht noch
ausführlich auf die Performanz von regulären Ausdrücken ein, so dass man
sich als Leser schließlich für alle Anwendungsfälle gerüstet fühlt. Als
wäre das alles noch nicht genug, folgen schließlich noch vier Kapitel
über die regulären Ausdrücke und ihren praktischen Einsatz in vier
Programmiersprachen bzw. Frameworks (Perl, Java, .NET, PHP). Schade,
dass hier Python keine größere Rolle spielt, aber die derzeitige
Implemtierung scheint auch einfach noch nicht besonders ausgereift zu
sein. Mit dem `neuen Python regex-Modul`_ steht aber wohl schon der
Ersatz in den Startlöchern.

.. raw:: html

   </p>

Am Ende bleibt tatsächlich keine Frage offen. Im der täglichen
Entwicklungsarbeit blättert man schnell immer wieder an die
entsprechenden Stellen des Buches, und reift so langsam zum Experten
auch in der Praxis. Atomic Groupings, Possessive Quantifiers,
Backtracking, Laziness vs. Greediness? Alles kein Problem...

.. raw:: html

   </p>

Zu kaufen bei Amazon:

.. raw:: html

   </p>

`Mastering Regular Expressions von Jeffrey E.F. Friedl`_

.. raw:: html

   <p>

.. raw:: html

   <script type="text/javascript"></p><p>var flattr_uid = '12306';</p><p>var flattr_tle = 'Buchempfehlung: Mastering Regular Expressions von Jeffrey E.F. Friedl';</p><p>var flattr_dsc = 'Und da dachte ich, ich weiß schon so Einiges über reguläre Ausdrücke. Aber nichts da: spätestens im dritten Kapitel von Mastering Regular Expressions von Jeffrey E.F. Friedl schwand der Glaube an ...';</p><p>var flattr_cat = 'text';</p><p>var flattr_lng = 'de_DE';</p><p>var flattr_tag = 'Buchempfehlung, Reguläre Ausdrücke';</p><p>var flattr_url = 'http://www.dasskript.com/blogposts/89';</p><p>var flattr_btn = 'compact';</p><p></script>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   <script src="http://api.flattr.com/button/load.js" type="text/javascript"></script>

.. raw:: html

   </p>

.. raw:: html

   </p>

.. _neuen Python regex-Modul: http://pypi.python.org/pypi/regex
.. _Mastering Regular Expressions von Jeffrey E.F. Friedl: http://www.amazon.de/gp/product/0596528124/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=jsusde-21&linkCode=as2&camp=1638&creative=6742&creativeASIN=0596528124
