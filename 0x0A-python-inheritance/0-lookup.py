#!/usr/bin/python3


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
	"""
    
    return dir(obj)
