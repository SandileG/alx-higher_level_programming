#!/usr/bin/python3

def add(a, b):
    try:
        result = int(a) + int(b)
        return result
    except ValueError:
        return None

if __name__ == "__main__":
    pass
