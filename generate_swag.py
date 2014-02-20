import sys
import os


def get_py_files(cwd):
    return [os.path.join(root, f)
            for root, dirs, files in os.walk(cwd)
            for f in files if f.endswith('.py')]


def is_flask_file(f):
    with open(f, 'r') as data:
        return '@app.route(' in data.read()


def filter_flask_files(files):
    return filter(is_flask_file, files)


def get_route_lines(files):
    lines = []
    for f in files:
        with open(f, 'r') as data:
            content = data.readlines()
            for line in content:
                if '@app.route(' in line:
                    lines.append(line)
                #if '@requires_auth' in line:
                    #lines[-1] = (lines[-1][0], lines[-1][1], True)
                #if "'''" in line or '"""' in line:
                    #lines[-1] = (lines[-1][0], line.strip(), lines[-1][2])
    return lines


def print_route_lines(files):
    for f in files:
        with open(f, 'r') as data:
            content = data.readlines()
            for line in content:
                if '@app.route(' in line:
                    print line


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print filter_flask_files(get_py_files(sys.argv[1]))
    else:
        print filter_flask_files(get_py_files(os.getcwd()))
