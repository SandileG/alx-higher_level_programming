#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        srt or None: The key with the biggest integer value,
        or none if no score is found.
    """

    if a_dictionary:
        # Find key with maximum value.
        best_key = max(a_dictionary, key=a_dictionary.get)
        return (best_key)
    else:
        return (None)
