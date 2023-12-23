#!/usr/bin/python3
"""
Module that defines a square class.
"""


class Square:
    """
    Square class with private instance attribute size.
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

    @property
    def size(self):
        """
        Getter method for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Compute and returns the area of the square
        """
        return self.__size ** 2
