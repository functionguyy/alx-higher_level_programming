#!/usr/bin/python3
for n in range(0, 9):
    for i in range(1, 10):
        if n > i or n == i:
            continue
        elif n == 8 and i == 9:
            print("{:d}{:d}".format(n, i))
        else:
            print("{:d}{:d}".format(n, i), end=", ")
