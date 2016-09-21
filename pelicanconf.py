#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Bouda'
SITENAME = 'Peter Bouda'
SITESUBTITLE = 'Embedded Qt, Python and JavaScript'
SITEURL = 'http://www.peterbouda.eu' #

USE_FOLDER_AS_CATEGORY = True
ARTICLE_EXCLUDES = [ 'tutorials' ]
TYPOGRIFY = True

DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ['images', 'tutorials']
#DISPLAY_PAGES_ON_MENU = True
#DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 3

PLUGIN_PATHS = [ 'plugins' ]
PLUGINS = [ 'pelican_comment_system' ]
PELICAN_COMMENT_SYSTEM = True

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = feeds/all.atom.xml
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/legocoder'),
          ('LinkedIn', 'https://linkedin.com/in/peterbouda'),
          ('Github', 'https://github.com/pbouda'),
          ('E-Mail', 'mailto:hey@peterbouda.eu'))

#DEFAULT_PAGINATION = 10

THEME = "themes/miniport"

#PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

#DISQUS_SITENAME = 'pbouda'
#GOOGLE_ANALYTICS = 'UA-35434502-1'

#GITHUB_URL = 'https://github.com/pbouda'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
