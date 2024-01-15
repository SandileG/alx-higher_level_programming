#!/usr/bin/python3
"""
Module containing the Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """

        super().__init__(size, size)

    def __str__(self):
        """
        Returns:
            str: The string representation of the square.
        """
        return ("[Square] "
                f"{self._Rectangle__width}/{self._Rectangle__height}")

    def integer_validation(self, name, value):
        """
        Validates the input value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
           TypeError: If the value is not an integer.
           ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
