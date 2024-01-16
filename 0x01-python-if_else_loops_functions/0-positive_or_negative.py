#!/usr/bin/python3
import random

number = random.randint(-10,10)

#let's check if the number is positive negative or a zero 

if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
