def max_potions_to_drink(n, potions):
    health = 0
    potions_drunk = 0
    for potion in potions:
        health += potion
        if health >= 0:
            potions_drunk += 1
        else:
            break
    return potions_drunk

# Read input
n = int(input())  # Number of potions
potions = list(map(int, input().split()))  # Potions' effects

# Calculate and print the result
result = max_potions_to_drink(n, potions)
print(result)
