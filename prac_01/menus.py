"""
CP1404/CP5632 - Practical
A Simple Menu Program
By Hexon Hartley Jimenez
"""

name = input("Enter name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    elif choice == "Q":
        print(f"Quit {name}")
    else:
        print("Invalid Choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
