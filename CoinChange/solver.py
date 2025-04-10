def coin_change(target, coins):
    if target <= 0:
        return "Invalid target amount. Please enter a positive value."

    # Scale the target for precision (convert target to pence, e.g., 1.23 => 123)
    scale = 100  # To work in pence (cents)
    target = int(round(target * scale))  # Convert target to an integer value in pence

    # Scale coin denominations to pence
    coins = [(name, int(round(value * scale))) for name, value in coins]

    # Sort coins in descending order (largest coin first)
    coins.sort(key=lambda x: x[1], reverse=True)

    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # No coins needed for 0 amount
    coin_used = [-1] * (target + 1)

    # Dynamic programming to find minimum number of coins
    for name, value in coins:
        for j in range(value, target + 1):
            if dp[j - value] + 1 < dp[j]:
                dp[j] = dp[j - value] + 1
                coin_used[j] = value

    if dp[target] == float('inf'):
        return "No solution possible with the given denominations."

    # Build the result
    result = {}
    amount = target
    while amount > 0:
        for name, value in coins:
            if value == coin_used[amount]:
                result[name] = result.get(name, 0) + 1
                amount -= value
                break

    # Format result for display
    result_list = [f"{coin}: {count}" for coin, count in result.items()]
    return dp[target], result_list  # Return the total number of coins and formatted result



























