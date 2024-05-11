# Function to check if r can be made using the numbers 11 and 111
def can_make_r(r):
    # If r is greater than or equal to 111, it can always be made
    if r >= 111:
        return "YES"
    else:
        # Otherwise, check if it can be made using a combination of 11s and 111s
        for i in range(0, r // 11 + 1):
            if (r - 11 * i) % 111 == 0:
                return "YES"
    return "NO"

# Read input
t = int(input().strip())

# Process each test case
for _ in range(t):
    r = int(input().strip())
    result = can_make_r(r)
    print(result)
