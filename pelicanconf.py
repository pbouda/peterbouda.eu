#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Bouda'
SITENAME = 'Programming Society'
#SITESUBTITLE = 'Peter writing about Open Source Language Technologies.'
SITEURL = 'http://www.peterbouda.eu' #

DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ['images', 'tutorials']
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = feeds/all.atom.xml
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Poio', 'http://www.poio.eu'),
         ('QuantHistLing', 'http://www.quanthistling.info/'),
         ('CIDLeS', 'http://www.cidles.eu/'),
         ('Archive', '/archives.html')
        )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/legocoder'),
          ('Tumblr', 'http://languagediversity.tumblr.com'),
          ('Google+', 'https://plus.google.com/+PeterBouda'),
          ('LinkedIn', 'http://www.linkedin.com/pub/peter-bouda/9/929/917'),
          ('Github', 'https://github.com/pbouda'),
          ('E-Mail', 'mailto:pbouda@cidles.eu'))

DEFAULT_PAGINATION = 10

THEME = "themes/initializr"

DISQUS_SITENAME = 'pbouda'
GOOGLE_ANALYTICS = 'UA-35434502-1'

#GITHUB_URL = 'https://github.com/pbouda'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
