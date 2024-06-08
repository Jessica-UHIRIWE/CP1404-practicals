def main():
    # Constants
    LENGTH = 10

    # Ask the user for a password
    password = input("Enter your password: ")

    # Repeat until the password meets the exact length
    while len(password) != LENGTH:
        print(f"Password must be exactly {LENGTH} characters long.")
        password = input("Enter your password: ")

    # Print asterisks as long as the password
    print("*" * len(password))


# Call the main function to execute the program
main()