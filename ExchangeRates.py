# ExchangeRates.py
# FINE 3300 - Currency exchange calculator (USD and CAD)

import csv


class ExchangeRates:

    def __init__(self, filename):
        # Save the name of the CSV file
        self.filename = filename

    def convert(self, amount, source_currency, target_currency):
        # Open the CSV file. "utf-8-sig" gets rid of the BOM at the start.
        file = open(self.filename, "r", encoding="utf-8-sig", newline="")
        reader = csv.DictReader(file)

        # Loop through every row. Each time, save the row.
        # After the loop finishes, last_row holds the last row of the file.
        last_row = None
        for row in reader:
            last_row = row

        file.close()

        # Get the FXAUSDCAD value from the last row.
        # It is text, so change it to a number with float().
        rate = float(last_row["FXAUSDCAD"])

        # The rate is CAD per 1 USD
        if source_currency == "USD" and target_currency == "CAD":
            converted_amount = amount * rate     # USD to CAD: multiply
        elif source_currency == "CAD" and target_currency == "USD":
            converted_amount = amount / rate     # CAD to USD: divide
        else:
            converted_amount = amount            # same currency

        return converted_amount


# ----- Main program -----

# Make the object using the CSV file name
exchange = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

# Ask the user for the three inputs
amount = float(input("Enter the amount to convert: "))
source_currency = input("Enter the source currency (USD or CAD): ").upper()
target_currency = input("Enter the target currency (USD or CAD): ").upper()

# Call the convert method
converted_amount = exchange.convert(amount, source_currency, target_currency)

# Print the answer with $ sign, commas, 2 decimals, and currency code
print(f"${amount:,.2f} {source_currency} = ${converted_amount:,.2f} {target_currency}")