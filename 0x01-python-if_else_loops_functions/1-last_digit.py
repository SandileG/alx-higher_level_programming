#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)


def last_digit(number):
    try:
        last_digit = number % 10
    except TypeError:
        print("Last digit of", number, "is not an integer")
        return

    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    else:
        print(f"Last digit of {number} is {last_digit} and is less than 6 and is not 0")


# Call the last_digit function with the random number
last_digit(number)
