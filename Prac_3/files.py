# Task 1: Write user's name to a file
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

# Task 2: Read name from the file and print a greeting
with open("name.txt", 'r') as file:
    name = file.read().strip()  # Remove any leading or trailing whitespace
print(f"Hi {name}!")

# Task 3: Read the first two numbers from numbers.txt and print their sum
with open("numbers.txt", 'r') as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    total = first_number + second_number
print("Sum of the first two numbers:", total)

# Task 4: Read all numbers from numbers.txt and print their total
total = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        total += int(line.strip())
print("Total of all numbers in the file:", total)

