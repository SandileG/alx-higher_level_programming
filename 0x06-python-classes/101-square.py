#!/usr/bin/python3
"""
Module that defines a Square class.
"""


class Square:
    """
    Square class definition
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance

        Args:
            size: The size of the square (default is 0).
            position: The position of the square (default is (0, 0)).
        """
        self.size = size
        self.__position = position

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
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Setter method for position attribution.

        Args:
            value: The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positiv integers.
        """

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#'.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """
        String representation of the square.
        """
        result = ""
        if self.__size == 0:
            return result

        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result.rstrip()
