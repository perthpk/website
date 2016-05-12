#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Perth Parkour'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Perth'

DEFAULT_LANG = 'en'

THEME = "themes/medius"
INDEX_SAVE_AS = 'pages/blog.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('Blog', '/pages/blog.html'),)
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
