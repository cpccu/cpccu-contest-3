def max_potions(n, potions):
    max_potions_count = 0
    health = 0

    for potion in potions:
        health += potion
        if health >= 0:
            max_potions_count += 1
        else:
            break  # Stop if health becomes negative

    return max_potions_count

if __name__ == "__main__":
    n = int(input())
    potions = list(map(int, input().split()))

    result = max_potions(n, potions)
    print(result)