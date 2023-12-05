#!/usr/bin/python3


def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Unsupported operand type")
    return (a + b)


if __name__ == "__main__":
    pass
