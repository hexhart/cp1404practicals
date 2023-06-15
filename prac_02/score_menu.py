"""
CP1404/CP5632 - Practical 2
Score Menu Program
By Hexon Hartley Jimenez
"""

MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    score = get_valid_score()  # To initialize initial score
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":

        if choice == "G":
            score = get_valid_score()

        elif choice == "P":
            print_score_result(score)

        elif choice == "S":
            print_star(score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("farewell")


def get_valid_score():
    score = int(input("Enter valid score between 0-100: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter valid score: "))
    return score


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_score_result(score):
    score_result = determine_score(score)
    print(f"Score: {score} is {score_result}")


def print_star(score):
    star_count = "*" * score
    print(f"{star_count}")


main()
