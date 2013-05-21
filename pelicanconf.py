#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Bouda'
SITENAME = 'Das Skript.'
SITEURL = '' # http://www.peterbouda.eu

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = feeds/all.atom.xml
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Poio - Python for Linguists', 'http://media.cidles.eu/poio/'),
          ('QuantHistLing', 'http://www.quanthistling.info/'),
          ('CIDLeS', 'http://www.cidles.eu/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/legocoder'),
          ('Github', 'https://github.com/pbouda'),
          ('LinkedIn', 'http://www.linkedin.com/pub/peter-bouda/9/929/917'),
          ('E-Mail', 'mailto:pbouda@cidles.eu'),)

DEFAULT_PAGINATION = 10

THEME = "themes/notmyidea"

DISQUS_SITENAME = 'pbouda'
GOOGLE_ANALYTICS = 'UA-35434502-1'

#GITHUB_URL = 'https://github.com/pbouda'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
