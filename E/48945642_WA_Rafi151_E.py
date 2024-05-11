n = int(input())  # Number of potions
potions = list(map(int, input().split()))  # List of potion effects

total_health = 0  # Initialize total health change
count = 0  # Initialize potion count

# Iterate through potions
for potion in potions:
    total_health += potion  # Update total health change
    if total_health >= 0:  # If health is not negative
        count += 1  # Increment potion count
    else:
        break  # Stop drinking potions if health becomes negative

print(count)  # Output the maximum number of potions
