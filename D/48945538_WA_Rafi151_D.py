def can_make_number(z):
    while z >= 11:
        if z % 11 == 0:
            return "YES"
        z -= 11
    return "YES" if z == 0 else "NO"

# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    z = int(input())  # Number you have to make
    # Check if it's possible to make the number and print the result
    print(can_make_number(z))
