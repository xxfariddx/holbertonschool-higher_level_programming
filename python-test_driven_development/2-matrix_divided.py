#!/usr/bin/python3
"""
This module provides a function matrix_divided(matrix, div) that
divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Must contain integers or floats.
        div (int, float): The number to divide by.

    Returns:
        list: A new matrix representing the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_len = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    return [[round(item / div, 2) for item in row] for row in matrix]
