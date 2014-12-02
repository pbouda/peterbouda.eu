Revisiting PyQt and OpenGL
##########################
:date: 2014-07-23 10:00
:category: Graphics
:tags: PyQt, OpenGL
:image: /images/pyqt_opengl.png
:imagewidth: 1026

It's been I while since I used OpenGL with PyQt, for example in my `live coding experiments with GLSL shaders <{filename}/livecoding-glsl-shaders-with-ipython.rst>`_. Those were still done with PyQt4 and the good old ``QGLWidget``. In Qt5 the preferred way to render in OpenGL canvases is to use the new ``QOpenGL*`` classes. Those have the advantage that they provide a full collection of OpenGL drawing functions, so it is not necessary to import any external OpenGL library (like PyOpenGL) anymore. The disadvantage is that there is currently no convenient way to create and initialize such a window with a nice render function, as was provided by the ``QGLWidget``.

I finally collected some code from the PyQt5 OpenGL examples and with some modification I was able to run it (`from the snapshot of PyQt5 on Github <https://github.com/baoboa/pyqt5/blob/master/examples/opengl/openglwindow.py>`_). Their class ``OpenGLWindow`` provides what you need for the first steps, you can just subclass it and add your code to your own ``render()`` function. I added some more interesting shaders from `here <http://www.iquilezles.org/www/material/nvscene2008/rwwtt.pdf>`_, et voilà le chocolat:

https://github.com/pbouda/stuff/blob/master/opengl/pyqt/chocolux.py

Time to connect this with some live coding...