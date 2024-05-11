def life(arr,n):
    arr = sorted(arr)
    total = sum(arr)

    if total>=0:
        return n
    
    for i in range(n):
        total+=abs(arr[i])
        if total>=0:
            return n-i-1
        

        


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    print(life(arr,n))