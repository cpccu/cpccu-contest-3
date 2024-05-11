# Function to check if z can be made using the numbers 11 and 111
def can_make_z(z):
    # If z is greater than or equal to 11, it can always be made
    if z >= 11:
        return "YES"
    else:
        return "NO"

# Read input
t = int(input().strip())

# Process each test case
for _ in range(t):
    z = int(input().strip())
    result = can_make_z(z)
    print(result)
