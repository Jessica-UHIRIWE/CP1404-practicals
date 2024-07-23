def main():
    score = get_valid_score()
    while True:
        print(" Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice, please choose again.")

def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input; please enter an integer.")

def print_result(score):
    """Determine and print the result based on the score."""
    if 90 <= score <= 100:
        result = "Excellent"
    elif 80 <= score < 90:
        result = "Good"
    elif 50 <= score < 80:
        result = "Passable"
    else:
        result = "Bad"
    print(f"Your result is: {result}")

def show_stars(score):
    """Print as many stars as the score."""
    print('*' * score)

# Call the main function to execute the program
main()
