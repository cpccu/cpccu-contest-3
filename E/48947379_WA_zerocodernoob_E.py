n = int(input())
potions = list(map(int, input().split()))

health = 0
count = 0

for i in range(n):
    if potions[i] >= 0 or health + potions[i] >= 0:
        health += potions[i]
        count += 1

print(count)
