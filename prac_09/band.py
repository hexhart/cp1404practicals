"""
CP1404/CP5632 Practical 9 By Hexon Hartley Jimenez
Band class file
Estimated: 45 minutes
Actual: 20 minutes
"""


class Band:
    """Class represents Band object."""

    def __init__(self, band):
        """Initializes a Band name and an empty list of musicians."""
        self.band = band
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musicians_info = [str(musician) for musician in self.musicians]
        return f"{self.band}  ({', '.join(musicians_info)})"

    def add(self, musician):
        """Add musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musicians playing their instruments."""
        play_info = []
        for musicians in self.musicians:
            play_info.append(musicians.play())
        return "\n".join(play_info)
