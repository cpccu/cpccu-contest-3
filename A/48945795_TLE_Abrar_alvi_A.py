def max_k(n):
    if n == 1:
        return 1
    else:
        k = 1
        while n & (n - k) != 0:
            k <<= 1
        return k - 1

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        result = max_k(n)
        print(result)

