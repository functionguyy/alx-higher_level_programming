#!/usr/bin/python3
"""Modules defines function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle
    of n

    args:
        n: integer
    """
    t = []
    if n > 0:
        for i in range(n):
            elem = []
            if len(t) > 0:
                last_list = t[-1]
                last_seen_num = 0
                for num in last_list:
                    elem.append(last_seen_num + num)
                    last_seen_num = num
            elem.append(1)
            t.append(elem)
    return t
