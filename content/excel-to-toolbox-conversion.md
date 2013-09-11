Title: Creating a dictionary: Excel to Toolbox conversion
Date: 2013-08-29 11:18
Category: Linguistics

In our current dictionary project "Bilingual Dictionary Piação-Portuguese" we
decided to use Microsoft Excel to edit the dictionary data. This choice had
some pragmatic reasons, like that most people/linguists can easily work with a
stylesheet, even if they don't know about all the features of Excel, and that
Excel allows to export data in a structured way (as "comma separated values" in
a "CSV file"). Still, as the [Toolbox](http://www-01.sil.org/computing/toolbox/)
dictionary generator is state-of-the-art in language documentation, we needed a
way to convert the Excel data to a Toolbox file. We did some first tests with
a simple Python script and everything worked out well until now, so here is a
short description of our workflow.

We created an empty Toolbox project that will give you a list of standard fields
like `Lexeme`, `Sound file`, etc. We added two or three example sentences,
customized the fields, and generated a first dictionary to see how the output
will look in the end and to get an example data file that we could use as a
template for the Excel data. The data file will be saved in the project folder
somewhere, in our case it was in
`Toolbox Project\DictionaryFactoryPackage\Dictionary.txt`. You can open the
file in a simple text editor to see the content. In our case, an entry looked
like this:

    :::text
    \lx à bia
    \sf
    \pc
    \ph aβiɐ
    \se
    \ps adv.
    \un
    \dn rápido, depressa
    \sn
    \rn rápido
    \va
    \et antropónimo Bia
    \ec referência metonímica à alcunha de
    um homem para designar uma
    característica que lhe era peculiar
    \wh da alcunha de um senhor (Bia) que
    achava que tudo se podia resolver
    rapidamente, mesmo que sem
    qualidade. Doc. em CAORG 2004
    \pce
    \xv A covana colou do parreiral à bia e
    a resmar.
    \sfx
    \ff
    \xn ""A mulher saiu de casa depressa e a
    falar sozinha."
    \rf Ferreira 2000-2011. 
    \nt
    \cf
    \dt 19

For most of the Toolbox fields we defined a column in Excel, with a custom name
so that our editors where able to understand the column's content from the name
in Excel. With the column names and the field names in Toolbox we created the
following template in Python:

    :::python
    TEMPLATE = """\\lx {Lexema}
    \\sf 
    \\pc 
    \\ph {Transcrição Fonética}
    \\se
    \\ps {Classe de Palavras}
    \\un
    \\dn {Significado}
    \\sn
    \\rn 
    \\va
    \\et {Etimologia}
    \\ec {Comentário de etimologia}
    \\wh {Historia da Palavra}
    \\pce
    \\xv {Exemplos}
    \\sfx
    \\ff
    \\xn {Exemplos PT}
    \\rf {Fonte dos exemplos}
    \\nt
    \\cf
    \\dt 31.07.2013
    """

The Excel column names are in the curely brackets, so that we can use Python's
`format()` method to fill in the content. For the CSV file we had to export the
Excel data in LibreOffice Calc, as Excel does not support UTF-8 export (shame
on you, Microsoft!). We exported a single CSV file for each sheet in Calc,
so that we had a list of CSV files. With the template above and this collection
of CSV files it was easy to create a new `Dictionary.txt` for Toolbox:

    :::python
    import csv
    import codecs
    import glob

    with codecs.open("Dictionary.txt", "w", "utf-8") as tbfile:
        tbfile.write("\_sh v3.0  231  MDF 4.0\n\n")
        for f in glob.glob("Dictionary_database_NEW_*.csv"):
            with codecs.open(f, "r", "utf-8") as csvfile:
                minderico = csv.reader(csvfile, dialect='excel', delimiter=';', quotechar='"')

                for i, row in enumerate(minderico):
                    if i == 0:
                            header = row
                    else:
                        data = dict()
                        for j, h in enumerate(header):
                            data[h] = row[j]
                        try:
                            tbfile.write(TEMPLATE.format(**data))
                        except KeyError:
                            print(f)
                            print(data)
                            break


The code even catches the error when a column name is wrong in the Excel sheet.
This will output a file `Dictionary.txt` that you can copy to your Toolbox
project folder to overwrite the original `Dictionary.txt`. With this we were
able to generate the whole dictionary in Toolbox.