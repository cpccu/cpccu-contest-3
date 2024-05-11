def ans(n):
    while n>-1:
        s = set(str(n))
        if ('1' in s and len(s)==1 ) or n==0:
            return 'YES'
        n-=11
        
        
    
    return 'NO'
    

    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ans(n))
