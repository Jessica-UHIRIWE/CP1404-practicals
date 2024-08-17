import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """Format the phrase as a sentence."""
    if not phrase:
        return '.'
    return phrase[0].upper() + phrase[1:] + '.'


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message
    car_default_fuel = Car()
    assert car_default_fuel.fuel == 0, "Car does not set default fuel correctly"

    car_custom_fuel = Car(fuel=10)
    assert car_custom_fuel.fuel == 10, "Car does not set custom fuel correctly"

    assert is_long_word("not") == False
    assert is_long_word("supercalifrag") == True
    assert is_long_word("Python", 6) == True

    assert format_sentence('hello') == 'Hello.'
    assert format_sentence('It is an ex parrot.') == 'It is an ex parrot.'
    assert format_sentence('this is a test') == 'This is a test.'


# Run the tests
run_tests()

# Uncomment the following line and run the doctests
# doctest.testmod()
