#!/usr/bin/python3
def square_matrix_simple(matrix: list = []) -> list:
    """Function that computes the square value of all integers of a matrix

    Args:
        matrix: 2D array


    Return:
        2D array squared values
    """
    new_matrix = [[row[i]**2 for i in range(len(row))] for row in matrix]
    return new_matrix
