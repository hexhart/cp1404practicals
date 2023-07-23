"""
CP1404/CP5632 Practical 7 By Hexon Hartley Jimenez
Project Class file
Estimated:
Actual:
"""


class Project:
    """Class representing the Project"""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Constructs of Project from the given task details"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%"
