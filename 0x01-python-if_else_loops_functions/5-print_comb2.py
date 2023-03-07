#!/usr/bin/python3
for i in range(0, 10):
    for n in range(0, 10):
        if i == 9 and n == 9:
            print("{:d}{:d}".format(i, n))
        else:
            print("{:d}{:d}".format(i, n), end=",")
