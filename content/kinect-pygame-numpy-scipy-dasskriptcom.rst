Kinect, PyGame, Numpy, SciPy @ dasskript.com
############################################
:date: 2012-01-26 11:34
:author: pbouda
:slug: kinect-pygame-numpy-scipy-dasskriptcom

Ich habe die letzten Wochen ein bisschen mit den `Python Tools für
Visual Studio`_ herumgespielt, auf der Website gibt es mit PyKinect
einen schönen Wrapper um das offizielle Kinect-SDK von Microsoft. Ich
wollte das mit einem Wassereffekt auf Basis von PyGame und Numpy
kombinieren, den habe ich `hier`_ gefunden. Heraus kam das:

.. raw:: html

   </p>

`http://teatrominde.tumblr.com/#15777992755`_

.. raw:: html

   </p>

Der Code dazu ist hier:

.. raw:: html

   </p>

`https://github.com/pbouda/stuff/blob/master/dances/WaterDance/WaterDance/Program.py`_

.. raw:: html

   </p>

Das Tiefenbild habe ich noch per Gauss-Filter aus SciPy verschönert,
damit es nicht so kantig aussieht. Alles läuft auf meinem Notebook recht
flüssig, das ist schon beeindruckend. Python gilt als langsam, ist es
wohl auch, aber für die meisten Zwecke reicht es dann doch.

.. raw:: html

   <p>

.. raw:: html

   <script type="text/javascript"></p><p>var flattr_uid = '12306';</p><p>var flattr_tle = 'Kinect, PyGame, Numpy, SciPy';</p><p>var flattr_dsc = 'Ich habe die letzten Wochen ein bisschen mit den Python Tools für Visual Studio herumgespielt, auf der Website gibt es mit PyKinect einen schönen Wrapper um das offizielle Kinect-SDK von Microsoft. I...';</p><p>var flattr_cat = 'text';</p><p>var flattr_lng = 'de_DE';</p><p>var flattr_tag = 'PyGame, NumPy, SciPy, PTVS, Kinect';</p><p>var flattr_url = 'http://www.dasskript.com/blogposts/98';</p><p>var flattr_btn = 'compact';</p><p></script>

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

.. _Python Tools für Visual Studio: http://pytools.codeplex.com/
.. _hier: http://www.pygame.org/pcr/water/index.php
.. _`http://teatrominde.tumblr.com/#15777992755`: http://teatrominde.tumblr.com/#15777992755
.. _`https://github.com/pbouda/stuff/blob/master/dances/WaterDance/WaterDance/Program.py`: https://github.com/pbouda/stuff/blob/master/dances/WaterDance/WaterDance/Program.py
