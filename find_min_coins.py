def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # dp[i] = min number of coins needed for amount i
    dp = [float("infinity")] * (amount + 1)
    dp[0] = 0
    # Coins used for each amount
    coin_used = [[] for _ in range(amount + 1)]

    # Fill dp table
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]

    # Build result dictionary
    result = {}
    for coin in coin_used[amount]:
        result[coin] = result.get(coin, 0) + 1

    return result


# Test
print(find_min_coins(113))
print(find_min_coins(218))
print(find_min_coins(999))
print(find_min_coins(10327))