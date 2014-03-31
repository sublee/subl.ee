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

from flask import Flask, make_response, render_template
from lxml import html
from markdown import markdown
import yaml


__version__ = '2.2.0'
__all__ = ['app']


ASSETS = os.path.join(os.path.dirname(__file__), 'assets')
PROFILE = os.path.join(os.path.dirname(__file__), 'profile.md')
META = os.path.join(os.path.dirname(__file__), 'meta.yml')
THEMES = os.path.join(os.path.dirname(__file__), 'themes.yml')
DEFAULT_THEME = 'sublee'


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


@app.route('/')
@load_meta
def index(meta):
    """The homepage."""
    with open(PROFILE) as f:
        profile_html = markdown(f.read())
    h1 = html.fromstring(profile_html).xpath('//h1')[0].text
    context = {'profile_title': h1, 'profile_html': profile_html}
    context.update(meta)
    return render_template('index.html', **context)


@app.route('/style.css')
def default_css():
    return css(DEFAULT_THEME)


@app.route('/style-<theme>.css')
def css(theme):
    with open(THEMES) as f:
        themes = yaml.load(f)
    colors = themes[theme]
    response = make_response(render_template('style.css_t', **colors))
    response.headers['Content-Type'] = 'text/css'
    return response


@load_meta
def error(meta, error):
    """The HTTP error page."""
    context = {'error': error}
    context.update(meta)
    return render_template('error.html', **context)


for status in range(400, 420) + range(500, 506):
    register_error_handler = app.errorhandler(status)
    register_error_handler(error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
