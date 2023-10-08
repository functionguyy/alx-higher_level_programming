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
