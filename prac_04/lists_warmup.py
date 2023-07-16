"""
CP1404/CP5632 - Practical 4 By Hexon Hartley Jimenez
List Warmup Program
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# What values do the following expressions have?
# Answer Response:
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 6, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Task 1: Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(f"First element updated: {numbers}")

# Task 2: Change the last element of numbers to 1
numbers[-1] = 1
print(f"Last element updated: {numbers}")

# Task 3: Print all the elements from numbers except the first two (slice)
# Answer: numbers[2:]
print(f"Excluding first two elements: {numbers[2:]}")

# Task 4: Print whether 9 is an element of numbers
# Answer: 9 in numbers
