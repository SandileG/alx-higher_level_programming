#!/usr/bin/python3
import random


def get_last_digit(number):
    if number < 0:
        return number % -10
    elif number >= 0:
        return number % 10


def print_last_digit_message(number):
    last_digit = get_last_digit(number)

    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    else:
        print(
            f"Last digit of {number} is {last_digit} "
            f"and is less than 6 and not 0"
        )


# Example usage
number = random.randint(-10000, 10000)
print_last_digit_message(number)
