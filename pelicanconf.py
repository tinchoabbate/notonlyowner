#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Martin Abbatemarco'
SITENAME = 'Notonlyowner'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Buenos_Aires'

LOCALE = 'en_US'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False
DIRECT_TEMPLATES = ['index']

# URL Settings (https://github.com/getpelican/pelican/blob/master/docs/settings.rst#url-settings)
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DEFAULT_PAGINATION = 10

# Markdown config
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5'
}

STATIC_PATHS = [
    'extra/robots.txt',
    'extra/favicon.ico'
]

IGNORE_FILES = ['.track']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = [THEME + '/plugins']
PLUGINS = ['assets', 'post_stats']

GOOGLE_ANALYTICS = False
