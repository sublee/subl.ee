# -*- coding: utf-8 -*-
"""
    sublee
    ~~~~~~

    http://subl.ee/

    :copyright: (c) 2013-2015 by Heungsub Lee
    :license: Public Domain.

"""
from __future__ import unicode_literals, with_statement
from datetime import date, datetime
import io
import itertools
import os
import re
import sys

from cssmin import cssmin as minify_css
from flask import Flask, render_template
from htmlmin import minify as minify_html
import inflection
import jinja2
from markdown import Markdown
from slimit import minify as minify_js
from werkzeug.exceptions import NotFound
import yaml


__version__ = '2.3.0'
__all__ = ['app']


ROOT = os.path.dirname(__file__)
DOCS = os.path.join(ROOT, 'docs')
META = os.path.join(ROOT, 'meta.yml')
THEMES = os.path.join(ROOT, 'themes.yml')


DEFAULT_THEME = 'sublee-light'
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.abbr',
    'markdown.extensions.attr_list',
    'markdown.extensions.def_list',
    'markdown.extensions.meta',
    'markdown.extensions.smarty',
]
MINIFIERS = {
    'text/html': minify_html,
    'text/css': minify_css,
    'text/javascript': minify_js,
}


#: The Flask application.
app = Flask(__name__, static_url_path='/-')


def jinja_minify_js(caller, mangle_toplevel=False):
    return minify_js(caller(), mangle=True, mangle_toplevel=mangle_toplevel)


def jinja_meta(content, **attrs):
    buf = io.StringIO()
    buf.write('<meta ')
    for key, attr in attrs.items():
        key = key.replace('_', '-')
        attr = jinja2.escape(attr)
        buf.write('{key}="{attr}" '.format(key=key, attr=attr))
    content = jinja2.escape(content)
    buf.write('content="{content}" />'.format(content=content))
    return jinja2.Markup(buf.getvalue())


app.jinja_env.globals.update(
    zip=itertools.izip, minify_js=jinja_minify_js, meta=jinja_meta,
    cdnjs=(lambda path: '//cdnjs.cloudflare.com/ajax/libs/' + path))


@app.after_request
def minify_response(response):
    for content_type, minify in MINIFIERS.items():
        if response.content_type.startswith(content_type):
            data = response.get_data(as_text=True)
            response.set_data(minify(data))
            break
    # response.headers['Cache-Control'] = 'max-age=600'
    return response


def copyright_year(year_since=None, dash='\u2013'):
    """Generates an auto-renewed year range of the copyright."""
    this_year = date.today().year
    if year_since is None or year_since == this_year:
        return str(this_year)
    return '{0}{1}{2}'.format(year_since, dash, this_year)


def make_context(*args, **kwargs):
    with open(META) as f:
        meta = yaml.load(f)
    copyright_year_since = meta.get('copyright_year_since')
    c = dict(meta, theme=DEFAULT_THEME,
             copyright_year=copyright_year(copyright_year_since))
    c.update(*args, **kwargs)
    return c


def normalize_doc_meta(raw_meta):
    normal_meta = {}
    for key, values in raw_meta.items():
        key = inflection.underscore(key)
        value = '\n'.join(values)
        normal_meta[key] = value
    return normal_meta


@app.route('/', defaults={'doc_name': 'profile'})
@app.route('/<doc_name>/')
def doc(doc_name):
    filename = os.path.join(DOCS, os.path.extsep.join([doc_name, 'md']))
    try:
        with open(filename) as f:
            doc_text = f.read().decode('utf-8')
    except IOError:
        raise NotFound
    markdown = Markdown(extensions=MARKDOWN_EXTENSIONS)
    doc_html = markdown.convert(doc_text)
    doc_meta = normalize_doc_meta(markdown.Meta)
    stat = os.stat(filename)
    doc_modified_at = datetime.utcfromtimestamp(stat.st_mtime)
    ctx = make_context(doc_html=doc_html, doc_name=doc_name,
                       doc_modified_at=doc_modified_at, **doc_meta)
    return render_template('doc.html', **ctx)


@app.route('/themes/')
def themes():
    """Theme selector."""
    with open(THEMES) as f:
        themes = yaml.load(f)
    ctx = make_context(themes=themes)
    return render_template('themes.html', **ctx)


def render_error(error):
    """The HTTP error page."""
    ctx = make_context(error=error)
    return render_template('error.html', **ctx)
for status in range(400, 420) + range(500, 506):
    @app.errorhandler(status)
    def _error(error, status=status):
        return render_error(error), status
    del _error


@app.route('/runker/')
def subleerunker():
    """Frame wrapper of <Subleerunker>."""
    res = render_template('subleerunker.html')
    return res, 200, {'Content-Type': 'application/xhtml+xml'}


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
    res = render_template('style.css_t', rgba=rgba, **colors)
    return res, 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except (IndexError, ValueError):
        port = 8080
    app.run(host='0.0.0.0', port=port)
