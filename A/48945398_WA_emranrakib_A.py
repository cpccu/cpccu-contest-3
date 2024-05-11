def max_k(n):
    if n == 1:
        return 0

    left, right = 0, n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if (n & (n - 1) & (n - 2) & (n - 3) & mid) == 0:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the input n for each test case
    n = int(input())
    # Calculate and print the maximum value of k satisfying the condition
    print(max_k(n))
