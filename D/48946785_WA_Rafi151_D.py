def can_make_x(x):
    while x > 0:
        # Subtract the largest possible number (111...111)
        # from x as many times as possible
        x -= 111
        if x % 11 == 0 or x <= 0:
            return "YES"
    return "NO"

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number to make
    x = int(input())
    # Check if x can be made
    print(can_make_x(x))
