def max_potions(n, potions):
    max_potions_drunk = 0
    current_health = 0

    for potion in potions:
        current_health += potion
        if current_health >= 0:
            max_potions_drunk += 1
        else:
            break

    return max_potions_drunk

# Read the input
n = int(input())  # Number of potions
potions = list(map(int, input().split()))  # Potion effects

# Calculate and output the maximum number of potions you can drink
print(max_potions(n, potions))
