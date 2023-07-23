"""
CP1404/CP5632 Practical 7 By Hexon Hartley Jimenez
myguitars.py- a program to read all guitars and store them in a list of Guitar objects
"""


def main():
    """
    Reads the guitars file and store them in a list of Guitar objects

    Displays the guitars in a list
    Displays the guitars in a sorted manner
    """
    # Read guitars from file and store them in a list of Guitar objects
    guitars = read_guitars_from_file('guitars.csv')

    # Display the guitars
    print("Guitars as they are:")
    display_guitars(guitars)

    # Sort the guitars by year (oldest to newest)
    guitars.sort()

    # Display the sorted guitars
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)


# Guitar class definition
class Guitar:
    """Class representing Guitars"""

    def __init__(self, name, year, cost):
        """Initialize the Guitar constructs, format/protocol is Name, Year, Cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format of the Guitar"""
        return f"{self.name}, {self.year}, ${self.cost:.2f}"

    def __lt__(self, other):
        """Less than comparison method to sort guitars based on their year"""
        return self.year < other.year


def read_guitars_from_file(filename):
    """Reads the guitars.csv file and returns list of guitars and their properties"""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """To display the list of guitars"""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
