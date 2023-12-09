#!/usr/bin/pyhton3


def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: A set containing elements present in only one set.
    """
    only_diff_set = set_1.symmetric_difference(set_2)

    return (only_diff_set)
