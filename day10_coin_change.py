# Day 10 - Coin Change

coins = [1, 2, 5]
amount = 11

dp = [float('inf')] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print(-1)
else:
    print("Minimum coins:", dp[amount])
