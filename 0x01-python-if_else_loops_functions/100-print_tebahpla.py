#!/usr/bin/python3

for i in range(122, 96, -1):
    upperCase = (ord(chr(i)) - ord('a') + ord('A'))
    lowerCase = ord(chr(i))
    print("{:s}".format(chr(upperCase) if ord(chr(i)) % 2 != 0 else
          chr(lowerCase)), end="")
