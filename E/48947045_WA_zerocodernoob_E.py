def max_potions(n, a):

  min_health = 0
  max_potions = 0


  for i in range(n):

    min_health = max(min_health + a[i], 0)


    if min_health > 0:
      max_potions += 1

  return max_potions


n = 6
a = [4, -4, 1, -3, 1, -3]
result = max_potions(n, a)
print(result) 