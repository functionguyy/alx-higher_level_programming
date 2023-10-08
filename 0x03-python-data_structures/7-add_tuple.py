#!/usr/bin/python3
def create_matrix(tuple_of_tuples: tuple = ()) -> list:
    """Function creates a 2D list

    Args:
        tuple_of_tuples: tuple object

    Return:
        2D list object
    """
    list_of_lists = []
    for t in tuple_of_tuples:
        list_of_lists.append(list(t))
    return list_of_lists


def argument_matrix_element(list_of_lists: list = []) -> None:
    """Function that adjust the number of elements in each list inside the 2D
    list

    Args:
        list_of_lists: list object

    Return:
        None
    """
    for list_element in list_of_lists:
        col_num = len(list_element)
        if col_num < 2:
            for i in range(2 - col_num):
                list_element.append(0)
        if col_num > 2:
            del list_element[2:]


def add_tuple(tuple_a: tuple = (), tuple_b: tuple = ()) -> tuple:
    """Function that adds 2 tuples

    Args:
        tuple_a: first tuple object
        tuple_b: Second tuple object

    Return:
        tuple of the sum of elements in tuple_a and tuple_b
    """
    if type(tuple_a) is tuple and type(tuple_b) is tuple:
        tuple_pack = (tuple_a, tuple_b)
        list_of_lists = create_matrix(tuple_pack)
        argument_matrix_element(list_of_lists)
        sum_1 = 0
        sum_2 = 0
        for list_element in list_of_lists:
            a, b = list_element
            sum_1 = sum_1 + a
            sum_2 = sum_2 + b
    return (sum_1, sum_2)
