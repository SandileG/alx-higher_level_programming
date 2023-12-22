#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely/

    :param fct: The function to be executed.
    :param args: Arguments to be passed to the function.
    :return: Result of the function or None if an exception occurs.
    """

    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return (None)
