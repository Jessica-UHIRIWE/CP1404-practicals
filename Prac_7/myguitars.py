from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header if there is one
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def main():
    """Main function to handle the process."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("Guitars loaded from file:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    # Add new guitars
    while True:
        name = input("Enter guitar name (or leave blank to finish): ")
        if not name:
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

    # Write updated list to file
    with open(filename, 'w') as file:
        file.write("Name,Year,Cost\n")  # Write header
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

    print("\nUpdated list of guitars:")
    display_guitars(guitars)


if __name__ == "__main__":
    main()
