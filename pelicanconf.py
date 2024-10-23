#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Peter Bouda"
SITENAME = "Peter Bouda"
SITESUBTITLE = "Natural Language Processing Consultant"
SITEURL = "http://www.peterbouda.eu"  #

USE_FOLDER_AS_CATEGORY = True
ARTICLE_EXCLUDES = ["tutorials"]
TYPOGRIFY = True

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = [
    "images",
    "tutorials",
    "extra/android-chrome-192x192.png",
    "extra/android-chrome-512x512.png",
    "extra/apple-touch-icon.png",
    "extra/browserconfig.xml",
    "extra/favicon-16x16.png",
    "extra/favicon-32x32.png",
    "extra/favicon.ico",
    "extra/manifest.json",
    "extra/mstile-70x70.png",
    "extra/mstile-144x144.png",
    "extra/mstile-150x150.png",
    "extra/mstile-310x150.png",
    "extra/mstile-310x310.png",
    "extra/safari-pinned-tab.svg",
]

EXTRA_PATH_METADATA = {
    "extra/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extra/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extra/browserconfig.xml": {"path": "browserconfig.xml"},
    "extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/manifest.json": {"path": "manifest.json"},
    "extra/mstile-70x70.png": {"path": "mstile-70x70.png"},
    "extra/mstile-144x144.png": {"path": "mstile-144x144.png"},
    "extra/mstile-150x150.png": {"path": "mstile-150x150.png"},
    "extra/mstile-310x150.png": {"path": "mstile-310x150.png"},
    "extra/mstile-310x310.png": {"path": "mstile-310x310.png"},
    "extra/safari-pinned-tab.svg": {"path": "safari-pinned-tab.svg"},
}

# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = "Europe/Lisbon"

DEFAULT_LANG = "en"

DEFAULT_PAGINATION = 3

PLUGIN_PATHS = ["plugins"]
PLUGINS = []
PELICAN_COMMENT_SYSTEM = True

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = feeds/all.atom.xml
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("LinkedIn", "https://linkedin.com/in/peterbouda"),
    ("Github", "https://github.com/pbouda"),
    ("E-Mail", "mailto:pbouda@outlook.com"),
)

# DEFAULT_PAGINATION = 10

THEME = "themes/miniport"
