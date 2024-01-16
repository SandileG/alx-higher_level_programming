#!/usr/bin/python3
"""
Defines function that simplifies process of JSON string conversion.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
