def max_potions(n, a):

  min_health = 0
  max_potions = 0


  for i in range(n):

    min_health = max(min_health + a[i], 0)


    if min_health > 0:
      max_potions += 1

  return max_potions


test_cases = [
    (6, [4, -4, 1, -3, 1, -3], 5),
    (3, [1, 2, 3], 3),
    (5, [-2, 4, -1, 2, -1], 4),
]

for n, a, expected in test_cases:
  result = max_potions(n, a)
  if result != expected:
    print(f"Test failed for n={n}, a={a}, expected={expected}, got={result}")
  else:
    print(f"Test passed for n={n}, a={a}, expected={expected}, got={result}")