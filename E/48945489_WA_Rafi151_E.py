def max_potions(n, potions):
    dp = [0] * (n + 1)
    dp[0] = 0  # Initial health

    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1] + potions[i - 1], dp[i - 1])

    return dp[n]

# Read input
n = int(input())
potions = list(map(int, input().split()))

# Calculate and print the result
print(max_potions(n, potions))
