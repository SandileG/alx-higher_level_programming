#!/usr/bin/python3
"""
Defines function that writes string to text file and returns number of character.
"""


def write_file(filename="", text=""):
    """
    Writes a string to text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)  # Write text and get character count.
    return num_chars
