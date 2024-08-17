from prac_09.taxi import Taxi

# Create a new taxi object with name "Prius 1" and 100 units of fuel
my_taxi = Taxi("Prius 1", 100)

# Drive the taxi 40 km
my_taxi.drive(40)

# Get taxi's details and the current fare
taxi_details_1 = my_taxi.__str__()
current_fare_1 = my_taxi.get_fare()

# Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# Get the updated taxi's details and the current fare
taxi_details_2 = my_taxi.__str__()
current_fare_2 = my_taxi.get_fare()
