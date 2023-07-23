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


if __name__ == "__main__":
    main()
