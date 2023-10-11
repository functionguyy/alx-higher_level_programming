#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keysToDeleteList = []

    if type(a_dictionary) is dict:
        for k, v in a_dictionary.items():
            if v == value:
                keysToDeleteList.append(k)

        for k in keysToDeleteList:
            del a_dictionary[k]

    return a_dictionary
