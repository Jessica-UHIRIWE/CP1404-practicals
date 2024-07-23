import csv


def read_csv(filename):
    """
    Read the CSV file and return a list of lists representing the data.
    """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            data.append(row)
    return data


def get_champions_and_counts(data):
    """
    Process the data to get champions and their win counts.
    Returns a dictionary where keys are champions and values are their win counts.
    """
    champions = {}
    for row in data:
        champion = row[0]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """
    Process the data to extract countries of champions.
    Returns a sorted list of unique countries.
    """
    countries = set()
    for row in data:
        champion = row[0]
        country = row[1]
        countries.add(country)
    sorted_countries = sorted(countries)
    return sorted_countries


def display_results(champions, countries):
    """
    Display the processed results: champions and their win counts,
    and the list of countries in alphabetical order.
    """
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)


def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)

    champions = get_champions_and_counts(data)
    countries = get_countries(data)

    display_results(champions, countries)



main()
