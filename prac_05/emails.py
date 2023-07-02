"""
CP1404/CP5632 Practical 5 By Hexon Hartley Jimenez
Emails program
This program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one which ends the program.
Has a function to extract name from the email and print after blank is entered from Email user input.
Estimated: 30 minutes
Actual: 45 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":  # Loop initializes, ends when blank input is entered
        name = get_name_from_email(email)  # function call to return name from email input
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):  # function to extract name from email
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
