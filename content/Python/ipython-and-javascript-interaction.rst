IPython and Javascript interaction
##################################
:date: 2013-01-24 11:56
:category: Python
:tags: Python, Javascript, IPython
:slug: ipython-and-javascript-interaction

This `IPython notebook`_ demonstrates the interaction between Python and
a popup window that is opened via Javascript. The interaction is one-way
in this case, from the notebook to the popup. We write data to the popup
and call functions in the popup by executing Javascript from within the
notebook. The goal is to demonstrate some simple interactions. In the
end, I hope that techniques like these could be used for `livecoding`_
in Python, with a HTML5 visualization window.

First, the notebook server and the HTML that we load in the popup must
be located on the same domain. For this, we need to copy the
`index.html`_ to the root directory of the IPython server.
Unfortunately, it is not easy to find out what the root directory is.
The default is the home directory of the user, so if you didn’t mess
with your config just copy the html file to your home directory. If you
changed your config you probably know whether you changed the root (it’s
the setting ``ipython_dir``).

The ``index.html`` contains an empty `D3 scatterplot`_ that we will fill
with data from within this notebook. The notebook is available on Github
here:

https://github.com/pbouda/stuff/blob/master/ipynb/Javascript%20Interactions%20I.ipynb


Open a browser popup
--------------------

IPython contains several helper methods in ``IPython.display`` to output
HTML, Javascript, etc. to the current cell’s output. We use those
helpers to write Javascript that opens a popup window. We save a
reference to the opened window in ``window.audiencePopup``. We can later
access the open popup via this reference. First, we open some URL to see
if something simple works:

.. code-block:: python

   from IPython.display import HTML, Javascript, display
   js = """window.audiencePopup = window.open('http://www.heise.de','audienceWindow');"""
   display(Javascript(js))


Change the location
-------------------

We are now able to change the URL of the popup. We set the URL to the
local ``index.html`` that you downloaded above. We have to prepend
``/files/`` so that the IPython server knows that we are looking for a
local, static file. The notebook server then serves this file to the
popup window:

.. code-block:: python

   js = """window.audiencePopup.location.href = "/files/index.html";"""
   display(Javascript(js))

As said above, the ``index.html`` has to be served from the same domain
as your current IPython notebook for security reasons. If everything
works than you should now see the empty scatterplot in the popup.

Write some data to the popup
----------------------------

We will now write some data to the popup. If you look into
``index.html`` you will see a Javascript variable ``data`` that contains
an empty list. The scatterplot is created from coordinates in that list.
In the first step we will set the ``data`` variable to a Python list of
coordinates. For this we just have to convert the Python list to a JSON
string and set the Javascript variabel to a parsed version of that JSON
string. We use the Javascript function ``JSON.parse``:

.. code-block:: python

   import json
   data = [ [0, 0], [1, 1], [0.5, 0.5] ]
   js = """window.audiencePopup.data = JSON.parse('{0}');""".format(json.dumps(data))
   display(Javascript(js))

The scatterplot don’t change, because we have to tell it to update
itself first. But you can already have a look the the content of the
``data`` variable in the popup window. We just display the value in an
``alert`` window:

.. code-block:: python

   js = """alert(window.audiencePopup.data);"""
   display(Javascript(js))

The ``index.html`` also containts a function ``update()`` that we can
just call to repaint the scatterplot. Again, we are able to call this
Javascript function directly from within the current notebook:

.. code-block:: python

   js = """window.audiencePopup.update();"""
   display(Javascript(js))

You should now see the data points in the scatterplot. You can see a
screencast where I execute this notebook here:

.. raw:: html

   <video poster="https://s3.amazonaws.com/peterbouda.eu/IPython+and+Javascript+interaction.png" style="width:100%" preload="none" controls="" tabindex="0">
      <source type="video/mp4" src="https://s3.amazonaws.com/peterbouda.eu/IPython+and+Javascript+interaction.m4v"></source>
   </video>

.. _IPython notebook: http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html
.. _livecoding: http://toplap.org/
.. _index.html: https://raw.github.com/pbouda/stuff/master/ipynb/index.html
.. _D3 scatterplot: http://bl.ocks.org/2595950
.. _`https://github.com/pbouda/stuff/blob/master/ipynb/Javascript%20Interactions%20I.ipynb`: https://github.com/pbouda/stuff/blob/master/ipynb/Javascript%20Interactions%20I.ipynb
