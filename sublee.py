# -*- coding: utf-8 -*-
"""
    sublee
    ~~~~~~

    http://subl.ee/

    :copyright: (c) 2013-2014 by Heungsub Lee
    :license: Public Domain.
"""
from __future__ import unicode_literals, with_statement
from datetime import date
import itertools
import os
import re
import sys

from flask import Flask, render_template
from lxml import html
from markdown import markdown
import yaml


__version__ = '2.2.1'
__all__ = ['app']


ASSETS = os.path.join(os.path.dirname(__file__), 'assets')
PROFILE = os.path.join(os.path.dirname(__file__), 'profile.md')
META = os.path.join(os.path.dirname(__file__), 'meta.yml')
THEMES = os.path.join(os.path.dirname(__file__), 'themes.yml')
DEFAULT_THEME = 'sublee'
MARKDOWN_EXTENSIONS = ['markdown.extensions.def_list']
EN_DASH = '\u2013'


paths = {'static_url_path': '',
         'static_folder': ASSETS,
         'template_folder': ASSETS}
app = Flask(__name__, **paths)
app.jinja_env.globals.update(
    zip=itertools.izip,
    cdnjs=(lambda path: '//cdnjs.cloudflare.com/ajax/libs/' + path))


def copyright_year(year_since=None, dash=EN_DASH):
    """Generates an auto-renewed year range of the copyright.
    """
    this_year = date.today().year
    if year_since is None or year_since == this_year:
        return str(this_year)
    return '{0}{1}{2}'.format(year_since, dash, this_year)


def decorate_profile_doc(doc):
    doc.xpath('//ul')[0].attrib['class'] = 'sentences'
    return doc


def make_context(*args, **kwargs):
    with open(META) as f:
        meta = yaml.load(f)
    copyright_year_since = meta.get('copyright_year_since')
    c = dict(meta, theme=DEFAULT_THEME,
             copyright_year=copyright_year(copyright_year_since))
    c.update(*args, **kwargs)
    return c


@app.route('/')
def index():
    """The homepage."""
    with open(PROFILE) as f:
        profile_md = f.read().decode('utf-8')
    profile_html = markdown(profile_md, extensions=MARKDOWN_EXTENSIONS)
    profile_doc = html.fromstring(profile_html)
    profile_doc = decorate_profile_doc(profile_doc)
    profile_html = html.tostring(profile_doc)
    profile_title = profile_doc.xpath('//h1')[0].text
    ctx = make_context(profile_title=profile_title, profile_html=profile_html)
    return render_template('index.html', **ctx)


@app.route('/themes/')
def themes():
    """Theme selector."""
    with open(THEMES) as f:
        themes = yaml.load(f)
    ctx = make_context(themes=themes)
    return render_template('themes.html', **ctx)


def error(error):
    """The HTTP error page."""
    ctx = make_context(error=error)
    return render_template('error.html', **ctx)
for status in range(400, 420) + range(500, 506):
    register_error_handler = app.errorhandler(status)
    register_error_handler(error)


@app.route('/runker/')
def subleerunker():
    """Frame wrapper of <Subleerunker>."""
    return render_template('subleerunker.html')


def rgba(color, alpha=1):
    """Converts RGB hex string to CSS RGBA expression."""
    if color.startswith('#'):
        rgb_hex = color[1:]
        if len(rgb_hex) == 3:
            rgb_hex = '{0}{0}{1}{1}{2}{2}'.format(*rgb_hex)
        r = int(rgb_hex[0:2], 16)
        g = int(rgb_hex[2:4], 16)
        b = int(rgb_hex[4:6], 16)
    elif color.startswith('rgb('):
        r, g, b = re.findall('\d+', color)
    elif color.startswith('rgba('):
        return color
    return 'rgba({0}, {1}, {2}, {3})'.format(r, g, b, alpha)


@app.route('/style-<theme>.css')
def css(theme):
    """Generates a CSS file from the given theme."""
    with open(THEMES) as f:
        themes = yaml.load(f)
    colors = themes[theme]
    css = render_template('style.css_t', rgba=rgba, **colors)
    return css, 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except (IndexError, ValueError):
        port = 8080
    app.run(host='0.0.0.0', port=port)
