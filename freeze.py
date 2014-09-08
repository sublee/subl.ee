# -*- coding: utf-8 -*-
import os
import sys

from flask_frozen import Freezer
import yaml

from sublee import app, THEMES


@app.route('/404.html')
def not_found():
    client = app.test_client()
    response = client.get('/404')
    return response.data


app.config['FREEZER_DESTINATION'] = sys.argv[1]
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'runker', 'CNAME']
freezer = Freezer(app, with_static_files=False)


@freezer.register_generator
def css():
    with open(THEMES) as f:
        themes = yaml.load(f)
    for theme in themes.viewkeys():
        yield {'theme': theme}


if __name__ == '__main__':
    freezer.freeze()
