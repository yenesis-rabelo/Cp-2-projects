def show_available_countries(countries):
    print("\n========== Available Countries ==========")
    fixed_countries = ["USA", "UK", "Canada", "Euro"]
    for country in fixed_countries:
        if country.lower() in countries:
            print(f"- {country}")
    print("=========================================\n")

def show_coin_result(result):
    if isinstance(result, str):
        print(result)
    else:
        num_coins, coin_list = result
        print(f"Minimum number of coins needed: {num_coins}")
        print("Coins used:", ", ".join(coin_list))




