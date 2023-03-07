#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1

if number < 0:
    sign *= -1

last_digit = (number % 10) * sign
first_str = "Last digit of {0:d} is {1:d} and is greater than {2:d}"
second_str = "Last digit of {0:d} is {1:d} and is less than {2:d} and not {3:d}"
if last_digit > 5:
    print(first_str.format(number, last_digit, 5))
elif last_digit < 6 and last_digit != 0:
    print(second_str.format(number, last_digit, 6, 0))
else:
    print("Last digit of {:d} is {:d}".format(number, last_digit))
