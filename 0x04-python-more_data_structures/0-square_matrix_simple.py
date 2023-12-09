#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list): 2-dimensional array.

    Returns:
        list: New matrix with squared values.
    """
    # Create new matrix with same size as input matrix.
    new_matrix = [[0 for _ in range(len(row))]for row in matrix]

    # Iterate through input elements of matrix and square each value.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return (new_matrix)
