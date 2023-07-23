"""
CP1404/CP5632 Practical 7 By Hexon Hartley Jimenez
Project Management Client Program
Estimated:
Actual:
"""
import datetime
from prac_07.project import Project

FILENAME = "project.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """
    Main function to run the travel tracker program
    """
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")




if __name__ == "__main__":
    main()
