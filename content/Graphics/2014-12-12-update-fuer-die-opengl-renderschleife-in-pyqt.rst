Update für die OpenGL-Renderschleife in PyQt
############################################
:date: 2015-01-30 11:00
:category: Graphics
:tags: PyQt, OpenGL, Raymarching
:image: /images/pyqt_opengl_raymarching.png
:imagewidth: 1026

Ich versuche gerade mich in das Thema Raytraching bzw. Raymarching einzuarbeiten. Dabei bin wieder auf mein Qt-OpenGL-Programmgerüst zurückgekommen, dass ich in `einem meiner letzten Artikel <{filename}2014-07-23-revisiting-pyqt-and-opengl.rst>`_ beschrieben habe. Leider hat das Skript nicht auf Anhieb auf einem neuen Rechner funktioniert, was ich auf unterschiedliche Implementierungen der OpenGL-Bibliothek in Qt oder gar den Grafiktreiber zurückführe. Bestimme von mir verwendete Befehle erzeugten Fehlermeldungen, u.a. konnte ich das OpenGL-Viereck für das Fraktal nicht per ``QL_QUADS`` zeichnen. Ich habe also das Programmgerüst etwas angepasst und auf reine OpenGL ES 2.0 Befehle reduziert. Statt einem Viereck zeichne ich jetzt zwei Dreiecke, die ich per *Vertex Array* übergebe. Ich benutze dafür die Methode ``glDrawElements()``, der ich die Indizes auf die einzelnen Dreickspunkte im *Vertex Array* übergebe. Die ``render``-Schleife sieht jetzt in etwa folgendermaßen aus:

.. code-block:: python

    gl.glViewport(0, 0, self.width(), self.height())
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    self.program.bind()

    vertices = array.array("f", [
         1,  1, 0,
        -1,  1, 0,
        -1, -1, 0,
         1, -1, 0
    ])

    indices = array.array("B", [0,1,2,0,2,3])

    gl.glEnableVertexAttribArray(self.vAttr)
    gl.glVertexAttribPointer(self.vAttr,
        3,
        gl.GL_FLOAT,
        gl.GL_FALSE,
        0,
        vertices)
    gl.glDrawElements(gl.GL_TRIANGLES, 6, gl.GL_UNSIGNED_BYTE, indices)
    gl.glDisableVertexAttribArray(self.vAttr)

    self.program.release()

Diese Gerüst eignet sich damit auch hervorragend für erste Raymarching-Experimente, da letztendlich wiederum nur ein simples Viereck mit den Eckpunkten ``[-1, -1]`` und ``[1, 1]`` gezeichnet wird. In dieses hinein lassen sich dann per Shader Fraktale oder eben Raytracing-Objekte zeichen. Allgemein scheint PyQt eine schöne Umgebung für Shader-Experimente zu sein, wie ich immer wieder festestellen muss. Mit dem Programmgerüst kann man schnell die Shader sowie deren Input und Output modifizieren. Der Screenshot oben basiert auf den Shadern des `4k-Intro-Frameworks von iquilezles.org <http://www.iquilezles.org/www/material/isystem1k4k/isystem1k4k.htm>`_, eine fantastische Website zum Thema Grafikprogrammierung und `interessanten Artikeln zum Thema Raymarching <http://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm>`_. Hier ist noch der Link zu meinem aktuellen Experiment, das die oben abgebildete Kugel rendert, und das die OpenGL-Renderschleife in Aktion zeigt:

https://github.com/pbouda/stuff/blob/master/opengl/pyqt/raymarching.py