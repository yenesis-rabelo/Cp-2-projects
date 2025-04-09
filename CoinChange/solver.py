def coin_change(target, coins):
    # Solves the Coin Change Problem allowing decimal values
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
