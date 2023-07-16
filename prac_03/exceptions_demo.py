"""
CP1404/CP5632 - Practical 3 by Hexon Hartley Jimenez
Answer the following questions:
1. When will a ValueError occur?
Answer 1: ValueError occurs when a non-integer value (i.e. String) has been entered in numerator OR denominator

2. When will a ZeroDivisionError occur?
Answer 2:

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer 3: To avoid ZeroDivisionError, we must implement an If Else condition to capture invalid values
when 0 is entered in the denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # if else condition to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
