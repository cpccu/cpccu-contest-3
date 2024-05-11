def max_k(n):
    k = n - 1
    result = n
    while k >= 1 and result != 0:
        result &= k
        k -= 1
    return k + 1

# Input handling
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(max_k(n))
