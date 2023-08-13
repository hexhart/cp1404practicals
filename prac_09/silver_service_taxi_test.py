"""
CP1404/CP5632 Practical 9 By Hexon Hartley Jimenez
SilverServiceTaxi client program file
Estimated: 45 minutes
Actual: 45 minutes
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Testing SilverServiceTaxi class"""
    my_taxi = SilverServiceTaxi("Hummer", 100, 2)
    distance_driven = my_taxi.drive(18)
    print(my_taxi)
    print(f"The total cost of the fare including flagfall charge: ${my_taxi.get_fare():.2f}")
    print(
        f"For an {distance_driven}km trip in a SilverServiceTaxi with fanciness of {my_taxi.fanciness}," 
        f"the fare should be ${my_taxi.get_fare():.2f}")


main()
