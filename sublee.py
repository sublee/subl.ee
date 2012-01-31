from collections import OrderedDict, defaultdict
import json
import os
import re
import shutil

import baker
import jinja2
from PIL import Image


def chain():
    def deco(f):
        import types
        if isinstance(f, types.FunctionType):
            deco.funcs.append(f)
            return f
        else:
            rv = []
            for g in deco.funcs:
                rv.append(g(f))
            return rv
    deco.funcs = []
    return deco


class Builder(object):

    def __init__(self, output, data):
        self.output = output
        self.data = data

    build_all = chain()

    @build_all
    def build_index(self):
        jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
        template = jinja_env.get_template('index.html')
        rendered = template.render(**self.data).encode('utf-8')
        with open(os.path.join(self.output, 'index.html'), 'w') as f:
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
    def build_icon(self, sharpness=0.25):
        ico = Image.open('favicon.ico')
        w, h = ico.size
        css = defaultdict(list)
        empty = (0, 0, 0)
        for x in xrange(w):
            for y in xrange(h):
                color = ico.getpixel((x, y))
                if color == empty:
                    continue
                selector = '.row-%d .col-%d' % (y, x)
                style = 'background: rgb%r;' % (color,)
                css[selector].append(style)
                sharp_size = (8, 8)
                for direction, xd, yd in [('top', 0, -1), ('right', 1, 0),
                                          ('bottom', 0, 1), ('left', -1, 0)]:
                    try:
                        sample = ico.getpixel((x + xd, y + yd))
                        if sample == empty:
                            raise IndexError
                    except IndexError:
                        sample = (255, 255, 255)
                    if sample == color:
                        continue
                    sharp = self.sharpen(color, sample, sharpness)
                    style = '''
                        border-{direction}-color: rgb{sharp!r};
                        border-{direction}-width: 1px;
                    '''.format(direction=direction, sharp=sharp)
                    css[selector + ' div'].append(style)
                    sharp_size = (sharp_size[0] - abs(xd),
                                  sharp_size[1] - abs(yd))
                if sharp_size != (8, 8):
                    style = 'width: %dpx; height: %dpx;' % sharp_size
                    css[selector + ' div'].append(style)
        with open(os.path.join(self.output, 'style.css'), 'a') as f:
            print>>f; print>>f, '/* favicon */'
            for selector, styles in css.iteritems():
                line = '%s { %s }' % (selector, ' '.join(styles))
                line = re.sub('\s+', ' ', line)
                print>>f, line,
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
    if all(builder.build_all()):
        print 'ok'
    else:
        print 'error'


if __name__ == '__main__':
    baker.run()
