import csv
import os

def load_coin_denominations():
    """Loads available countries and their coin denominations."""
    countries = {}
    try:
        with open("coin_denominations.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                country = row[0].strip()
                coins = [coin.split("-") for coin in row[1:]]
                countries[country.lower()] = [(name, float(value)) for name, value in coins]
    except FileNotFoundError:
        print("Error: Coin denomination file not found.")
    return countries

def coin_change(target, coins):
    """Solves the Coin Change Problem allowing decimal values."""
    if target <= 0:
        return "Invalid target amount. Please enter a positive value."
    
    smallest_denomination = min(coin[1] for coin in coins)
    scale = int(1 / smallest_denomination)
    target = int(round(target * scale))
    coins = [(name, int(value * scale)) for name, value in coins]
    
    coins.sort(key=lambda x: x[1], reverse=True)
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    coin_used = [-1] * (target + 1)
    
    for name, value in coins:
        for j in range(value, target + 1):
            if dp[j - value] + 1 < dp[j]:
                dp[j] = dp[j - value] + 1
                coin_used[j] = value
    
    if dp[target] == float('inf'):
        return "No solution possible with the given denominations."
    
    result = []
    amount = target
    while amount > 0:
        for name, value in coins:
            if value == coin_used[amount]:
                result.append(name)
                amount -= value
                break
    
    return dp[target], result

def main():
    """Main function to handle user interaction."""
    countries = load_coin_denominations()
    
    while True:
        print("\nAvailable countries:")
        for country in countries.keys():
            print(f"- {country.capitalize()}")
        
        country = input("Enter the country (or 'exit' to quit): ").strip().lower()
        if country == "exit":
            print("Goodbye!")
            break
        
        if country not in countries:
            print("Invalid country. Please choose from the list.")
            continue
        
        while True:
            try:
                target = float(input("Enter the target amount (or -1 to choose another country): ").strip())
                if target == -1:
                    break
                
                result = coin_change(target, countries[country])
                
                if isinstance(result, str):
                    print(result)
                else:
                    num_coins, coin_list = result
                    print(f"Minimum number of coins needed: {num_coins}")
                    print("Coins used:", ", ".join(coin_list))
            except ValueError:
                print("Invalid input. Please enter a valid numerical value.")

if __name__ == "__main__":
    main()



