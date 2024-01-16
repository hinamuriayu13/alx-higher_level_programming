#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Check the last digit of the number
last_digit = abs(number) % 10

# Check if the number is positive, negative, or zero
if last_digit > 5:
    print(
        "Last digit of", number,
        "is", last_digit, "and is greater than 5"
    )
    if number < 0:
        print(number, "is negative")
    elif number > 0:
        print(number, "is positive")
    else:
        print(number, "is zero")
elif last_digit < 6 and last_digit != 0:
    print(
        "Last digit of", number,
        "is", last_digit, "and is less than 6 and not 0"
    )
    if number < 0:
        print(number, "is negative")
    elif number > 0:
        print(number, "is positive")
    else:
        print(number, "is zero")
else:
    print(
        "Last digit of", number,
        "is", last_digit, "and is 0"
    )
    print(number, "is zero")
