"""
CP1404/CP5632 - Practical 2
Password checking program
By Hexon Hartley Jimenez
"""
# Mr.Lindsay, May I know if my coding is correct? Any tips how to improve my code?

MINIMUM_LENGTH = 6


def main():
    print(f"Minimum password length is {MINIMUM_LENGTH} characters")
    password = get_password()
    print_password_asterisk(password)


def get_password():
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password did not meet the minimum {MINIMUM_LENGTH} character requirements")
        password = input("Enter a password: ")
    return password


def print_password_asterisk(password):
    print("*" * len(password))


main()
