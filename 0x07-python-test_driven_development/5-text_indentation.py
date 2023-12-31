#!/usr/bin/python3
"""
Module for indenting text.
"""


def text_indentation(text):
    """
    Print text with two lines after each .?:

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = 0
    while t < len(text) and text[t] == ' ':
        t += 1

    while t < len(text):
        print(text[t], end="")
        if text[t] == "\n" or text[t] in ".?:":
            if text[t] in ".?:":
                print("\n")
            t += 1
            while t < len(text) and text[t] == ' ':
                t += 1
            continue
        t += 1
