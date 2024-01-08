#!/usr/bin/python3
"""
Module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
    - matrix (list of lists): Matrix to be divided.
    - div (int or float): Number by which to divide the matrix.

    Returns:
    - list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
    - TypeError:
        If matrix is not a list of lists of integers or floats,
        if each row of the matrix does not have the same size,
        or if div is not a number.
    - ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places.
    result_matrix = [
        [round(element / div, 2) for element in row] for row in matrix
    ]

    return result_matrix
