# Function to check if x can be made using the given numbers
def can_make_x(x):
    # Check all possible combinations
    for i in range(0, x//11 + 1):
        for j in range(0, x//111 + 1):
            for k in range(0, x//1111 + 1):
                if 11*i + 111*j + 1111*k == x:
                    return "YES"
    return "NO"

# Read input
t = int(input().strip())

# Process each test case
for _ in range(t):
    x = int(input().strip())
    result = can_make_x(x)
    print(result)
