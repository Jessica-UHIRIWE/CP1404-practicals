from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object with fanciness of 2
luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Drive the taxi 18 km
luxury_taxi.drive(18)

# Calculate the fare
calculated_fare = luxury_taxi.get_fare()

# Expected fare: (2 * 1.23 * 18) + 4.50
expected_fare = (2 * 1.23 * 18) + 4.50

# Assert to check if the calculated fare is as expected
assert abs(calculated_fare - expected_fare) < 0.01, f"Expected fare: {expected_fare}, but got {calculated_fare}"

# Assert to check the string representation
assert str(luxury_taxi) == "Hummer, fuel=182, odo=18, 18km on current fare, $2.46/km plus flagfall of $4.50", \
    f"Unexpected string representation: {str(luxury_taxi)}"

# If all assertions pass, print a success message
print("All tests passed successfully!")
