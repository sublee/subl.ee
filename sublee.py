from collections import OrderedDict
import json
import os
import re
import shutil

import baker
import jinja2


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
