"""
CP1404/CP5632 Practical By Hexon Hartley Jimenez
"Quick Pick" Lottery Ticket Generator program
"""
import random

MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1
NUMBERS_PER_LINE = 6


def main():
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            if number_of_quick_picks < 0:
                print("Input error! Enter an integer")
            else:
                is_valid_input = True

            for i in range(number_of_quick_picks):
                quick_pick = []
                for j in range(NUMBERS_PER_LINE):
                    number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
                    while number in quick_pick:
                        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
                    quick_pick.append(number)
                quick_pick.sort()

                print(" ".join(f"{number:2}" for number in quick_pick))

        except ValueError:
            print("Invalid input (must be an integer)")


main()
