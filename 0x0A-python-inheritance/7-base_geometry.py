#!/usr/bin/python3
"""Defines a class BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """An empty class with area and integer_validator methods."""

    def area(self):
        """Raises an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
