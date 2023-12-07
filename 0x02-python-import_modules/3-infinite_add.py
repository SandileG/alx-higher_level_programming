#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]

    # Ensure the existence of arguments before attempting addition.
    if args:
        result = sum(map(int, args))
        print(result)
    else:
        print(0)
