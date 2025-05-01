import time
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

amounts = [113, 218, 999, 10327, 112432]

# Measure execution time
for amount in amounts:
    print(f"\nTesting amount: {amount}")

    # Greedy
    start_time = time.time()
    find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    print(f"Greedy Time: {greedy_time:.6f} seconds")

    # DP
    start_time = time.time()
    find_min_coins(amount)
    dp_time = time.time() - start_time
    print(f"DP Time: {dp_time:.6f} seconds")