# -*- coding: utf-8 -*-
"""
    sublee
    ~~~~~~

    A Flask application for the homepage of Heungsub Lee.

    :copyright: (c) 2013 by Heungsub Lee
    :license: Public Domain.
"""
from __future__ import with_statement
import functools
import os

from flask import Flask, render_template, send_from_directory
from lxml import html
from markdown import markdown
import yaml


__version__ = '2.0.0'
__all__ = ['app']


RESOURCES = 'resources'
PROFILE = 'profile.md'
META = 'meta.yml'


paths = {'static_url_path': '',
         'static_folder': RESOURCES,
         'template_folder': RESOURCES}
app = Flask(__name__, **paths)


def load_meta(func):
    with open(os.path.join(app.static_folder, META)) as f:
        meta = yaml.load(f)
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return func(meta, *args, **kwargs)
    return wrapped


@app.route('/')
@load_meta
def index(meta):
    with open(os.path.join(app.static_folder, PROFILE)) as f:
        profile_html = markdown(f.read())
    h1 = html.fromstring(profile_html).xpath('//h1')[0].text
    context = {'profile_title': h1, 'profile_html': profile_html}
    context.update(meta)
    return render_template('index.html', **context)


@app.errorhandler(404)
@load_meta
def error_404(meta, error):
    context = {'error': error}
    context.update(meta)
    return render_template('404.html', **context)
