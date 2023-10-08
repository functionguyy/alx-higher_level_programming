#!/usr/bin/python3
def print_matrix_integer(matrix: list = [[]]) -> int:
    """Function that prints a matrix of integers

    Args:
        matrix: 2-D list object
    Return:
        print matrix integers
    """
    if type(matrix) is list:
        for element in matrix:
            if len(element) > 0:
                matrix_element = element.copy()
                n = len(matrix_element) - 1
                for element in matrix_element:
                    if matrix_element.index(element) < n:
                        print("{:d}".format(element), end=" ")
                    else:
                        print("{:d}".format(element))
            else:
                print()  # if no argument is passed print new line
