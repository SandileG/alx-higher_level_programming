#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class or its subclass."""


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
