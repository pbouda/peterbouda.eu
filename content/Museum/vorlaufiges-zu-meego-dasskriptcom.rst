Vorläufiges zu MeeGo
####################
:date: 2010-03-03 11:54
:slug: vorlaufiges-zu-meego

`MeeGo`_ wird also nun das neue mobile Betriebssystem von Nokia und
Intel heißen; nach dem `oFono-Projekt`_ jetzt also die zweite große
Zusammenarbeit zwischen den beiden Firmen. Bei MeeGo handelt es sich um
einen Zusammenschluss zwischen Maemo (dem Linux von Nokia) und Moblin
(dem Intel-Linux) und, was für mich das Entscheidenste an der Sache ist,
wird ein komplett Qt-basiertes UI haben, wie es ja auch schon für
`geplant war. Der größte Diskussionspukt unter Entwicklern war übrigens
das zu verwendende Paketformat für MeeGo: hier gab es die
(Intel-)RPM-Fraktion, die es mit einer skeptischen (Nokia-)-DEB-Gruppe
zu tun hatte. Offensichtlich wird es aber wohl bei der offiziellen
Vorgabe RPM bleiben. Genaueres zu MeeGo lassen sich in Nokia
offizieller`_\ `Software-Strategie`_ sowie in einem hervorragenden
`Artikel von Zchydem`_ nachlesen.

Für Qt-Entwickler gibt es ein interessantes Bild, das in den meisten
Beiträgen auftauchte:

|image0|

Qt wird also die zentrale Entwicklungsumgebung für MeeGo. Für die breite
Masse der Entwickler sieht Nokia die "Web RunTime" (WRT) vor, die auf
der Qt-Webkit-Implementierung basiert. Schon jetzt können ja Qt-Widgets
in QWebKit per HTML dargestellt werden, hier bieten sich in der WRT in
Zukunft interessante Anwendungsmöglichkeiten (Notiz an selbst: Zeit also
für einen baldigen Artikel zu QWebKit...). Rechen- und Hardwareintensive
wie Spiele, Fotoapplikationen etc. sollen nativ in Qt bzw. "hybrid"
entwickelt werden.

Was bedeutet das nun für den Technologiebegeisterten Qt-Entwickler? Nun,
aus meiner Sicht würde ich mir ein paar der zukünftige Kerntechnologien
näher anschauen:

-  `QML`_ gehört mit Sicherheit dazu, evtl. sogar als Haupt-UI-Sprache
   für die WRT und Qt
-  aufbauend darauf kommt mit `Qt Quick`_ eine Komplettlösung für Qt 4.7
   und den Qt Creator
-  QWebKit wird in Zukunft noch einer wichtigere Rolle spielen
-  `Qt Mobility`_ und die Ovi Services werden vermutlich integriert
   werden
-  Dabei wiederum werden GPS-Daten und Karten die Hauptrolle für
   zukünftige Dienste und UIs sein, wenn ich `dieses Interview`_ richtig
   deute; vielleicht wars aber nur eine Ausrede für den ja so sehr
   kritisierten Kauf von Navteq

Jedenfalls würde ich das mal als spannende Aussichten für jeden
Qt-Entwickler bezeichnen!

.. _MeeGo: http://meego.com/
.. _oFono-Projekt: http://ofono.org/
.. _`geplant war. Der größte Diskussionspukt unter Entwicklern war übrigens das zu verwendende Paketformat für MeeGo: hier gab es die (Intel-)RPM-Fraktion, die es mit einer skeptischen (Nokia-)-DEB-Gruppe zu tun hatte. Offensichtlich wird es aber wohl bei der offiziellen Vorgabe RPM bleiben. Genaueres zu MeeGo lassen sich in Nokia offizieller`: http://qt.gitorious.org/maemo-6-ui-framework
.. _Software-Strategie: http://www.nokia.com/NOKIA_COM_1/Technology/pdf/Nokia_software_strategy_white_paper.pdf
.. _Artikel von Zchydem: http://zchydem.enume.net/2010/02/26/meego-thoughts/
.. _QML: 
.. _Qt Quick: http://blog.qt.nokia.com/2010/02/15/meet-qt-quick/
.. _Qt Mobility: http://labs.trolltech.com/page/Projects/QtMobility
.. _dieses Interview: http://www.allaboutmaemo.com/news/item/11200_Video_Anssi_Vanjoki_on_the_fut.php

.. |image0| image:: http://meego.com/sites/all/files/users/u6/MeeGo-Arch.png
