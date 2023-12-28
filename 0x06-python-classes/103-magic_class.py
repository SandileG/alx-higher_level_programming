#!/usr/bin/python3
"""
Module that defines a MagicClass.
"""
import


class MagicClass:
    """
    Represents a class with magical calculations.
    """

    def __init__(self, radius):
        """
        Initializes a new MagicClass instance.

        Args:
            radius: The radius for magical calculations.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radiuds must ne a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the magical area.

        Returns:
            The magical area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the magical circumference.

        Returns:
            The magical circumference.
        """
        return 2 * math.pi * self.__radius
