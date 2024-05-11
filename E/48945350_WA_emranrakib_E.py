def max_potions(n, potions):
    dp = [0] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + potions[i - 1])
        
    return dp[n]

# Read the number of potions
n = int(input())

# Read the potion values
potions = list(map(int, input().split()))

# Calculate and print the maximum number of potions that can be drunk
print(max_potions(n, potions))
