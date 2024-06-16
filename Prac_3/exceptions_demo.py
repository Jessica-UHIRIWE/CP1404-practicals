"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- A ValueError will occur if the input provided for either the numerator or the denominator cannot be converted to an integer.
2. When will a ZeroDivisionError occur?
- A ZeroDivisionError will occur if the user inputs 0 as the denominator, resulting in division by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, we can modify the code to handle the case where the denominator is 0 by adding a condition to check if the denominator is 0 before performing the division operation.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
