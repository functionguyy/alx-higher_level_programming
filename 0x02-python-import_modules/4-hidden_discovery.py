#!/usr/bin/python3
import hidden_4


def my_function():
    names = dir(hidden_4)
    for name in names:
        if name.startswith("__"):
            continue
        print("{:s}".format(name))


if __name__ == '__main__':
    my_function()
