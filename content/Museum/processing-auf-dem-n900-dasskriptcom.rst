Processing auf dem N900
#######################
:date: 2010-03-20 11:28
:slug: processing-auf-dem-n900

Processing ist eine Java-basierte Programmiersprache, die bisher vor
allem im Computerkunstbereich eingesetzt wird und sich dort wegen ihrer
einfachen Erlernbarkeit und einer hervorragenden Grafikbibliothek großer
Beliebtheit erfreut. Aber auch im Embedded-Bereich wird Processing z.B.
Schaltungen mit `dem Mikrokontroller Arduino`_ verwendet. Und es `macht
Spaß`_.

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
schickt::

   # This code is public domain
   import sys
   from PySide import QtGui, QtWebKit, QtCore

   def main():
       app = QtGui.QApplication(sys.argv)
       QtGui.QApplication.setApplicationName("Processing")
       MainWindow = QtWebKit.QWebView()
       page = MyWebPage()
       MainWindow.setPage(page)
       MainWindow.show()
       MainWindow.load(QtCore.QUrl("http://p.altcanvas.com/"))
       sys.exit(app.exec_())

   class MyWebPage(QtWebKit.QWebPage):

       def __init__(self):
           QtWebKit.QWebPage.__init__(self)

       def userAgentForUrl(self, url):
           return "Mozilla/5.0 (X11; U; Linux armv7l; de-DE; rv:1.9.2a1pre) Gecko/20091127 Firefox/3.5 Maemo Browser 1.5.6 RX-51 N900"
           
   main()

Und siehe da: MouseClicked- und MouseDragged-Events funktionieren auf
dem N900 einwandfrei! Ich habe auf der Website ein Projekt namens
"touch" freigegeben, dieses könnt ihr in der "Gallery" ausprobieren.
Damit das Python-Skript auf dem N900 läuft müsst ihr das Paket
"pyside-qt4-webkit" aus "extras-devel" installieren. Ihr könnt das
Skript auch auf dem Desktop starten und seht so, wie sich das
Processing-Programm auf dem N900 verhalten wird. Entwickeln könnt ihr
ganz einfach auf der Website im Desktop-Browser.

Das Python-Skript könnt ihr auch `hier herunterladen`_.

.. _dem Mikrokontroller Arduino: http://www.heise.de/ct/projekte/machmit/processing/wiki/
.. _macht Spaß: http://peterbouda.blogspot.com/search/label/Arduino
.. _Website mit einer Javascript-Processing-Umgebung: http://jyro.blogspot.com/2010/03/portable-apps-for-iphone-android-pre.html
.. _hier herunterladen: http://peterbouda.de/downloads/processing.py.txt
