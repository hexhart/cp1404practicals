"""
CP1404/CP5632 - Practical 2
Updated Program that determines score status
By Hexon Hartley Jimenez
"""
import random


def main():
    score = float(input("Enter score: "))
    print(determine_score_status(score))

    random_score = random.randint(0, 100)
    print(f"Random Score: {random_score}")
    print(f"Random Score Status:{determine_score_status(random_score)}")


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
