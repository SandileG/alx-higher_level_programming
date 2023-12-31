#!/usr/bin/python3
"""
Module that defines a square class.
"""


class Square:
    """
    Sqaure class with a private instance attribute size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
