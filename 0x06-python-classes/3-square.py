#!/usr/bin/python3
"""
Module that defines a square class.
"""


class Square:
    """
    Sqaure class with private instance attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.__size ** 2
