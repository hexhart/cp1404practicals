"""
CP1404/CP5632 Practical 9 By Hexon Hartley Jimenez
UnreliableCar class file
Estimated: 45 minutes
Actual: 36 minutes
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialized version of Car that includes reliability percentage"""

    def __init__(self, name, fuel, reliability):
        """Initialize UnreliableCar instance, based on parent class Car"""
        # call the Car's version of __init__, and then set the reliability to the value passed in
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string representation similar to Car that includes reliability"""
        return f"{super.__str__(self)}, reliability={self.reliability}%"

    def drive(self, distance):
        """Drive the car with a chance based on reliability"""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
