#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to delete.

    Returns:
        dict: The updated dictionary.
    """
    # Check if key exists before attempting to delete.
    if key in a_dictionary:
        del a_dictionary[key]

    return (a_dictionary)
