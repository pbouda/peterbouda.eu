Tutorial: Wie man ein Qt-Projekt für Maemo erstellt (Teil 1)
############################################################
:date: 2010-03-04 14:53
:slug: tutorial-wie-man-ein-qt-projekt-fur-maemo-erstellt-teil-1

Hier mal kurz und knapp, wie ihr möglichst schnell zu einem Qt-Projekt
kommt, das ihr als Debian-Paket auf dem N900 installieren könnt:
definitiv das kompakteste Tutorial, das es zu diesem Thema gibt. Als
Voraussetzung müsst ihr zunächst einmal den `Qt Creator`_ installieren,
außerdem sollte ihr das offizielle `Maemo-SDK als virtuelles Image`_
installiert und startklar haben (ihr braucht die Desktop-Version des
SDKs, also die Datei
"Maemo\_Ubuntu\_Intrepid\_Desktop\_SDK\_Virtual\_Image\_Final.7z"). Das
SDK ist ein virtuelles Image, ihr startet das Entwicklungsbetriebssystem
am Besten mit dem `VMWare Player`_. Der Qt Creator-Download beinhaltet
im Übrigen alle nötigen Bibliotheken, das Qt-SDK müsst ihr also nicht
separat installieren.

Ich werde das Tutorial in zwei Teilen veröffentlichen, der erste Teil
beschäftigt sich mit der Erstellung des Qt-Projekts, der zweite dann mit
der Paketerstellung für das N900.

**Als erstes** erstellt ihr in eurem Projektordner drei Unterordner:
"src" (für den ganzen Quellcode), "debian" (für die Debian-Daten) und
"data" (für Icons usw.):

|image0|

**Als zweites** legt ihr das Projekt mit dem Qt Creator an. Dieser wird
also gestartet und dann über "Datei->Neu" ein neues Projekt angelegt. Im
ersten Dialog wählt ihr als Projekttyp "Qt4-Gui-Anwendung":

|image1|

Im zweiten Dialog gebt ihr den Projektnamen ein und wählt das oben
erstellte "src"-Verzeichnis als "Erzeugen in:"-Pfad:

|image2|

Die folgenden beiden Dialoge für die zu integrierenden Module und den
Klassennamen für das Hauptfenster könnt ihr bei den vorgegebenen
Einstellungen belassen. Am Schlusss auf "Abschließen" klicken, und Qt
Creator erstellt euch alle nötigen Projektdateien. Blöderweise macht er
das aber in einem "Projektname"-Unterordner in "src". Alle Dateien
sollen aber direkt im Verzeichnis "src" liegen. Also schließt ihr den Qt
Creator erst einmal wieder, und kopiert alle Dateien aus dem
"Projektname"-Unterordner direkt nach "src". Der
"Projektname"-Unterordner kann dann gelöscht werden. Bei dieser
Gelegenheit nennt ihr die "Projektname.pro"-Datei um nach "src.pro".
Nach diesem Schritt sollte euer Projektbaum so ausschauen:

|image3|

**Als dritten Schritt** erstellt ihr in eurem Haupt-Projektordner (im
Beispiel der Ordner "mobileqt") eine Datei mit dem Namen
"projektname.pro" (klein geschrieben; im Beispiel "mobileqt.pro"). Diese
Datei füllt ihr mit folgendem Inhalt, am Besten mit einem einfache
Texteditor wie "gedit" o.ä.::

  QMAKEVERSION = $$[QMAKE_VERSION]
  ISQT4 = $$find(QMAKEVERSION, ^[2-9])
  isEmpty( ISQT4 ) {
  error("Use the qmake include with Qt4.4 or greater, on Debian that is qmake-qt4");
  }

  TEMPLATE = subdirs
  SUBDIRS  = src

Diese Datei könnt ihr jetzt wieder mit dem Qt Creator öffnen, ein
Doppelklick auf "projektname.pro" sollte das bewerkstelligen.

**Im vierten Schritt** sollte euer Qt Creator zunächst folgendermaßen
ausschauen:

|image4|

Mit dem Play-Button unten links könnt ihr das Projekt starten, es sollte
ein leeres Hauptfenster erscheinen. Für den Anfang reicht uns das, wir
werden das Fenster in anderen Tutorials mit Inhalt und Menü versehen. Um
das Programm später auf dem N900 installieren zu können muss jetzt die
"src.pro" angepasst werden. Mit einem beherzten Doppelklick auf den
entsprechenden Eintrag unter "projektname->src->scr.pro" im Qt Creator
öffnet ihr die Datei zum Editieren und fügt folgenden Code hinzu::

  unix {
      #VARIABLES
      isEmpty(PREFIX) {
          PREFIX = /usr/local
      }

      BINDIR = $$PREFIX/bin
      DATADIR =$$PREFIX/share

      DEFINES += DATADIR=\"$$DATADIR\" PKGDATADIR=\"$$PKGDATADIR\"

      #MAKE INSTALL

      INSTALLS += target desktop scalable

      target.path =$$BINDIR

      desktop.path = $$DATADIR/applications/hildon
      desktop.files += ../data/$${TARGET}.desktop

      scalable.path = $$DATADIR/icons/hicolor/scalable/hildon
      scalable.files += ../data/scalable/$${TARGET}.png

  }

Diese Anweisungen werden später, nach Erstellung des Debian-Pakets, das
kompilierte Programm, eine Desktop-Datei und ein Icon auf das Gerät
installieren. Dazu müsst ihr noch im "data"-Verzeichnis eine Datei
"projektname.desktop" erstellen, die in etwa folgenden Inhalt haben
sollte::

  [Desktop Entry]
  Encoding=UTF-8
  Version=0.1
  Type=Application
  Name=mobileqt
  Exec=mobileqt
  Icon=mobileqt
  X-HildonDesk-ShowInToolbar=true
  X-Osso-Type=application/x-executable

Unter "data/scalable" legt ihr das Icon für die Anwendung als .png- oder
.jpg-Datei ab, die Größe sollte 64x64 Pixel betragen. Am Ende dieses
ersten Teils des Tutorials solltet ihr dann folgende Projektstruktur vor
euch haben:

|image5|

Dieses war der erste Teil des Tutorials. Im zweiten Teil werden wir die
Anwendung für die Debian-Paketierung vorbereiten, das Ganze dann in
Scratchbox (auf dem virtuellen Image) kompilieren und packen und
anschließend auf das N900 installieren.

`Hier geht's direkt zum zweiten Teil des Tutorials`_

.. _Qt Creator: http://qt.nokia.com/downloads
.. _Maemo-SDK als virtuelles Image: http://maemovmware.garage.maemo.org/2nd_edition/
.. _VMWare Player: http://www.vmware.com/de/products/player/
.. _Hier geht's direkt zum zweiten Teil des Tutorials: |filename|tutorial-wie-man-ein-qt-projekt-fur-maemo-erstellt-teil-2-dasskriptcom.rst

.. |image0| image:: /static/tutorials/1/tut1_1.png
.. |image1| image:: /static/tutorials/1/tut1_2.png
.. |image2| image:: /static/tutorials/1/tut1_3.png
.. |image3| image:: /static/tutorials/1/tut1_4.png
.. |image4| image:: /static/tutorials/1/tut1_5.png
.. |image5| image:: /static/tutorials/1/tut1_6.png
