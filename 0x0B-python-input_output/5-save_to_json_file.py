#!/usr/bin/python3
"""
Defines function that writes object to text file using JSON representation,
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved.
	filename (str): The name of the file to save the JSON representation,

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
