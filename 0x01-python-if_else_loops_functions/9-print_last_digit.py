#!/usr/bin/python3


def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit


# Example usage:
result = print_last_digit(98)
print(result)


result = print_last_digit(-98)
print(result)


result = print_last_digit(0)
print(result)
