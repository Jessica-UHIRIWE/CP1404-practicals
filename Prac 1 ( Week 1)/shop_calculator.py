def calculate_total_price(num_items, item_prices):

    total_price = sum(item_prices)

    # Apply a 10% discount if the total price is over $100
    if total_price > 100:
        total_price *= 0.9

    return total_price


def main():
    try:
        num_items = int(input("Number of items: "))
        if num_items < 0:
            print("Invalid number of items!")
            return

        item_prices = []
        for i in range(num_items):
            price = float(input(f"Price of item {i + 1}: $"))
            item_prices.append(price)

        total_price = calculate_total_price(num_items, item_prices)
        print(f"Total price for {num_items} items is ${total_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


if __name__ == "__main__":
    main()