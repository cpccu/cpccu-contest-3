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

# Read input
n = int(input())
potions = list(map(int, input().split()))

# Calculate and output the result
print(max_potions(n, potions))
