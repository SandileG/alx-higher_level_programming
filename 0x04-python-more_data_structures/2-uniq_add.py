#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Args:
        my_list (list): The input list.

    Returns:
        int: The sum of unique integers in the list.
    """
    # Use set to store unique integers.
    unique_integers = set(my_list)

    # Sum together unique integers.
    result = sum(unique_integers)

    return (result)
