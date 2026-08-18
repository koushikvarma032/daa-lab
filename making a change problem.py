def min_coins(coins, amount):
    # Create DP array
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    # Calculate minimum coins for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Example
coins = [1, 3, 4]
amount = 6

result = min_coins(coins, amount)

print("Minimum coins required:", result)