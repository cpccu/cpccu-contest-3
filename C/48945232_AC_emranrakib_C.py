def arrange_array(n, a):
    # Sort the array
    a.sort()

    # Initialize an array to store the arranged elements
    b = [0] * (2 * n)

    # Place the largest elements at odd indices
    for i in range(n):
        b[2 * i + 1] = a[n + i]

    # Place the smallest elements at even indices
    for i in range(n):
        b[2 * i] = a[i]

    return b

# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the input n and the array a for each test case
    n = int(input())
    a = list(map(int, input().split()))

    # Arrange the array and print the result
    result = arrange_array(n, a)
    print(*result)
