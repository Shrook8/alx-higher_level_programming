#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, end = ' ')
if (number > 0):
    print("The number is positive")
if (number == 0):
    print("The number is zero")
if (number < 0):
    print("The number is negative")
