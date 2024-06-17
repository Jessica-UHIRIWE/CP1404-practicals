def print_income_report(incomes, number_of_months):
    """Prints the income report for the given list of incomes over the specified number of months."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]  # Retrieve income for the current month
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: $"))
        incomes.append(income)

    print_income_report(incomes, number_of_months)


main()
