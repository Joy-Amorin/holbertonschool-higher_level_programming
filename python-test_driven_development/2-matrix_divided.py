#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """function to divided elements"""

    list_matrix = list(map(list, matrix))

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if i + 1 < len(matrix):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix \
must have the same size")

        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix \
list of lists) of integers/floats")

            list_matrix[i][j] = round(list_matrix[i][j] / div, 2)
    """'round' function for rounding decimal numbers """

    return (list_matrix)
