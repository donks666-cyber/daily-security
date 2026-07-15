#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = 'Daily Security'
SITENAME = '去社会安全'
SITEDESCRIPTION = '去社会安全资讯 — 漏洞、工具、技术与新闻'
SITEURL = 'https://daily-security.xunpeijie.workers.dev'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

DATE_FORMATS = {
    'en': '%b %d, %Y',
}

THEME = 'themes/daily-security'
THEME_STATIC_DIR = 'static'
M_THEME_COLOR = '#22272e'
M_CSS_FILES = [
    'https://fonts.googleapis.com/css?family=Source+Code+Pro:400,400i,600%7CSource+Sans+Pro:400,400i,600,600i&subset=latin-ext',
    'static/m-dark.compiled.css',
    'static/css/custom.css',
]

M_BLOG_NAME = SITENAME
M_BLOG_DESCRIPTION = SITEDESCRIPTION
M_BLOG_URL = 'https://daily-security.xunpeijie.workers.dev'

M_FAVICON = ('images/favicon.png', 'image/png')

M_NEWSLETTER_URL = ''

M_SOCIAL_TWITTER_SITE = '@daily_security'
M_SOCIAL_IMAGE = 'images/logo.svg'
M_SOCIAL_BLOG_SUMMARY = SITEDESCRIPTION

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extras']
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

MARKUP = ['markdown', 'restructuredtext']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = '资讯'

PLUGIN_PATHS = ['themes/m.css/plugins']
PLUGINS = [
    'm.abbr',
    'm.alias',
    'm.code',
    'm.components',
    'm.filesize',
    'm.gh',
    'm.gl',
    'm.htmlsanity',
    'm.images',
    'm.link',
    'm.metadata',
]

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description']

M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = False
