import requests

API_KEY = "2106de0b4b0df8d33d577943" 
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def convert_currency(base_currency, target_currency, amount):
    url = BASE_URL + base_currency.upper()

    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching exchange rates.")
        return

    data = response.json()
    if data['result'] != "success":
        print("Invalid base currency or API key.")
        return

    
    rates = data['conversion_rates']
    if target_currency.upper() not in rates:
        print("Target currency not supported.")
        return

    rate = rates[target_currency.upper()]
    converted_amount = amount * rate

    print(f"\n{amount} {base_currency.upper()} = {converted_amount:.2f} {target_currency.upper()}")
    print(f"Exchange Rate: 1 {base_currency.upper()} = {rate:.4f} {target_currency.upper()}")

def main():
    print("== Currency Converter ==")
    base = input("From Currency (e.g., USD): ")
    target = input("To Currency (e.g., INR): ")
    amount = float(input("Amount to convert: "))

    convert_currency(base, target, amount)

main()
