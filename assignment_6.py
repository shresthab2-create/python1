def get_currency_pair():
    # Define supported currency pairs and their exchange rates
    currency_pairs = {
        'USD to EUR': 0.85,
        'EUR to USD': 1.18,
        'USD to GBP': 0.75,
        'GBP to USD': 1.33,
        'EUR to GBP': 0.88,
        'GBP to EUR': 1.14
    }

    print("Supported currency pairs:")
    for pair in currency_pairs.keys():
        print(pair)

    while True:
        try:
            # Prompt the user to enter a currency pair
            currency_pair = input("Enter the currency pair (e.g., 'USD to EUR'): ").strip()
            if currency_pair not in currency_pairs:
                raise ValueError("Unsupported currency pair. Please choose from the supported pairs.")
            return currency_pair, currency_pairs[currency_pair]
        except ValueError as e:
            print(f"Invalid input: {e}")


def get_amount():
    while True:
        try:
            # Prompt the user to enter an amount
            amount = float(input("Enter the amount: "))
            if amount < 0:
                raise ValueError("The amount must be a non-negative number.")
            return amount
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid non-negative number.")


def convert_currency(amount, exchange_rate):
    # Convert the amount using the exchange rate
    return amount * exchange_rate


def main():
    # Get the currency pair and exchange rate
    currency_pair, exchange_rate = get_currency_pair()

    # Get the amount to be converted
    amount = get_amount()

    # Convert the amount
    converted_amount = convert_currency(amount, exchange_rate)

    # Display the converted amount
    from_currency, to_currency = currency_pair.split(" to ")
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")


if __name__ == "__main__":
    main()
