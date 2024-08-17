import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if the random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            # Drive normally as the car is reliable this time
            return super().drive(distance)
        else:
            # Car is unreliable this time and drives 0 km
            return 0
