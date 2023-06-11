"""
CP1404/CP5632 - Practical 2
Loops Program
By Hexon Hartley Jimenez
"""

# Odd numbers between 1 - 20 with space between each odd numbers
for i in range(1, 21, 2):
    print(i, end=' ')
print("")

# a. count in 10s from 0 to 100:
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b. countdown from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars:
star_count = int(input("Enter a number: "))
stars = "*" * star_count
print(f"Number of stars: {star_count}")
print(f"{stars}")

# d. print n lines of increasing stars:
for stars_per_line in range(1, star_count + 1):
    print("*" * stars_per_line)
