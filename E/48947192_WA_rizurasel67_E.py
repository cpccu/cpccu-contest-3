def max_potions(n, a):
    max_potions=0
    for i in range(n):
        health=0
        potions=0
        for j in range(i, n):
            health += a[j]
            if health >= 0:
                potions += 1
            else:
                omitted_potions = j - sum(1 for x in range(j, i - 1, -1) if health - a[x] < 0)
                potions += omitted_potions
                break
        max_potions = max(max_potions, potions)
    return max_potions

n = int(input())

a = list(map(int,input().split()))

print(max_potions(n, a))
