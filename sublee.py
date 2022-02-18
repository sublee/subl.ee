"""
   sublee
   ~~~~~~

   https://subl.ee/

   :copyright: (c) 2013-2019 by Heungsub Lee
   :license: Public Domain

"""
import base64
import glob
import io
import itertools
import mimetypes
import os
import re
from datetime import date
from typing import Any, Dict, Iterator, Optional, Tuple, Union
from urllib.parse import urlparse

import click
import jinja2
import markupsafe
import weasyprint
import yaml
from flask import (Flask, Response, make_response, render_template,
                   render_template_string, send_file, url_for)
from flask_frozen import Freezer
from markdown import Markdown
from werkzeug.exceptions import NotFound

__version__ = '2.5.0'
__all__ = ['app']


ROOT = os.path.dirname(__file__)
DOCS = os.path.join(ROOT, 'docs')
META = os.path.join(ROOT, 'meta.yml')
THEMES = os.path.join(ROOT, 'themes/*.yml')


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
app = Flask(__name__, static_folder=None)


def jinja_meta(content: str, **attrs: str) -> markupsafe.Markup:
    """A Jinja function generating <meta> element."""
    buf = io.StringIO()
    buf.write('<meta ')

    for key, attr in attrs.items():
        key = key.replace('_', '-')
        attr = markupsafe.escape(attr)
        buf.write('{key}="{attr}" '.format(key=key, attr=attr))

    content = markupsafe.escape(content)
    buf.write('content="{content}" />'.format(content=content))

    return markupsafe.Markup(buf.getvalue())


def jinja_rgba(color: str, alpha: float = 1.0) -> str:
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


def jinja_cdnjs(path: str) -> str:
    """A Jinja function generating a URL at cdnjs."""
    return 'https://cdnjs.cloudflare.com/ajax/libs/%s' % path


def jinja_update(d1: Dict[Any, Any],
                 d2: Union[Dict[Any, Any], jinja2.Undefined],
                 ) -> Dict[Any, Any]:
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
    'rgba': jinja_rgba,
    'cdnjs': (lambda path: '//cdnjs.cloudflare.com/ajax/libs/' + path),
})
app.jinja_env.filters.update({
    'update': jinja_update,
})
app.jinja_env.tests.update({
    'splitted_trigram_bar': jinja_splitted_trigram_bar,
})


def load_themes() -> Dict[str, Dict[str, str]]:
    """Parses theme YAML files into a single dictionary."""
    themes: Dict[str, Dict[str, str]] = {}
    for path in glob.glob(THEMES):
        with open(path) as f:
            themes.update(yaml.load(f, Loader=yaml.FullLoader))
    return themes


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

    context: Dict[str, Any] = {}
    context['copyright_year'] = meta['copyright_year_since']
    context['themes'] = load_themes()
    context.update(meta)
    context.update(*args, **kwargs)

    return context


def markdown(text: str) -> Tuple[str, Dict[str, str]]:
    """Renders a Markdown document."""
    markdown = Markdown(extensions=MARKDOWN_EXTENSIONS)
    html = markdown.convert(text)
    meta = {k: '\n'.join(v) for k, v in markdown.Meta.items()}
    return html, meta


def data_uri(path: str) -> str:
    """Encodes a file as a data URI."""
    mimetype, charset = mimetypes.guess_type(path, strict=False)
    if mimetype is None:
        mimetype = 'application/octet-stream'
    if charset is None:
        mediatype = mimetype
    else:
        mediatype = f'{mimetype};charset={charset}'

    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode()

    return f'data:{mediatype};base64,{data}'


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
    with open(os.path.join(ROOT, 'css', 'print.css')) as f:
        css = weasyprint.CSS(string=f.read(), font_config=font_config)

    doc = html.render(stylesheets=[css], font_config=font_config)

    if 'FREEZER_DESTINATION' in app.config:
        if len(doc.pages) != 1:
            raise AssertionError(f'resume.pdf contains {len(doc.pages)} pages')

    pdf = io.BytesIO()
    doc.write_pdf(pdf)
    pdf.seek(0)

    res: Response = send_file(pdf, mimetype='application/pdf')
    return res


@app.route('/themes/')
def themes() -> str:
    """Theme selector."""
    ctx = make_context(themes=load_themes())
    return render_template('themes.html', **ctx)


@app.route('/favicon.ico')
def favicon() -> Response:
    res: Response = send_file(os.path.join(ROOT, 'favicon.ico'))
    return res


@app.route('/og.png')
def og() -> Response:
    res: Response = send_file(os.path.join(ROOT, 'og.png'))
    return res


@app.route('/theme:<theme>.css')
def theme_css(theme: str) -> Tuple[str, int, Dict[str, str]]:
    """Generates a CSS file from the given theme."""
    themes = load_themes()
    style = themes[theme]

    with io.StringIO() as buf:
        buf.write(render_template('theme.css_t', theme=theme, **style))

        def _data_uri(path: str) -> str:
            return data_uri(os.path.join(ROOT, 'themes', theme, path))

        if 'css' in style:
            buf.write(render_template_string(style['css'], data_uri=_data_uri))
        if 'css_file' in style:
            with open(os.path.join(ROOT, 'themes', style['css_file'])) as f:
                buf.write(render_template_string(f.read(), data_uri=_data_uri))

        try:
            dark_style = themes[theme + ':dark']
        except KeyError:
            pass
        else:
            buf.write('@media (prefers-color-scheme: dark) {')
            buf.write(render_template('theme.css_t', **dark_style))
            buf.write('}')

        buf.write('''
        [data-detect-theme="%s"]::before {
            content: "ready";
        }
        ''' % theme)

        css = buf.getvalue()

    return css, 200, {'Content-Type': 'text/css'}


@app.route('/base.css')
def base_css() -> Response:
    res: Response = send_file(os.path.join(ROOT, 'css', 'base.css'))
    return res


@app.route('/print.css')
def print_css() -> Response:
    res: Response = send_file(os.path.join(ROOT, 'css', 'print.css'))
    return res


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

    res: Response = make_response(buf.getvalue())
    res.mimetype = 'text/plain'
    return res


@app.route('/sitemap.txt')
def sitemap_txt() -> Response:
    buf = io.StringIO()

    print(url_for('index', _external=True), file=buf)
    print(url_for('resume', _external=True), file=buf)

    res: Response = make_response(buf.getvalue())
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
    def theme_css() -> Iterator[Dict[str, str]]:
        for theme in load_themes().keys():
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
    # Config URL scheme and server name.
    with open(META) as f:
        meta = yaml.load(f, Loader=yaml.FullLoader)
    url_root = urlparse(meta['url_root'])
    app.config['PREFERRED_URL_SCHEME'] = url_root.scheme
    app.config['SERVER_NAME'] = url_root.hostname

    # Freeze the website.
    app.config['FREEZER_DESTINATION'] = dest
    freezer = prepare_freezing(app)
    freezer.freeze()


if __name__ == '__main__':
    cli()
