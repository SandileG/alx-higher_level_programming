#!/usr/bin/python3
"""
Defines a function that reads a text file (utf-8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content)