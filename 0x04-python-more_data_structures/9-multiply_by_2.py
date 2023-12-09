#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Retruns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        dict: A new dicitionary with values multiplied by 2.
    """
    # Create new dictionary with values multiplied by 2.
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}

    return (new_dict)
