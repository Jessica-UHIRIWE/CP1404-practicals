from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the list of taxis with their string representation."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi from the list of taxis."""
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input. Enter a number.")
        return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return the cost."""
    try:
        distance = float(input("Drive how far? "))
        if distance < 0:
            print("Distance cannot be negative.")
            return 0
        taxi.drive(distance)
        fare = taxi.get_fare()
        return fare
    except ValueError:
        print("Invalid input. Enter a number.")
        return 0


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0

    print("Let's drive!")

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Final taxi statuses:")
            display_taxis(taxis)
            break

        elif choice == 'c':
            print("Available taxis:")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)

        elif choice == 'd':
            if current_taxi is None:
                print("Select a taxi first.")
            else:
                fare = drive_taxi(current_taxi)
                if fare > 0:
                    print(f"Trip cost: ${fare:.2f}")
                    total_bill += fare

        else:
            print("Invalid option.")

        print(f"Bill to date: ${total_bill:.2f}")


if __name__ == "__main__":
    main()
