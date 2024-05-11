def max_k(n):
    if n == 1:
        return 1
    else:
        power_of_2 = 1 << (n.bit_length() - 1)
        return power_of_2

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        result = max_k(n)
        print(result)
