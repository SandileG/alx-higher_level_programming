#!/usr/bin/python3
"""
Defines a rebel MyInt class that inherits from int.
"""


class MyInt(int):
    """
    A rebel integer class with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equalityy operator.
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator.
        """

        return super().__eq__(other)
