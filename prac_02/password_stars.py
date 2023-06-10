"""
Password checking program for Prac 2 of Week 2
By Hexon Hartley Jimenez
"""
# Mr.Lindsay, May I know if my coding is correct? Any tips how to improve my code?

MINIMUM_LENGTH = 6


def main():
    print("Minimum password length is 6 characters")
    password = get_password()
    print("*" * len(password))


def get_password():
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password did not meet the minimum {MINIMUM_LENGTH} character requirements")
        password = input("Enter a password: ")
    return password


main()
