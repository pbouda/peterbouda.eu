Visualizing Swadesh words in dictionaries
#########################################
:date: 2014-02-14 11:29
:category: Language
:tags: IPython, Swadesh, Witotoan
:iframe: http://www.peterbouda.eu/tutorials/swadeshviewer/index.html
:iframeheight: 800

Swadesh viewer for dictionary data
==================================

In this tutorial we will demonstrate how to extract entries that contain
words from a `Swadesh
list <http://en.wikipedia.org/wiki/Swadesh_list>`__ from data in
digitized dictionaries. The translation graph connects entries in
dioctionaries, via annotation for "heads" and "translations" within the
dictionary. We will demonstrate how to visualize this data with a
plotting library and hwo to export parts of the graph to JSON for
interactive visualizations in the web.

You can download this tutorial as `IPython
notebook <http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html>`__
here:

https://github.com/pbouda/notebooks/blob/master/Swadesh%20viewer%20for%20dictionary%20data.ipynb

Data
----

For this tutorial we will use data from the project "`Quantitative
Historical Linguistics <http://www.quanthistling.info/>`__\ ". The
website of the project provides a ZIP package of GrAF/XML files for the
printed sources that were digitized within the project:

http://www.quanthistling.info/data/downloads/xml/data.zip

The ZIP package contains several files encoded as described in the `ISO
standard
24612 <http://www.iso.org/iso/catalogue_detail.htm?csnumber=37326>`__
"Linguistic annotation framework (LAF)". The QuantHistLing data contains
dictionary and wordlist sources. Those were first tokenized into
entries, for each entry you will find annotations for at least the head
word(s) ("head" annotation) and translation(s) ("translation"
annotation) in the case of dictionaries. We will only use the
dictionaries of the "Witotoan" compoment in this tutorial. The ZIP
package also contains a CSV file "sources.csv" with some information for
each source, for example the languages as ISO codes, type of source,
etc. Be aware that the ZIP package contains a filtered version of the
sources: only entries that contain a Spanish word that is part of the
Spanish swadesh list are included in the download package.

For a simple example how to parse one of the source please see here:

http://graf-python.readthedocs.org/en/latest/Querying%20GrAF%20graphs.html

What are translation graphs?
----------------------------

In our case, translation graphs are graphs that connect all spanish
translation with every head word that we find for each translation in
our sources. The idea is that spanish is some kind of interlingua in our
case: if a string of a spanish translation in one source matches a
string in another source this will only be *one* node in our graph. For
the head words, this is not the case: matching strings in head words in
different source are different nodes in the graph. This holds even if
the different sources describe the same language, as different sources
will use different orthographies.

To fullfil that need, head words are internally represented as a string
with two parts: the head word and its source. Both parts are seperated
by a pipe symbol "\|". For example, in a `DOT
file <http://en.wikipedia.org/wiki/DOT_language>`__ such a node looks
like this:

    "ócáji\|thiesen1998" [lang=boa, source=thiesen1998\_25\_339];

The square brackets contain additional attributes here. These attributes
are not part of the node's name, they contain just additonal information
that we store with the nodes.

In comparison, a spanish translation looks like this:

    "vaca" [lang=spa];

There is no attribute "source" here, as this translation might occur in
several sources. An edge connecting the two nodes looks like this:

    "vaca" -- "ócáji\|thiesen1998";

To handle such graphs our scripts use the `NetworkX Python
library <http://networkx.lanl.gov/>`__.

Requirements
------------

The following Python libraries are required to process the GrAF/XML
files and create the translation graphs:

-  NetworkX: http://networkx.lanl.gov/
-  graf-python: https://github.com/cidles/graf-python
-  requests: http://docs.python-requests.org/en/latest/ (only if you
   want automated download of the data)

To visualize the graphs we use the `D3.js <http://d3js.org/>`__ library,
but we will load this on-the-fly when we start with the visualization.

.. code-block:: python

    import os
    import csv
    import codecs
    import re
    import glob
    
    import networkx
    import graf

Get Witotoan sources
--------------------

In the first step we download and extract the data. You may change to a
local "tmp" directory before the download or just download the data to
the current working directory. For this you need to install the Python
library ``requests``. You may also download and extract the data
manually, the data is only downloaded for you if the file
``sources.csv`` is not found.

.. code-block:: python

    os.chdir("/Users/pbouda/Projects/git-github/notebooks/swadeshviewer")
    if not os.path.exists("sources.csv"):
        import requests
        import zipfile
        r = requests.get(
            "http://www.quanthistling.info/data/downloads/xml/data.zip")
        with open("data.zip", "wb") as f:
            f.write(r.content)
    
        z = zipfile.ZipFile("data.zip")
        z.extractall()

Now we open the file "sources.csv" and read out all the sources that are
part of the component "Witotoan" and that are dictionaries. We will
store a list of those source in ``witotoan_sources``:

.. code-block:: python

    sources = csv.reader(open("sources.csv", "rU"), delimiter="\t")
    witotoan_sources = list()
    for source in sources:
        if source[5] == "Witotoan" and source[1] == "dictionary":
            witotoan_sources.append(source[0])

GrAF to NetworkX
----------------

Next we define a helper function that transform a GrAF graph into a
networkx graph. For this we traverse the graph by querying for all
entries. For each entry we look for connected nodes that have "head" or
"translation" annotation. All of those nodes that are Spanish are stored
in the list ``spa``. All non-Spanish annotations are stored in
``others``. In the end the collected annotation are added to the new
networkx graph, and each spanish node is connected to all the other
nodes for each entry:

.. code-block:: python

    def graf_to_networkx(graf, source = None):
        g = networkx.Graph()
        for (node_id, node) in graf.nodes.items():
            spa = list()
            others = dict()
            if node_id.endswith("..entry"):
                _, page, pos_on_page, _ = node_id.split("..")
                for e in node.out_edges:
                    if e.annotations.get_first().label == "head" or e.annotations.get_first().label == "translation":
                        # get lang
                        for n in e.to_node.links[0][0].nodes:
                            if n.annotations.get_first().label == "iso-639-3":
                                if n.annotations.get_first().features.get_value("substring") == "spa":
                                    spa.append(e.to_node.annotations.get_first().features.get_value("substring"))
                                    break
                                else:
                                    others[e.to_node.annotations.get_first().features.get_value("substring")] = n.annotations.get_first().features.get_value("substring")
                                    break
                if len(spa) > 0:
                    for head in spa:
                        g.add_node(head, attr_dict={ "lang": "spa" })
                        for translation in others:
                            g.add_node(u"{0}|{1}".format(translation, source), attr_dict={
                                "lang": others[translation],
                                "source": source,
                                "page": page,
                                "pos_on_page": pos_on_page
                            })
                            g.add_edge(head, u"{0}|{1}".format(translation, source))
        return g

Parse GrAF/XML files
--------------------

Now we parse all the XML files of the extracted ZIP package. For this we
traverse through all the directories that have a name in
\`witotoan\_sources'. The files we are looking for are the
"-dictinterpretation.xml" files within each directory, as those contain
the annotations for "heads" and "translations".

First we create an empty list ``graphs`` that will later store all the
networkx graphs:

.. code-block:: python

    parser = graf.GraphParser()
    graphs = []

Then we loop through all the Witotoan sources, parse the XML files and
transform the graphs into networkx graph by calling the helper function
that we defined above. We print a progress report within the loop, as
parsing and transformation might take some time:

.. code-block:: python

    for d in witotoan_sources:
        for f in glob.glob(os.path.join(d, "dict-*-dictinterpretation.xml")):
            print("Parsing {0}...".format(f))
            graf_graph = parser.parse(f)
            g = graf_to_networkx(graf_graph, d)
            graphs.append(g)
    print("OK")

.. parsed-literal::

    Parsing thiesen1998/dict-thiesen1998-25-339-dictinterpretation.xml...
    Parsing minor1987/dict-minor1987-1-126-dictinterpretation.xml...
    Parsing minor1971/dict-minor1971-3-74-dictinterpretation.xml...
    Parsing burtch1983/dict-burtch1983-19-262-dictinterpretation.xml...
    Parsing leach1969/dict-leach1969-67-161-dictinterpretation.xml...
    Parsing walton1997/dict-walton1997-9-120-dictinterpretation.xml...
    Parsing preuss1994/dict-preuss1994-797-912-dictinterpretation.xml...
    OK


Merge all graphs
----------------

Now we can merge all the individual graphs for each source into one big
graph. This will collapse all Spanish nodes and so connect the nodes
that have a common Spanish translation:

.. code-block:: python

    import copy
    combined_graph = copy.deepcopy(graphs[0])
    for gr in graphs[1:]:
        for node in gr:
            combined_graph.add_node(node, gr.node[node])
        for n1, n2 in gr.edges_iter():
            combined_graph.add_edge(n1, n2, gr.edge[n1][n2])

We count the nodes in the graph and the `number of connected
components <http://networkx.lanl.gov/reference/generated/networkx.algorithms.components.connected.number_connected_components.html#networkx.algorithms.components.connected.number_connected_components>`__
to get an impression how the graph "looks". The number of nodes is much
higher then the number of connected components, so we already have a lot
of the nodes connected in groups, either as a consequence from being
part of one dictionary entry or through the merge we did via the Spanish
node:

.. code-block:: python

    len(combined_graph.nodes())



.. parsed-literal::

    23749



.. code-block:: python

    networkx.algorithms.components.number_connected_components(combined_graph)



.. parsed-literal::

    4614


Extract a subgraph for all the words in the Spanish Swadesh list
----------------------------------------------------------------

Next we will extract a subgraph from full graph. We will only search for
nodes that have a Spanish word that is a part of the `Swadesh
list <http://en.wikipedia.org/wiki/Swadesh_list>`__. The `Natural
Language Toolkit (NLTK) <http://www.nltk.org/>`__ contains Swadesh lists
for several languages and we will use NLTK's version of the Spanish
list. You don't need to install the NLTK library (although I recommend
learning about it!), as we will load the data directly from the NLTK
github repository. Again, we use ``requests`` to download the data, but
you may also download and extract the data manually.

First we download and extract the Swadesh data:

.. code-block:: python

    #os.chdir("c:/Users/Peter/Documents/Corpora/qlc")
    if not os.path.exists(os.path.join("swadesh", "es")):
        import requests
        import zipfile
        r = requests.get(
            "https://github.com/nltk/nltk_data/blob/gh-pages/packages/corpora/swadesh.zip?raw=true")
        with open("swadesh.zip", "wb") as f:
            f.write(r.content)
    
        z = zipfile.ZipFile("swadesh.zip")
        z.extractall()

Next, we get all the Spanish words from the Swadesh file:

.. code-block:: python

    swadesh_words = list()
    with codecs.open(os.path.join("swadesh", "es"), "r", "utf-8") as f:
        for line in f:
            swadesh_words.append(line.strip())

Now we are ready to loop through the graph and find all nodes are part
of the Swadesh list. We will store all those nodes and their connections
in seperate graphs, one graph for each Swadesh term. This allows us to
use different word lists later, for example to extract semantic domains
like *body parts*, *food*, etc.

.. code-block:: python

    swadesh_graphs = list()
    for i, _ in enumerate(swadesh_words):
        swadesh_graphs.append(networkx.Graph())
        
    for node in combined_graph:
        if "lang" in combined_graph.node[node] and \
                combined_graph.node[node]["lang"] == "spa" and \
                node in swadesh_words:
            # get the index of the word in the Swadesh list
            i = swadesh_words.index(node)
            swadesh_graphs[i].add_node(node)
            
            for n in combined_graph[node]:
                if "lang" in combined_graph.node[n] and \
                        combined_graph.node[n]["lang"] != "spa":
                    word, source = n.split("|")
                    lang = combined_graph.node[n]["lang"]
                    page = combined_graph.node[n]["page"]
                    pos_on_page = combined_graph.node[n]["pos_on_page"]
                    swadesh_graphs[i].add_node(lang)
                    swadesh_graphs[i].add_edge(node, lang)
                    swadesh_graphs[i].add_node(word,
                        attr_dict={ "data_source": source,
                                    "page": page,
                                    "pos_on_page": pos_on_page })
                    swadesh_graphs[i].add_edge(lang, word)


Export the subgraph as JSON data
--------------------------------

Another method to visualize the graph is the `D3 Javascript
library <http://d3js.org/>`__. For this we need to export the graph as
JSON data that will be loaded by a HTML document. The networkx contains
a ``networkx.readwrite.json_graph`` module that allows us to easily
transform the graph into a JSON document. The JSON data structure can
then be writte to a file with the help of the Python ``json`` module:

.. code-block:: python

    from networkx.readwrite import json_graph
    import json
    
    for i, g in enumerate(swadesh_graphs):
        json_data = json_graph.node_link_data(g)
        json.dump(json_data, codecs.open("swadesh_data_{0}.json".format(i), "w", "utf-8"))

.. code-block:: python

    json.dump(swadesh_words, codecs.open("swadesh_list.json", "w", "utf-8"))

Finally we need to create a HTML file to display the data. You can
download an HTML file form here:

https://github.com/pbouda/notebooks/blob/master/swadeshviewer/index.html

Put the file ``index.html`` into the folder with the JSON files. Then
open the file in any browser. You can view an online version here:

http://www.peterbouda.eu/tutorials/swadeshviewer/index.html
