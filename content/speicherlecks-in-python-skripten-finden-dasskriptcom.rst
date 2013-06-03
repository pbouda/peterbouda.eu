Speicherlecks in Python-Skripten finden
#######################################
:date: 2011-08-19 11:10
:slug: speicherlecks-in-python-skripten-finden

Da ich gerade ein kleines Speicherproblem mit einer Python-Anwendung
hatte (und ich dachte schon, 8 GB RAM reichen erst einmal...), habe ich
mich mal nach einem Memory-Profiler für Python-Skripte umgeschaut. Und
leider nichts Vernünftiges gefunden. Was auch daran liegt, dass ich
komplett auf Python 3 umgestiegen bin, und die Python-2-Profiler dann
leider komplett den Dienst versagen. Hier mal drei Pakete, die wohl
unter Python 2 funktionieren sollen:

-  `heapy`_: Ist angeblich das komplexeste, aber auch beste aller Tools.
   Als Ergebnis einer Master-Thesis entstanden, die es auch auf der
   Webseite zum Herunterladen gibt. Portierung auf Python 3 wohl nicht
   in Sicht. Und nach kurzer Ansicht des Quellcodes wohl auch nicht mal
   an einem Nachmittag durchführbar.
-  `PySizer`_: Weniger mächtig als heapy, und noch älter. Portierung
   nicht in Sichtweite.
-  `dowser`_: Die einfachste Art und Weise für Memory-Profiling. Das
   Tool lässt sich äußerst einfach in eigene Python-Skripte einbinden
   und stellt die Information dann per cherrypy zur Verfügung. So hat
   man während der Laufzeit des Skripts in einem Webbrowser einen
   Überblick über die aktuellen Objekte und deren Speicherverbrauch. Ich
   habe es fast geschafft, das Ding unter Python 3 zum Laufen zu
   bringen; allerdings benutzt es die Python Imaging Library, für die es
   noch keine vernünftige Python-3-Version gibt. So fehlen auf der
   Ausgabe-Webseite dann die Bilder. Außerdem konnte ich die
   TRACE-Seiten nicht öffnen. Es waren wohl einfach zu viele Objekte in
   meinem Skript.

Wieder einmal das leidige Thema: Python 3 ist bestimmt toll, aber wenn
es halt jeder ignoriert werden wir in 10 Jahren immer noch Anwendungen
unter Python 2.x entwickeln. Übrigens habe ich letztendlich einen
anderen Weg für das Speicherproblem gefunden. Das Problem war ein
Parser; mit regulären Audrücken komme ich jetzt mit weniger Speicher und
viel schneller ans Ziel.

.. _heapy: http://guppy-pe.sourceforge.net/#Heapy
.. _PySizer: http://pysizer.8325.org/
.. _dowser: http://www.aminus.net/wiki/Dowser
