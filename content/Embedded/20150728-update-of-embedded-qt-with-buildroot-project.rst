Update of Embedded Qt with Buildroot project
============================================
:date: 2015-07-28 09:23
:tags: Qt, Buildroot
:image: https://cloud.peterbouda.eu/index.php/s/Guq7fGkURyqf6mG/download
:imagewidth: 800

I while ago I published a first version of my `Buildroot configuration for
Embedded Qt development
<{filename}/Embedded/20150602-embedded-qt-with-buildroot.rst>`_. Since then the
project evolved and there are now a few important additions available:

1) I added a helper script ``build.sh`` to the project that starts the whole
configuration and build process. No need to enter shell commands manually
anymore! You can pass a parameter to the script, to choose a configuration.
Currently, the main purpose is to either load the configuration for the
Raspberry A/B(+) or the one for the Raspberry 2. Check the
README how it works.

2) I added a first test configuration that uses systemd as init system. I am now
using systemd in my project `Die Brummbeere <http://brummbeere.readthedocs.org/>`_
to be able to set a dependency on network access before I start the app, and
thought that it makes sense to make the configuration available. The
configuration just uses the standard setup of systemd on Buildroot. You can
use the systemd configuration via passing an option to the ``build.sh`` script
or manully load it in Buildroot as explained in the README.

3) I added support for remote deployment via Qt Creator. I had to change from
the Dropbear SSH server to OpenSSH for that, as for some reason Qt Creator just
could not copy files to the Raspberry via Dropbear. Now everything works and
I added a chapter with the setup process in Qt Creator to the README. With
screenshots and everything, to make it easy for everyone to use remote
deployment.

And here is the repository:

https://github.com/pbouda/buildroot-qt-dev

Happy embedded development!
