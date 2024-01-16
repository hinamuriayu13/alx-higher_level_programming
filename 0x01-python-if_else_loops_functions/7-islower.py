#!/usr/bin/python3

def islower(c):
    if len(c) != 1:
        return False

    ascii_value = ord(c)
    return 97 <= ascii_value <= 122


print("a is {}".format("lower" if islower("a") else "upper"))
