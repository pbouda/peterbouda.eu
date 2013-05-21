Processing auf dem N900 @ dasskript.com
#######################################
:date: 2010-03-20 11:28
:author: pbouda
:slug: processing-auf-dem-n900-dasskriptcom

Processing ist eine Java-basierte Programmiersprache, die bisher vor
allem im Computerkunstbereich eingesetzt wird und sich dort wegen ihrer
einfachen Erlernbarkeit und einer hervorragenden Grafikbibliothek großer
Beliebtheit erfreut. Aber auch im Embedded-Bereich wird Processing z.B.
Schaltungen mit `dem Mikrokontroller Arduino`_ verwendet. Und es `macht
Spaß`_.

.. raw:: html

   </p>

Vor kurzem hat nun Jayesh Salvi eine `Website mit einer
Javascript-Processing-Umgebung`_ veröffentlicht. Die Beispiele auf der
Website funktionieren alle recht gut auch auf dem N900, ich hatte aber
Probleme mit den Mouse-Events. In den von mir getesteten Browsern
(MicroB, Midori, Firefox) konnte ich keine vernünftigen Toucheingaben
machen, weil meist der Browser diese Eingaben abfängt um z.B. den
Bildschirm zu scrollen. Am Besten funktionierte es mit Midori, der eine
WebKit-Engine verwendet. Also habe ich ein kleines PySide-Skript
geschrieben, dass mir nur die die Processing-Umgebung unter
"http://p.altcanvas.com/" öffnet und den MicroB-UserAgent-String
schickt:

.. raw:: html

   </p>

.. raw:: html

   <p>

::

    # This code is public domainimport sysfrom PySide import QtGui, QtWebKit, QtCoredef main():    app = QtGui.QApplication(sys.argv)    QtGui.QApplication.setApplicationName("Processing")    MainWindow = QtWebKit.QWebView()    page = MyWebPage()    MainWindow.setPage(page)    MainWindow.show()    MainWindow.load(QtCore.QUrl("http://p.altcanvas.com/"))    sys.exit(app.exec_())class MyWebPage(QtWebKit.QWebPage):    def __init__(self):        QtWebKit.QWebPage.__init__(self)    def userAgentForUrl(self, url):        return "Mozilla/5.0 (X11; U; Linux armv7l; de-DE; rv:1.9.2a1pre) Gecko/20091127 Firefox/3.5 Maemo Browser 1.5.6 RX-51 N900"        main()

.. raw:: html

   </p>

Und siehe da: MouseClicked- und MouseDragged-Events funktionieren auf
dem N900 einwandfrei! Ich habe auf der Website ein Projekt namens
"touch" freigegeben, dieses könnt ihr in der "Gallery" ausprobieren.
Damit das Python-Skript auf dem N900 läuft müsst ihr das Paket
"pyside-qt4-webkit" aus "extras-devel" installieren. Ihr könnt das
Skript auch auf dem Desktop starten und seht so, wie sich das
Processing-Programm auf dem N900 verhalten wird. Entwickeln könnt ihr
ganz einfach auf der Website im Desktop-Browser.

.. raw:: html

   </p>

Hier ein kleines Screen-Video:

.. raw:: html

   </p>

.. raw:: html

   </p>

Das Python-Skript könnt ihr auch `hier herunterladen`_.

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   <script type="text/javascript"></p><p>var flattr_uid = '12306';</p><p>var flattr_tle = 'Processing auf dem N900';</p><p>var flattr_dsc = 'Processing ist eine Java-basierte Programmiersprache, die bisher vor allem im Computerkunstbereich eingesetzt wird und sich dort wegen ihrer einfachen Erlernbarkeit und einer hervorragenden Grafikbibli...';</p><p>var flattr_cat = 'text';</p><p>var flattr_lng = 'de_DE';</p><p>var flattr_tag = 'N900, Processing, QWebKit, PySide';</p><p>var flattr_url = 'http://www.dasskript.com/blogposts/27';</p><p>var flattr_btn = 'compact';</p><p></script>

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

.. _dem Mikrokontroller Arduino: http://www.heise.de/ct/projekte/machmit/processing/wiki/
.. _macht Spaß: http://peterbouda.blogspot.com/search/label/Arduino
.. _Website mit einer Javascript-Processing-Umgebung: http://jyro.blogspot.com/2010/03/portable-apps-for-iphone-android-pre.html
.. _hier herunterladen: http://peterbouda.de/downloads/processing.py.txt
