t = int(input())

for _ in range(t):
    n = int(input())
    k = n
    while k > 0:
        if n & k == 0:
            break
        k -= 1
    if k==1:
        print(k)
    else:
        print(k+1)
