
                        ##
                    ####  ##
                  ######  ####
                ##    ##  ######
              ####  ##  ########
              ######    ##########
              ##      ############
                ######    ########
              ######      ######  ##
              ######    ######  ####
            ##############    ######
            ############    ##    ##
            ############  ####    ##
            ############  ##########
              ############  ######
                  ##########

                  # subl.ee #
  
from collections import OrderedDict, defaultdict
import json
import os
import re
import shutil
import types

import baker
import jinja2
from PIL import Image


def chain():
    def deco(f):
        if isinstance(f, types.FunctionType):
            deco.funcs.append(f)
            return f
        else:
            def gen(self):
                for f in deco.funcs:
                    yield f, f(self)
            return gen(f)
    deco.funcs = []
    return deco


class Builder(object):

    def __init__(self, output, data):
        self.output = output
        self.data = data

    build_all = chain()

    @build_all
    def build_html(self):
        jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
        for filename in ['index.html', '404.html']:
            template = jinja_env.get_template(filename)
            rendered = template.render(**self.data).encode('utf-8')
            with open(os.path.join(self.output, filename), 'w') as f:
                f.write(rendered)
        return True

    @build_all
    def build_static(self, extensions=['css', 'ico', 'gif']):
        for filename in os.listdir('.'):
            if filename.split('.')[-1] not in extensions:
                continue
            try:
                shutil.copy2(filename, self.output)
            except IOError:
                pass
        return True

    @build_all
    def build_icon(self, sharpness=0.5):
        ico = Image.open('favicon.ico')
        w, h = ico.size
        css = defaultdict(list)
        black = (0, 0, 0)
        white = (255, 255, 255)
        def color_hex(color):
            limit = lambda x: max(0, min(255, x))
            return '#%02x%02x%02x' % tuple(map(limit, color))
        def sharp_style(direction, color, sample, sharpness):
            sharp = self.sharpen(color, sample, sharpness)
            form = '''border-{direction}-color: {color};
                      border-{direction}-width: 1px;'''
            return form.format(direction=direction, color=color_hex(sharp))
        for x, y in ((x, y) for x in xrange(w) for y in xrange(h)):
            color = ico.getpixel((x, y))
            if color == black:
                continue
            selector = '.c%dr%d' % (x, y)
            style = 'background: %s;' % color_hex(color)
            css[style].append(selector)
            # sharpen
            i_size = (8, 8)
            selector += ' i'
            for direction, xd, yd in [('top', 0, -1), ('right', 1, 0),
                                      ('bottom', 0, 1), ('left', -1, 0)]:
                try:
                    sample = ico.getpixel((x + xd, y + yd))
                    if sample == black:
                        raise IndexError
                except IndexError:
                    sample = white
                if sample == color:
                    continue
                style = sharp_style(direction, color, sample, sharpness)
                css[style].append(selector)
                if sample == white:
                    style = sharp_style(direction, color, black, sharpness)
                    css[style].append('.error ' + selector)
                i_size = (i_size[0] - abs(xd), i_size[1] - abs(yd))
            if i_size != (8, 8):
                style = 'width: %dpx; height: %dpx;' % i_size
                css[style].append(selector)
        css_path = os.path.join(self.output, 'style.css')
        with open(css_path, 'a') as f:
            for style, selectors in css.iteritems():
                f.write('%s { %s }' % (', '.join(selectors), style))
        # minify
        with open(css_path) as f:
            css = f.read()
        with open(css_path, 'w') as f:
            f.write(re.sub('\s*([{:;,}])\s*', '\\1', re.sub('\s+', ' ', css)))
        return True

    def sharpen(self, color, sample, sharpness):
        composite = map(lambda x: sum(x) / 2., zip(color, sample))
        diff = map(lambda x: x[0] - x[1], zip(composite, color))
        sharp = map(lambda x: x[0] - x[1] * sharpness, zip(color, diff))
        return tuple(map(int, sharp))


@baker.command
def build(output, data='data.json'):
    output = os.path.abspath(output)
    if not os.path.isdir(output):
        raise ValueError('%r is not a directory' % output)
    with open(data) as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    builder = Builder(output, data)
    for meth, success in builder.build_all():
        print meth.__name__, '...', 'ok' if success else 'error'


if __name__ == '__main__':
    baker.run()
