#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

if last_digit > 0:
    print("Last digit of", number, "is", last_digit, "and is not 0")
    if number < 0:
        print(number, "is negative")
    else:
        print(number, "is positive")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
    print(number, "is zero")
