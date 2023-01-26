#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for k in range(len(matrix)):
        for j in range(len(matrix[k])):
            print("{:d}".format(matrix[k][j]), end="")
            if j < len(matrix[k]) - 1:
                print(" ", end="")
        print()
