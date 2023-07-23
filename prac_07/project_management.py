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
    """Displays the list of incomplete and completed projects"""
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


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i}: {project}")

    try:
        project_index = int(input("Project choice: "))
        if 0 <= project_index < len(projects):
            project = projects[project_index]
            percent_complete_str = input("New Percentage: ")
            priority_str = input("New Priority (leave blank to retain existing value): ")

            if percent_complete_str:
                project.percent_complete = int(percent_complete_str)
            if priority_str:
                project.priority = int(priority_str)

            print("Project updated successfully.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Project not updated.")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
        print("New project added successfully.")
    except ValueError:
        print("Invalid date format. Project not added.")


def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date >= date]
    filtered_projects.sort()
    for project in filtered_projects:
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
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
