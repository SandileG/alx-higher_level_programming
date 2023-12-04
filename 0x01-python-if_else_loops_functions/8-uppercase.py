#!/usr/bin/python3


def uppercase(s):
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            print("{:c}".format(ascii_value - 32), end="")
        else:
            print("{:c}".format(ascii_value), end="")
