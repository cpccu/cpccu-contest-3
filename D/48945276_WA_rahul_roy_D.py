def ans(n):
    s = str(n)
    aa = len(s)
    nn = int(s[0])  

    x = int('1' * aa) * nn  

    n -= x  
    if n % 11 == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ans(n))
