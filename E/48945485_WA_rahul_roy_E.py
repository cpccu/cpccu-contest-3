def life(arr,n):
    total = 0
    ans = 0
    for i in range(n):
        total+=arr[i]
        if arr[i]>=0:
            ans+=arr[i]
        
        if total<0:
            return ans
        


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    print(life(arr,n))