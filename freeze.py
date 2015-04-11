# -*- coding: utf-8 -*-
from glob import glob
import os
import sys

from flask_frozen import Freezer
import yaml

from sublee import app, DOCS, THEMES


app.config['FREEZER_DESTINATION'] = sys.argv[1]
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME']
freezer = Freezer(app, with_static_files=False)


@app.route('/404.html')
def not_found():
    client = app.test_client()
    response = client.get('/404/')
    return response.data


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


if __name__ == '__main__':
    freezer.freeze()
