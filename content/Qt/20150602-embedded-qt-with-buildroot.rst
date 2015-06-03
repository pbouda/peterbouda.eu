Embedded Qt with Buildroot
##########################
:date: 2015-06-03 17:04
:tags: Qt, Buildroot
:image: https://owncloud.cidles.eu/public.php?service=files&amp;t=2ee6169bb674e8eaf29950f3dd853c86&amp;download
:imagewidth: 800
:twitter: https://twitter.com/legocoder/status/606125703055015936

I already posted about my project `Die Brummbeere
<{filename}/Qt/20150504-die-brummbeere-an-embedded-owncloud-music-player.rst>`_,
an ownCloud music player built with Qt. For the development on the Raspberry,
I am heavily dependent on `Buildroot <http://buildroot.net/>`_, which is an
awesome project to quickly build your own Linux system with customized libraries
and applications. Qt5 is part of the packages provided by Buildroot, but it
still took me a while to figure out all the dependencies that I need to have
OpenGL support, build a usable Qt multimedia module and get network access with
SSL/TLS support. I thought that this setup might be intersting to others and
extracted the basic configuration from the Die Brummbeere project and created
a seperate Buildroot project that just compiles Qt, with support for remote
deployment in Qt Creator via SSH. In the end it's just a Buildroot configuration
files and a few simple scripts. Oh, and a README, of course :-) It's available
on GitHub:

https://github.com/pbouda/buildroot-qt-dev

Let me know if you think this is useful!
