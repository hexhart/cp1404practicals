"""
CP1404/CP5632 Practical 6 By Hexon Hartley Jimenez
Guitars class file
Estimated: 30 minutes
Actual:
"""


class Guitar:
    """Class representing Guitars"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise the Guitar constructs"""
        self.name = name
        self.year = year
        self.cost = cost

