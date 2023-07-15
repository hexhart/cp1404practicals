"""
CP1404/CP5632 Practical 5 By Hexon Hartley Jimenez
Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Mazda", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)  # prints the __str__method

    print("\n")  # whitespace to separate the output
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in {limo.name}: {limo.fuel} units")
    distance_driven = limo.drive(115)
    print(f"Distance driven: {distance_driven} km")
    print(limo)  # prints the __str__method


main()
