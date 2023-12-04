"""
   sublee
   ~~~~~~

   https://subl.ee/

   :copyright: (c) 2013-2023 by Heungsub Lee
   :license: Public Domain

"""
import bisect
import io
from pathlib import Path
from datetime import date, datetime, timezone
import subprocess
import time
from typing import Any, Dict, List, Optional, Tuple, Union
import uuid
from xml.etree import ElementTree

import cairosvg
import click
import fitz  # Its package name is PyMuPDF.
import weasyprint
from flask import (Flask, Response, make_response, render_template,
                   render_template_string, request, send_file, url_for)
from flask_frozen import Freezer
from markdown import Markdown
from markupsafe import Markup
from PIL import Image
from werkzeug.exceptions import HTTPException, NotFound

__version__ = '3.1.0'
__all__ = ['app']


ROOT = Path(__file__).parent
AUTHOR = 'Heungsub Lee'
EMAIL = 'heungsub@subl.ee'
COPYRIGHT_YEAR_SINCE = 2012
GOOGLE_ANALYTICS = 'G-YY0SXHSEV5'
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
app.jinja_env.globals['dummy'] = str(uuid.uuid4())


def copyright_year(year_since: Optional[int] = None,
                   dash: str = '\u2013',
                   ) -> str:
    """Generates an auto-renewed year range of the copyright."""
    this_year = date.today().year
    if year_since is None or year_since == this_year:
        return str(this_year)
    return '{0}{1}{2}'.format(year_since, dash, this_year)


def make_context(**kwargs: Any) -> Dict[str, Any]:
    """Makes a template context with defaults."""
    if 'FREEZER_DESTINATION' in app.config:
        url_root = '%(PREFERRED_URL_SCHEME)s://%(SERVER_NAME)s' % app.config
    else:
        url_root = request.url_root.rstrip('/')

    context: Dict[str, Any] = {
        'author': AUTHOR,
        'email': EMAIL,
        'google_analytics': GOOGLE_ANALYTICS,
        'copyright_year': copyright_year(COPYRIGHT_YEAR_SINCE),
        'url_root': url_root,
        'url_path': request.path,
    }

    context.update(**kwargs)
    return context


def markdown(text: str) -> Tuple[str, Dict[str, str]]:
    """Renders a Markdown document."""
    markdown = Markdown(extensions=MARKDOWN_EXTENSIONS)
    html = markdown.convert(text)
    meta = {k: '\n'.join(v) for k, v in markdown.Meta.items()}
    return html, meta


def send_raster(svg_path: Path, height: Optional[int]) -> Response:
    """Sends a reheightd raster image in PNG from a SVG file."""
    with svg_path.open('r') as f:
        png = cairosvg.svg2png(file_obj=f, output_height=height)
    return Response(png, mimetype='image/png')


def render_icon(size: Union[int, Tuple[int, int]], radius: int = 0) -> str:
    """Renders :file:`artwork/icon.svg_t` with the given size and radius."""
    with (ROOT/'artwork'/'icon.svg_t').open('r') as f:
        svg_t = f.read()

    if isinstance(size, int):
        width = height = size
    else:
        width, height = size

    emblem = ElementTree.parse(ROOT/'artwork'/'emblem.svg')
    emblem_path_commands = emblem.find('/{*}path').get('d')

    context = {
        'width': width,
        'height': height,
        'radius': radius,
        'emblem_path_commands': emblem_path_commands,
    }
    return render_template_string(svg_t, **context)


def guess_mtime(path: Path) -> datetime:
    """Guesses the last updated time of the given file."""
    mtime = datetime.utcfromtimestamp(path.stat().st_mtime)

    def run(cmd: List[str]) -> str:
        r = subprocess.run(cmd, capture_output=True, text=True)
        return r.stdout.strip()

    try:
        run(['git'])
    except FileNotFoundError:
        # git command not available.
        return mtime

    if run(['git', 'diff', '--name-only', str(path)]):
        # The file has been modified from its last commit.
        return mtime

    git_time_str = run('git log -1 --pretty=%cI'.split() + [str(path)])
    git_time = datetime.fromisoformat(git_time_str).astimezone(timezone.utc)
    return git_time


def render_resume() -> Tuple[str, Dict[str, str], datetime]:
    with (ROOT/'resume.md').open(encoding='utf-8') as f:
        html, meta = markdown(f.read())
    updated = guess_mtime(ROOT/'resume.md')
    return html, meta, updated


@app.route('/')
def index() -> str:
    with (ROOT/'index.md').open(encoding='utf-8') as f:
        html, meta = markdown(f.read())
    ctx = make_context(html=html, **meta)
    return render_template('index.html', **ctx)


@app.route('/resume/')
def resume() -> str:
    html, meta, updated = render_resume()
    ctx = make_context(html=html, updated=updated, **meta)
    return render_template('resume.html', **ctx)


# Share the font config among multiple GET /resume.pdf requests for getting
# speed up.
wp_font_config = weasyprint.text.fonts.FontConfiguration()


@app.route('/resume.pdf')
def resume_pdf() -> Response:
    """Renders the resume as a PDF document.

    Querystring options:

        mode=debug  Render as HTML rather than PDF.
        mode=prod   Optimize line-height

    """
    resume, _, updated = render_resume()
    with (ROOT/'css'/'resume-pdf.css').open() as f:
        css = f.read()
    html = render_template('resume-pdf.html',
                           html=resume, css=css, updated=updated)

    # "mode=debug" querystring switches to render as HTML rather than PDF for
    # debugging directly in a web browser.
    if request.args.get('mode') == 'debug':
        return make_response(html)

    wp_html = weasyprint.HTML(string=html)

    def render_pdf(line_height: Optional[float]) -> weasyprint.Document:
        if line_height is None:
            ss = []
        else:
            ss = [weasyprint.CSS(string=f'body{{line-height:{line_height}}}')]

        return wp_html.render(stylesheets=ss, font_config=wp_font_config)

    def optimize_line_height() -> Optional[float]:
        # Maximize line-height unless 2 or more pages are rendered.
        line_heights = [x/1000 for x in range(1100, 1401)]
        expected_pages = 1

        started = time.monotonic()
        i = bisect.bisect_right(line_heights, expected_pages,
                                key=lambda h: len(render_pdf(h).pages))
        elapsed = time.monotonic() - started

        i = 0 if i == 0 else i-1
        line_height = line_heights[i]

        app.logger.info(f'Optimized line-height: {line_height} '
                        f'({elapsed:.2f} sec elapsed)')

        return line_height

    if request.args.get('mode') == 'prod':
        # "mode=prod" querystring enables the line-height optimization.
        line_height = optimize_line_height()
    elif 'FREEZER_DESTINATION' in app.config:
        # Always enable the optimization in the freezing mode.
        line_height = optimize_line_height()
    else:
        line_height = None

    doc = render_pdf(line_height)

    if 'FREEZER_DESTINATION' in app.config and len(doc.pages) != 1:
        raise AssertionError(f'resume.pdf has {len(doc.pages)} pages')

    pdf = io.BytesIO()
    doc.write_pdf(pdf)
    pdf.seek(0)

    res: Response = send_file(pdf, mimetype='application/pdf')
    return res


@app.route('/resume-social.png')
def resume_social() -> Response:
    # Use PyMuPDF (fitz) to rasterize resume.pdf
    pdf_res = resume_pdf()
    pdf_res.direct_passthrough = False

    pdf = fitz.open('pdf', pdf_res.data)
    first_page = pdf[0]

    pix = first_page.get_pixmap(dpi=300)

    # Crop 1200x630 on the top by PIL because it is easier
    img = Image.open(io.BytesIO(pix.tobytes()))
    assert img.width >= 1200
    img = img.resize((1200, int(1200/img.width*img.height)))
    img = img.crop((0, 0, 1200, 630))

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return Response(buf.getvalue(), mimetype='image/png')


@app.route('/style.css')
def style() -> Response:
    return send_file(ROOT/'css'/'style.css')


@app.route('/emblem.svg')
def emblem() -> Response:
    return send_file(ROOT/'artwork'/'emblem.svg')


@app.route('/emblem.png', defaults={'height': None})
@app.route('/emblem-<int:height>.png')
def emblem_raster(height: Optional[int]) -> Response:
    return send_raster(ROOT/'artwork'/'emblem.svg', height)


@app.route('/icon.svg')
def icon() -> Response:
    r = float(request.args.get('r', 0))
    svg = render_icon(226, r)
    return Response(svg, mimetype='image/svg+xml')


@app.route('/icon.png', defaults={'height': None})
@app.route('/icon-<int:height>.png')
def icon_raster(height: Optional[int]) -> Response:
    svg = icon().data.decode('utf-8')
    png = cairosvg.svg2png(file_obj=io.StringIO(svg), output_height=height)
    return Response(png, mimetype='image/png')


@app.route('/social.svg')
def social() -> Response:
    svg = render_icon((600, 315))
    return Response(svg, mimetype='image/svg+xml')


@app.route('/social.png')
def social_raster() -> Response:
    svg = social().data.decode('utf-8')
    png = cairosvg.svg2png(file_obj=io.StringIO(svg), output_height=630)
    return Response(png, mimetype='image/png')


@app.route('/favicon.svg')
def favicon() -> Response:
    svg = render_icon(226, 41)
    return Response(svg, mimetype='image/svg+xml')


@app.route('/favicon.ico')
def favicon_raster() -> Response:
    svg = favicon().data.decode('utf-8')
    png = cairosvg.svg2png(file_obj=io.StringIO(svg), output_height=256)
    img = Image.open(io.BytesIO(png))

    buf = io.BytesIO()
    img.save(buf, format='ICO')
    return Response(buf.getvalue(), mimetype='image/x-icon')


@app.route('/manifest.webmanifest')
def manifest() -> Response:
    manifest = render_template('manifest.webmanifest')
    return Response(manifest, mimetype='application/manifest+json')


@app.route('/runker/')
def subleerunker() -> str:
    """A frame wrapper of 'SUBLEERUNKER'."""
    url = 'https://sublee.github.io/subleerunker/'
    return render_template('runker.html', url=url)


@app.route('/robots.txt')
def robots() -> Response:
    buf = io.StringIO()

    sitemap_url = url_for('sitemap', _external=True)
    print('Sitemap: %s' % sitemap_url, file=buf)

    res: Response = make_response(buf.getvalue())
    res.mimetype = 'text/plain'
    return res


@app.route('/sitemap.txt')
def sitemap() -> Response:
    buf = io.StringIO()

    print(url_for('index', _external=True), file=buf)
    print(url_for('resume', _external=True), file=buf)

    res: Response = make_response(buf.getvalue())
    res.mimetype = 'text/plain'
    return res


@app.errorhandler(HTTPException)
def render_error(error: HTTPException) -> Tuple[str, int]:
    """The HTTP error page."""
    ctx = make_context(error=error)

    if error.code is None:
        status_code = 500
    else:
        status_code = error.code

    return render_template('error.html', **ctx), status_code


def prepare_freezing(app: Flask) -> Freezer:
    """Prepares to freeze the Flask application."""
    freezer = Freezer(app, with_static_files=False)

    app.config.update({
        'FREEZER_DESTINATION_IGNORE': ['.git*'],
        'FREEZER_IGNORE_MIMETYPE_WARNINGS': True,
    })

    @app.route('/404.html')
    def not_found() -> str:
        page, _ = render_error(NotFound())
        return page

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
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['SERVER_NAME'] = 'subl.ee'

    # Freeze the website.
    app.config['FREEZER_DESTINATION'] = dest
    freezer = prepare_freezing(app)
    freezer.freeze()


if __name__ == '__main__':
    cli()
