# -*- coding: utf-8 -*-
from flask_frozen import Freezer

from sublee import app


@app.route('/404.html')
def not_found():
    client = app.test_client()
    response = client.get('/404')
    return response.data


freezer = Freezer(app, with_static_files=False)


if __name__ == '__main__':
    freezer.freeze()
