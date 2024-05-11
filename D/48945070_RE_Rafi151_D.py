# Function to check if r can be made using the given numbers
def can_make_r(r):
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if 111*i + 11*j + k == r:
                    return "YES"
    return "NO"

# Read input
t = int(input().strip())

# Process each test case
for _ in range(t):
    r = int(input().strip())
    result = can_make_r(r)
    print(result)
