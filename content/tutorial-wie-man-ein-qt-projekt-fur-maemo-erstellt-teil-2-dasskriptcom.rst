Tutorial: Wie man ein Qt-Projekt für Maemo erstellt (Teil 2)
############################################################
:date: 2010-03-05 16:05
:slug: tutorial-wie-man-ein-qt-projekt-fur-maemo-erstellt-teil-2

Hier also nun der zweite Teil des Tutorials über das erstellen eines
Qt-Projekts für Maemo. Für alle, die neu dabei sind: `hier geht's zum
ersten Teil`_. Dort werden die ersten **vier Schritte** beschrieben.

.. raw:: html

   </p>

**Im fünften Schritt** bereiten wir das Projekt für die
Debian-Paketierung vor. Dazu könnt ihr den Qt Creator wieder schließen.
Der Debian-Paketierer braucht etwa zwei Hände voll Dateien, die das
Paket beschreiben. Diese Datein müssen in dem im ersten Schritt
erstellte "debian"-Ordner liegen. Um euch die Sache zu vereinfachen habe
ich euch diese Dateien als Beispiel in ein Archiv gepackt:

`Debian-Dateien für das mobileqt-Projekt`_

Die Dateien müsst ihr also aus dem Archiv in den "debian"-Ordner
entpacken. Folgende Dateien müssen für jedes Projekt angepasst werden:

-  **changelog:** Hier könnt ihr zunächst einmal euren Projektnamen
   eintragen. Für spätere Versionen muss das changelog jeweils erweitert
   werden, und zwar über den Befehl "debchange". Genaueres dazu gibt es
   `hier`_.
-  **control:** Hier muss zunächst Projektname und -beschreibung
   angepasst werden. In der Zeile "Maintainer:" sollte euer Name und
   E-Mail-Adresse stehen. Wichtig sind die Felder mit den Präfixen
   "XSBC-" bzw. "XB-". Um euer Paket später in das maemo-Repository zu
   bekommen (zur Installation über den Programmmanager), solltet ihr
   einen "XSBC-Bugtracker:" angeben. Die einfachste Möglichkeit ist eine
   Anmeldung eurer Anwendung bei "bugs.maemo.org", so wie es `hier`_
   beschrieben ist. Anschliessend könnt ihr den Anwendungsnamen in die
   Beispiel-control-Datei in den "product="-Parameter eintragen. Die
   Felder "XB-Maemo-Icon-26:" und "XSBC-Maemo-Display-Name:" geben ein
   Icon und einen Namen für den Programmmanager auf dem N900 an. Wenn
   ihr diese Felder leer lasst, dann wird kein Icon verwendet und es
   erscheint der Name, wie er in der "Package:" Zeile steht. Das Icon
   muss die Größe 48x48 haben. Wie ihr den Icon-Code für die
   "control"-Datei erstellt, könnt ihr `hier nachlesen`_. Wenn ihr kein
   Icon braucht dann könnt ihr das entsprechende Feld einfach aus
   "control" entfernen. Dieses Icon ist wie gesagt nur für den
   Programmmanager. Das Anwendungsicon für den Desktop haben wir im
   vierten Schritt abgehandelt.
-  **copyright:** Hier müsst hier halt euren Namen und die
   entsprechenden Copyright-Informationen eintragen.
-  **files:** In dieser Datei den Projektnamen ändern, bei späteren,
   neuen Versionen eurer Anwendung auch die Versionsnummer.

.. raw:: html

   </p>

Das war es dann auch schon für die Vorbereitung der Paketierung. Eine
genauere Beschreibung der einzelnen Dateien findet ihr beispielsweise
`hier`_.

.. raw:: html

   </p>

Nun müsst ihr für den **sechsten Schritt** den gesamten Verzeichnisbaum
in die virtuelle Maschine des SDKs kopieren. Also den VMWare Player
anwerfen, warten bis das SDK gebootet wurde, dann das Projekt komplett
in die Maschine kopieren; das sollte per Copy&Paste funktionieren, wenn
ihr die "VMWare Tools" innerhalb der virtuellen Maschine installiert
habt. Dort am Besten in den Pfad "/scratchbox/users/maemo/home/maemo",
dann habt ihr aus Scratchbox gleich Zugriff darauf:

|image0|

Anschließend startet ihr in der virtuellen Maschine ein Terminal. In
diesem Terminal startet ihr Scratchbox mit dem Befehl
"/scratchbox/login", in dieser Umgebung werden alle Maemo-Anwendungen
kompiliert. Mit "sb-conf select FREMANTLE\_ARMEL" wählt ihr innerhalb
von Scratchbox das ARMEL-Target aus, so läuft die Anwendung dann später
auf dem ARM-Prozessor des N900:

.. raw:: html

   <p>

::

    maemo@maemo-desktop:~$ /scratchbox/login Welcome to Scratchbox, the cross-compilation toolkit!Use 'sb-menu' to change your compilation target.See /scratchbox/doc/ for documentation.[sbox-FREMANTLE_X86: ~] > sb-conf select FREMANTLE_ARMELShell restarting...[sbox-FREMANTLE_ARMEL: ~] >

.. raw:: html

   </p>

Mit "cd mobileqt" ins Projektverzeichnis wechseln. Nun reicht ein
einfaches "dpkg-buildpackage -rfakeroot" um das .deb-Paket zu erstellen:

.. raw:: html

   <p>

::

    [sbox-FREMANTLE_ARMEL: ~] > cd mobileqt/[sbox-FREMANTLE_ARMEL: ~/mobileqt] > dpkg-buildpackage -rfakeroot  dpkg-buildpackage: source package is mobileqtdpkg-buildpackage: source version is 0.1-1dpkg-buildpackage: source changed by Peter Bouda dpkg-buildpackage: host architecture armeldpkg-buildpackage: source version without epoch 0.1-1: Using Scratchbox tools to satisfy builddeps... hier kommen viele Zeilen ...dpkg-deb: ignoring 3 warnings about the control file(s) dpkg-genchangesdpkg-genchanges: warning: unknown information field `Xb-Maemo-Icon-26' in input data in package's section of control info filedpkg-genchanges: including full source code in uploaddpkg-buildpackage: full upload; Debian-native package (full source is included)

.. raw:: html

   </p>

In dem Verzeichnis "über" dem Projektverzeichnis (im Beispiel:
"/scratchbox/users/maemo/home/maemo") findet ihr jetzt u.a. eine Datei
mit dem Namen "projektname\_0.1-1\_armel.deb". Glückwunsch: Dieses Paket
kann sofort auf dem N900 installiert werden!

.. raw:: html

   </p>

Im **siebten Schritte** installieren wir das Paket per "X Terminal" und
dem "dpkg"-Kommandozeilentool auf das N900. Dazu muss der root-Zugang
auf dem Gerät aktiviert sein, am einfachsten geht das per
`rootsh-Paket`_. Dann einfach die im sechsten Schritt erstellt
.deb-Datei auf das Gerät kopieren (per USB, Bluetooth, `SSH`_ oder auf
eine Speicherkarte). Ich kopiere die Datei meist per SSH nach
"/home/user/MyDocs", dann findet man die Datei später auch einfach per
Dateimanager (im Prinzip kann man das Paket auuh einfach per Klick im
N900-Dateimanager installieren, für coole Hacker wie uns wäre das aber
viel zu einfach). Auf dem Gerät das "X Terminal" starten und als erstes
mit "sudo gainroot" zum Chef werden. Dann in das Verzeichnis wecheln, in
dem die .deb-Datei liegt, und das Paket mit "dpkg -i
projektname\_0.1-1\_armel.deb" installieren:

.. raw:: html

   <p>

::

    ~ $ sudo gainrootRoot shell enabledBusyBox v1.10.2 (Debian 3:1.10.2.legal-1osso26+0,5) built-in shell (ash)Enter 'help' for a list of built-in commands./home/user # cd MyDocs/home/user/MyDocs # dpkg -i mobileqt_0.1-1_armel.deb(Reading database ... 25458 files and directories currently installed.)Unpacking mobileqt (from mobileqt_0.1-1_armel.deb) ...Setting up mobileqt (0.1-1) .../home/user/MyDocs #

.. raw:: html

   </p>

Fertig! Jetzt könnt ihr die Anwendung über den Anwendungsbildschirm
starten:

|image1|

|image2|

Wahnsinn: ein leeres Hauptfenster auf dem N900, selbst programmiert und
installiert! Bald mehr dazu, wie ihr das Fenster nun mit Inhalten füllt.
:-) Die Anwendung kann übrigens jederzeit per "dpkg -r projektname" im
Terminal oder über den Programmmanager wieder vom Gerät entfernt werden.

.. raw:: html

   </p>

Soweit also zum ersten Tutorial über die Qt-Entwicklung hier auf
`mobileqt.de`_. Ich hoffe die Schritte waren verständlich erklärt und
ihr konntet alles bei euch zu Hause nachvollziehen. Falls nicht: als
Alternative kommt demnächst wohl `MADDE`_ in Frage, womit sich die
Einstiegshürde deutlich senken wird. Über jede Rückmeldung zu diesem
Tutorial würde ich mich sehr freuen! Hier noch der komplette Download
der Beispielanwendung:

.. raw:: html

   </p>

`Download der kompletten Beispielanwendung inklusive aller Dateien`_

.. raw:: html

   <p>

.. raw:: html

   <script type="text/javascript"></p><p>var flattr_uid = '12306';</p><p>var flattr_tle = 'Tutorial: Wie man ein Qt-Projekt für Maemo erstellt (Teil 2)';</p><p>var flattr_dsc = 'Hier also nun der zweite Teil des Tutorials über das erstellen eines Qt-Projekts für Maemo. Für alle, die neu dabei sind: hier geht\'s zum ersten Teil. Dort werden die ersten vier Schritte beschrieb...';</p><p>var flattr_cat = 'text';</p><p>var flattr_lng = 'de_DE';</p><p>var flattr_tag = 'Maemo, C++, Tutorial, Paketerstellung';</p><p>var flattr_url = 'http://www.dasskript.com/blogposts/15';</p><p>var flattr_btn = 'compact';</p><p></script>

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

.. _hier geht's zum ersten Teil: http://www.mobileqt.de/blogposts/13
.. _Debian-Dateien für das mobileqt-Projekt: /tutorials/1/mobileqt_debian.zip
.. _hier: http://debiananwenderhandbuch.de/toolspakerzeugen.html#debchange
.. _hier: http://wiki.maemo.org/Bugs:Adding_Extra_products
.. _hier nachlesen: http://wiki.maemo.org/Packaging#Displaying_an_icon_in_the_Application_Manager_next_to_your_package
.. _hier: http://debiananwenderhandbuch.de/debianpaketeerstellen.html
.. _rootsh-Paket: http://wiki.maemo.org/Root_access#rootsh
.. _SSH: http://wiki.maemo.org/SSH
.. _mobileqt.de: http://mobileqt.de
.. _MADDE: http://wiki.maemo.org/MADDE
.. _Download der kompletten Beispielanwendung inklusive aller Dateien: /tutorials/1/mobileqt_tutorial1.zip

.. |image0| image:: /tutorials/1/tut1_7.png
.. |image1| image:: /tutorials/1/tut1_8.png
.. |image2| image:: /tutorials/1/tut1_9.png
