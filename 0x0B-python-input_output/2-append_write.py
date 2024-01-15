#!/usr/bin/python3
"""
Defines function that appends string at end of text file.
"""


def append_write(filename="", text=""):
    """
    Appends string to end of UTF8 file, returns number of chars added.

    Args:
        filename (str): The name of the file to append to.
	text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """

    with open(filename, 'a', encoding='utf-8') as file:  # Open in append mode
        num_chars = file.write(text)  # Append text and get character count.
    return num_chars
