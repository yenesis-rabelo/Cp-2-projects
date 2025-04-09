def show_available_countries(countries):
    print("\nAvailable countries:")
    for country in countries.keys():
        print(f"- {country.capitalize()}")

def show_coin_result(result):
    if isinstance(result, str):
        print(result)
    else:
        num_coins, coin_list = result
        print(f"Minimum number of coins needed: {num_coins}")
        print("Coins used:", ", ".join(coin_list))
