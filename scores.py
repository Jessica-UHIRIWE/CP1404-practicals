import random


def get_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def main():
    # Ask the user for the number of scores
    num_scores = int(input("Enter the number of scores: "))

    # Generate random scores and determine results
    with open('results.txt', 'w') as file:
        for _ in range(num_scores):
            score = random.randint(0, 100)
            result = get_result(score)
            file.write(f"{score} is {result}\n")


main()
