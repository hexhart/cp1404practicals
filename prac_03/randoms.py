"""
CP1404/CP5632 - Practical 3
Randoms program
By Hexon Hartley Jimenez
"""
import random

print(random.randint(5, 20))
# line 1 response 1: produced a random number between 5 and 20
# line 1 response 2: smallest generated was 5 and largest 20 upon several program executions

print(random.randrange(3, 10, 2))
# line 2 response 1: it generated a number 7 on first program execution and another random number under 10
# line 2 response 2: smallest number generated was 3 and largest 9
# line 2 response 3: No, the starting point is 3 and step is 2, so next number would be 3 + 2 = 5

print(random.uniform(2.5, 5.5))
# line 3 response 1: Get a random number in the range [2.5, 5.5) depending on rounding.
# line 3 response 2: smallest 2.628385338842072, largest 5.41350301343293


# To produce a random number between 1 and 100 inclusive
generate_number = random.randint(0, 100)  # randint is used to include both starting and end point
print(generate_number)
