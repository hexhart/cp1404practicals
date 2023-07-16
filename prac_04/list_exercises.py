"""
CP1404/CP5632 - Practical 4 By Hexon Hartley Jimenez
List Exercises program
"""

# Task 1: Basic List operations
numbers = []
for i in range(5):
    new_number = int(input("Number: "))
    numbers.append(new_number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the number is", sum(numbers) / len(numbers))

# Task 2: Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
