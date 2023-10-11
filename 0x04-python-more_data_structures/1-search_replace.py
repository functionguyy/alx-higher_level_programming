#!/usr/bin/python3
def search_replace(my_list: list, search, replace) -> list:
    """Function that replaces all occurences of an element by another in a new
    list

    Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element
    Return:
        new list with replace element

    """

    new_list = []
    for list_element in my_list:
        if list_element == search:
            new_list.append(replace)
        else:
            new_list.append(list_element)
    return new_list
