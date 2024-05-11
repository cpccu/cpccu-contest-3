def max_potions(n, potions):
    max_potions_possible = [0] * (n + 1)  # Initialize an array to store the maximum potions possible at each step
    
    max_potions_possible[0] = 0  # Base case
    
    for i in range(1, n + 1):
        # Calculate the maximum potions possible at this step
        max_potions_possible[i] = max(max_potions_possible[i - 1] + potions[i - 1], 0)
    
    return max(max_potions_possible)  # Return the maximum number of potions possible

# Read the input
n = int(input())  # Number of potions
potions = list(map(int, input().split()))  # Potions' effects

# Calculate and print the maximum number of potions you can drink
print(max_potions(n, potions))
