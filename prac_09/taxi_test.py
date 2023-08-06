"""
CP1404/CP5632 Practical 9 By Hexon Hartley Jimenez
Taxi test program to test Taxi class
Estimated: 45 minutes
Actual: 15 minutes
"""
# from prac_09 import taxi
from taxi import Taxi


def main():
    # Create my_taxi object, with name, fuel and price
    my_taxi = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi at 40km
    my_taxi.drive(40)

    # Print taxi's details and current fare
    print(f"{my_taxi}, current fare costs ${my_taxi.get_fare():.2f}")

    # Start a new fare, then drive car at 100km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print details of the new fare and cost
    print(f"{my_taxi}, current fare costs ${my_taxi.get_fare():.2f}")


main()
