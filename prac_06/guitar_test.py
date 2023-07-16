"""
CP1404/CP5632 Practical 6 By Hexon Hartley Jimenez
Guitars test code
Estimated: 30 minutes
Actual: 30 minutes
"""
from prac_06.guitars import Guitar

CURRENT_YEAR = 2023


def test_guitar_methods():
    """Test for Guitars class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    # Test get_age()
    print("\n")
    print(f"{guitar.name} get_age() - Expected {101}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {11}. Got {other.get_age()}")
    print()

    # Test is_vintage()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")
    print()

    # Test is_vintage() with different f-string
    print(f"{guitar.get_age()}-year old guitar is_vintage() - Expected {True}. Got {guitar.is_vintage()}")


if __name__ == '__main__':
    test_guitar_methods()
