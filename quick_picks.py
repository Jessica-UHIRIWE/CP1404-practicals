import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))

def generate_quick_pick():
    """Generate a single quick pick."""
    numbers = set()
    while len(numbers) < NUMBERS_PER_QUICK_PICK:
        numbers.add(random.randint(MIN_NUMBER, MAX_NUMBER))
    return sorted(numbers)

def main():
    for i in range(NUM_QUICK_PICKS):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


main()
