"""
CP1404/CP5632 - Practical 2
Updated Program that determines score status
By Hexon Hartley Jimenez
"""
import random


def main():
    score = float(input("Enter score: "))
    determine_score(score)

    random_score = random.randint(0, 100)
    print(f"Random Score: {random_score}")
    determine_score(random_score)


def determine_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
