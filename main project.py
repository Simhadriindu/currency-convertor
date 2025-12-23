import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error fetching data"

    data = response.json()
    rate = data['rates'].get(to_currency.upper())

    if rate:
        converted = amount * rate
        return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
    else:
        return "Invalid target currency"

# Example usage
amount = float(input("Enter amount: "))
from_currency = input("From (currency code): ")
to_currency = input("To (currency code): ")

result = convert_currency(amount, from_currency, to_currency)
print(result)
