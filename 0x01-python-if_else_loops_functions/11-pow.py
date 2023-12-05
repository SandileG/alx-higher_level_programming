#!/usr/bin/python3


def pow(a, b):
    result = a ** b

    if b < 0:
        result = 1 / result

    return result


# Test cases
print(pow(2, 2))
print(pow(-2, 2))
print(pow(10, -2))
print(pow(-98, -10))
