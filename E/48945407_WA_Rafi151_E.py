def max_potions(n, potions):
    potions.sort(reverse=True)  # Sort potions in descending order of health gain
    current_health = 0
    max_potions_drunk = 0
    
    for potion in potions:
        current_health += potion
        if current_health >= 0:
            max_potions_drunk += 1
        else:
            break
    
    return max_potions_drunk

# Read the input
n = int(input())  # Number of potions
potions = list(map(int, input().split()))  # Health gain from each potion

# Calculate and output the maximum number of potions that can be drunk without health becoming negative
result = max_potions(n, potions)
print(result)
