import random as rn


def area_calculator():
    length = int(input("Enter the length:"))
    width = rn.randint(1, length)
    print(" This is the width:", width)
    print(" area is:", length * width)

