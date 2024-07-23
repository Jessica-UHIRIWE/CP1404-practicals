
def main():
    print_line(20)
    print("Welcome")
    print_line(8)


def print_line(length):
    print("-" * length)


main()


def main( parameter_1, parameter_2):
    print_line(parameter_1)
    print("Welcome")
    print_line( parameter_2)


def print_line(length):
    print("-" * length)


main(10,2)