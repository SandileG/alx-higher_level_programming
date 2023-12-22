#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer and returns True if successful, else returns False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return (False)
