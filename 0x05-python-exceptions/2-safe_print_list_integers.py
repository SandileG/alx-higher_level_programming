#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    """
    Prints the first x elements of a list, only integers.
    """
    printed_integers = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
        print()
    except (IndexError, ValueError, TypeError):
        print()

    return (printed_integers)
