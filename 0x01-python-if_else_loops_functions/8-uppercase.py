#!/usr/bin/python3
def uppercase(str):
    n = ""
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            u = (ord(letter) - ord('a')) + ord('A')
            n += chr(u)
        else:
            n += letter
    print("{:s}".format(n))
