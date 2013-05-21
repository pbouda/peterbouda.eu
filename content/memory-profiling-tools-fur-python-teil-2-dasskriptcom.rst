Memory Profiling Tools für Python, Teil 2
#########################################
:date: 2011-09-02 11:33
:category: Python
:slug: memory-profiling-tools-fur-python-teil-2-dasskriptcom

Kaum hatte ich den `vorhergehenden Blogeintrag`_ fertig, bin ich mehr
oder weniger zufällig auf zwei weitaus interessantere Projekte gestoßen,
die Speicherlecks in Python-Anwendungen aufspüren sollen. Hier also, der
Vollständigkeit halber:

*  `Meliae`_: Für Python 2, wird aber im Gegensatz zu heapy aktiv weiter
   entwickelt. Für meine Zwecke aber derzeit unbrauchbar, bis es auch
   mit Python 3 funktioniert.
*  `gdb-heap`_: dies scheint aber nun wirklich der beste Ansatz zu sein:
   über die Python-Schnittstelle von gdb klinkt man sich direkt in eine
   laufende Anwendung ein und schaut sich im Speicher um. Es gibt ein
   spezielles Python-Modul zur Analyse der einzelnen Objekte, das an die
   Speicherverwaltung von Python angepasst ist. Einziger Wermutstropfen:
   das Tool scheint sehr an die gdb-Version von Fedora gebunden zu sein.
   Bei einem kurzen Versuch unter Ubuntu wollte jedenfalls das
   Python-Modul nicht starten. Definitiv aber ein Projekt, das ich
   weiter beobachten werde. Auf der Seite findet sich außerdem ein Link
   auf `einen Vortrag auf der PyCon US 2011`_, der sehr schön die
   einzelnen Ansätze zur Speicheranalyse unter Python erklärt.

.. _vorhergehenden Blogeintrag: http://www.dasskript.com/blogposts/93
.. _Meliae: https://launchpad.net/meliae
.. _gdb-heap: https://fedorahosted.org/gdb-heap/
.. _einen Vortrag auf der PyCon US 2011: http://blip.tv/file/4878749?filename=Pycon-PyCon2011DudeWheresMyRAMADeepDiveIntoHowPythonUses441.ogv
