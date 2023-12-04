#!/usr/bin/python3


def uppercase(s):
    result = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            result += "{:c}".format(ascii_value - 32)
        else:
            result += "{:c}".format(ascii_value)
    print(result)  # Print the final result after the string is processed
