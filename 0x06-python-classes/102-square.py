#!/usr/bin/python3
"""
Module that defines a Square class
"""


class Square:
    """Represents a square with a size."""
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value: The size to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparator based on the square area.

        Args:
            other: The other Square instance to compare.

        Returns:
            True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparator based on the square area.

        Args:
            other: The other Square instance to compare.

        Returns:
            True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparator based on the square area.

        Args:
            other: The other Square instance to compare.

        Returns:
            True if area is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparator based on the square area.

        Args:
            other: The other Square instance to compare.

        Returns:
            True if area is less than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparator based on the square area.

        Args:
            other: The other Square instance to compare.

        Returns:
            True if area is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparator based on the square area.

        Args:
            other: The other Square instance to compare.

        Returns:
            True: area is greater than or equal to other. False: otherwise.
        """
        return self.area() >= other.area()
