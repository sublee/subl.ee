"""
   sublee
   ~~~~~~

   https://subl.ee/

   :copyright: (c) 2013-2019 by Heungsub Lee
   :license: Public Domain

"""
import io
import itertools
import os
import re
from datetime import date
from typing import Any, Dict, Iterator, Optional, Tuple, Union
from urllib.parse import urlparse

import click
import jinja2
import weasyprint
import yaml
from flask import (Flask, Response, make_response, render_template, send_file,
                   url_for)
from flask_frozen import Freezer
from markdown import Markdown
from werkzeug.exceptions import NotFound

__version__ = '2.4.0'
__all__ = ['app']


# Disable __future__.unicode_literals warning.
# See http://click.pocoo.org/5/python3/#unicode-literals for more details.
click.disable_unicode_literals_warning = True


ROOT = os.path.dirname(__file__)
DOCS = os.path.join(ROOT, 'docs')
META = os.path.join(ROOT, 'meta.yml')
THEMES = os.path.join(ROOT, 'themes.yml')


DEFAULT_THEME = 'sublee'
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.abbr',
    'markdown.extensions.attr_list',
    'markdown.extensions.def_list',
    'markdown.extensions.meta',
    'markdown.extensions.smarty',
    'markdown.extensions.toc',
]


# The Flask application.
app = Flask(__name__, static_url_path='/-')


def jinja_meta(content: str, **attrs: str) -> jinja2.Markup:
    """A Jinja function generating <meta> element."""
    buf = io.StringIO()
    buf.write('<meta ')

    for key, attr in attrs.items():
        key = key.replace('_', '-')
        attr = jinja2.escape(attr)
        buf.write('{key}="{attr}" '.format(key=key, attr=attr))

    content = jinja2.escape(content)
    buf.write('content="{content}" />'.format(content=content))

    return jinja2.Markup(buf.getvalue())


def jinja_cdnjs(path: str) -> str:
    """A Jinja function generating a URL at cdnjs."""
    return 'https://cdnjs.cloudflare.com/ajax/libs/%s' % path


def jinja_update(d1: dict, d2: Union[dict, jinja2.Undefined]) -> dict:
    """A Jinja filter updating the target dictionary with the given
    dictionary.
    """
    if not isinstance(d2, jinja2.Undefined):
        d1.update(d2)
    return d1


def jinja_splitted_trigram_bar(trigram: str, offset: int) -> bool:
    """A Jinja test checking whether a tiagram has a splitted bar at the
    offset. For example, (☲, 1) is true while (☲, 0) and (☲, 2) is false.
    """
    # 9776 is unicode number of ☰ (u'\u2630', TRIGRAM_FOR_HEAVEN).
    # The unicode distance of a trigram from the trigram for heaven is a 3-bit
    # digit.  Splitted bars are at non-negative bits.
    return bool((ord(trigram) - 9776) & (1 << offset))


app.jinja_env.globals.update({
    'meta': jinja_meta,
    'cdnjs': (lambda path: '//cdnjs.cloudflare.com/ajax/libs/' + path),
})
app.jinja_env.filters.update({
    'update': jinja_update,
})
app.jinja_env.tests.update({
    'splitted_trigram_bar': jinja_splitted_trigram_bar,
})


def copyright_year(year_since: Optional[int] = None,
                   dash: str = '\u2013',
                   ) -> str:
    """Generates an auto-renewed year range of the copyright."""
    this_year = date.today().year
    if year_since is None or year_since == this_year:
        return str(this_year)
    return '{0}{1}{2}'.format(year_since, dash, this_year)


def make_context(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """Makes a template context with defaults."""
    with open(META) as f:
        meta = yaml.load(f, Loader=yaml.FullLoader)

    copyright_year_since = meta.pop('copyright_year_since')
    c = dict(meta, copyright_year=copyright_year(copyright_year_since))

    c.update(*args, **kwargs)
    return c


def markdown(text: str) -> Tuple[str, Dict[str, str]]:
    """Renders a Markdown document."""
    markdown = Markdown(extensions=MARKDOWN_EXTENSIONS)
    html = markdown.convert(text)
    meta = {k: '\n'.join(v) for k, v in markdown.Meta.items()}
    return html, meta


@app.route('/')
def index() -> str:
    with open(os.path.join(ROOT, 'index.md'), encoding='utf-8') as f:
        html, meta = markdown(f.read())
    ctx = make_context(html=html, **meta)
    return render_template('index.html', **ctx)


@app.route('/resume/')
def resume() -> str:
    with open(os.path.join(ROOT, 'resume.md'), encoding='utf-8') as f:
        html, meta = markdown(f.read())
    ctx = make_context(html=html, **meta)
    return render_template('resume.html', **ctx)


@app.route('/resume.pdf')
def resume_pdf() -> Response:
    font_config = weasyprint.fonts.FontConfiguration()
    html = weasyprint.HTML(string=resume())
    with open(os.path.join(ROOT, 'static/print.css')) as f:
        css = weasyprint.CSS(string=f.read(), font_config=font_config)

    pdf = io.BytesIO()
    html.write_pdf(pdf, stylesheets=[css], font_config=font_config)
    pdf.seek(0)

    return send_file(pdf, mimetype='application/pdf')


@app.route('/themes/')
def themes() -> str:
    """Theme selector."""
    with open(THEMES) as f:
        themes = yaml.load(f, Loader=yaml.FullLoader)
    ctx = make_context(themes=themes)
    return render_template('themes.html', **ctx)


@app.route('/favicon.ico')
def favicon() -> Response:
    return send_file(os.path.join(ROOT, 'favicon.ico'))


def rgba(color: str, alpha: float = 1.0) -> str:
    """Converts RGB hex string to CSS RGBA expression."""
    if color.startswith('#'):
        rgb_hex = color[1:]
        if len(rgb_hex) == 3:
            rgb_hex = '{0}{0}{1}{1}{2}{2}'.format(*rgb_hex)
        r = int(rgb_hex[0:2], 16)
        g = int(rgb_hex[2:4], 16)
        b = int(rgb_hex[4:6], 16)
    elif color.startswith('rgb('):
        r, g, b = re.findall(r'\d+', color)
    elif color.startswith('rgba('):
        return color
    return 'rgba({0}, {1}, {2}, {3})'.format(r, g, b, alpha)


@app.route('/style-<theme>.css')
def css(theme: str) -> Tuple[Response, int, Dict[str, str]]:
    """Generates a CSS file from the given theme."""
    with open(THEMES) as f:
        themes = yaml.load(f, Loader=yaml.FullLoader)
    colors = themes[theme]
    res = render_template('style.css_t', rgba=rgba, **colors)
    return res, 200, {'Content-Type': 'text/css'}


@app.route('/runker/')
def subleerunker() -> str:
    """A frame wrapper of 'SUBLEERUNKER'."""
    url = 'https://sublee.github.io/subleerunker/'
    return render_template('runker.html', url=url)


@app.route('/robots.txt')
def robots_txt() -> Response:
    buf = io.StringIO()

    sitemap_url = url_for('sitemap_txt', _external=True)
    print('Sitemap: %s' % sitemap_url, file=buf)

    res = make_response(buf.getvalue())
    res.mimetype = 'text/plain'
    return res


@app.route('/sitemap.txt')
def sitemap_txt() -> Response:
    buf = io.StringIO()

    print(url_for('index', _external=True), file=buf)
    print(url_for('resume', _external=True), file=buf)

    res = make_response(buf.getvalue())
    res.mimetype = 'text/plain'
    return res


def render_error(error: Exception) -> str:
    """The HTTP error page."""
    ctx = make_context(error=error)
    return render_template('error.html', **ctx)


for status in itertools.chain(range(400, 420), range(500, 506)):
    def _error(error: Exception, status: int = status) -> Tuple[str, int]:
        return render_error(error), status

    try:
        app.errorhandler(status)(_error)
    except KeyError:
        # Ignore errors during registering an error handler.
        # KeyError occurs when handling status code 402.
        pass

    del _error


def prepare_freezing(app: Flask) -> Freezer:
    """Prepares to freeze the Flask application."""
    freezer = Freezer(app, with_static_files=False)

    app.config.update({
        'FREEZER_DESTINATION_IGNORE': ['.git*', 'CNAME'],
        'FREEZER_IGNORE_MIMETYPE_WARNINGS': True,
    })

    @app.route('/404.html')
    def not_found() -> str:
        return render_error(NotFound())

    @freezer.register_generator
    def doc() -> Iterator[Dict[str, str]]:
        for filename in glob(os.path.join(DOCS, '*.md')):
            filename = os.path.basename(filename)
            doc_name, __ = filename.rsplit(os.path.extsep, 1)
            yield {'doc_name': doc_name}

    @freezer.register_generator
    def css() -> Iterator[Dict[str, str]]:
        with open(THEMES) as f:
            themes = yaml.load(f, Loader=yaml.FullLoader)
        for theme in themes.keys():
            yield {'theme': theme}

    return freezer


# Command-line Interface


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--host', '-h', default='0.0.0.0')
@click.option('--port', '-p', type=click.IntRange(1, 65536), default=8080)
def run(host: str, port: int) -> None:
    """Run a web server for the website."""
    app.run(host=host, port=port, debug=True)


@cli.command()
@click.argument('dest', type=click.Path(file_okay=False, writable=True))
def freeze(dest: str) -> None:
    """Freeze the website as static files."""
    app.config['FREEZER_DESTINATION'] = dest
    freezer = prepare_freezing(app)
    freezer.freeze()


if __name__ == '__main__':
    cli()
