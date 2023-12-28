#!/usr/bin/python3
"""
Module that defines a MagicClass.
"""
import math


class MagicClass:
    """
    Represents a circle with a radius.
    """

    def __init__(self, radius=0):
        """
        Initializes the circle with the given radius.

        Args:
            radius: The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """

        self._radius = 0  # Initialize radius to 0

        # Check if radius is a valid number (int or float)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self._radius = radius  # Assign the radius value

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """

        return math.pi * self._radius ** 2

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """

        return 2 * math.pi * self._radius
