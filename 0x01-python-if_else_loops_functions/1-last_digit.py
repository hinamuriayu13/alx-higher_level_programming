#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Check the last digit of the number
last_digit = abs(number) % 10
last_digit_with_sign = -last_digit if number < 0 else last_digit

# Check if the number is positive, negative, or zero
print("Last digit of", number, "is", last_digit_with_sign, end=" ")

if last_digit_with_sign > 5:
    print("and is greater than 5")
elif last_digit_with_sign < 6 and last_digit_with_sign != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
