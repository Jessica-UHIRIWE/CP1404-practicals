from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""

    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # Adjust price per km based on fanciness

    def get_fare(self):
        """Return the price for the taxi trip including the flagfall charge."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flagfall added."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
