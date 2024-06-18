def get_valid_age (low, high):
    age = int(input(" Age:"))
    while age < low or age > high:
        print("Invalid Age")
        age = int(input(" Age:"))
        return age