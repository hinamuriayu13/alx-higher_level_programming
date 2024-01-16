def islower(c):
    return ord('a') <= ord(c) <= ord('z')

# Test cases with different characters
print("x is {}".format("lower" if islower("x") else "upper"))
print("Q is {}".format("lower" if islower("Q") else "upper"))
print("Z is {}".format("lower" if islower("Z") else "upper"))
print("7 is {}".format("lower" if islower("7") else "upper"))
print("f is {}".format("lower" if islower("f") else "upper"))
