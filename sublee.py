# -*- coding: utf-8 -*-
"""
    sublee
    ~~~~~~

    http://subl.ee/

    :copyright: (c) 2013-2014 by Heungsub Lee
    :license: Public Domain.
"""
from __future__ import with_statement
import functools
import os
import re
import sys

from flask import Flask, make_response, render_template
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


paths = {'static_url_path': '',
         'static_folder': ASSETS,
         'template_folder': ASSETS}
app = Flask(__name__, **paths)


def load_meta(func):
    """A decorator which gives the current meta data as the first argument of
    the function.

       @load_meta
       def some_func(meta):
           # work with meta
           pass

       some_func()

    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        with open(META) as f:
            meta = yaml.load(f)
        return func(meta, *args, **kwargs)
    return wrapped


def decorate_profile_doc(doc):
    doc.xpath('//ul')[0].attrib['class'] = 'sentences'
    return doc


@app.route('/')
@load_meta
def index(meta):
    """The homepage."""
    with open(PROFILE) as f:
        profile_md = f.read().decode('utf-8')
    profile_html = markdown(profile_md, extensions=MARKDOWN_EXTENSIONS)
    profile_doc = html.fromstring(profile_html)
    profile_doc = decorate_profile_doc(profile_doc)
    h1 = profile_doc.xpath('//h1')[0].text
    context = {'profile_title': h1, 'profile_html': html.tostring(profile_doc)}
    context['theme'] = DEFAULT_THEME
    context.update(meta)
    return render_template('index.html', **context)


def rgba(rgb_hex, alpha=1):
    """Converts RGB hex string to CSS RGBA expression."""
    rgb_hex = re.sub('^#', '', rgb_hex)
    if len(rgb_hex) == 3:
        rgb_hex = '{0}{0}{1}{1}{2}{2}'.format(*rgb_hex)
    r = int(rgb_hex[0:2], 16)
    g = int(rgb_hex[2:4], 16)
    b = int(rgb_hex[4:6], 16)
    return 'rgba({0}, {1}, {2}, {3})'.format(r, g, b, alpha)


@app.route('/style-<theme>.css')
def css(theme):
    """Generates a CSS file from the given theme."""
    with open(THEMES) as f:
        themes = yaml.load(f)
    colors = themes[theme]
    css = render_template('style.css_t', rgba=rgba, **colors)
    response = make_response(css)
    response.headers['Content-Type'] = 'text/css'
    return response


@load_meta
def error(meta, error):
    """The HTTP error page."""
    context = {'error': error}
    context['theme'] = DEFAULT_THEME
    context.update(meta)
    return render_template('error.html', **context)


for status in range(400, 420) + range(500, 506):
    register_error_handler = app.errorhandler(status)
    register_error_handler(error)


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except (IndexError, ValueError):
        port = 8080
    app.run(host='0.0.0.0', port=port)
