from prac_09.unreliable_car import UnreliableCar

# Create a new UnreliableCar object with 50% reliability
my_unreliable_car = UnreliableCar("Unreliable Prius", 100, 50)

# Attempt to drive the car 30 km
distance_driven_1 = my_unreliable_car.drive(30)

# Attempt to drive the car another 30 km
distance_driven_2 = my_unreliable_car.drive(30)

# The distances driven are now stored in the variables distance_driven_1 and distance_driven_2.
