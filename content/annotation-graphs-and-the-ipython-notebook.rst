Annotation graphs and the IPython notebook
##########################################
:date: 2012-12-18 10:53
:category: Python
:slug: annotation-graphs-and-the-ipython-notebook

I recently became obsessed with annotation graphs and linguistic graphs
in general. Since September I am working with the `graf-python`_ library
that implements the `ISO 24612 - Linguistic annotation framework (LAF)`_
standard. I planned to publish the corpora of our research center in an
XML format that is easy to use, that is somehow officially recognized
and that allows stand-off annotations so that I can share data and sets
of annotations independently. GrAF/XML looked like an optimal solution,
so I gave it a try.

.. raw:: html

   </p>

First, I published a subset of the data of the `QuantHistLing`_ project
as GrAF/XML files. I wrote a tutorial how to access the data in Python
`which is available as part of the graf-python documentation`_. But I
also had the idea of making the dictionary data of the project more
accessible to researchers. One thing we commonly use in language
comparison are `Swadesh lists`_ that contain a fixed set of words for
200 concepts that are supposed to be general and exist in most of the
languages. As most of our dictionaries contain a Spanish translation my
idea was to connect the dictionaries via those translations, but only
use the words of the Spanish Swadesh list. I developed an `IPython
notebook`_ to connect the dictionaries of the Witotoan language family
via the stem of the Spanish word *comer*. I basically transformed the
annotation graphs from GrAF into a `networkX`_ graph that I could easily
visualize using the `D3 javascript library`_:

.. raw:: html

   </p>

Published at ``_\ `http://bl.ocks.org/4250342`_\ 

.. raw:: html

   </p>

You can find an in-depth description about the transformation and the
complete notebook `in another turotial for graf-python`_. It already
looks quite nice, IMO. I am now trying to make the visualization more
useful to linguists, by providing more interactivity and maybe search
options to query for words or sets of words. As an intermediate summary
I can already tell that IPython helped a lot in working interactively
with linguistic data in this case. I could try out different ways to
combine and visualize graphs easily and use a JSON representation of
Python data structures to publish the results in a HTML/Javascript
application. Right now I save the JSON data into files and I am still
looking for a way to directly stream the data from IPython to Javascript
somehow. There are different ways how Python and Javascript can interact
in an IPython notebook, the “official” solution is to provide an HTML
representation of the Python objects as far as I understand. My goal is
to completely decouple the two if possible.

.. raw:: html

   </p>

.. _graf-python: https://github.com/cidles/graf-python
.. _ISO 24612 - Linguistic annotation framework (LAF): http://www.iso.org/iso/catalogue_detail.htm?csnumber=37326
.. _QuantHistLing: http://www.quanthistling.info/
.. _which is available as part of the graf-python documentation: http://graf-python.readthedocs.org/en/latest/Querying%20GrAF%20graphs.html
.. _Swadesh lists: http://en.wikipedia.org/wiki/Swadesh_list
.. _IPython notebook: http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html
.. _networkX: http://networkx.lanl.gov/
.. _D3 javascript library: http://d3js.org/
.. _: http://bl.ocks.org/4250342
.. _`http://bl.ocks.org/4250342`: http://bl.ocks.org/4250342
.. _in another turotial for graf-python: http://graf-python.readthedocs.org/en/latest/Translation%20Graph%20from%20GrAF.html
