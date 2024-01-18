#!/usr/bin/python3
"""
Script to add command-line arguments to a Python list and save it to a JSON file.

Usage:
    ./7-add_item.py [arg1] [arg2] ...

Arguments:
    [arg1], [arg2], ... : Command-line arguments to be added to the list.

File:
    add_item.json : JSON file to store the list.

Dependencies:
    5-save_to_json_file.py : Function to save a Python object to a JSON file.
    6-load_from_json_file.py : Function to load a Python object from a JSON file.
"""

import sys

if __name__ == "__main__":
    # Dynamic imports using __import__
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # Filename for saving and loading the list
    filename = "add_item.json"

    # Load existing list from file, create empty list if file doesn't exist
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, filename)
