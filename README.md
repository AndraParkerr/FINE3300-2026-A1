# FINE 3300 Assignment 1 – Exchange Rate Calculator

## Project Description

This project is a Python currency exchange calculator that converts between US dollars (USD) and Canadian dollars (CAD). It reads the exchange rate from a Bank of Canada CSV file and calculates the converted amount.

## Files

- `ExchangeRates.py` – My Part 1 implementation of the currency converter.
- `ExchangeRatesAI.py` – The AI-generated version created with Claude for Part 2.
- `BankOfCanadaExchangeRate.2026.csv` – The CSV file containing the exchange-rate data.

## Requirements

- Python 3
- All three files must be saved in the same project folder.

## How to Run

Open a terminal in the project folder and run either program:

```bash
python3 ExchangeRates.py
```

or

```bash
python3 ExchangeRatesAI.py
```

Enter the amount, source currency (`USD` or `CAD`), and target currency (`USD` or `CAD`) when prompted.

## Test Results

Using the exchange rate of 1.3978 CAD per USD from the CSV file:

- 100,000 USD to CAD: `$100,000.00 USD = $139,780.00 CAD`
- 100,000 CAD to USD: `$100,000.00 CAD = $71,540.99 USD`
