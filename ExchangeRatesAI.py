# ExchangeRatesAI.py
# FINE 3300 - Currency exchange calculator (USD <-> CAD)
# The exchange rate is read from the last data row of a Bank of Canada CSV file.

import csv


class ExchangeRates:
    """Converts between USD and CAD using a rate stored in a CSV file."""

    def __init__(self, filename):
        # Store the CSV filename so convert() can use it later
        self.filename = filename

    def get_rate(self):
        """Read the FXAUSDCAD rate (CAD per 1 USD) from the last data row."""
        # "utf-8-sig" removes the BOM at the start of the file so the first
        # column name is read correctly. newline="" is recommended for csv.
        with open(self.filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)   # Uses the header row as column names
            rows = list(reader)             # Put every data row into a list

        last_row = rows[-1]                 # The last data row in the file
        rate = float(last_row["FXAUSDCAD"]) # Convert the text value to a number
        return rate

    def convert(self, amount, source_currency, target_currency):
        """Convert an amount from the source currency to the target currency."""
        rate = self.get_rate()  # CAD per 1 USD, read from the CSV (not hardcoded)

        if source_currency == "USD" and target_currency == "CAD":
            converted_amount = amount * rate    # USD -> CAD: multiply
        elif source_currency == "CAD" and target_currency == "USD":
            converted_amount = amount / rate    # CAD -> USD: divide
        else:
            converted_amount = amount           # Same currency: no change

        return converted_amount


# ----- Main program -----
filename = "BankOfCanadaExchangeRate.2026.csv"
exchange = ExchangeRates(filename)

# Ask the user for input (input() returns text, so convert the amount to float)
amount = float(input("Enter the amount to convert: "))
source_currency = input("Enter the source currency (USD or CAD): ").strip().upper()
target_currency = input("Enter the target currency (USD or CAD): ").strip().upper()

# Do the conversion
converted_amount = exchange.convert(amount, source_currency, target_currency)

# Display the result: dollar sign, commas, 2 decimals, currency code
print(f"${amount:,.2f} {source_currency} = ${converted_amount:,.2f} {target_currency}")