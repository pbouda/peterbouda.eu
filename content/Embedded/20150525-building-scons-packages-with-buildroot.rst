Building scons packages with buildroot
======================================
:date: 2015-05-25 12:13
:tags: buildroot, scons

For my hardware project `Die Brummbeere
<http://brummbeere.readthedocs.org/en/latest/>`_ I started to work with
buildroot a lot. For sound visualization in Die Brummbeere I wanted to use
`the sonotopy library <https://github.com/alex-berman/sonotopy>`_, and use my
existing buildroot toolchain to compile it for the Raspberry. Unfortunately, it
didn't work out of the box. First, it was not quite clear how to build scons
for the host, but a quick search for scons and buildroot led me to:

.. code-block:: sh

   $ make host-scons

After that I started to create my own package for sonotopy based on the
information in the buildroot documentation. I added a ``Config.in`` and
``sonotopy.mk`` file that I copied from another scons-based package in buildroot
(benejson) and modified them, but without luck. My ``Config.in`` contains:

.. code-block:: config

   config BR2_PACKAGE_SONOTOPY
		bool "sonotopy"
		select HOST_SCONS
		depeds on BR2_PACKAGE_FFTW
		help
			Sonotopy is a C++ library for perceptually analyzing the contents of
			an acoustic signal in real time.

			https://github.com/alex-berman/sonotopy


My ``sonotopy.mk`` is:

.. code-block:: config

	################################################################################
	#
	# sonotopy
	#
	################################################################################

	SONOTOPY_VERSION = master
	SONOTOPY_SOURCE = master.tar.gz
	SONOTOPY_SITE = https://github.com/pbouda/sonotopy/archive/
	SONOTOPY_LICENSE = GPLv3+
	SONOTOPY_LICENSE_FILES = LICENSE
	SONOTOPY_INSTALL_STAGING = YES
	SONOTOPY_DEPENDENCIES = host-scons

	define SONOTOPY_BUILD_CMDS
		(cd $(@D); \
			$(TARGET_CONFIGURE_OPTS) CROSS=$(TARGET_CROSS) \
			$(SCONS))
	endef

	define SONOTOPY_INSTALL_STATIC_LIB
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/sonotopy.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/sonotopy.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/AudioParameters.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/AudioParameters.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/BeatTracker.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/BeatTracker.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/CircleMap.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/CircleMap.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/CircleMapParameters.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/CircleMapParameters.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/CircleTopology.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/CircleTopology.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/CircularBuffer.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/CircularBuffer.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/DisjointGridMap.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/DisjointGridMap.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/DisjointGridTopology.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/DisjointGridTopology.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/EventDetector.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/EventDetector.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/GridMap.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/GridMap.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/GridMapParameters.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/GridMapParameters.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/Normalizer.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/Normalizer.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/Random.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/Random.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/RectGridTopology.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/RectGridTopology.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/Smoother.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/Smoother.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/SOM.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/SOM.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/SpectrumAnalyzer.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/SpectrumAnalyzer.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/SpectrumAnalyzerParameters.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/SpectrumAnalyzerParameters.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/SpectrumBinDivider.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/SpectrumBinDivider.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/SpectrumMap.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/SpectrumMap.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/SpectrumMapParameters.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/SpectrumMapParameters.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/Stopwatch.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/Stopwatch.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/Topology.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/Topology.hpp; \
		$(INSTALL) -D -m 0644 $(@D)/include/sonotopy/TwoDimArray.hpp \
			$(STAGING_DIR)/usr/include/sonotopy/TwoDimArray.hpp
		$(INSTALL) -D -m 0644 $(@D)/build/release/src/libsonotopy.a \
			$(1)/usr/lib/libsonotopy.a
	endef

	define SONOTOPY_INSTALL_STAGING_CMDS
		$(call SONOTOPY_INSTALL_STATIC_LIB,$(STAGING_DIR))
	endef

	$(eval $(generic-package))

The package compiles fine, but the architecture of resulting binary file is that
of my host, and not of my target (the Raspberry). Luckily, I got some help on
the buildroot IRC channel. I had to still modify sonotopy's ``SConstruct`` file,
so that it uses the ``CROSS`` environment variable to set the correct compiler
and linker variables:

.. code-block:: python

	if 'CROSS' in os.environ:
		cross = os.environ['CROSS']
		env.Append(CROSS = cross)
		env.Replace(CC = cross + 'gcc')
		env.Replace(CXX = cross + 'g++')
		env.Replace(LD = cross + 'ld')

Now sonotopy compiled fine and I could use it in my projects on the Raspberry.
To try it out you may just use my own fork of sonotopy on GitHub:

https://github.com/pbouda/sonotopy

Sonotopy comes with a few examples with requirements that I didn't want to
compile for my project. I already have Qt with audio input and output, so I 
build a little Qt project to visualize the GridMap calculations of sonotopy
in a QML view. The project is called Sonobeere, the current tree with the
GridMap example is on GitHub:

https://github.com/pbouda/sonobeere/tree/5a6efd0275cea9f4dd1c3920def19766663b0f8f
