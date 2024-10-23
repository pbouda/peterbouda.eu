#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.


sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://www.peterbouda.eu"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

FEED_ALL_RSS = "feeds/all.rss"
CATEGORY_FEED_RSS = "feeds/{slug}.rss"

DELETE_OUTPUT_DIRECTORY = False
