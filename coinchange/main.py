import csv
import os

def create_coin_denominations_file():
    """Creates a CSV file with coin denominations for at least four countries if it does not exist."""
    filename = "coin_denominations.csv"
    if not os.path.exists(filename):
        data = [
            ["USA", "Penny-1", "Nickel-5", "Dime-10", "Quarter-25"],
            ["UK", "Penny-1", "Two Pence-2", "Five Pence-5", "Ten Pence-10", "Twenty Pence-20", "Fifty Pence-50"],
            ["Canada", "Penny-1", "Nickel-5", "Dime-10", "Quarter-25", "Loonie-100", "Toonie-200"],
            ["Euro", "One Cent-1", "Two Cents-2", "Five Cents-5", "Ten Cents-10", "Twenty Cents-20", "Fifty Cents-50", "One Euro-100", "Two Euros-200"]
        ]
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

def load_coin_denominations(country):
    """Loads coin denominations from a CSV file for the specified country."""
    try:
        with open("coin_denominations.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].strip().lower() == country.lower():
                    coins = [coin.split("-") for coin in row[1:]]
                    return [(name, int(value)) for name, value in coins]
    except FileNotFoundError:
        print("Error: Coin denomination file not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return None

def coin_change(target, coins):
    """Solves the Coin Change Problem using a dynamic approach."""
    if target <= 0:
        return "Invalid target amount. Please enter a positive value."
    
    coins.sort(key=lambda x: x[1], reverse=True)  # Sort by highest value first
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
    
    # Backtrack to find the coins used
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
    create_coin_denominations_file()  # Ensure the file exists
    
    country = input("Enter the country: ").strip()
    coins = load_coin_denominations(country)
    
    if not coins:
        print("No coin denominations found for the given country.")
        return
    
    try:
        target = int(input("Enter the target amount: ").strip())
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return
    
    result = coin_change(target, coins)
    
    if isinstance(result, str):
        print(result)
    else:
        num_coins, coin_list = result
        print(f"Minimum number of coins needed: {num_coins}")
        print("Coins used:", ", ".join(coin_list))

if __name__ == "__main__":
    main()

