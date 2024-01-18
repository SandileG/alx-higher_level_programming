#!/usr/bin/python3
"""
Defines a class that returns a dictionary description with data structure.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary description for JSON serialization.
    """

    # Get the dictionary representation of the object's attribues
    obj_dict = obj.__dict__.copy()

    # Convert non-serializable attributes to serializable formats
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            continue
        elif hasattr(value, '__dict__'):
            obj_dict[key] = value.__dict__.copy()
        else:
            obj_dict[key] = str(value)

    return obj_dict
