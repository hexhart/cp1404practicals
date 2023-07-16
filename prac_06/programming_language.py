"""
CP1404/CP5632 Practical 6 By Hexon Hartley Jimenez
Intermediate Exercise: Programming languages class file
Estimated: 30 minutes
Actual: 30 minutes
"""


class ProgrammingLanguage:
    """Class representing programming langauge"""

    def __init__(self, name, typing, reflection, year):
        """Construct of ProgrammingLanguage from the given task details"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """This determines if language is dynamically types or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns the string representations of ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
