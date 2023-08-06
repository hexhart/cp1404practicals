"""
CP1404/CP5632 Practical 9 By Hexon Hartley Jimenez
SilverServiceTaxi class file
Estimated: 45 minutes
Actual: 45 minutes
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of Taxi class that represents SilverServiceTaxi"""
    # adding a class variable, flagfall set to 4.50
    flagfall = 4.50

    # adding new attribute fanciness into constructor and multiplied by price_per_km
    def __init__(self, name, fuel, fanciness):
        """Initializes SilverServiceTaxi instances"""
        super().__init__(name, fuel)
        self.fanciness = fanciness

        # customizable instance variable that has the initial base price * fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    # override fare method to include the flagfall (extra charge)
    def get_fare(self):
        """Get the fare price"""
        # get the total of the fare + flagfall charge
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return string representation of SilverServiceTaxi including flagfall"""
        # reusing the parent class's __str__ method
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
