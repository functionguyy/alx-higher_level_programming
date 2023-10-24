#!/usr/bin/python3
def list_division(my_list_1: list, my_list_2: list, list_length: int) -> list:
    """Function that divides element by element 2 lists

    Args:
        my_list_1: list object
        my_list_2: list object
        list_length: integer

    Description:
        if 2 elements can't be divided, the division result should be equal to
        0
        if an element is not an integer or float: print `wrong type`
        if the division can't be done: print `division by 0`
        if my_list_1 or my_list_2 is too short: print `out of range`
    Return:
        new list of length list_length with all divisions
    """
    new_list = list()
    result = 0
    for n in range(list_length):
        try:
            a = my_list_1[n]
            b = my_list_2[n]
            result = a / b
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            new_list.append(result)

    return new_list
