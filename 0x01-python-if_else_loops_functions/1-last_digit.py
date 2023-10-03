#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1

if number < 0:
    sign *= -1

last_digit = (abs(number) % 10) * sign
first_str = "Last digit of {:d} is {:d} and is greater than {:d}"
second_str = "Last digit of {:d} is {:d} and is less than {:d} and not {:d}"
third_str = "Last digit of {:d} is {:d} and is {:d}"
if last_digit > 5:
    print(first_str.format(number, last_digit, 5))
elif last_digit < 6 and last_digit != 0:
    print(second_str.format(number, last_digit, 6, 0))
else:
    print(third_str.format(number, last_digit, 0))
