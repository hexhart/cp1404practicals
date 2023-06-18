"""
CP1404/CP5632 - Practical 3 by Hexon Hartley Jimenez
Files program
"""

# Task 1 Program:
out_file = open('name.txt', 'w')
name = input("Enter name: ")
print(f"{name}", file=out_file)
out_file.close()

# Task 2 Program:
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# Task 3 Program:
number_file = open("numbers.txt", 'r')
first_number = int(number_file.readline())
second_number = int(number_file.readline())
number_file.close()
print(first_number + second_number)

# Task 4 Program:
number_file = open("numbers.txt", 'r')
sum_of_numbers = 0  # set an initial value
for line in number_file:
    numbers = int(line)  # read all the numbers in file
    sum_of_numbers += numbers
number_file.close()
print(sum_of_numbers)
