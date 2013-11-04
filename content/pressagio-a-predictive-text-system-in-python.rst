pressagio: A predictive text system in Python
#############################################
:date: 2013-11-04 13:56
:category: Python
:tags: Poio, n-gram

`Pressagio <http://media.cidles.eu/poio/pressagio/>`_ is a predictive text
library that I am currently working on. It is written in Python and I started
this project as a pure Python port of the amazing `presage library
<http://presage.sourceforge.net/>`_. The original idea was to implement text
prediction on mobile phones for under-resourced languages like Bavarian or
Sorbian, but pressagio could of course be used for any language for which some
corpus is available. You can try out an online demo of the text prediction
on the `Poio website <http://www.poio.eu/>`_.

Here is a short introduction how to build an n-gram model for a language
that you want to support via pressagio. First, you have to prepare some text
file that contains raw text, without markup or any other content. A good
example is the output of the `Wikipedia to GrAF conversion that I described
a few weeks ago
<|filename|/parsing-wikipedia-dumps-and-converting-to-iso-24612-graf-xml.md>`_.
The GrAF package contains a .txt file that we will use for the tutorial in this
post.

Build the n-gram model
======================

We will build and store an n-gram model to allow text prediction for Bavarian.
A sqlite database will store the model, so that you do not need any other
database system on your computer. Python supports sqlite out-of-the-box.
Besides sqlite, pressagio also support postgres as a store for the n-gram
models. To create the model for a single cardinality (e.g. unigram or bigrams),
the pressagio library contains a `text2ngram
<https://github.com/cidles/pressagio/blob/master/scripts/text2ngram>`_ script
in the ``scripts`` folder of the source distribution. This script supports
several command line options, for example to set the cardinality of the model
and the output file. You can get a list of all options by passing ``--help`` to
the script:

.. code-block:: console

	h:\ProjectsWin\git-github\pressagio\scripts>c:\Python33\python.exe text2ngram --help
	Usage: text2ngram [options] file1 file2 ...

	Options:
	  --version             show program's version number and exit
	  -h, --help            show this help message and exit
	  -n NGRAM, --ngram=NGRAM
	                        Specify ngram cardinality N
	  -l LOWERCASE, --lowercase=LOWERCASE
	                        Enable lowercase conversion mode
	  -a APPEND, --append=APPEND
	                        Enable append mode for database
	  -o OUTFILE, --output=OUTFILE
	                        Output file name O

We will generate a model for unigrams, bigrams and trigrams, as this is what
we need for the text prediction. In addition to the ``-n`` option we will also
pass a filename for sqlite database (``-o bar.sqlite``) and the path to the text
file with the Wikipedia articles (``barwiki-20131030.txt``). We have to call
``text2ngram`` three times, once for each cardinality. For the unigrams we use:

.. code-block:: console

	h:\ProjectsWin\git-github\pressagio\scripts>c:\Python33\python.exe text2ngram -n 1 -o bar.sqlite barwiki-20131030.txt
	Parsing barwiki-20131030.txt...
	Writing result to bar.sqlite...

Then the bigrams:

.. code-block:: console

	h:\ProjectsWin\git-github\pressagio\scripts>c:\Python33\python.exe text2ngram -n 2 -o bar.sqlite barwiki-20131030.txt
	Parsing barwiki-20131030.txt...
	Writing result to bar.sqlite...

And finally the trigrams:

.. code-block:: console

	h:\ProjectsWin\git-github\pressagio\scripts>c:\Python33\python.exe text2ngram -n 3 -o bar.sqlite barwiki-20131030.txt
	Parsing barwiki-20131030.txt...
	Writing result to bar.sqlite...

The result of the three steps will be a sqlite database with three tables
``_1_gram``, ``_2_gram`` and ``_3_gram``. Those will contain the counts for each
n-gram of the Wikipedia corpus.

Use pressagio to suggest completions
====================================

Based on this information pressagio can now calculate the most likely
completions for any Bavarian string. The whole process is controlled via a
configuration file that points to the database file and contains several option
for smoothing, the number of suggestions etc. You can find an `example config file
<https://github.com/cidles/pressagio/blob/master/scripts/example_profile.ini>`_
in the ``scripts`` folder. The same folder also contains an `example script
for prediction
<https://github.com/cidles/pressagio/blob/master/scripts/predict>`_ that makes
use of this config file. This example assumes that there is a file
``bar.sqlite`` in the same folder as the prediction script and the config file.

The script first imports the ``configparser`` module. We emebed the import in
a ``try`` block in order to support both Python 2 and 3, as the name of the
module changed between the two versions:

.. code-block:: python
	try:
	    import configparser
	except ImportError:
	    import ConfigParser as configparser

	import pressagio.callback
	import pressagio

Next, we define a sub-class of ``pressagio.callback.Callback``, which is used
to pass the input string to the predictor. In a real-world setting this callback
is called by the text predictor and has to return the strings before and after
the cursor. For simplicity we assume that there is no text after the cursor:

.. code-block:: python

	class DemoCallback(pressagio.callback.Callback):
	    def __init__(self, buffer):
	        super().__init__()
	        self.buffer = buffer

	    def past_stream(self):
	        return self.buffer
	    
	    def future_stream(self):
	        return ''

We can now open and parse the config file:

.. code-block:: python

	config_file = "example_profile.ini"

	config = configparser.ConfigParser()
	config.read(config_file)

With the parsed configuration and the callback we can create a ``Pressagio``
object:

.. code-block:: python

	callback = DemoCallback("Des is a Te")
	prsgio = pressagio.Pressagio(callback, config)

The object has a method ``predict()`` that will return a list of the suggestions
calculated from the n-gram model:

.. code-block:: python

	predictions = prsgio.predict()
	print(predictions)

That's it! Feel free to try this out with any corpus you have, and don't forget
to try our online demo at the Poio website:

http://www.poio.eu/

Poio is completely open source, the data we use is from Wikipedia and is
completely free for download on the Poio website.