"""
Estimated Time: 60 minutes
Current Time: 4:00 PM
Finished Time: 4:40 PM
Actual Time Taken: 40 minutes
"""

from guitar import Guitar


def run_tests():
    """Run tests for Guitar class methods."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 765.40)

    print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 11. Got {another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()
