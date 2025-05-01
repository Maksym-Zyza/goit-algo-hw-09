def find_coins_greedy(amount):
    # Coin denominations, sorted
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    # Iterate over each coin denomination
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            if count > 0:
                result[coin] = count

    return result


# Test
print(find_coins_greedy(113))
print(find_coins_greedy(218))
print(find_coins_greedy(999))
print(find_coins_greedy(10327))