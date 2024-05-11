import math

# Function to find the largest power of 2 less than or equal to n
def largest_power_of_2(n):
    return 2 ** math.floor(math.log2(n))

# Number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    n = int(input())  # Input integer n
    k = largest_power_of_2(n)  # Find the largest power of 2 less than or equal to n
    print(k)
