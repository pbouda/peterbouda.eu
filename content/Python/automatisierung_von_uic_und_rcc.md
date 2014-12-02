Title: Automatisierung von uic und rcc
Date: 2011-08-09 16:17
Category: Python

In einem PyQt- oder PySide-Projekt verwaltet man oft ein oder mehrere Ressourcen- und UI-Dateien. Diese Dateien erstellt man in einem C++-Qt-Projekt innerhalb des Qt Creator mit dem Qt Designer, mit den Kommandozeilen-Utilities `uic` bzw. `rcc` werden diese Dateien dann in C++-Code umgewandelt. Der Qt Creator bzw. Projektdatei und `qmake` nehmen dem Entwickler dabei die meiste Arbeit ab: die Code-Dateien werden automatisch aus den entsprechenden `ui`- und `qrc`-Dateien generiert. Sobald man eine der Dateien im visuellen Editor bearbeitet, wird beim nächsten Build alles automatisch aktualisiert. Wie sieht es aber unter Python aus? Häufig verwendet man hier ja nicht einmal eine komplette IDE, für kleine Projekte zut es gut und gern auch ein einfacher Code-Editor. Ich stelle hier ein kleines Skript vor, das auch ohne IDE zumindest einen Teil der Arbeit übernimmt. Zwar muss man das Skript bei jeder Änderung der `ui`- und `qrc`-Dateien manuell starten, aber zumindest muss man nicht mehr alle Dateien per Hand umwandeln.

# Projektgerüst

Ich setze hier voraus, dass ihr ein bestimmtes Projektgerüst verwendet. Die Ressourcendateien, UI-Dateien sowie Python-Code-Dateien befinden sich dabei in je einem eigenen Ordner. Da Ressourcendateien auf projektweite Dateien verweisen, befinden sie sich häufig im Hauptordner des Projekts. Ein typisches PyQt- bzw. PySide-Projekt sieht bei mir folgendermaßen aus:

![Projektgerüst PyQt-Projekt](|filename|../tutorials/11/tut11_1.png)

Der `bin`-Ordner enthält das Einstiegsskript der Anwendung. Dieses lädt die Klasse des Hauptfensters aus dem Package `helloworld`, das sich im Ordner `src` befindet. Die Hauptfensterklasse wiederum lädt den UI-Code aus dem Unterordner `ui`, also aus dem Package `helloworld.ui`. Die Original-UI-Dateien liegen unter `ui`, die Ressourcendatei `helloworld.qrc` liegt im Hauptordner des Projekts. Das Ziel ist es jetzt also, möglichst unkompliziert die UI-Dateien aus `ui` sowie die Ressourcendatei in Python-Code umzuwandeln und in den enstsprechenden Dateien im Ordner `src/helloworld/ui` abzulegen.

# Das Skript

Um diesen Schritt möglichst einfach und möglichst plattformunabhängig durchführen zu können, habe ich folgendes kleines Python-Skript geschrieben, dass diese Arbeit durchführt:

<pre class="brush:python;">
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from subprocess import call

if sys.platform == "win32":
    bindir = "c:/Python27/Lib/site-packages/PyQt4/bin"
else:
    bindir = "/usr/bin"

uic_path = os.path.join(bindir, "pyuic4")
#uic_path = os.path.join(bindir, "pyside-uic")
rcc_path = os.path.join(bindir, "pyrcc4")
#rcc_path = os.path.join(bindir, "pyside-rcc")
    
ui_path = "ui"
rc_path = ""
out_path = "src/helloworld/ui"

ui_files = { "helloworld.ui": "ui_helloworld.py" }
rc_files = { "helloworld.qrc": "helloworld_rc.py" }

for file in ui_files:
    file_path = os.path.join(ui_path, file)
    out_file_path = os.path.join(out_path, ui_files[file])
    call([uic_path, file_path, "-o", out_file_path])
    
for file in rc_files:
    file_path = os.path.join(rc_path, file)
    out_file_path = os.path.join(out_path, rc_files[file])
    call([rcc_path, file_path, "-o", out_file_path])
</pre>

Das Skript überprüft zunächst die Plattform und setzt entsprechend den Pfad zur den `rcc`- und `uic`-Tools von PyQt oder PySide (für PySide müssen die Kommentare entfernt werden). Falls die Tools in einem anderen Verzeichnis liegen (z.B. unter `/usr/local/bin` statt `/usr/bin`) dann müsst ihr nur die Variable `bindir` entsprechend anpassen. In den beiden Variablen `ui_files` und `rc_files` listet ihr dann alle eure UI- und Ressourcendateien auf, und gebt als Wert jeweils den gewünschten Ausgabedateinamen an. Bei mir landen alle Dateien ausschlueßlich in `src/helloworld/ui`, aber das könnt ihr selbstverständlich an eure Bedingungen anpassen. Jedes Mal, wenn ihr die Dateien dann in eurem Projekt ändert oder Dateien hinzufügt, dann ruft ihr einfach das Skript auf:

<pre class="brush:bash;">
python generate_ui.py
</pre>

Und schon habt ihr die Code-Dateien wieder auf dem aktuellen Stand.

Mehr über dieses Thema findet ihr zum Beispiel in meinem Buch <a href="http://www.amazon.de/gp/product/3941841505/ref=as_li_tf_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=3941841505&linkCode=as2&tag=jsusde-21">PyQt und PySide. GUI- und Anwendungsentwicklung mit Python und Qt</a><img src="http://www.assoc-amazon.de/e/ir?t=jsusde-21&l=as2&o=3&a=3941841505" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />.