import csv

def load_coin_denominations(filename="coin_denominations.csv"):
    # Loads available countries and their coin denominations
    countries = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                country = row[0].strip()
                coins = [coin.split("-") for coin in row[1:]]
                countries[country.lower()] = [(name, float(value)) for name, value in coins]
    except FileNotFoundError:
        print("Error: Coin denomination file not found.")
    return countries
