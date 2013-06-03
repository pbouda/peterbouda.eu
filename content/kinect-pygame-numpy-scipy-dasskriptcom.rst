Kinect, PyGame, Numpy, SciPy
############################
:date: 2012-01-26 11:34
:category: Python
:slug: kinect-pygame-numpy-scipy

Ich habe die letzten Wochen ein bisschen mit den `Python Tools für
Visual Studio`_ herumgespielt, auf der Website gibt es mit PyKinect
einen schönen Wrapper um das offizielle Kinect-SDK von Microsoft. Ich
wollte das mit einem Wassereffekt auf Basis von PyGame und Numpy
kombinieren, den habe ich `hier`_ gefunden. Heraus kam das:

http://teatrominde.tumblr.com/#15777992755

https://github.com/pbouda/stuff/blob/master/dances/WaterDance/WaterDance/Program.py

Das Tiefenbild habe ich noch per Gauss-Filter aus SciPy verschönert,
damit es nicht so kantig aussieht. Alles läuft auf meinem Notebook recht
flüssig, das ist schon beeindruckend. Python gilt als langsam, ist es
wohl auch, aber für die meisten Zwecke reicht es dann doch.


.. _Python Tools für Visual Studio: http://pytools.codeplex.com/
.. _hier: http://www.pygame.org/pcr/water/index.php
