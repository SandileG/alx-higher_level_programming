#!/usr/bin/python3

import dis
import marshal
import types

def get_names_from_pyc(pyc_file):
    with open(pyc_file, 'rb') as f:
        magic = f.read(4)
        timestamp = f.read(4)
        code_object = marshal.load(f)

        names = [name for name in code_object.co_names if not name.startswith('__')]
        return names

if __name__ == "__main__":
    pyc_file = "hidden_4.pyc"
    names = get_names_from_pyc(pyc_file)
    for name in sorted(names):
        print(name)
