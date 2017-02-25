#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jay Gondin'
SITENAME = 'Jay Gondin'
ALT_NAME = 'Jay Gondin'
SITESUBTITLE = 'A tour of my Data Science projects'
DESCRIPTION = 'A blog about data science, analitics, AI, machine learning, deep learning.'
#SITEURL = 'https://jgondin.github.io'
SITEURL = 'http://localhost:8000'

#META_IMAGE = SITEURL + "static/img/og_logo.jpg"
#META_IMAGE_TYPE = "image/jpeg"
FAVICON_PATH = '/theme/images/icons/linkedin.png'
PATH = 'content'


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

#THEME = '/hdd/gondin/projects-github/pelican-themes/notmyidea-cms'


SUMMARY_MAX_LENGTH = 50

#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

"""
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/j_gondin'),
	('github', 'https://github.com/jgondin'),
    ('linkedin','https://www.linkedin.com/in/gondin'),
    ('Email','mailto:jay.gondin@gmail.com'),)

SHARE = True

FOOTER = ("&copy; 2017 Jose (Jay) Gondin. All rights reserved.<br>" +
	"Code snippets in the pages are released under " +
    "<a href=\"http://opensource.org/licenses/MIT\" target=\"_blank\">" +
    "The MIT License</a>, unless otherwise specified.")



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Theme Settings
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
PAGINATED_DIRECT_TEMPLATES = ( 'index','categories', 'pages')
STATIC_PATHS = ['pdfs']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False



MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Contact', '/pages/contact.html'),
    ('Resume', '/pdfs/jay_resume.pdf'),
    ('Archives', '/archives.html'),
    ('Tags','/tags.html')
    
)

RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUPUT_DIRECTORY = True

TWITTER_USERNAME = 'j_gondin'
LINKEDIN = 'jgondin'

#Plugin settings
MARKUP = ('md', 'ipnb')

PLUGIN_PATH = 'plugins'
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']
