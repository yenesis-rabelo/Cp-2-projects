def coin_change(target, coins):
    if target < 0:
        return "Invalid target amount. Please enter a positive value."

    # Convert the full amount (dollars and cents) to cents
    target_cents = round(target * 100)

    # Convert coin values to cents
    coins = [(name, int(round(value * 100))) for name, value in coins]
    coins.sort(key=lambda x: x[1], reverse=True)

    dp = [float('inf')] * (target_cents + 1)
    dp[0] = 0
    coin_used = [-1] * (target_cents + 1)

    for name, value in coins:
        for j in range(value, target_cents + 1):
            if dp[j - value] + 1 < dp[j]:
                dp[j] = dp[j - value] + 1
                coin_used[j] = value

    if dp[target_cents] == float('inf'):
        return "No solution possible with the given denominations."

    result = {}
    amount = target_cents
    while amount > 0:
        for name, value in coins:
            if value == coin_used[amount]:
                result[name] = result.get(name, 0) + 1
                amount -= value
                break

    result_list = [f"{coin}: {count}" for coin, count in result.items()]
    return dp[target_cents], result_list




































