Die Brummbeere: an embedded ownCloud music player
=================================================
:date: 2015-05-04 11:47
:tags: Qt, Embedded, IoT, ownCloud, Music
:image: http://brummbeere.readthedocs.org/en/latest/_images/brummbeere_raspi.jpg
:imagewidth: 500
:twitter: https://twitter.com/legocoder/status/595174587991592961

I recently `published here a short post
<{filename}/Qt/20150317-twomusic-open-source-audio-player-for-owncloud.rst>`_ about
TwoMusic, an open source music player for ownCloud. As I got interested in
embedded systems and embedded development the last few weeks, I turned the
player into a project for the Raspberry and other boards that run Linux. My
first goal was to boot directly into a minimal Linux system that supports Qt and
its multimedia module. The book "`Embedded Linux lernen mit dem Raspberry Pi
<http://www.amazon.de/gp/product/386490143X/ref=as_li_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=386490143X&linkCode=as2&tag=jsusde-21&linkId=BJJLZYFHUKSX4EHC>`_"
was a very helpful introduction about the whole procedure, and I recommend it
to anyone who reads German.

In the end I came up with my first embedded Linux system that boots the Qt
music player with touch screen support. To reflect the focus on embedded
platforms and especially the Raspberry I changed the project name to "Die
Brummbeere". The documentation of the project on GitHub now contains a longer
description about `how to build your own embedded system
<http://brummbeere.readthedocs.org/en/latest/raspi.html>`_ that boots Die
Brummbeere, so I won't go into details here. As a summary, with all the work
that is done around Linux, the Raspberry, Qt and buildroot, it was amazingly
easy to build your own embedded device. I really felt like on the shoulders of
giants during the development of the project and hope to be able to give back
in the future...

Die Brummbeere still runs on desktop computers (and probably mobile phones), but
the user interface does not really integrate into anything existing. My goal
over the next weeks is to understand the cross-platform opportunities of Qt
regarding user interfaces better. Maybe develop some kind of responsive approach
to Qt GUIs that allows to share most of the QML code. I really like what
`Microsoft presented as their Continuum approach
<http://techcrunch.com/2015/04/29/microsoft-announces-continuum-turning-windows-10-phones-into-desktops/>`_,
I am very curious how you could mimic that with Qt.