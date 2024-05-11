def ans(n):
    length = len(str(n))
    x = int('1'*length)

    n = n-x
    if n%11==0:
        return 'YES'
    return 'NO'

    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ans(n))