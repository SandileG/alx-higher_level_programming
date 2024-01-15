#!/usr/bin/python3
"""
Defines a function that adds a new attribute to an object.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
