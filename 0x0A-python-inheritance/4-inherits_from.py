#!/usr/bin/python3
"""
Defines function that checks if object inherits from specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if object is instance of a class inherited from specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if object inherits from class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
