def rearrange_array(arr):
    # Sort the array
    arr.sort()

    # Initialize two pointers for the two halves of the sorted array
    i = 0
    j = len(arr) // 2

    # Initialize an empty result array
    result = []

    # Alternate between adding elements from the larger and smaller halves of the sorted array
    while j < len(arr):
        result.append(arr[j])
        j += 1
        result.append(arr[i])
        i += 1

    return result

# Read input
t = int(input())  # Number of testcases
for _ in range(t):
    n = int(input())  # Length of the array
    arr = list(map(int, input().split()))  # Array elements

    # Rearrange the array
    rearranged_arr = rearrange_array(arr)

    # Print the rearranged array
    print(*rearranged_arr)
