Memory Profiling Tools für Python, Teil 2 @ dasskript.com
#########################################################
:date: 2011-09-02 11:33
:author: pbouda
:slug: memory-profiling-tools-fur-python-teil-2-dasskriptcom

Kaum hatte ich den `vorhergehenden Blogeintrag`_ fertig, bin ich mehr
oder weniger zufällig auf zwei weitaus interessantere Projekte gestoßen,
die Speicherlecks in Python-Anwendungen aufspüren sollen. Hier also, der
Vollständigkeit halber, die Vo:

.. raw:: html

   </p>

-  `Meliae`_: Für Python 2, wird aber im Gegensatz zu heapy aktiv weiter
   entwickelt. Für meine Zwecke aber derzeit unbrauchbar, bis es auch
   mit Python 3 funktioniert.
-  `gdb-heap`_: dies scheint aber nun wirklich der beste Ansatz zu sein:
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

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   <script type="text/javascript"></p><p>var flattr_uid = '12306';</p><p>var flattr_tle = 'Memory Profiling Tools für Python, Teil 2';</p><p>var flattr_dsc = 'Kaum hatte ich den vorhergehenden Blogeintrag fertig, bin ich mehr oder weniger zufällig auf zwei weitaus interessantere Projekte gestoßen, die Speicherlecks in Python-Anwendungen aufspüren sollen. ...';</p><p>var flattr_cat = 'text';</p><p>var flattr_lng = 'de_DE';</p><p>var flattr_tag = 'Python, Memory-Profiling';</p><p>var flattr_url = 'http://www.dasskript.com/blogposts/94';</p><p>var flattr_btn = 'compact';</p><p></script>

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

.. _vorhergehenden Blogeintrag: http://www.dasskript.com/blogposts/93
.. _Meliae: https://launchpad.net/meliae
.. _gdb-heap: https://fedorahosted.org/gdb-heap/
.. _einen Vortrag auf der PyCon US 2011: http://blip.tv/file/4878749?filename=Pycon-PyCon2011DudeWheresMyRAMADeepDiveIntoHowPythonUses441.ogv
