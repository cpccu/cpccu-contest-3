def ans(n):
    if n%11==0:
        return 'YES'
    
    x = str(n)
    f = x[0]
    xx =n - int('1'*len(x))

    if xx%11==0:
        return 'YES'
    return 'NO'
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ans(n))
