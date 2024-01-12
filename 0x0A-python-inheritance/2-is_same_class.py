#!/usr/bin/python3
"""
Defines function that checks if object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if object is instance of specified class, False otherwise.
    """
    return type(obj) is a_class
