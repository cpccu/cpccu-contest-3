import math

def max_k(n):
    if n == 1:
        return 1
    else:
        return 2 ** math.floor(math.log2(n))

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        result = max_k(n)
        print(result)