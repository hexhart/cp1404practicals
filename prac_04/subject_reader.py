"""
CP1404/CP5632 Practical 4 By Hexon Hartley Jimenez
Data file -> lists program
"""
FILENAME = "subject_data.txt"


def main():
    subjects = get_subjects()
    display_subjects(subjects)
    print(subjects)  # Print test to ensure task 2 returns nested list


def get_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        # REMOVED: print(line)  # See what a line looks like
        # REMOVE: print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # REMOVED: print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # Print to see how the elements are represented
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
