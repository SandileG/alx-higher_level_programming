#!/usr/bin/python3

def get_names_from_pyc(pyc_file):
    with open(pyc_file, 'rb') as f:
        code = types.CodeType(*list(f.read()))
        names = [name for name in code.co_names if not name,startswith("__")]
        return (names)

__name__ == "__main__":
pyc_file = "hidden_4.pyc"
names = get_names_from_pyc(pyc_file)
for name in sorted(names):
    print(name)
