#!/usr/bin/python3


def pow(a, b):
    result = 1
    for _ in range(abs(b)):
        result *= a


    if b < 0:
        result = 1 / result


    return (result)


# Test cases
print(pow(2. 3))
print(pow(98, 2))
print(pow(98, 0))
print(pow(1400, -2))
print(pow(-4, 5))
