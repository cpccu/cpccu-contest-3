def find_maximum_k(n):
    leftmost_set_bit = 0

    for i in range(31, -1, -1):
        if n & (1 << i):
            leftmost_set_bit = i
            break

    result = (1 << (leftmost_set_bit + 1)) - 1

    return result

t = int(input())
for _ in range(t):
    n = int(input())
    result = find_maximum_k(n)
    print(result)
