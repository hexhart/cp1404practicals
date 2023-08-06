"""
CP1404/CP5632 Practical 9 By Hexon Hartley Jimenez
UnreliableCar client program file
Estimated: 45 minutes
Actual: 36 minutes
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar Class"""

    # create new cars, one good and one bad to test reliability
    good_car = UnreliableCar("Mazda 2", 100, 80)
    bad_car = UnreliableCar("Recycled Car", 100, 30)

    # test drive cars
    for distance in range(1, 10):
        print(f"Drive test car at a distance {distance:2}km:")
        print(f"{good_car.name:12} drove {good_car.drive(distance):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(distance):2}km\n")

    # print drive test result
    print(f"\n{good_car.name}, reliability: {good_car.reliability}%")
    print(f"{bad_car.name}, reliability: {bad_car.reliability}%")


main()
