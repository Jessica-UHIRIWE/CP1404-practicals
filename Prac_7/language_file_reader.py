"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    try:
        # Open the file for reading
        with open('languages.csv', 'r') as in_file:
            # File format is like: Language,Typing,Reflection,Year,Pointer Arithmetic
            # 'Consume' the first line (header) - we don't need its contents
            in_file.readline()
            # All other lines are language data
            for line in in_file:
                # Strip newline from end and split it into parts (CSV)
                parts = line.strip().split(',')

                # Debug: Print the parts to verify the format
                print(parts)

                # Check if line has the correct number of columns
                if len(parts) != 5:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue

                # Reflection and Pointer Arithmetic are stored as strings, convert to Boolean
                reflection = parts[2] == "Yes"
                pointer_arithmetic = parts[4] == "Yes"

                # Construct a ProgrammingLanguage object using the elements
                # year should be an int
                language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
                # Add the language we've just constructed to the list
                languages.append(language)

    except FileNotFoundError:
        print("Error: The file 'languages.csv' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    # Loop through and display all languages (using their str method)
    print("Programming Languages from custom class:")
    for language in languages:
        print(language)


def using_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)  # use default dialect, Excel
        print("CSV rows using csv module:")
        for row in reader:
            print(row)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print("CSV header fields:", file_field_names)
        # Language will be a new subclass of the tuple data type class
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)  # use default dialect, Excel

        print("NamedTuples:")
        for row in reader:
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open("languages.csv", "r") as in_file:
        in_file.readline()
        print("CSV NamedTuples:")
        for language in map(Language._make, csv.reader(in_file)):
            print(f"{language.name} was released in {language.year}")
            print(f"Pointer Arithmetic: {language.pointer_arithmetic}")
            print(repr(language))


if __name__ == "__main__":
    # Run each function separately as needed
    main()
    # Uncomment the following lines to run each specific function:
    # using_csv()
    # using_namedtuple()
    # using_csv_namedtuple()
