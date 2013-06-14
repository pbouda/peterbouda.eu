Title: Sirup, Scheiben und Kreissegmente mit SymPy
Date: 2013-06-14 14:58
Category: Python

<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

Ich lese gerade das durchaus empfehlenswerte Buch <a href="http://www.amazon.de/
gp/product/048669609X/ref=as_li_qf_sp_asin_tl?ie=UTF8&camp=1638&creative=6742&cr
eativeASIN=048669609X&linkCode=as2&tag=jsusde-21">Foundations and Fundamental
Concepts of Mathematics</a><img src="http://www.assoc-
amazon.de/e/ir?t=jsusde-21&l=as2&o=3&a=048669609X" width="1" height="1"
border="0" alt="" style="border:none !important; margin:0px !important;" /> von
Howard Eves. Das erste Kapitel handelt von vor-Euklidischer Mathematik und
schließt mit einer Reihe interessanter Aufgaben, über die sich schon die
Babylonier und Griechen den Kopf zerbrochen haben. Eine besonders schöne
Fragestellung geht so (Aufgabe 1.1.5):

Eine Scheibe mit Radius R rotiert vertikal an einer horizontalen Achse. Die
Scheibe taucht dabei in eine Flüssigkeit ein, so dass ein Teil davon benetzt
wird. In welcher Höhe muss man die Scheibe über der Flüssigkeit befestigen,
damit die benetzte Fläche *über* der Flüssigkeit maximal wird?

Das Problem trat anscheinend bei der Sirupherstellung in der Antike auf. Ich
habe das Ganze mal versucht zu zeichnen, die rote Fläche soll die gesuchte
benetzte Oberfläche anzeigen:

![Scheibe rotiert über Flüssigkeit](/static/images/sirupscheibe.png)

Zur Lösung des Problems verwende ich hier die Bibliothek
[SymPy](http://sympy.org/). Dieser Text wurde als [IPython
Notebook](http://ipython.org/notebook.html) verfasst, dieses gibt es zum
Download:

[https://github.com/pbouda/peterbouda.eu/blob/master/notebooks/sympy_scheibenseg
ment.ipynb](https://github.com/pbouda/peterbouda.eu/blob/master/notebooks/sympy_
scheibensegment.ipynb)

## Voraussetzungen

Wir setzen voraus, dass wir die Formeln für die Flächen der einzelnen Teile der
Scheibe berechnen können. Dazu gehört:

* der gesamte Flächeninhalt der Scheibe: $$A_1 = R^2\pi$$
* der Ring auf der Scheibe, der insgesamt bei Rotation mit der Flüssigkeit in
Berührung kommt(wobei `r` dann der Höhe der Achse über der Flüssigkeit
entspricht): $$A_2 = r^2\pi$$
* der Teil der Scheibe, der jeweils unter Wasser ist (siehe
http://de.wikipedia.org/wiki/Kreissegment): $$A_3 = R^2\arccos{r\over R} -
r\sqrt{R^2 - r^2}$$

Die von uns gesuchte Fläche ist dann einfach: $$A = A_1 - A_2 - A_3$$
also eingesetzt: $$A = R^2\pi - r^2\pi - R^2\arccos{r\over R} + r\sqrt{R^2 -
r^2}$$

Diese Formel können wir gleich so in SymPy übernehmen:

In[54]:
```
from sympy import *
%load_ext sympy.interactive.ipythonprinting

r, R = symbols("r R")

A = R**2*pi - r**2*pi - R**2*acos(r/R) + r*sqrt(R**2 - r**2)
A
```


$$- R^{2} \operatorname{acos}{\left (\frac{r}{R} \right )} + \pi R^{2} - \pi r^{2} + r \sqrt{R^{2} - r^{2}}$$


## Empirisches Maximum

Als Erstes wollen wir das Maximum empirisch bestimmen, also einfach gegebene
Werte für `R` und `r` einsetzen und ausgeben. Dazu können wir als zunächst `R`
einen festen Wert zuweisen, ich nehme einfach 10 für den Radius der Scheibe:

In[52]:
```
A_10 = A.subs(R, 10)
A_10
```


$$- \pi r^{2} + r \sqrt{- r^{2} + 100} - 100 \operatorname{acos}{\left (\frac{1}{10} r \right )} + 100 \pi$$


Für `r` probieren wir jetzt Werte zwischen 0 und 9:

In[55]:
```
for i in range(10):
    print("{0}/10 -> {1}".format(i, A_10.subs(r, i).evalf()))
```

    0/10 -> 157.079632679490
    1/10 -> 173.904656513122
    2/10 -> 184.244972086429
    3/10 -> 187.892740241230
    4/10 -> 184.626440388448
    5/10 -> 174.200964088797
    6/10 -> 156.332408029586
    7/10 -> 130.671341314465
    8/10 -> 96.7472246499041
    9/10 -> 53.8176697304459
    

Die benetzte Fläche ist hier also maximal für `r = 3/10*R` (also `r = 3` für `R
= 10`). Wir können uns die Werte zwischen 2 und 4 für `r` noch genauer
anschauen:

In[27]:
```
import numpy
for i in [2.0+k*0.1 for k in range(20)]:
    print("{0}/10 -> {1}".format(i, A_10.subs(r, i).evalf()))
```

    2.0/10 -> 184.244972086429
    2.1/10 -> 184.914434156967
    2.2/10 -> 185.516768466727
    2.3/10 -> 186.051760290858
    2.4/10 -> 186.519193409771
    2.5/10 -> 186.918850022558
    2.6/10 -> 187.250510657582
    2.7/10 -> 187.513954080027
    2.8/10 -> 187.708957196178
    2.9/10 -> 187.835294954213
    3.0/10 -> 187.892740241230
    3.1/10 -> 187.881063776257
    3.2/10 -> 187.800033998950
    3.3/10 -> 187.649416953652
    3.4000000000000004/10 -> 187.428976168492
    3.5/10 -> 187.138472529157
    3.6/10 -> 186.777664146939
    3.7/10 -> 186.346306220629
    3.8/10 -> 185.844150891815
    3.9000000000000004/10 -> 185.270947093061
    

Hier ist der Wert bei `3.0` maximal. Wir können also annehmen, dass die Höhe der
Scheibe in etwa `3/10*R` sein sollte. Das ist auch der Wert, der in der Antike
berechnet und dann für die Höhe der Scheibe verwendet wurde.

## Analytisches Maximum

Das analytische Maximum bestimmen wir einfach aus der Ableitung von `A` nach
`r`:

In[33]:
```
A_diff = diff(A, r, 1)
A_diff
```


$$\frac{R}{\sqrt{1 - \frac{r^{2}}{R^{2}}}} - \frac{r^{2}}{\sqrt{R^{2} - r^{2}}} - 2 \pi r + \sqrt{R^{2} - r^{2}}$$


Es lohnt sich übrigens als Übung diese Ableitung auch einmal manuell aus der
Formel zu berechnen. Um die Extremwerte zu bestimmten setzen wir die Ableitung
auf `0`:

In[43]:
```
extremwerte = solve(A_diff, r)
extremwerte
```


$$\begin{bmatrix}- \frac{\sqrt{R^{2}}}{\sqrt{1 + \pi^{2}}}, & \frac{\sqrt{R^{2}}}{\sqrt{1 + \pi^{2}}}, & - \frac{\pi \sqrt{R^{2}}}{\sqrt{1 + \pi^{2}}}, & \frac{\pi \sqrt{R^{2}}}{\sqrt{1 + \pi^{2}}}\end{bmatrix}$$


Die negativen Werte können wir in diesem Fall beseite lassen. Für `R = 10`
werden die anderen beiden Extremwerte zu:

In[48]:
```
maximum = extremwerte[1].subs(R, 10).evalf()
minimum = extremwerte[3].subs(R, 10).evalf()
maximum, minimum
```


$$\begin{pmatrix}3.03314471053353, & 9.52890513988687\end{pmatrix}$$


Das es sich tatsächlich um ein Maximum und ein Minimum handelt sieht man zum
Beispiel, wenn man die Werte in die Formel von `A_10` einsetzt:

In[51]:
```
(A_10.subs(r, maximum).evalf(), A_10.subs(r, minimum).evalf())
```


$$\begin{pmatrix}187.896539791088, & 26.9881893328488\end{pmatrix}$$


Alternativ kann man natürlich die zweite Ableitung bemühen. Das überlasse ich
dem Leser hiermit als Übung.
