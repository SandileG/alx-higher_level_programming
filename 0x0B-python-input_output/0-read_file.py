#!/usr/bin/python3
"""
Defines a function that reads a text file (utf-8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads the contents of a UTF-8 text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')  # print without extra newline.
