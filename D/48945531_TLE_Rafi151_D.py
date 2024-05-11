def can_make_number(z):
    # Check if z can be formed by summing up 11 or 111
    for i in range(z // 111 + 1):
        for j in range((z - i * 111) // 11 + 1):
            if i * 111 + j * 11 == z:
                return "YES"
    return "NO"

# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    z = int(input())  # Number to make

    # Check if the number can be formed and print the result
    print(can_make_number(z))
