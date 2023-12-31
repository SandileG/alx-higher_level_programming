#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    """
    try:
        printed_elements = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            printed_elements += 1
        print()
        return (printed_elements)
    except IndexError:
        print()
        return (printed_elements)
