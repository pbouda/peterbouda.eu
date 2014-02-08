Title: Parsing Wikipedia dumps and conversion to ISO 24612 (GrAF-XML)
Date: 2013-09-10 15:53
Category: Language
Tags: Poio, Wikipedia

At the moment I am heavily working on our data management and conversion library
[Poio API](http://media.cidles.eu/poio/poio-api/). Until now it mainly targets
files formats used in language documentation, but I am quite interested in using
the content of Wikipedias to do some linguistic analysis like finding semantic
classes or testing part-of-speech taggers. As you might know, the original
[Wikipedia dumps](http://dumps.wikimedia.org/) are somehow contaminated with
Wiki markup that is not easy to erase. There are all kind of historical markup
structures in there and sometimes the syntax is plainly wrong, but still works
to generate a good-enough page on the Wikipedia website. In this post I will
explain how to download and clean a Wikipedia dump and then use Poio API to
transform it into a [GrAF-XML file](http://www.balisage.net/Proceedings/vol10/html/Bouda01/BalisageVol10-Bouda01.html).

# The Wikipeda Extractor

Two years ago I tested several Wikipedia extraction tools, and found that the
[Wikipedia Extractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor)
gives the best output. Things might have changed since then, but I stick to it,
also because it is a single Python script that I can easily change if I need
to. The newest version can output JSON or XML. As XML was the one and only
output format two years ago I stick to the XML output as all my tools are based
on this format. In fact, it is not *true* XML, as the root element is missing
(the Wikipedia Extractor calls the format "tanl"). All the Wikipedia articles
are just enclosed by `<doc>` tags, one after the other:

    :::xml
    <doc id="55" url="http://bar.wikipedia.org/wiki?curid=55" title="Wikipedia:Archiv/Boarische Umschrift">Wikipedia:Archiv/Boarische Umschrift
    Fürs Boarische gibts koa einheitliche Umschrift. Ma orientiert si in da Schreibweis an da deutschen Orthografie....
    </doc><doc id="60" url="http://bar.wikipedia.org/wiki?curid=60" title="Deitschland">Deitschland
    Deitschland is a Staat in Mittleiropa. Ois Bundesstaat wiad de "Bundesrepublik Deutschland" aus dena 16 deitschn Ländan buidt....
    </doc>
    [...]

The whole output is split over several files, where the files' size is
controllable via a command line variable. I use to call the Wikipedia Extractor
with the following arguments (I use the [Bavarian Wikipedia dump]
(http://dumps.wikimedia.org/barwiki/20130905/) as an example here):

    :::text
    WikiExtractor.py -w -f tanl barwiki-20130905-pages-articles.xml.bz2 extracted

This will put all output files into a folder `extracted`.

# Concatenate and clean the files

The next step is then to create a real XML file from this. It is not too hard,
we just have to add a root tag and clean the data a bit more, otherwise an XML
parser will complain about certain characters like the "lower than" `<`. I
start with the following code to get rid of certain general problems like
unparsable characters, add the root tags and concatenate all the files:

    :::python
    import sys
    import re
    import codecs

    re_apostroph = re.compile("\"")

    def re_title_cleaned(matchobj):
        return matchobj.group(1) + re_apostroph.sub("", matchobj.group(2)) + matchobj.group(3)


    # Concatenate output files
    filenames = glob.glob(os.path.join("extracted", "*.raw"))
    with codecs.open("barwiki.xml", 'w', 'utf-8') as outfile:
        for fname in filenames:
            with codecs.open(fname, "r", "utf-8") as infile:
                for line in infile:
                    outfile.write(line)

    # first clean step
    f1 = codecs.open("barwiki.xml", "r", "utf-8")
    f2 = codecs.open("barwiki_cleaned.xml", "w", "utf-8")

    f2.write("<xml>\n")

    re_title = re.compile("(title=\")(.*)(\">)")
    re_xml_tag = re.compile("<(?!/?doc)[^>]*>")
    re_and = re.compile("&")
    re_lower = re.compile("< ")

    for i, line in enumerate(f1):
        line = re_title.sub(re_title_cleaned, line)

        line = re_xml_tag.sub(" ", line)
        line = re_and.sub("&amp;", line)
        line = re_lower.sub("&lt; ", line)

        f2.write(line)

    f2.write("</xml>\n")

    f1.close()
    f2.close()

There is one complex regular expression substition here, that cleans the `title`
attributes of the `<doc>` tags. The titles sometimes contain an apostroph `"`,
which is also the seperator for attribute values in XML and cannot be used in
this location. So I just remove them. The output of this script are two files:
the `barwiki.xml` just contains the concatenated files, the `barwiki_cleaned.xml`
contains the cleaned XML.

In the case of the Bavarian Wikipedia there are still
some more quirks in the data. You can find out what kind of problems there are
if you try to parse the file now with the Python ElementTree module, for
example:

    :::python
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    tree = ET.ElementTree("barwiki_cleaned.xml")

The parser will throw an error and tell you which line and column caused the
problem. So I went through all the remaining problems in the Bavarian Wikipedia,
and added several more lines to my clean script to remove or modify the lines
that cause the problems:

    :::python
    f1 = codecs.open("barwiki_cleaned.xml", "r", "utf-8")
    f2 = codecs.open("barwiki_cleaned2.xml", "w", "utf-8")

    re_date = re.compile("\-?\-? ?\d\d?:\d\d, \d\d?. .{2,8}\.? \d\d\d\d \(CES?T\)")
    re_dashes = re.compile("\-\-")
    re_wrong_tags = re.compile("</noinclude[^>]")
    re_arrows = re.compile("(<==<==<==<|>==>==>==>)")
    re_special1 = re.compile("Le<")
    re_special2 = re.compile("ci<:")
    re_img = re.compile(" [^ ]*\.jpg\|")

    lines_to_delete = [
        u"<!-- BITTE bei den Biografien der entsprechenden Personen auf der Bearbeitungsseite unten bei  Kategorien die folgende Zeile EINFÜGEN:",
        u"  </noinclude</includeonly»<includeonly</includeonly» BITTSCHÖN ENTFERN DII KOMMENTARE </includeonly</includeonly»",
        u"<!-- BITTE bei den Biografien der entsprechenden Personen auf der Bearbeitungsseite unten bei Kategorien die folgende Zeile EINFÜGEN:"
    ]

    for line in f1:
        if line.rstrip() in lines_to_delete:
            f2.write("\n")
            continue

        line = re_date.sub(re_empty, line)
        line = re_dashes.sub("-", line)
        line = re_arrows.sub("", line)
        line = re_wrong_tags.sub("", line)

        line = re_special1.sub("Le&lt;", line)
        line = re_special2.sub("ci&lt;:", line)

        line = re_img.sub(" ", line)

        f2.write(line)

    f1.close()
    f2.close()

In the end I have a clean file `barwiki_cleaned2.xml` that contains XML with
all the articles of the Bavarian Wikipedia and is parsable with EementTree.

I still add a third cleaning step to remove articles that are not real content.
Wikipedia contains several helper and meta-data articles that contain
explanations for authors and other stuff that we don't need. Luckily, those have
a title that contains a prefix that ends with a colon `:`, so we can just look
for a certain pattern in the titles and remove those `<doc>` elements from the
XML tree. I also remove articles that are smaller than 200
characters (those are too short to measure semantic similarity, in one of my
use cases):

    :::python
    tree = ET.ElementTree(file="barwiki_cleaned2.xml")
    root = tree.getroot()

    re_special_title = re.compile("\w+:\w", re.UNICODE)

    remove_list = list()

    for doc in root:
        title = doc.attrib['title']
        if re_special_title.match(title):
            remove_list.append(doc)
        elif len(doc.text) < 200:
            remove_list.append(doc)

    for doc in remove_list:
        root.remove(doc)
    tree.write("barwiki_cleaned3.xml", encoding="UTF-8")

After this step I finally end up with a `barwiki_cleaned3.xml` that contains
clean data with only the content articles. This file can already be used to
process the Wikipedia, but I wanted to also publish the files in a standardized
format. I chose [ISO 24612](http://www.iso.org/iso/catalogue_detail.htm?csnumber=37326),
as this makes it extremely easy to later combine heterogenous data sources or
add layers of annotations in the resulting annotation graph.

# Conversion to GrAF-XML with Poio API

The last step is extremely simple, as one of Poio API's core use case is the
conversion of files. Normally, you would have to write a parser and a writer
for each of the file formats you want to support. But for the XML output of
the Wikipedia Extractor there already exists a parser in Poio API, and GrAF-XML
is supported as the basic pivot format. Which means that any file format that
is supported in Poio API can be converted to GrAF-XML. The conversion is
dead simple: we initialize a `Converter` object with the Wikipedia parser
and the GrAF writer, and then tell the converter to `parse()` and `write()`:

    :::python
    parser = poioapi.io.wikipedia_extractor.Parser("Wikipedia.xml")
    writer = poioapi.io.graf.Writer()

    converter = poioapi.io.graf.GrAFConverter(parser, writer)
    converter.parse()
    converter.write("Wikipedia.hdr")

This will write a set of GrAF files that you can read and query with the
[graf-python](http://media.cidles.eu/poio/graf-python/) library or
with any of the [tools and connectors](http://www.anc.org/software/) that were
developed at the American National Corpus to work with their GrAF-XML corpus
files.