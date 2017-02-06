# -*- coding: utf-8 -*-
"""
   sublee
   ~~~~~~

   http://subl.ee/

   :copyright: (c) 2013-2017 by Heungsub Lee
   :license: Public Domain

"""
from __future__ import unicode_literals, with_statement

from datetime import date, datetime
from functools import partial, wraps
import io
import itertools
import os
import re
import socket
from urlparse import urlparse

import click
from cssmin import cssmin as minify_css
from flask import Flask, render_template
from htmlmin import minify as minify_html
import inflection
import jinja2
from markdown import Markdown
from slimit import minify as minify_js
from werkzeug.exceptions import NotFound
import yaml


__version__ = '2.3.1'
__all__ = ['app']


# Disable __future__.unicode_literals warning.
# See http://click.pocoo.org/5/python3/#unicode-literals for more details.
click.disable_unicode_literals_warning = True


ROOT = os.path.dirname(__file__)
DOCS = os.path.join(ROOT, 'docs')
META = os.path.join(ROOT, 'meta.yml')
THEMES = os.path.join(ROOT, 'themes.yml')


DEFAULT_THEME = 'sublee-light'
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.abbr',
    'markdown.extensions.def_list',
    'markdown.extensions.headerid',
    'markdown.extensions.meta',
    'markdown.extensions.smarty',
    'markdown_attr_plus',
]
MINIFIERS = {
    'text/html': partial(minify_html, remove_optional_attribute_quotes=False),
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


def update_dict(d1, d2):
    d1.update(d2)
    return d1


def is_splitted_trigram_bar(trigram, offset):
    # 9776 is unicode number of ☰ (u'\u2630', TRIGRAM_FOR_HEAVEN).
    # The unicode distance of a trigram from the trigram for heaven is a 3-bit
    # digit.  Splitted bars are at non-negative bits.
    return (ord(trigram) - 9776) & (1 << offset)


app.jinja_env.globals.update({
    'zip': itertools.izip,
    'minify_js': jinja_minify_js,
    'meta': jinja_meta,
    'cdnjs': (lambda path: '//cdnjs.cloudflare.com/ajax/libs/' + path),
})
app.jinja_env.filters.update({'update': update_dict})
app.jinja_env.tests.update({'splitted_trigram_bar': is_splitted_trigram_bar})


@app.after_request
def minify_response(response):
    if not response.direct_passthrough:
        for content_type, minify in MINIFIERS.items():
            if response.content_type.startswith(content_type):
                data = response.get_data(as_text=True)
                response.set_data(minify(data))
                break
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


@app.route('/runker/')
def subleerunker():
    """Frame wrapper of <Subleerunker>."""
    res = render_template('subleerunker.html')
    return res, 200, {'Content-Type': 'application/xhtml+xml'}


def render_error(error):
    """The HTTP error page."""
    ctx = make_context(error=error)
    return render_template('error.html', **ctx)
for status in range(400, 420) + range(500, 506):
    def _error(error, status=status):
        return render_error(error), status
    try:
        app.errorhandler(status)(_error)
    except:
        # Ignore errors during registering an error handler.  KeyError occurs
        # when handling 402 status code on Flask-0.11.
        pass
    del _error


def prepare_freezing(app):
    from glob import glob
    from flask_frozen import Freezer
    freezer = Freezer(app, with_static_files=False)
    app.config.update({
        'FREEZER_DESTINATION_IGNORE': ['.git*', 'CNAME'],
        'FREEZER_IGNORE_MIMETYPE_WARNINGS': True,
    })
    @app.route('/404.html')
    def not_found():
        return render_error(NotFound())
    @freezer.register_generator
    def doc():
        for filename in glob(os.path.join(DOCS, '*.md')):
            filename = os.path.basename(filename)
            doc_name, __ = filename.rsplit(os.path.extsep, 1)
            yield {'doc_name': doc_name}
    @freezer.register_generator
    def css():
        with open(THEMES) as f:
            themes = yaml.load(f)
        for theme in themes.viewkeys():
            yield {'theme': theme}
    return freezer


# Command-line Interface


@click.group()
def cli():
    pass


@cli.command()
@click.option('--host', '-h', default='0.0.0.0')
@click.option('--port', '-p', type=click.IntRange(1, 65536), default=8080)
@click.option('--debug', is_flag=True)
def run(host, port, debug):
    """Run a web server for the website."""
    app.run(host=host, port=port, debug=debug)


@cli.command()
@click.argument('dest', type=click.Path(file_okay=False, writable=True))
def freeze(dest):
    """Freeze the website as static files."""
    app.config['FREEZER_DESTINATION'] = dest
    freezer = prepare_freezing(app)
    freezer.freeze()


@cli.command('verify-links')
@click.option('--timeout', type=float, default=3)
@click.option('--fail-on-warning', is_flag=True)
@click.pass_context
def verify_links(ctx, timeout, fail_on_warning):
    """Verify all hyper-links to be alive."""
    from collections import defaultdict
    from threading import Lock, Thread
    import lxml.html
    import requests
    client = app.test_client()
    # collect hyper-links.
    freezer = prepare_freezing(app)
    src_urls = list(freezer.all_urls())
    linked_urls = defaultdict(set)
    with click.progressbar(src_urls, label='Collecting', show_pos=True) as bar:
        for src_url in bar:
            res = client.get(src_url)
            if res.mimetype not in ['text/html', 'application/xhtml+xml']:
                continue
            html = lxml.html.fromstring(res.data)
            for linked_url in html.xpath('//a/@href'):
                if linked_url.split('://', 1)[0] in ['http', 'https']:
                    linked_urls[linked_url].add(src_url)
    # verify collected hyper-links.
    ERROR, WARNING, NOTICE = 0, 1, 2
    broken_urls = []
    with click.progressbar(length=len(linked_urls),
                           label='Verifying', show_pos=True) as bar:
        lock = Lock()
        def bar_updater(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                try:
                    return f(*args, **kwargs)
                finally:
                    lock.acquire()
                    bar.update(1)
                    lock.release()
            return wrapped
        # some websites such as LinkedIn denies HTTP requests if User-Agent not
        # in a header.
        @bar_updater
        def verify_link(url, src_urls, headers={'User-Agent': 'subl.ee'}):
            if urlparse(url).hostname.endswith('linkedin.com'):
                broken_urls.append((NOTICE, url, src_urls,
                                    'LinkedIn denies non-browser request'))
                return
            try:
                res = requests.get(url, headers=headers, timeout=timeout)
            except requests.exceptions.Timeout as exc:
                broken_urls.append((WARNING, url, src_urls, exc))
            except requests.RequestException as exc:
                broken_urls.append((ERROR, url, src_urls, exc))
            except socket.error as exc:
                broken_urls.append((ERROR, url, src_urls, exc))
            else:
                if res.status_code != 200:
                    broken_urls.append((ERROR, url, src_urls, res))
        threads = []
        for linked_url, src_urls in linked_urls.items():
            thread = Thread(target=verify_link, args=(linked_url, src_urls))
            threads.append(thread)
            thread.daemon = True
            thread.start()
        # join all threads.
        for thread in threads:
            thread.join()
    # report.
    if not broken_urls:
        ctx.exit()
    erred = False
    for level, url, src_urls, reason in broken_urls:
        args = (', '.join(sorted(src_urls)), url, reason)
        if level == ERROR:
            click.secho('E %s -> %s: %s' % args, fg='red')
            erred = True
        elif level == WARNING:
            click.secho('W %s -> %s: %s' % args, fg='yellow')
            if fail_on_warning:
                erred = True
        elif level == NOTICE:
            click.secho('N %s -> %s: %s' % args, fg='green')
    if erred:
        ctx.exit(1)


if __name__ == '__main__':
    cli()
