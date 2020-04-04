Live Coding with Kivy and IPython
#################################
:date: 2014-07-02 10:00
:tags: Kivy, IPython, Live Coding
:image: /images/kivy_livecode_screen.png
:imagewidth: 1026

I recently began to implement some game prototypes with the help of `Kivy <http://kivy.org/>`_, a very interesting Python library originally developed to prototype innovative user interfaces. Combined with IPython, Kivy could also be interesting for `live coding <{filename}/Python/livecoding-glsl-shaders-with-ipython.rst>`_, and so I checked out how the `input hooks for other event loops <http://minrk.github.io/ipython-doc/dev/api/generated/IPython.lib.inputhook.html>`_ work in IPython. Currently, there are hooks for Qt, glut, pyglet, GTK, wx and tk build in. That means that you can use any of those frameworks to develop GUI apps interactively from within an IPython shell.

For Kivy, I copied one of the existing hooks and came up with the following code:

https://github.com/pbouda/stuff/blob/master/kivy_livecode/helpers.py

The function ``enable_kivy()`` would return an Kivy ``app`` object that you can then use to add widget interactively. Just start an IPython shell and add a rectangle to a Kivy window, for example:

.. code-block:: python

    [1] import helpers
    [2] app = helpers.enable_kivy()
    [3] from kivy.graphics import *
    [4] with app.root.canvas:
        Color(1.0, 0.2, 0.0)
        Rectangle(pos=(850,450), size=(200,200))

Unfortunately, you have to patch the Kivy sources to run in interactive mode at the moment. Kivy has a so-called ``slave`` mode, but it is not available when you call the default ``run()`` method on the ``App`` object. Here is a simple patch that just pipes the ``slave`` parameter to the ``runcTouchApp()`` method and will allow you to start the Kivy app in slave mode:

https://github.com/pbouda/kivy/commit/e1659dea1986f4a6006193d697c86d3694652cc1

Have fun!

