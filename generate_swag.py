import sys
import os
import json
from pprint import pprint


def get_py_files(cwd):
    return [os.path.join(root, f)
            for root, dirs, files in os.walk(cwd)
            for f in files if f.endswith('.py')]


def is_flask_file(f):
    with open(f, 'r') as data:
        return '@app.route(' in data.read()


def filter_flask_files(files):
    return filter(is_flask_file, files)


def clean(s):
    s = s.strip()
    s = s.replace('@app.route(','')
    s = s.replace(')','')
    return s


def get_routes(f):
    with open(f, 'r') as data:
        content = data.readlines()
    return [clean(x) for x in content if '@app.route(' in x or "'''" in x]


def map_route_lines(files):
    return map(get_routes, files)


def get_json_routes(routes):
    obj = {}
    for group in routes:
        for line in group:
            if 'methods=[' in line:
                sides = line.split(', methods=')
                sides[0] = sides[0].replace("'",'')
                sides[1] = sides[1].replace("'",'')
                sides[1] = sides[1].replace("]",'')
                sides[1] = sides[1].replace("[",'')
                obj[sides[0]] = sides[1]
    return obj


def generate_json(content):
    blob = {'version': '0.2',
            'endpoints': []}


if __name__ == '__main__':
    pprint(map_route_lines(filter_flask_files(get_py_files(sys.argv[1]
                                                           if len(sys.argv) >= 2
                                                           else os.getcwd()))))
