#!/usr/bin/python3
"""
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """An empty class with an unimplemented area method."""

    def area(self):
        """Exception message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
