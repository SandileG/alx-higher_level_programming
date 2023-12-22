#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    """
    Divides two integers and prints the result.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
	return (result)
