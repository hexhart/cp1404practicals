"""
CP1404/CP5632 Practical 7 By Hexon Hartley Jimenez
Project Management Client Program
Estimated:
Actual:
"""
import datetime
from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def load_projects(filename):
    projects = []
    try:
        with open(filename, "r") as file:
            header = file.readline().strip().split("\t")
            for line in file:
                data = line.strip().split("\t")
                if len(data) == len(header):
                    name, start_date, priority, cost_estimate, percent_complete = data
                    try:
                        start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                        priority = int(priority)
                        cost_estimate = float(cost_estimate)
                        percent_complete = int(percent_complete)
                        project = Project(name, start_date, priority, cost_estimate, percent_complete)
                        projects.append(project)
                    except ValueError:
                        print(f"Invalid data format in line: {line}")
                else:
                    print(f"Invalid data in line: {line}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. No projects loaded.")
    return projects


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.percent_complete < 100]
    completed_projects = [project for project in projects if project.percent_complete == 100]

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def main():
    """Main function to run project management program"""
    # projects = []

    filename = "project.txt"
    projects = load_projects(filename)

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
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
