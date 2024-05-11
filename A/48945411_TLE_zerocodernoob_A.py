def find_maximum_k(n):
    k = n
    for i in range(n, 0, -1):
        k &= i
        if k == 0:
            return i

t = int(input())
for _ in range(t):
    n = int(input())
    result = find_maximum_k(n)
    print(result)
