import csv
import os

def load_coin_denominations():
    filename = os.path.join(os.path.dirname(__file__), "coin_denominations.csv")
    countries = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 2:  # Skip blank/malformed lines
                    continue
                country = row[0].strip()
                coins = []
                for coin in row[1:]:
                    if "-" in coin:
                        name, value = coin.split("-")
                        coins.append((name.strip(), float(value)))
                countries[country.lower()] = coins
    except FileNotFoundError:
        print(f"Error: Coin denomination file not found at {filename}")
    return countries




