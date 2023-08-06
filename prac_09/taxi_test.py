"""
CP1404/CP5632 Practical 9 By Hexon Hartley Jimenez
Taxi test program to test Taxi class
Estimated: 45 minutes
Actual: 15 minutes
"""
# from prac_09 import taxi
from taxi import Taxi

# Create my_taxi object, with name, fuel and price
my_taxi = Taxi("Prius 1", 100, 1.23)
my_taxi.drive(40)
print(f"{my_taxi}, current fare costs ${my_taxi.get_fare():.2f}")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"{my_taxi}, current fare costs ${my_taxi.get_fare():.2f}")
