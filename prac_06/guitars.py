"""
CP1404/CP5632 Practical 6 By Hexon Hartley Jimenez
Guitars class file
Estimated: 30 minutes
Actual:
"""
CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Class representing Guitars"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise the Guitar constructs"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format of the Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if guitar is 50 or more years old, otherwise False"""
        return self.get_age() >= VINTAGE_AGE
