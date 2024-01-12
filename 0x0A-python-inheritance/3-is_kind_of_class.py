#!/usr/bin/python3
"""Defines function that checks if object is instance of class."""


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance of a class inherited from specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if object is instance of class, False otherwise.
    """
    return isinstance(obj, a_class)
